#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 2 (SVM) mini-project.

    Use a SVM to identify emails from the Enron corpus by their authors:    
    Sara has label 0
    Chris has label 1
"""
    
import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess
from sklearn import svm


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()

#########################################################
### your code goes here ###
# features_train = features_train[:len(features_train)/100]
# labels_train = labels_train[:len(labels_train)/100]

clf = svm.SVC(kernel = 'rbf', C = 10000)

t0 = time()
clf.fit(features_train, labels_train)
print "training time:", round(time()-t0, 3), "s"

t0 = time()
rs_test = clf.predict(features_test)
print "training time:", round(time()-t0, 3), "s"

from sklearn.metrics import accuracy_score
print(accuracy_score(rs_test, labels_test))

print(sum(rs_test))
# print('predict 10 = {}'.format(rs_test[10]))
# print('predict 26 = {}'.format(rs_test[26]))
# print('predict 50 = {}'.format(rs_test[50]))
#########################################################


