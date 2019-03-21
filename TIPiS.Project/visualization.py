import os
import math
import matplotlib.pyplot as plt

import data_processing as dp
from configs.global_config import (
	PATH_SCANS,
	PATH_IMAGES_PREPARED,
	PATH_ANNOTATION,
	PATH_CANDIDATES
)



def show_nodules(images, labels):
	row_count = math.ceil(math.sqrt(len(images)))
	col_count = math.ceil(len(images) / row_count)
	widths = [images[0].shape[0] for i in range(col_count)]
	heights = [images[0].shape[1] for i in range(row_count)]

	fig, axes = plt.subplots(row_count, col_count,
						  figsize=(8,7), gridspec_kw={ "width_ratios" : widths, "height_ratios" : heights})
	axes = axes.ravel()
	plt.setp(axes, xticks=[], yticks=[])
	plt.subplots_adjust(top=0.95, wspace=0, hspace=0.3)
	

	for i in range(len(images)):
		axes[i].imshow(images[i], cmap="gray")
		axes[i].set_xlabel(labels[i])

	fig.suptitle("Nodules images")

	plt.show()


def print_title(title):
	console_columns, console_rows = os.get_terminal_size(1)
	print("=" * (console_columns - 1))
	print(f"{title:^{console_columns - 1}}")
	print("=" * (console_columns - 1))
