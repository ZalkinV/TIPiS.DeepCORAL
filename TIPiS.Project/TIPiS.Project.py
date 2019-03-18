import pandas as pd
import os

from CTScan import CTScan
import data_processing as dp
import image_processing as im


PATH_SCANS = "../data/images_raw/"
PATH_ANNOTATION = "../data/info/annotations.csv"
PATH_CANDIDATES = "../data/info/candidates.csv"


if __name__ == "__main__":
	scan_names = dp.get_scan_names(PATH_SCANS)

	print("Candidates preparing:")
	candidates = dp.prepare_candidates(PATH_CANDIDATES)

	dp.save_scan_nodules(PATH_SCANS, scan_names, candidates)

	pass
