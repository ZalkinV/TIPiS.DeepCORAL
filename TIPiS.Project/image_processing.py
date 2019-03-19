import data_processing as dp



HU_MIN = -1000 # Min Haunsfield Unit
HU_MAX = 400 # Max Haunsfield Unit
SIZE_NODULE_IMAGE = 128



def cut_nodule(scan, world_coords, size):
	x_v, y_v, z_v = dp.world_to_voxel(world_coords, scan.origin, scan.spacing)
	
	nodule_image_origin = cut_subimage(scan.raw_image, x_v, y_v, z_v, size)
	nodule_image_normalized = normalize_image(nodule_image_origin, HU_MIN, HU_MAX)

	return nodule_image_normalized


def cut_subimage(image, x, y, z, size):
	left = max(x - size // 2, 0)
	right = left + size
	image_width = image.shape[1]
	if right > image_width:
		left -= right - image_width
		right = image_width

	bottom = max(y - size // 2, 0)
	top = bottom + size
	image_height = image.shape[2]
	if top > image_height:
		bottom -= top - image_height
		top = image_height
	
	subimage = image[z, left : right,  bottom : top]
	return subimage


def normalize_image(image, min_val, max_val):
	image = (image - min_val)/(max_val - min_val)
	image[image > 1] = 1
	image[image < 0] = 0
	return image


def save_nodules_images(file, scan, nodules_info):
	nodule_index = 0
	for nodule_info in nodules_info.itertuples(index=False):
		world_coords = nodule_info[1:4]
		nodule_class = nodule_info[-1]
		image = cut_nodule(scan, world_coords, SIZE_NODULE_IMAGE)

		nodule_name = str(nodule_index)
		file.create_dataset(nodule_name, data=image)
		file[nodule_name].attrs["coords"] = world_coords
		file[nodule_name].attrs["class"] = nodule_class

		nodule_index += 1
