import numpy as np
import pandas as pd
import os

from CTScan import CTScan
import image_processing as im


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
	candidates_all.rename(columns={"coordX" : "x", "coordY" : "y", "coordZ" : "z"}, inplace=True)
	candidates_prep = delete_negative(candidates_all, 3)

	return candidates_prep


def cut_nodule(scan, world_coords, size):
	x_v, y_v, z_v = world_to_voxel(world_coords, scan.origin, scan.spacing)
	
	nodule_image_origin = im.cut_image(scan.raw_image, x_v, y_v, z_v, size)
	nodule_image_normalized = im.normalize_image(nodule_image_origin, -1000, 400)

	return nodule_image_normalized


def world_to_voxel(world_coords, origin, spacing):
	streched_coord = np.absolute(np.array(world_coords) - origin)
	voxel_coords = streched_coord / spacing
	return tuple(map(int, voxel_coords))
