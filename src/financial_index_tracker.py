# Copyright 2024 Dimitar Dimitrov
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""
Main module
"""
import argparse
import logging
import sys

logger = logging.getLogger(__name__)

parser = argparse.ArgumentParser(description='Configuration parameters',
                                 fromfile_prefix_chars='@')

def define_cli_arguments():
    """This function is used to parse the command line arguments"""

    parser.add_argument('-i', '--index',
                        type=str,
                        default='NASDAQ',
                        choices=(['NASDAQ', 'S&P500']),
                        help='Financial index to track')
    parser.add_argument('-l', '--loglevel',
                        default="INFO",
                        choices=(['INFO', 'DEBUG', 'ERROR']),
                        help="The logging level, default is INFO")

def main():
    """Main function"""

    define_cli_arguments()
    args = parser.parse_args()

    # Setup logging
    file_handler = logging.FileHandler(filename='Financial_index_tracker.log', mode='w')
    stdout_handler = logging.StreamHandler(sys.stdout)
    handlers = [file_handler, stdout_handler]
    logging.basicConfig(level=args.loglevel.upper(),
                        format='%(asctime)s %(name)30s [%(levelname)8s] - %(message)s',
                        handlers=handlers)

if __name__ == '__main__':
    main()
