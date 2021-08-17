# -*- coding: utf-8 -*-
"""
Created on Sun Aug  8 13:03:07 2021

@author: AMALITECH
"""
"import needed models"

import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import roc_auc_score

                                    #import csv file

df=pd.read_csv('Placement_Data_Full_Class.csv')


                            #data cleaning  and processing

"check if the columnto be used for labels is clean"
print(df.status.nunique())
"check if there are null values"
print(df.columns[df.isnull().any()])

"select best colums for feature set"

data=df[['ssc_p','hsc_p','degree_p','etest_p','mba_p']]

"create a new column which is a replacement of the labels with numerical values"
df['sucess_status']=df.status.apply(lambda x:0 if x=='Not Placed' else 1)
labels=df['sucess_status']


                                  #Machine learning classifier
 
"spitting data into training and validation sets"                            
X_train,X_test,y_train,y_test=train_test_split(data,labels,test_size =0.3,random_state=1)

"scaling features"
sc=StandardScaler()
X_train=sc.fit_transform(X_train)


"model fit "            
model=LogisticRegression()
model.fit(X_train, y_train)

# saving model as a pickle
import pickle
pickle.dump(model,open("Job_Placement_ml_model.sav", "wb"))
pickle.dump(sc, open("scaler.sav", "wb"))

def predicter(x):
    return model.predict(x)