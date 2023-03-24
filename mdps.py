# -*- coding: utf-8 -*-
"""
Created on Fri Mar 24 11:46:21 2023

@author: Milind M
"""

import pickle
import numpy as np
import streamlit as st
from streamlit_option_menu import option_menu


#loading the saved model

diabetic_pred_model=pickle.load(open('trained_model_diabetic.sav','rb'))
heart_pred_model=pickle.load(open('trained_model_heart.sav','rb'))

#sidebar for navigation
with st.sidebar:
    selected=option_menu('Multiple Disease Prediction System',
                         
                         ['Diabetic Prediction System',
                          'Heart Disease Prediction System'],
                         
                         icons=['activity','heart'],
                         
                         default_index=0)
    
#diabetic prediciton page
if (selected=='Diabetic Prediction System'):
    st.title("Diabetic prediction model using ML")
    
    col1,col2,col3=st.columns(3)
    with col1:
        Pregnancies=st.text_input("Number of pregnancies")
    with col2:    
        Glucose=st.text_input("Glucose Level")
    with col3:    
        BloodPressure=st.text_input("Number BloodPressure")
    with col1:
        SkinThickness=st.text_input("Number of SkinThickness")
    with col2:
        Insulin=st.text_input("Insulin value")
    with col3:
        BMI=st.text_input("BMI Ratio")
    with col1:
        DiabetesPedigreeFunction=st.text_input("Number of DiabetesPedigreeFunction")
    with col2:
        Age=st.text_input("Age in years")
    
    #end result or prediction note
    diagnosis=""
    
    #create button for result
    if st.button('Dignosis test result'):
        diab_prediction=diabetic_pred_model.predict([[Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age]])
        
        if (diab_prediction[0]==0):
            diagnosis="person dont have diabetis"
        else:
            diagnosis='person have diabetis'
            
    st.success(diagnosis)
            

    
if (selected=='Heart Disease Prediction System'):
    st.title("Heart Disease Prediction System model using ML")
    
    col1,col2,col3=st.columns(3)
    
    with col1:
        age=st.text_input("age in years")
    with col2:
        sex=st.text_input("sex")
    with col3:
        cp=st.text_input("Number cp")
    with col1:
        trestbps=st.text_input("Number of trestbps")
    with col2:
        chol=st.text_input("chol level")
    with col3:
        fbs=st.text_input("fbs")
    with col1:
        restecg=st.text_input("Number of restecg")
    with col2:
        thalach=st.text_input("thalach")
    with col3:
        exang=st.text_input("Number of exang")
    with col1:
        oldpeak=st.text_input("Number of oldpeak")
    with col2:
        slope=st.text_input("slope")
    with col3:
        ca=st.text_input("ca")
    with col1:
        thal=st.text_input("thal")
    
    #end result or prediction note
    diagnosis1=""
    
    #create button for result
    if st.button('Dignosis test result'):
        heart_prediction=heart_pred_model.predict([[age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal]])
        
        if (heart_prediction[0]==0):
            diagnosis1="person dont have heart disease"
        else:
            diagnosis1='person have heart disease'
            
    st.success(diagnosis)