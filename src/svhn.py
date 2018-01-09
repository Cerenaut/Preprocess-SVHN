from __future__ import print_function

import logging
import scipy.io as sio

import utils

def setup_arg_parsing():
    """
    Parse the commandline arguments
    """
    import argparse
    from argparse import RawTextHelpFormatter

    parser = argparse.ArgumentParser(formatter_class=RawTextHelpFormatter)

    parser.add_argument('--dataset', dest='dataset', required=False,
                        help='The type of dataset could be (train|test|valid)')

    parser.add_argument('--input_mat', dest='input_path', required=True,
                        help='Path to the MAT source file')

    parser.add_argument('--output_path', dest='output_path', required=True,
                        help='Path to folder for saving generated images')

    parser.add_argument('--grayscale', dest='grayscale', action='store_true', required=False,
                        help='Convert images to grayscale (default=%(default)s).')

    parser.add_argument('--logging', dest='logging', required=False,
                        help='Logging level (default=%(default)s). '
                             'Options: debug, info, warning, error, critical')

    parser.set_defaults(grayscale=False)
    parser.set_defaults(logging='warning')

    return parser.parse_args()

def main():
    """
    The main scope of the preprocessor containing the high level code
    """

    args = setup_arg_parsing()

    # Setup logging
    log_format = "[%(filename)s:%(lineno)s - %(funcName)s() - %(levelname)s] %(message)s"
    logging.basicConfig(format=log_format, level=utils.logger_level(args.logging))

    # Load MAT source file
    data = sio.loadmat(args.input_path)

    # Split data into features and labels
    features = data['X']
    labels = data['y']

    # Start preprocessing images
    utils.preprocess(args.dataset, features, labels, args.output_path, args.grayscale)

if __name__ == '__main__':
    main()
