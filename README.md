# ![](https://ga-dash.s3.amazonaws.com/production/assets/logo-9f88ae6c9c3871690e33280fcf557f33.png) **Capstone Project: Predicting Number of Injuries in a Crash**
## Executive Summary:

**How Important is Passenger Safety?** The first priority of any product manufacturer is to ensure the safety of the user. In the Automobile industry, it will be a life-saving measure. The designer and manufacturer should adopt high-level safety standards, besides attractive design, fuel efficiency, speed, and other fancy features. It is the most crucial aspect to gain trust among the buyers and increase the brand value.

The challenge is, how to improve existing safety mechanisms and which should be given more importance. It is very important for the company to invest more in research and development to solve these problems and ensure passenger safety. **But HOW to do that?**

**Calm Down!** There is always a solution, and the best is in front of you. The possible areas of safety improvements can be found by analyzing the data of various car crashes that occurred in the past. Various parameters such as Going Straight Ahead, Making Left Turn, Changing Lanes, Making Right Turn, and Slowing In Trafficway tops the list of crash factors. The roads and intersections are also considered in car-crash injury prediction. Various machine learning models were built and trained. Ada Boosting was the best model with the highest accuracy score of around 89% among all the models. We can also forecast the number of car crashes and injuries in the near future with the help of Autoregressive models, which help insurance companies to take necessary actions to avoid losses. The predictive model can also be used to investigate the incorrect predictions to check for false injury claims.

Now you are aware of car crashes which may lead to injury. So that advanced safety measures can be formulated and implemented in your brand.

We love to collaborate with an esteemed organization like yours. We will help you to ensure the passenger's safety.
**_Safety isn't Expensive; it is Priceless!_**

# Overview:
## Problem Statement:
- #### Predicting if a crash involves an injury or not, and what factors lead to more crashes.

The dataset (car_crash_report.csv) is collected from the [www.data.gov](https://catalog.data.gov/dataset/1-08-crash-data-report-detail) website. It consists of around 40 thousand observations of crashes in Tempe city (Arizona). The data includes vehicle-vehicle, vehicle-bicycle, and vehicle-pedestrian crashes along with the location, type of crash, and many other features.

From this dataset, we can predict if a crash involves injury or not, and figure out what factors lead to more crashes. This way, we can help the [Arizona Department of Transportation (ADOT)](https://azdot.gov/about-adot) minimize crashes and contribute to the [Vision Zero](https://en.wikipedia.org/wiki/Vision_Zero) initiative.

Our model will significantly help the insurance companies predict the number of injuries in a crash and investigate the incorrect predictions to check for false injury claims.

## Directory
- **Clean_dataframe**
    - **clean_df.csv :** The final dataframe resulting from data cleaning
- **data**
    - **car_crash_report.csv** Initial dataset that was downloaded from DATA.gov website
    - **Data_Dictionary.csv:** Represents type and a short description of all the features in car_crash_report.csv
- **st_images** - Contains images for streamlit app
- **Notebooks:**
    - 01_Car-Crash.ipynb
    - 02_NN_&_RNN_Deep_Learning.ipynb
    - 03_Conclusions_&_Recommendations.ipynb
- **Presentation_Slides.pdf**
- **README.md**
- **st-app.py** - Contains code for the Streamlit app.
- **Best_model_Ada_Boosting.pkl** - Saved Ada Boosting model to be used in the Streamlit app.

## Data Dictionary

Initially there were 35 features, so after using correlation heatmap (for numerical features) and boxplots (for categorical features) I came up with the following features that were the best to predict if the crash involves an injury or not.


|Feature|Type|Description|
|---|---|---|
|**Injury_Severity**|*int*|1 for serious injury and 0 for otherwise
|**AlcoholUse_Drv1**|*int*|0 for no alcohol influence on the driver_1 and 1 for yes
|**AlcoholUse_Drv2**|*int*|0 for no alcohol influence on the driver_2 and 1 for yes
|**Age_Drv1**|*int*|Age of driver_1
|**DrugUse_Drv1**|*int*|0 for no drug influence on the driver_1 and 1 for yes
|**Not_Clear_Weather**|*int*|0 for clear weather and 1 for not clear weather
|**Not_Dry_Surface**|*float*|0 for dry surface and 1 for not dry surface
|**Collision_Manner**|*Object*| Manner in which the vehicles collided. **Note: Dummy variable, later converted into 5 different int features containg values from 0 to 1 (Head_On,Left_Turn,Rear_End,Same_Direction,Other)**

For remaining variables, please refer to the **data/Data_Dictionary.csv** directory.

## Data Cleaning

- Filled null values with appropriate values
- Renamed Columns
- Set Datetime as the index to organise the dataset
- Dropped useless columns
- Converted as many as possible categorical features to numerical features
- Used Dummy variables

## EDA
- Plotted total number of injuries in each month from 2012 to 2021 to check the distribution of injury.
- Plotted correlation heatmap to check what features are highly correlated to injury in a crash
- Plotted boxplots for all the categorical features to check if they affect injury in a crash or not
- Plotted a horizontal bar chart to find out top 5 values for object type features like Street_Name, Cross_Street, etc.
- Plotted an **Injury Forecasting Graph** that predicts the total number of injuries in a month using an OLS statsmodel.

## Modeling

I trained a total of 11 models, and summarized the results below. Since my stakeholders include motor-vehicle insurance companies and I want to minimize insurance fraud cases for them, **so I chose model with the highest specificity score (ADA Boosting Model,64.63%).** Specificity is the ratio of true negatives to total negatives(tn/(tn+fp)). In our case true negatives are where our model correctly predicted that there was no injury and total negatives are sum of true negatives and false positives ( in our case, false positives are where our model predicted there was an injury but the opposite was true in reality).

||**Model**|**Specificity Score**|
|---|---|---|
|1|Logistic (GridSearch)|64.41%|
|2|Logistic (PCA)|64.31%|
|3|KNN (GridSearch)|63.49%|
|4|SVM|64.27%|
|5|Decision Tree|64.37%|
|6|Bagging Classifier|64.62%|
|7|Random Forest|64.62%|
|8|Extra Tree|64.43%|
|9|Naive Bayes (Bernoulli)|64.43%|
|10|**ADA Boosting**|**64.63%**|
|11|Neural Netork (NN)|64.43%|

**Note:** We can see from the above table that we have hit the upper limit of specificity score as all the models have score around 64.5%.
## Conclusions and Recommendations
- Injury_Severity (0.74), Age, Alcohol & Drug Use were the top correlated features to 'Toatl_injuries.'
- Different collision manner affects injury in a crash.
- Ada Boosting was the best model with the highest specificity score (64.63%).
- Installing video cameras at the top 5 streets/intersections where most accidents occurred would help to find the reason for more crashes so that it could be fixed.
- Free virtual driving lessons and strict punishment on alcohol/drug abuse while driving could help spread awareness about the traffic rules and ultimately less crashes.
