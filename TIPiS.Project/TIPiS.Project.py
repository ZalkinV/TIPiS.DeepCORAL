import pandas as pd
import os

from CTScan import CTScan
import data_processing as dp
import image_processing as im



if __name__ == "__main__":
	dp.process_data()
	X_data, y_data = dp.load_scan_nodules()
	pass
