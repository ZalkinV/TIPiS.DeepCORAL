import matplotlib.pyplot as plt

import data_processing as dp
from configs.global_config import (
	PATH_SCANS,
	PATH_IMAGES_PREPARED,
	PATH_ANNOTATION,
	PATH_CANDIDATES
)



def show_nodules(images, labels):
	pos_count = labels.count(1)
	neg_count = labels.count(0)
	col_count = max(pos_count, neg_count)

	fig, axes = plt.subplots(2, col_count, subplot_kw={ "xticks" : [], "yticks" : [] })

	cur_subplot = [0, 0]
	for index, label in enumerate(labels):
		axes[label, cur_subplot[label]].imshow(images[index], cmap="gray")
		cur_subplot[label] += 1

	fig.suptitle("Nodules images")
	axes[0, 0].set_ylabel("Negatives")
	axes[1, 0].set_ylabel("Positives")

	plt.show()
