# Preprocess-SVHN
Preprocess Google Street View House Number dataset for consumption by AGIEF.

## Introduction
The purpose of this repository is to provide some useful tools to preprocess the
[SVHN dataset](http://ufldl.stanford.edu/housenumbers/) to be compatible with [AGIEF](https://github.com/ProjectAGI/agi).

The dataset we're using is **Format 2** which contains 32x32 cropped digits
from the original images. There are 10 labels for this dataset (0-9) for each digit.

Benchmarks for the SVHN dataset, and others can be found [here](https://rodrigob.github.io/are_we_there_yet/build/classification_datasets_results.html#5356484e).

## Preprocessing
The training and test datasets are provided in the `mat` format by the authors.
They are then loaded into Numpy arrays, and the features are separated from the labels.

The data is then converted to images into `training` and `testing` directories. The format
for the filename is as follows: `TYPE_RANDOM_LABEL_LABELCOUNT.png`

- `TYPE`: Indicates dataset type, could be either `train` or `test`
- `RANDOM`: Short randomly generated UUID-style characters e.g. `7daa28`
- `LABEL`: The groundtruth label for the image (between 0-9)
- `LABELCOUNT`: The count for how many times a label was seen to easily

This format is required for the AGIEF to parse the images and extract the labels.

## Usage
TODO
