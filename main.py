import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score


from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from xgboost import XGBClassifier


import pickle
from flask import Flask, render_template, request
df=pd.read_excel("flood dataset.xlsx")
print(df.head())
print(df.info())
df = pd.read_excel("flood dataset.xlsx")
print(df.head())
print(df.info())

import matplotlib.pyplot as plt
import seaborn as sns

sns.histplot(df["Temp"], kde=True)
plt.show()

sns.boxplot(y=df["Temp"])
plt.show()