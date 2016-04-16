import os

import simplejson as json
import file_utils
import config

def dump_json(data, file_name):
    output_directory = config.NSL_JSON_OUTPUT_PATH

    file_utils.create_directory_dont_exist(output_directory)

    with open(os.path.join(output_directory, file_name), 'w') as outfile:
        json.dump(data, outfile, 
                sort_keys=True, 
                indent=config.JSON_INDENT)
