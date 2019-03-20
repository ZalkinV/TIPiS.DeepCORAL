HU_MIN = -1000 # Min Haunsfield Unit
HU_MAX = 400 # Max Haunsfield Unit
SIZE_NODULE_IMAGE = 128


# Roots
PATH_SCANS = "../data/images_raw/"
PATH_IMAGES_PREPARED = "../data/images_prepared/"
PATH_ANNOTATION = "../data/info/annotations.csv"
PATH_CANDIDATES = "../data/info/candidates.csv"


try:
    from local_settings import *
except ImportError:
    pass
