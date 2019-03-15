import pandas as pd
import os

from CTScan import CTScan
import data_processing as dp


PATH_SCANS = "../data/images_raw/"
PATH_ANNOTATION = "../data/info/annotations.csv"
PATH_CANDIDATES = "../data/info/candidates.csv"


if __name__ == "__main__":
	scan_names = dp.get_scan_names(PATH_SCANS)

	print("Candidates preparing:")
	candidates = dp.prepare_candidates(PATH_CANDIDATES)

	for scan_name in scan_names:
		current_scan = CTScan(scan_name, PATH_SCANS).read_scan()
		current_scan_candidates = candidates[candidates["seriesuid"]==scan_name]

		for nodule_info in current_scan_candidates.itertuples(index=False):
			world_coords = nodule_info[1 : 4]
			image = dp.cut_nodule(current_scan, world_coords, 128)
	pass
