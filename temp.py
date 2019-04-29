# -*- coding: utf-8 -*-
from sklearn import tree
from sklearn.externals import joblib
  
if __name__ == "__main__":
    clf = joblib.load('featuresNew.pkl')
    print("Введите значения: температура, влажность, скорость ветра")
    a = input()
    b = input()
    c = input()
    print (float(clf.predict([[a, b, c]]))) 

