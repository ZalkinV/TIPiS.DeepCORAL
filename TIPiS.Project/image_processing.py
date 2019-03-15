
def cut_image(image, x, y, z, size):
	left = max(x - size // 2, 0)
	right = left + size
	bottom = max(y - size // 2, 0)
	top = bottom + size
	sub_image = image[z, left : right,  bottom : top]
	return sub_image


def normalize_image(image, min, max):
	image = (image - min)/(max - min)
	image[image > 1] = 1
	image[image < 0] = 0
	return image
