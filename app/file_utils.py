import os
import zipfile
import config

def cleanup(directory):
    if config.CLEAN_JSON:
        print("Cleaning up \"{directory}\"".format(**locals()))
        for root, dirs, files in os.walk(directory, topdown=False):
            for name in files:
                os.remove(os.path.join(root, name))
            for name in dirs:
                os.rmdir(os.path.join(root, name))
        os.rmdir(directory)

def zipdir(path, output_file_name):
    print("Adding  \"{path}\" to \"{output_file_name}\"".format(**locals()))
    zipf = zipfile.ZipFile(output_file_name, 'w', zipfile.ZIP_DEFLATED)
    for root, dirs, files in os.walk(path):
        for file in files:
            zipf.write(os.path.join(root, file), file)
    zipf.close()
