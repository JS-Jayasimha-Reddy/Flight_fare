# *Flight Fare*
> App that predicts the nature of the tweets and label them as "Positive" or "Negative"

## Table of contents
* [General info](#general-info)
* [Model lifecycle](#model-lifecycle)
* [Screenshots of app](#screenshots-of-app)
* [Code sample](#code-sample)
* [Technologies Used](#technologies-used)
* [Setup](#setup)
* [Sources](#sources)
* [Contact](#contact)

## General info
This app determines if a Tweet/sentence is positive or negative/hate speech. Though any general sentence can be used,the title is named "Twitter Sentiment" as the model is 
trained on the tweets from twitter. Hence,the sentiment could be a little biased on how it is perceived on twitter platform.

## Model Lifecycle
The Standard datascience lifecycle was followed for building this model.
1. **Business understanding**- The objective is to determine if a tweet is positive or negative
2. **Data collection**- Dataset acquired from [Kaggle](https://www.kaggle.com/kazanova/sentiment140),the original dataset of 1.6 million tweets were reduced to a random sample of 62000 tweets due to computing limitations
3. **Data preprocessing/Preparation**- Several steps were performed to clean the data like removing dublicates, punctuations,stop words etc
4. **EDA**- Used plots like Word cloud to understand more about the data
5. **Modelling**- Used Naive bayes model with Hyperparameter tuning and roc-auc as the metric
6. **Evaluation**- Used AUC plot and AUC score of test and train data to determine the effectiveness of the model.This was double checked by a confusion matrix
7. **Deployment**- Model was deployed using Streamlit and on AWS server --Click [HERE](http://18.191.219.195:8501) for the demo

## Screenshots of app
#### 1.
<img src="https://github.com/JS-Jayasimha-Reddy/twitter_sentiment/blob/master/Images/tweet2.PNG">

#### 2.
<img src="https://github.com/JS-Jayasimha-Reddy/twitter_sentiment/blob/master/Images/tweet1.PNG">


## Code sample

<img src="https://github.com/JS-Jayasimha-Reddy/twitter_sentiment/blob/master/Images/note3.PNG" >


## Technologies Used

<p float="left">
  <img src="https://github.com/JS-Jayasimha-Reddy/twitter_sentiment/blob/master/Images/anaconda.jpg" width="200" height='150' />
  <img src="https://github.com/JS-Jayasimha-Reddy/twitter_sentiment/blob/master/Images/python.png" width="100" height="100" /> 
  <img src="https://github.com/JS-Jayasimha-Reddy/twitter_sentiment/blob/master/Images/aws.png" width="150" /> 
  <img src="https://github.com/JS-Jayasimha-Reddy/twitter_sentiment/blob/master/Images/sklearn.jpg" width="150" /> 
  <img src="https://github.com/JS-Jayasimha-Reddy/twitter_sentiment/blob/master/Images/streamlit.png" width="150" /> 
</p>


## Setup
- Clone the repository 
- All of the code is written on [Jupyter notebook](https://www.anaconda.com/products/individual) 
- Run the requirements.txt file on the command propmt using **pip install -r requirements.txt** to install the necessary libraries
- The model can be deployed on an AWS server using EC2 instance 

## Future Scope
- Further changes are planned to improve performance and accuracy by using Deep Learning techniques 

## Sources
Most of the code is self written. Some are inspired from various sources and if a code snippet is directly used , respective url is given. 
Sources include :
- [Applied AI](https://www.appliedaicourse.com/)
- [Stack Overflow](https://stackoverflow.com/)
- [Medium](https://medium.com/)

## Contact
- If there any difficulties in running the code or suggestions on imporvements , please email me at : jayasimhaarya@gmail.com
