import data_processing as dp



SIZE_NODULE_IMAGE = 128



def cut_nodule(scan, world_coords, size):
	x_v, y_v, z_v = dp.world_to_voxel(world_coords, scan.origin, scan.spacing)
	
	nodule_image_origin = cut_subimage(scan.raw_image, x_v, y_v, z_v, size)
	nodule_image_normalized = normalize_image(nodule_image_origin, -1000, 400)

	return nodule_image_normalized


def cut_subimage(image, x, y, z, size):
	left = max(x - size // 2, 0)
	right = left + size
	imageWidth = image.shape[1]
	if (right > imageWidth):
		left -= right - imageWidth
		right = imageWidth

	bottom = max(y - size // 2, 0)
	top = bottom + size
	imageHeight = image.shape[2]
	if (top > imageHeight):
		bottom -= top - imageHeight
		top = imageHeight
	
	subimage = image[z, left : right,  bottom : top]
	return subimage


def normalize_image(image, min, max):
	image = (image - min)/(max - min)
	image[image > 1] = 1
	image[image < 0] = 0
	return image


def save_nodules_images(file, scan, nodules_info):
	nodule_index = 0
	for nodule_info in nodules_info.itertuples(index=False):
		world_coords = nodule_info[1 : 4]
		image = cut_nodule(scan, world_coords, SIZE_NODULE_IMAGE)

		nodule_class = nodule_info[-1]
		nodule_name = str(nodule_index)
		nodule_index += 1

		file.create_dataset(nodule_name, data=image)
		file[nodule_name].attrs["coords"] = world_coords
		file[nodule_name].attrs["class"] = nodule_class
	pass
