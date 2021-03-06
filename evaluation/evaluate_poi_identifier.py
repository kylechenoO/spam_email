#!/usr/bin/python


"""
    Starter code for the evaluation mini-project.
    Start by copying your trained/tested POI identifier from
    that which you built in the validation mini-project.

    This is the second step toward building your POI identifier!

    Start by loading/formatting the data...
"""

import pickle
import sys
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit

data_dict = pickle.load(open("../final_project/final_project_dataset.pkl", "r") )

### add more features to features_list!
features_list = ["poi", "salary"]

data = featureFormat(data_dict, features_list)
labels, features = targetFeatureSplit(data)



### your code goes here 
from sklearn import cross_validation
from sklearn import tree
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score

X_train, X_test, y_train, y_test = cross_validation.train_test_split(features, labels, test_size = 0.3, random_state = 42)
clf = tree.DecisionTreeClassifier()
clf.fit(X_train, y_train)

# print('test size {}'.format(len(y_test)))
# print(clf.score(X_test, y_test))
# print(clf.predict(X_test))
# X_test[4] = [1.2]
# X_test[11] = [98980]
# X_test[19] = [87986876]
# X_test[21] = [897856876]
# print(clf.predict(X_test))
# print(clf.score(X_test, y_test))
print(precision_score(y_test, clf.predict(X_test)))
print(recall_score(y_test, clf.predict(X_test)))
