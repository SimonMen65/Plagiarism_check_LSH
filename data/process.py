# -*- coding: utf-8 -*-

'''
This Script is designed to process suspicious docs,
these docs shown in pair, where the .txt file contains raw text 
and a corresponding .xml file contains properties of this doc.
This Script should read all xml files, and move the txt doc to either true negative
or true positive folder.
'''


import xml.etree.ElementTree as ET
import os
from shutil import copyfile

TN_FOLDER = './data/processed/true_negative'
TP_FOLDER = './data/processed/true_positive'
TP_REF = "./data/processed/tp_ref"


def copy_file(dst_folder,filename):
    path = os.path.splitext(filename)[0]
    name = path.split('/')[-1]
    dst = dst_folder + '/' + name + '.txt'
    copyfile(path + '.txt', dst)

def save_ref(dst_folder, file_name, content):
    path = os.path.splitext(file_name)[0]
    name = path.split('/')[-1] + '-sr'
    save_path = os.path.join(dst_folder, name + ".txt")

    new_file = open(save_path, "w")
    new_file.write('\n'.join(content))
    new_file.close()

def process_features(file, doc):
    """Parse .xml files, determine if the doc is positive, and move it"""
    features = doc.findall(".//feature[@name='artificial-plagiarism'][@translation='false'][@obfuscation='none']")
    uniq_sr = set()

    for el in features:
        uniq_sr.add(el.attrib['source_reference'])

    if len(uniq_sr) > 0:
        copy_file(TP_FOLDER, file.name)
        save_ref(TP_REF, file.name, uniq_sr)

def parse_file(file):
    doc = ET.parse(file)

    # Choose only English documents
    for el in doc.findall(".//feature[@name='language']"):
        lang = el.attrib['value']
        if lang != "en":
            return

    ap_len = len(doc.findall(".//feature[@name='artificial-plagiarism']"))

    # Sort out original and plagiarized texts
    if ap_len == 0:
        copy_file(TN_FOLDER, file.name)
    else:
        process_features(file, doc)

def process_suspicious(input_dir):
    count = 0
    for filename in os.listdir(input_dir):
        if filename.endswith('.xml'):
            with open(os.path.join(input_dir, filename)) as file:
                parse_file(file)

if __name__ == '__main__':
    directory = './data/raw/suspicious_docs/'
    process_suspicious(directory)