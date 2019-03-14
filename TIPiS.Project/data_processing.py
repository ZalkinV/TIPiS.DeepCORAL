import numpy as np
import pandas as pd
import os

from CTScan import CTScan


def get_scan_names(scans_path):
	scan_names = set()
	for file_name in os.listdir(scans_path):
		file_name_wo_extension = file_name.rsplit('.', 1)[0]
		if file_name_wo_extension != "":
			scan_names.add(file_name_wo_extension)
	return scan_names


def read_scan_files(scans_path, scan_names):
	ct_scans = dict()
	for scan_name in scan_names:
		current_scan = CTScan(scan_name, scans_path)
		current_scan.read_scan()
		ct_scans[scan_name] = current_scan

		print(scan_name)
		print("\tOrigin:", current_scan.origin)
		print("\tSpacing:", current_scan.spacing)

	return ct_scans


def read_candidates(file_name, scan_names):
	candidates_all = pd.read_csv(file_name)
	candidates_interest = candidates_all.loc[candidates_all["seriesuid"].isin(scan_names)]
	return candidates_interest


def world_to_voxel(world_coords, origin, spacing):
	streched_coord = np.absolute(np.array(world_coords) - origin)
	voxel_coords = streched_coord / spacing
	return tuple(map(int, voxel_coords))
