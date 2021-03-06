# -*- coding: utf-8 -*-
"""
Created on Sat Mar  6 21:35:01 2021

@author: m-lin
"""

#　ライブラリのインポート
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.utils import all_estimators
import warnings

# classifierのアルゴリズム全てを取得する
allAlgorithms = all_estimators(type_filter="classifier")
warnings.simplefilter("error")

for(name, algorithm) in allAlgorithms :
  try :
    # 各アリゴリズムのオブジェクトを作成
    clf = algorithm()

    # 学習して、評価する
    clf.fit(x_train, y_train)
    y_pred = clf.predict(x_test)
    print(name,"の正解率 = " , accuracy_score(y_valid, y_pred))
  
  # WarningやExceptionの内容を表示する
  except Warning as w :
    print("\033[33m"+"Warning："+"\033[0m", name, ":", w.args)
  except Exception as e :
    print("\033[31m"+"Error："+"\033[0m", name, ":", e.args)