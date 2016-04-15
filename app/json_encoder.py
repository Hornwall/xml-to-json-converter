import os

import simplejson as json
import config

def dump_json(data, file_name):
    output_directory = config.NSL_JSON_OUTPUT_PATH

    if not os.path.exists(output_directory):
            print("The directory \"{output_directory}\" does not exist! Creating it now!".format(**locals()))
            os.makedirs(output_directory)

    with open(os.path.join(output_directory, file_name), 'w') as outfile:
        json.dump(data, outfile, 
                sort_keys=True, 
                indent=config.JSON_INDENT)
