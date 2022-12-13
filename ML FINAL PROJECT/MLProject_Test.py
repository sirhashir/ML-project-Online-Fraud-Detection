# -*- coding: utf-8 -*-
"""MLPROJECT_TEST.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1TrZOR1adZhGkdABOD_VSAXDdiCHQ9_l_
"""

from google.colab import drive
drive.mount('/content/drive/')

import pandas as pd
import numpy as np
import scipy as sc
import math
import sklearn as sk
import matplotlib.pyplot as plt
import seaborn as sns
import random
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import RandomizedSearchCV
from sklearn.ensemble import RandomForestClassifier,GradientBoostingClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LogisticRegression
from xgboost import XGBClassifier
from sklearn.neighbors import KNeighborsClassifier

from sklearn.svm import SVC
import lightgbm
from lightgbm import LGBMClassifier

"""IMPORTING THE DATASETS"""

dftest=pd.read_csv('drive/MyDrive/Colab Notebooks/Its_A_Fraud/test.csv')

df=pd.read_csv('drive/MyDrive/Colab Notebooks/Its_A_Fraud/prepro_withcolumndeletion.csv')

"""CHECKING THE NUMBER OF NUMERICAL AND CATEGORICAL FEATURES"""

c_features=df.select_dtypes(include=np.object).columns
n_features=df.select_dtypes(include=np.number).columns
print(len(c_features))
print(len(n_features))

"""KEEPING THE COLUMNS OF TEST AND TRAIN THE SAME"""

train_col = df.drop(columns = {"isFraud", "Unnamed: 0"})

train_col = train_col.columns

dftest = dftest[train_col]

n_features= dftest.select_dtypes(include=np.number).columns
c_features = dftest.select_dtypes(include=np.object).columns
print(len(c_features))
print(len(n_features))

"""REPLACING THE VALUES IN "P_EMAILDOMAIN" TO REDUCE THE NUMBER OF UNIQUE VALUES"""

map = {
    "netzero.net"      : "netzero",    "yahoo.co.jp"     : "yahoo",
    "prodigy.net.mx"   : "prodigy",    "windstream.net"  : "windstream",
    "outlook.es"       : "outlook",    "embarqmail.com"  : "centurylink",
    "charter.net"      : "charter",    "gmx.de"          : "gmx",
    "mail.com"         : "mail",       "centurylink.net" : "centurylink",
    "cableone.net"     : "cableone",   "hotmail.fr"      : "outlook",
    "sbcglobal.net"    : "yahoo",      "frontier.com"    : "frontier",
    "anonymous.com"    : "anonymous",  "yahoo.fr"        : "yahoo",
    "outlook.com"      : "outlook",    "live.com.mx"     : "outlook",
    "ymail.com"        : "yahoo",      "frontiernet.net" : "frontiernet",
    "cfl.rr.com"       : "spectrum",   "live.fr"         : "outlook",
    "hotmail.com"      : "outlook",    "cox.net"         : "cox",
    "hotmail.es"       : "outlook",    "aol.com"         : "aol",
    "msn.com"          : "microsoft",  "suddenlink.net"  : "suddenlink",
    "gmail.com"        : "google",     "protonmail.com"  : "proton",
    "roadrunner.com"   : "roadrunner", "web.de"          : "web.de",
    "gmail"            : "google",     "netzero.com"     : "netzero",
    "live.com"         : "outlook",    "icloud.com"      : "apple",
    "comcast.net"      : "comcast",    "hotmail.co.uk"   : "outlook",
    "yahoo.co.uk"      : "yahoo",      "att.net"         : "yahoo",
    "optonline.net"    : "optimum",    "sc.rr.com"       : "spectrum",
    "yahoo.com"        : "yahoo",      "verizon.net"     : "verizon",
    "servicios-ta.com" : "ta",         "bellsouth.net"   : "bellsouth",
    "hotmail.de"       : "outlook",    "twc.com"         : "spectrum", 
    "q.com"            : "qcom",       "rocketmail.com"  : "rocketmail",
    "juno.com"         : "juno",       "mac.com"         : "apple",
    "yahoo.com.mx"     : "yahoo",      "earthlink.net"   : "earthlink",
    "aim.com"          : "aim",        "ptd.net"         : "pdt",
    "yahoo.de"         : "yahoo",      "yahoo.es"        : "yahoo", 
    "me.com"           : "apple",      "scranton.edu"    : "scranton"
}

dftest.replace({'P_emaildomain':map}, inplace = True)

