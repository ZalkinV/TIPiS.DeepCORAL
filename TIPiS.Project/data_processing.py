import numpy as np
import pandas as pd
import os
import h5py

from CTScan import CTScan
import image_processing as im


PATH_IMAGES_PREPARED = "../data/images_prepared/"


def get_scan_names(scans_path):
	scan_names = set()
	for file_name in os.listdir(scans_path):
		file_name_wo_extension = file_name.rsplit('.', 1)[0]
		if file_name_wo_extension != "":
			scan_names.add(file_name_wo_extension)
	return list(scan_names)


def prepare_candidates(file_name):

	def delete_negative(candidates, neg_to_pos_ratio):
		indexes_pos = np.array(candidates[candidates["class"] == 1].index)
		indexes_neg = np.array(candidates[candidates["class"] == 0].index)

		np.random.seed(104)
		indexes_neg = np.random.choice(indexes_neg, len(indexes_pos) * neg_to_pos_ratio, replace=False)

		indexes_all = np.concatenate((indexes_pos, indexes_neg))
		resampled_candidates = candidates.iloc[indexes_all]
		return resampled_candidates


	candidates_all = pd.read_csv(file_name)

	print("\tCandidates before processing:")
	print(candidates_all.info(verbose=False, memory_usage="deep"))
	print(candidates_all.describe())

	candidates_all.rename(columns={"coordX" : "x", "coordY" : "y", "coordZ" : "z"}, inplace=True)
	candidates_prep = delete_negative(candidates_all, 3)

	print("\n\n\tCandidates after processing:")
	print(candidates_prep.info(verbose=False, memory_usage="deep"))
	print(candidates_prep.describe())

	return candidates_prep


def world_to_voxel(world_coords, origin, spacing):
	streched_coord = np.absolute(np.array(world_coords) - origin)
	voxel_coords = streched_coord / spacing
	return tuple(map(int, voxel_coords))


def save_nodules_images(scans_path, scan_names, candidates):
	for scan_name in scan_names:
		current_scan = CTScan(scan_name, scans_path).read_scan()
		current_scan_candidates = candidates[candidates["seriesuid"]==scan_name]

		scan_file_path = PATH_IMAGES_PREPARED + scan_name + ".hdf5"
		with h5py.File(scan_file_path, "w") as scan_file:
			im.save_nodule_image(scan_file, current_scan, current_scan_candidates)
	pass
