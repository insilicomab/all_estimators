# -*- coding: utf-8 -*-
"""
Created on Sat Mar  6 23:40:27 2021

@author: m-lin
"""

# ライブラリのインポート
import pandas as pd
from sklearn.utils import all_estimators
from sklearn.model_selection import KFold
import warnings
from sklearn.model_selection import cross_val_score

# classifierのアルゴリズム全てを取得する 
allAlgorithms = all_estimators(type_filter="classifier")

# K分割クロスバリデーション用オブジェクト
kfold_cv = KFold(n_splits=5, shuffle=True)
warnings.filterwarnings('ignore')

for(name, algorithm) in allAlgorithms :
  try :
    # 各アリゴリズムのオブジェクトを作成
    if(name == "LinearSVC") :
      clf = algorithm(max_iter = 10000)
    else:
      clf = algorithm()

    # scoreメソッドをもつクラスを対象とする
    if hasattr(clf,"score"):
        # クロスバリデーションを行う
        scores = cross_val_score(clf, x, y, cv=kfold_cv)
        print(name,"の正解率=")
        print(scores)
  
  # Exceptionは無視する
  except Exception as e :
    pass