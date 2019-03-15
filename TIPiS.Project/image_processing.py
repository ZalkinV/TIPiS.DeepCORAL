
def cut_image(image, x, y, z, size):
	left = max(x - size // 2, 0)
	right = left + size
	bottom = max(y - size // 2, 0)
	top = bottom + size
	sub_image = image[z, left : right,  bottom : top]
	return sub_image
