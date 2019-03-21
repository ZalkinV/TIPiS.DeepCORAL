import data_processing as dp
import visualization as vz



if __name__ == "__main__":
	X_data, y_data = dp.load_scan_nodules()
	vz.show_nodules(X_data, y_data)
