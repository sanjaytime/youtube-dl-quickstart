import argparse
import logging
import os

logger = logging.getLogger(name=os.path.basename(__file__))
logging.basicConfig(level=logging.INFO)


parser = argparse.ArgumentParser(description='Process a path')
parser.add_argument('mp3_folder_path', metavar='mp3_folder_path', type=str,
                    help='desired output path for the youtube files')

args = parser.parse_args()

args.mp3_folder_path

logger.info(f'argument provided: {args.mp3_folder_path}')

# Remove the Users/username part of the path
partial_path = args.mp3_folder_path.split('/', 3)[3]

# Add the rest
file_name = '%(title)s.%(ext)s'
output_path = f'~/{partial_path}/{file_name}'

# logger.info(f'output path being used in config: {output_path}')


text = """
-x
--restrict-filenames
# Put your desired output path below!  Keep the "%(title)s.%(ext)s" at the end.


-o ~/Music/My\ files\ in\ Dropbox/sample\ files/full\ songs\ to\ sample/%(title)s.%(ext)s

-o {}
--audio-quality 0
--audio-format mp3
""".format(output_path)

logger.info(text)