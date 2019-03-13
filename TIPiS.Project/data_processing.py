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

