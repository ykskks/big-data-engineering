#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Description

Usage:
    $python kmeans.py -f DATASET.csv -k No.clusters

    $python kmeans.py -f crater.csv -k 3
"""
from sklearn.cluster import KMeans
import csv
from collections import defaultdict
from optparse import OptionParser
import matplotlib.pyplot as plt


def clustering(feature, k):
    kmeans = KMeans(n_clusters=k)
    kmeans.fit(feature)
    pred = kmeans.labels_
    return pred


def dataFromFile(fname):
        """Function which reads from the file and yields a generator"""
        file_iter = open(fname, 'r')
        for line in file_iter:
                line = line.strip().rstrip(',')     # Remove trailing comma
                record = line.split(',')
                yield record


if __name__ == '__main__':

    optparser = OptionParser()
    optparser.add_option('-f', '--inputFile',
                         dest='input',
                         help='filename containing csv',
                         default=None)
    optparser.add_option('-k',
                         dest='k',
                         help='number of clusters',
                         default=3,
                         type='int')
    (options, args) = optparser.parse_args()
    inFile = None
    if options.input is None:
            inFile = sys.stdin
    elif options.input is not None:
            inFile = dataFromFile(options.input)
    else:
            print('No dataset filename specified, system with exit\n')
            sys.exit('System will exit')
    k = options.k

    feature=[]
    for record in inFile:
        feature.append(list(map(float,record)))
    pred = clustering(feature,k)

    #plot nodes
    plt.title("kmeans with k={}".format(k))
    x=[]
    y=[]
    for i in range(len(set(pred))):
        x.append([])
        y.append([])
    for i in range(len(pred)):
        x[pred[i]].append(feature[i][0])
        y[pred[i]].append(feature[i][1])
    color_list=['red','blue','yellow','green','purple','c', 'olivedrab']
    for i in range(len(x)):
        plt.scatter(x[i],y[i],label=i, c=color_list[i])
    plt.legend()
    plt.show()
