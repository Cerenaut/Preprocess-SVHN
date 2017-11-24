# Preprocess-SVHN
Preprocess Google Street View House Number (SVHN) dataset for consumption by [AGIEF](https://github.com/ProjectAGI/agi).

## Introduction
The tools provided are only compatible with **Format 2** of the [SVHN](http://ufldl.stanford.edu/housenumbers/) which contains 32x32 cropped digits from the original images. There are 10 classes for this dataset (0-9), one for each digit.

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
