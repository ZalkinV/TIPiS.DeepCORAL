import pandas as pd
import os

from CTScan import CTScan


PATH_SCANS = "../data/images_raw/"
PATH_ANNOTATION = "../data/info/annotations.csv"
PATH_CANDIDATES = "../data/info/candidates.csv"


if __name__ == "__main__":

	scan_file_names = set()
	for file_name in os.listdir(PATH_SCANS):
		file_name_wo_extension = file_name.rsplit('.', 1)[0]
		if file_name_wo_extension != "":
			scan_file_names.add(file_name_wo_extension)


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
