
def persist_data(data, filename):
    # Use Python built-in functions to write 'data' to 'filename'
    file = open(filename, 'a')
    file.write(data)
    file.close()


def read_file(filename):
    # Use Python built-in functions to read contents of 'filename' and print them to screen
    file = open(filename, 'r')
    print(file.read())
    file.close()

def write_file(filename, data):
    # Use Python built-in functions to write 'data' to 'filename'
    file = open(filename, 'w')
    file.write(data)
    file.close()

def delete_file(filename):
    # Use Python built-in functions to delete 'filename'
    import os
    os.remove(filename)

def overwrite_file(filename, data):
    # Use Python built-in functions to overwrite 'filename' with 'data'
    file = open(filename, 'w')
    file.write(data)
    file.close()

def append_file(filename, data):
    # Use Python built-in functions to append 'data' to 'filename'
    file = open(filename, 'a')
    file.append(data)
    file.close()

def write_binary_file(filename, data):
    # Use Python built-in functions to write 'data' as binary to 'filename'
    file = open(filename, 'bw')
    file.write(data)
    file.close()

import cv2

def read_image_file(filename):
    # Use OpenCV to read 'filename' as an image
    cv2.imread(filename)

import pandas as pd

def read_csv_file(filename):
    # Use Pandas to read 'filename' as a csv
    df = pd.read_csv(filename)
    df.head()
    

def write_csv_file(filename, df):
    # Use Pandas to write dataframe 'df' to 'filename'
    df.to_csv(filename)

import json

def read_json_file(filename):
    # Use json to read 'filename' as a json
    with open(filename, 'r') as f:
        json.load(f)

def write_json_file(filename, data):
    # Use json to write 'data' to 'filename'
    with open(filename, 'w'):
        json.dump(data, filename)

import pickle

def write_pickle_file(filename, data):
    # Use pickle to write 'data' to 'filename'
    with open(filename, 'w') as f:
        pickle.dump(data, f)


def read_pickle_file(filename):
    # Use pickle to read 'filename'
    with open(filename, 'r') as f:
        pickle.load(f)
