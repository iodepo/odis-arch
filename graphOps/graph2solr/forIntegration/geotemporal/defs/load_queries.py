import requests
import io
import os

# Takes a list and returns a map of strings
def read_files(files):
    contents = {}
    for i, file in enumerate(files, start=1):
        if file.startswith('http://') or file.startswith('https://'):
            try:
                response = requests.get(file)
                response.raise_for_status()
                contents['q' + str(i)] = response.text
            except requests.exceptions.HTTPError as err:
                print(f'HTTP error occurred for {file}: {err}')
            except requests.exceptions.RequestException as err:
                print(f'Error occurred for {file}: {err}')
        else:
            try:
                with io.open(file, 'r') as f:
                    contents['q' + str(i)] = f.read()
            except OSError as err:
                print(f'OS error occurred for {file}: {err}')
            except Exception as err:
                print(f'Error occurred for {file}: {err}')
    return contents

# Take a single argument and returns a string
def read_file(file):
    contents = ""
    if file.startswith('http://') or file.startswith('https://'):
        try:
            response = requests.get(file)
            response.raise_for_status()
            contents = response.text
        except requests.exceptions.HTTPError as err:
            print(f'HTTP error occurred for {file}: {err}')
        except requests.exceptions.RequestException as err:
            print(f'Error occurred for {file}: {err}')
    else:
        try:
            with io.open(file, 'r') as f:
                contents = f.read()
        except OSError as err:
            print(f'OS error occurred for {file}: {err}')
        except Exception as err:
            print(f'Error occurred for {file}: {err}')
    return contents