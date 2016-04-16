import os
import io
import zipfile
import config
import requests

from urllib.request import urlopen

def cleanup(directory):
    if config.CLEAN_FILES:
        print("Cleaning up \"{directory}\"".format(**locals()))
        for root, dirs, files in os.walk(directory, topdown=False):
            for name in files:
                os.remove(os.path.join(root, name))
            for name in dirs:
                os.rmdir(os.path.join(root, name))
        os.rmdir(directory)

def delete_file(path):
    print("deleting file: {path}".format(**locals()))
    os.remove(path)

def zipdir(path, output_file_name):
    print("Adding  \"{path}\" to \"{output_file_name}\"".format(**locals()))
    zipf = zipfile.ZipFile(output_file_name, 'w', zipfile.ZIP_DEFLATED)
    for root, dirs, files in os.walk(path):
        for file in files:
            zipf.write(os.path.join(root, file), file)
    zipf.close()

def create_directory_dont_exist(path):
    if not os.path.exists(path):
            print("The directory \"{path}\" does not exist! Creating it now!".format(**locals()))
            os.makedirs(path)

def download_and_extract(url, destination):
    create_directory_dont_exist(destination)

    print("Downloading: {url}".format(**locals()))
    response = urlopen(url)
    zip_file = zipfile.ZipFile(io.BytesIO(response.read()))
    print("Extracting to: {destination}".format(**locals()))
    zip_file.extractall(destination)

def upload_file(url, file_path):
    print("uploading {file_path} to {url}".format(**locals()))
    files = {"file": open(file_path, "rb")}
    response = requests.post(url, files=files)
    print("Response: " + response.text)
