# *Flight Fare*
> App that predicts the flight price for a given Airline 

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
This app predicts the price for a one-way flight given the factors like Airways, Source, Destination and so on. The price , Airways and the regions are limited to the information present in the dataset . Some final features are dropped at the end to make the app mimic real-file examples.

## Model Lifecycle
The Standard datascience lifecycle was followed for building this model.
1. **Business understanding**- The objective is to predict the flight fare for a one-way journey
2. **Data collection**- Dataset acquired from [Kaggle](https://www.kaggle.com/nikhilmittal/flight-fare-prediction-mh/)
3. **Data preprocessing/Preparation**- Several steps were performed to clean the data like removing dublicates,checking for outliers etc.
4. **EDA**- Used plots like Box plot , Violin plot to get more insight on the data
5. **Modelling**- Used Multiple models: KNN ,Randomforest,Gradient Boosted Decision Tree and selected the best performer for deployment 
6. **Evaluation**- Used Mean absolute error and Root mean squared error to determine the effectiveness of the model 
7. **Deployment**- Model was deployed using Streamlit and on Heroku server --Click [HERE](https://flightfare1.herokuapp.com/) for the demo

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
- If there are any difficulties in running the code or suggestions on imporvements , please email me at : jayasimhaarya@gmail.com
