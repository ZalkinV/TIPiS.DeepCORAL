import data_processing as dp


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
