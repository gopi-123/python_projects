#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan  6 18:27:51 2019

@author: gopinath
"""

# Simple Linear Regression

"""
Business Problem: To find out correlation between Salary and  Years of Experience
What is the best Business value that can be added to compmny ,
how to set the salaries for new employee by understanding the current underlying  model using the dataset Salary_Data.csv
For future  ,they can use the model that is underlying and can predict the salary range for new employee as per his/her experience

Linear Regression Algorithm : Finds linear relationship between the dependent variable and the independent variables.
"""

#import the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#import the dataset
dataset = pd.read_csv('Salary_Data.csv')

#create Independent variables (I.V) matrixx
#Create X matrix of features (  columns of independent variables which is X) and Dependent variables (y)
#pick all  line observations until all column-1(include all columns except last column)
X = dataset.iloc[: , : -1].values

# create Dependent variables vector 
y = dataset.iloc[: , 1].values 

# Splitting the dataset into the Training set and Test set list
from sklearn.cross_validation import train_test_split
X_train,X_test,y_train,y_test = train_test_split(X,y, test_size =1/3, random_state =0) 

# Feature Scaling
"""from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.transform(X_test)
sc_y = StandardScaler()
y_train = sc_y.fit_transform(y_train)""
"""

#fitting simple Linear Regression to the Training set
#Create a object of linear regressor class & fit the regressor to training set X_train and y_train
# The simple linear regressor now learns the corelations  training set i,e learns corelations of year of experience with the salary
#The fit method will take the values of X_train and y_train and then will compute the coefficients b 0 and b 1)
#’Salary = b 0 + b 1 × Experience’
#b 0 is the salary you get with no experience and b 1 is the increase in salary per year.


from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train, y_train)  #obtain a unique equation which is a Simple Linear Regression equation (y = b0 + b1 * x)

#Predicting the Test set results
#now lets see how our linear regressor  has learnt and it predict test set result based after our training
# create vector ofsalary prediction for new xtest
y_pred = regressor.predict(X_test)


#Visualize the Training set results
#look at observations of trainset
plt.scatter(X_train,y_train,color ='red' , label="observation points of training set")
plt.plot(X_train,regressor.predict(X_train) ,color ='blue' , label="training set prediction")
plt.title("Salary vs Experience( on Training set)")
plt.xlabel("Years of Experience")
plt.ylabel("Salary")

plt.legend()
plt.show()


#Visualize the Test set results
plt.scatter(X_test,y_test,color ='red', label="observation points of test set") #observation points of test set
plt.plot(X_train,regressor.predict(X_train) ,color ='blue' , label="training set prediction")
plt.title("Salary vs Experience( on Test set)")
plt.xlabel("Years of Experience")
plt.ylabel("Salary")

plt.legend()
plt.show()




