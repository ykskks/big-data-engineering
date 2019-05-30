"""
Description

Usage:
    $python gmm.py -f DATASET.csv -n number of mixture components

    $python gmm.py -f data1.csv -n 5
"""

import sys
import csv
from optparse import OptionParser
import matplotlib.pyplot as plt
from sklearn.mixture import GaussianMixture


def clustering(feature, n):
    gmm = GaussianMixture(n_components=n)
    pred = gmm.fit_predict(feature)
    return pred


def dataFromFile(fname):
        """Function which reads from the file and yields a generator"""
        file_iter = open(fname, 'r')
        for line in file_iter:
                line = line.strip().rstrip(',')       # Remove trailing comma
                record = line.split(',')
                yield record


if __name__ == '__main__':

    optparser = OptionParser()
    optparser.add_option('-f', '--inputFile',
                         dest='input',
                         help='filename containing csv',
                         default=None)
    optparser.add_option('-n',
                         dest='n',
                         help='number of mixture components',
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
    n = options.n
    feature=[]
    for record in inFile:
        feature.append(list(map(float, record)))
    pred = clustering(feature,n)

    #plot nodes
    plt.title("EM")
    x=[]
    y=[]
    for i in range(max(pred)+1):
        x.append([])
        y.append([])
    for i in range(len(pred)):
        x[pred[i]].append(feature[i][0])
        y[pred[i]].append(feature[i][1])

    for i in range(len(x)):
        plt.scatter(x[i],y[i],label=i, cmap='viridis')
    plt.legend()
    plt.show()
