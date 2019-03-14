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
	ct_scans = dp.read_scan_files(PATH_SCANS, scan_names)

	print("\n\nCandidates reading:")
	dp.read_candidates(PATH_CANDIDATES, ct_scans)
	pass
