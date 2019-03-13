import pandas as pd
import os

from CTScan import CTScan

import data_processing as dp

PATH_SCANS = "../data/images_raw/"
PATH_ANNOTATION = "../data/info/annotations.csv"
PATH_CANDIDATES = "../data/info/candidates.csv"


if __name__ == "__main__":
	scan_names = dp.get_scan_names(PATH_SCANS)

	print("CT scan files reading:")
	ct_scans = list()
	for scan_file_name in scan_file_names:
		ct_scans.append(CTScan(scan_file_name, PATH_SCANS))
		print(scan_file_name)
	print()


	print("Annotation:")
	annotation = pd.read_csv(PATH_ANNOTATION)
	print(annotation.info(), end='\n\n')
	print(annotation.describe(), end='\n\n\n')

	print("Candidates:")
	candidates = pd.read_csv(PATH_CANDIDATES)
	print(candidates.info(), end='\n\n')
	print(candidates.describe(), end='\n\n')
	print(candidates[candidates["class"]==1].count())
	pass
