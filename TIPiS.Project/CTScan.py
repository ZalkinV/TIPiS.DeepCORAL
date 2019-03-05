import numpy as np
import SimpleITK as sitk

from Nodule import Nodule



class CTScan:
	def __init__(self, file_name, file_path = ""):
		self.path = file_path + file_name + ".mhd"
		self.sitk_image = sitk.ReadImage(self.path)
		self.raw_image = sitk.GetArrayFromImage(self.sitk_image)
		self.nodule = None
		pass
