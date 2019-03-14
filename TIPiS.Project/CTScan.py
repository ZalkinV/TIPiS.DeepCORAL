import numpy as np

import SimpleITK as sitk

from Nodule import Nodule



class CTScan:
	""" Class for CTScan representation.
	origin - coordinates of pixel with coordinates (0, 0, 0) measured in mm
	spacing - distance between pixels in each dimension measured in mm
	nodule - nodule characteristics (coordinates, class, etc)"""

	def __init__(self, file_name, file_path = ""):
		self.path = file_path + file_name + ".mhd"
		self.sitk_image = None
		self.raw_image = None
		self.origin = None
		self.spacing = None
		self.nodules = None
		pass


	def read_scan(self):
		"""origin and spacing are reversing (np.flip()) because .mhg file contain coordinates in (z, y, x) order"""
		self.sitk_image = sitk.ReadImage(self.path)
		self.raw_image = sitk.GetArrayFromImage(self.sitk_image)
		self.origin = np.flip(np.array(self.sitk_image.GetOrigin()))
		self.spacing = np.flip(np.array(self.sitk_image.GetSpacing()))
		pass
