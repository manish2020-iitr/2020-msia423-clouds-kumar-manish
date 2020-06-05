
import argparse
import logging
import yaml
import pandas as pd

logging.basicConfig(format='%(name)-12s %(levelname)-8s %(message)s', level=logging.DEBUG)
logger = logging.getLogger('run-reproducibility')

from src.acquire import acquire
from src.featurize import *
from src.build_models import build_models
from test.test import *

if __name__ == '__main__':

    parser = argparse.ArgumentParser(description="Acquire, create features, and build model from clouds data")

    parser.add_argument('step', help='Which step to run', choices=['acquire', 'featurize', 'build_models', 'test'])
    parser.add_argument('--input', '-i', default=None, help='Path to input data')
    parser.add_argument('--config', help='Path to configuration file')
    parser.add_argument('--output', '-o', default=None, help='Path to save output CSV (optional, default = None)')

    args = parser.parse_args()

    # Load configuration file for parameters and tmo path
    with open(args.config, "r") as f:
        config = yaml.load(f, Loader=yaml.FullLoader)

    logger.info("Configuration file loaded from %s" % args.config)

    if args.input is not None:
        input = pd.read_csv(args.input)
        logger.info('Input data loaded from %s', args.input)

    if args.step == 'acquire':
        output = acquire(**config['acquire'])
    elif args.step == 'featurize':
        output = featurize_visible_range(input)
        output = featurize_vis_norm_range(output)
        output = featurize_log_entropy(output)
        output = featurize_entropy_x_contrast(output)
        output = featurize_IR_range(output)
        output = featurize_IR_norm_range(output)

    elif args.step == 'build_models':
        output = build_models(input)
    else:
        test_visible_range_happy()
        test_visible_range_unhappy()
        test_visible_norm_range_happy()
        test_visible_norm_range_unhappy()
        test_log_entropy_happy()
        test_log_entropy_unhappy()
        #test_IR_range_happy()
        test_IR_range_unhappy()
        test_IR_norm_range_unhappy()


    if args.output is not None:
        output.to_csv(args.output, index=False)

        logger.info("Output saved to %s" % args.output)
