# -*- coding: utf-8 -*-
"""
Collection of gloabl variables and functions that are used
(or may potentially be used) in different parts of the system
"""
import codecs
import pickle
from nltk.tokenize import word_tokenize

def read_file(filename):
    with codecs.open(filename, 'r', 'utf-8') as in_file:
        text = in_file.read()
    return (filename, text)


def tokenize_file(filename):
    """
    TODO 
    这个地方应该参考之前的一个作业
    我不确定nltk的这个方法是不是已经包含了stem什么的
    """
    filename, text = read_file(filename)
    token_text = word_tokenize(text)
    return (filename, token_text)


def load_lsh(filename):
    # Load pickled lsh object
    with open(filename, 'rb') as handle:
        return pickle.load(handle)

