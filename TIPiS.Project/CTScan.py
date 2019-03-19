import numpy as np

import SimpleITK as sitk



class CTScan:
	"""
	Class for CTScan representation.
	origin - coordinates of pixel with coordinates (0, 0, 0) measured in mm
	spacing - distance between pixels in each dimension measured in mm
	"""

	def __init__(self, file_name, file_path = ""):
		self.path = file_path + file_name + ".mhd"
		self.sitk_image = None
		self.raw_image = None
		self.origin = None
		self.spacing = None
		pass


	def read_scan(self):
		self.sitk_image = sitk.ReadImage(self.path)
		self.raw_image = sitk.GetArrayFromImage(self.sitk_image)
		self.origin = np.array(self.sitk_image.GetOrigin())
		self.spacing = np.array(self.sitk_image.GetSpacing())
		return self
