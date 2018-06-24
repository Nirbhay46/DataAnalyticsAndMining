from sklearn.svm import SVC
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
import numpy as np
classifier = SVC()
classifier2 = DecisionTreeClassifier()
trainX = pd.read_csv("Training_set.csv")
train_x = []
test_x = [60,70,10,25.777,4,6]
np.array(test_x)
test_x = np.reshape(test_x, (-1, 6))
print(test_x)
classifier = DecisionTreeClassifier()
train_x = trainX.get_values()
np.array(train_x)
trainY= pd.read_csv("train_y(label).csv",index_col=False)
train_y = np.array([trainY.iloc[0]['train']])
for i in range (1,len(trainY)):
    train_y = np.append(train_y,[trainY.iloc[i]['train']])
print("train x dimension :",train_x)
print("train y dimension :",train_y)
print("test x dimension :",test_x)
classifier.fit(X=train_x , y = train_y)
classifier2.fit(X=train_x , y = train_y)
prediction = classifier.predict((test_x))
prediction2  = classifier2.predict((test_x))
print("prediction from  SVC :",prediction)
print("prediction from decisiontree" : , prediction2)
