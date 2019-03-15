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
	candidates_all = pd.read_csv(file_name)
	candidates_all.rename(columns={"coordX" : "x", "coordY" : "y", "coordZ" : "z"}, inplace=True)
	candidates = candidates_all
	return candidates


def cut_nodule(scan, world_coords, size):
	x_v, y_v, z_v = world_to_voxel(world_coords, scan.origin, scan.spacing)
	
	nodule_image_origin = im.cut_image(scan.raw_image, x_v, y_v, z_v, size)
	nodule_image_normalized = im.normalize_image(nodule_image_origin, -1000, 400)

	return nodule_image_normalized


def world_to_voxel(world_coords, origin, spacing):
	streched_coord = np.absolute(np.array(world_coords) - origin)
	voxel_coords = streched_coord / spacing
	return tuple(map(int, voxel_coords))
