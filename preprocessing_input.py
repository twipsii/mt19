# -*- coding: utf-8 -*-

# Lorenz Nagele
# MT Uebung 4
# Python 3

import codecs
import os
import argparse

def preprocess_text(input_filename, output_filename):
    if not output_filename:
        output_filename = os.path.abspath(input_filename) + ".prep"
    with codecs.open(input_filename, "r", "UTF-8") as f:
        lines = f.readlines()
    
    lines = [line.strip() for line in lines if line.strip() != ""]
    lines = [line.strip().lower() for line in lines]
    
    with codecs.open(output_filename, "w+", "UTF-8") as f:
        for line in lines:
            f.write(line + "\n")
        
def main():
    parser = argparse.ArgumentParser(description="Preprocessing text from file")
    parser.add_argument("-i", dest="input_filename", help="Text file to be processed")
    parser.add_argument("-o", dest="output_filename", help="File to save output to")
    args = parser.parse_args()
    preprocess_text(args.input_filename, args.output_filename)

if __name__ == "__main__":
    main()