"""FILLING THE NULL VALUES IN THE CATEGORICAL FEATURES WITH MODE"""

for i in ['card4', 'card6','P_emaildomain','M6']:
    dftest[i].fillna(dftest[i].mode()[0], inplace=True)
    df[i].fillna(df[i].mode()[0], inplace=True)

# dftest[c_features].isna().sum()

# dftest[n_features].isna().sum()

# df[n_features].isna().sum()

"""FILLING THE NULL VALUES IN THE NUMERICAL FEATURES WITH MEAN"""

dftest.fillna(dftest.mean(), inplace = True)
df.fillna(df.mean(), inplace=True)

"""ONE HOT ENCODING"""

lst = ['ProductCD', 'card4', 'card6', 'P_emaildomain', 'M6']
df = pd.get_dummies(df, columns = lst)

df.drop(columns = "Unnamed: 0", inplace = True)

lst = ['ProductCD', 'card4', 'card6', 'P_emaildomain', 'M6']
dftest = pd.get_dummies(dftest, columns = lst)

df.isFraud.value_counts()

"""TAKING RANDOM VALUES FROM TRAIN WHERE TARGET IS 1 IN ORDER TO REDUCE IMBALANCE"""

no_fraud = df[df.isFraud == 0]
yes_fraud = df[df.isFraud == 1]

no_fraud_sample = no_fraud.sample(n =15497)

newdf = pd.concat([no_fraud_sample, yes_fraud], axis=0)

y_train=newdf['isFraud']
x_train = newdf.drop(columns = 'isFraud', axis = 1)

# y_train.value_counts()

xtrain_col = x_train.columns

"""# **MODELS START**

LOGISTIC REGRESSION 
"""


# logReg_param_grid = {'C': [-4,1,2,3,4,8, 13,15],
#               'penalty': ['l1', 'l2'],
#               'max_iter': [100,500,1000,1500]
#              }
# logReg = LogisticRegression()
# logReg_grid = GridSearchCV(logReg, logReg_param_grid, cv=6, verbose=10, scoring='roc_auc', n_jobs=-1)
# logReg_grid.fit(x_train,y_train)

"""XGBOOST"""


# xgb = XGBClassifier()
# xgb.fit(x_train,y_train)
# y_test = xgb.predict(dftest)

"""KNN """


# kn=KNeighborsClassifier()
# kn.fit(x_train,y_train)
# y_test=kn.predict(dftest)

"""Random Forest"""

# n_estimators = [1000, 1500]
# max_features = ['auto', 'sqrt']
# max_depth = [3, 5]
# max_depth.append(None)
# min_samples_split = [2, 5]
# min_samples_leaf = [2, 4, 5]
# bootstrap = [True, False]

# params_grid = {'n_estimators': n_estimators, 'max_features': max_features,
#                'max_depth': max_depth, 'min_samples_split': min_samples_split,
#                'min_samples_leaf': min_samples_leaf, 'bootstrap': bootstrap}

# rf_clf = RandomForestClassifier(random_state=42)

# rf_cv = GridSearchCV(rf_clf, params_grid, scoring="f1", cv=3, verbose=2, n_jobs=-1)


# rf_cv.fit(x_train, y_train)
# best_params = rf_cv.best_params_
# print(f"Best parameters: {best_params}")

# rf_clf = RandomForestClassifier(**best_params)
# rf_clf.fit(x_train, y_train)

# y_test=rf_clf.predict(dftest)

"""SVM"""



# svc_param_grid = {'C': [1,2,3,4,8,15],
#                   'degree' : [3,4,5],
#                   'tol': [1e-3, 1e-4, 1e-5]
#                  }
# svclass = SVC()
# svc_grid =  RandomizedSearchCV(svclass, svc_param_grid)
# svc_grid.fit(x_train,y_train)
# y_test = svc_grid.predict(dftest)

"""LGBM"""



lgbm = LGBMClassifier(learning_rate=0.01, num_iterations=10000, num_leaves=10, baggong="bagging_fraction", reg_alpha=2, reg_lambda=5, verbose=1)

lgbm.fit(x_train, y_train)

y_test = lgbm.predict(dftest)

"""# **MODELS END**

DOWNLOADING THE TEST DATA
"""

# len(y_test)

id = []

for i in range(147635):
  id.append(i)

df_pred = pd.DataFrame(id, columns = ['id'])

df_pred['isFraud'] = y_test

df_pred

from google.colab import files
df_pred.to_csv('prediction.csv', index = False)
files.download('prediction.csv')
