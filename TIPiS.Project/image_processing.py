
def cut_subimage(image, x, y, z, size):
	left = max(x - size // 2, 0)
	right = left + size
	bottom = max(y - size // 2, 0)
	top = bottom + size
	subimage = image[z, left : right,  bottom : top]
	return subimage


def normalize_image(image, min, max):
	image = (image - min)/(max - min)
	image[image > 1] = 1
	image[image < 0] = 0
	return image
