#!/usr/bin/env python


import glob
from datetime import datetime
import multiprocessing


def read_info(name: str) -> list[str]:
    all_data: list[str] = []
    with open(name, 'r') as file:
        line: str = file.readline()
        while line.strip() != '':
            all_data.append(line.strip())
            line = file.readline()
    return all_data


if __name__ == '__main__':
    filenames = [file_path for file_path in glob.glob('/home/thrv/.playground/urban/urban/urban/tenth_mod/file*')]

    start_time = datetime.now()
    for filename in filenames:
        read_info(filename)
    end_time = datetime.now()
    print(f'Linear call: {end_time - start_time}')

    start_time = datetime.now()
    with multiprocessing.Pool() as pool:
        pool.map(read_info, filenames)
    end_time = datetime.now()
    print(f'Multiprocessing call: {end_time - start_time:}')
