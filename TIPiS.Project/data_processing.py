import os


def get_scan_names(scans_path):
	scan_names = set()
	for file_name in os.listdir(scans_path):
		file_name_wo_extension = file_name.rsplit('.', 1)[0]
		if file_name_wo_extension != "":
			scan_names.add(file_name_wo_extension)
	return scan_names

