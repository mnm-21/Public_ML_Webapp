# -*- coding: utf-8 -*-
"""
@author Mayank Chandak
"""

import pickle
import streamlit as st
from streamlit_option_menu import option_menu


diabetes_model = pickle.load(open("diabetes_model.sav",'rb'))
heart_model = pickle.load(open("heart_model.sav",'rb'))
parkinson_model = pickle.load(open("parkinson_model.sav",'rb'))


with st.sidebar:
    selection = option_menu('Multiple Disease Prediction System using ML',
                            
                            ['Home Page',
                             'Diabetes',
                             'Heart Disease',
                             'Parkinson\'s Disease'],
                            
                            icons = ['house-door-fill','capsule','heart-pulse-fill','person'],
                            
                            default_index = 0)
    
# Home page    
if selection == 'Home Page':
    st.title('🚀 Welcome to my Multiple Disease Prediction Web App!')
    st.write("Hello! I am Mayank Chandak, a student at IIT Madras "
             "with a keen interest in Artificial Intelligence and Machine Learning. This web app is designed to predict multiple diseases "
             "such as Diabetes, Heart Disease, and Parkinson's Disease using machine learning models. Example values are already filled in "
             "the input boxes. Replace them with the values you want to test!")

    st.warning("**Caution:** Please note that the predictions provided by this web app are based on machine learning models and are not 100% accurate. "
               "Always consult with a healthcare professional for accurate diagnosis and advice.")


# Diabetes page
if(selection =='Diabetes'):
    st.title('🩸 Diabetes Prediction using ML model')
    # Example values for input fields
    example_values = {
    'Pregnancies': 1,
    'Glucose': 89,
    'BloodPressure': 66,
    'SkinThickness': 23,
    'Insulin': 94,
    'BMI': 28.1,
    'DiabetesPedigreeFunction': 0.167,
    'Age': 21
    }
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        Pregnancies = st.text_input('Number of Pregnancies',example_values['Pregnancies'])
        
    with col2:
        Glucose = st.text_input('Glucose Level',example_values['Glucose'])
    
    with col3:
        BloodPressure = st.text_input('Blood Pressure value',example_values['BloodPressure'])
    
    with col1:
        SkinThickness = st.text_input('Skin Thickness value',example_values['SkinThickness'])
    
    with col2:
        Insulin = st.text_input('Insulin Level',example_values['Insulin'])
    
    with col3:
        BMI = st.text_input('BMI value',example_values['BMI'])
    
    with col1:
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value',example_values['DiabetesPedigreeFunction'])
    
    with col2:
        Age = st.text_input('Age of the Person',example_values['Age'])
    
    
    def predict_diabetes(Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age):
        input_values = [Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]
    # Ensure all input values are numeric
        if all(isinstance(val, (int, float)) for val in input_values):
            diab_prediction = diabetes_model.predict([input_values])
            return diab_prediction
        else:
            return "Invalid input values. Ensure all values are numeric."


    diab_diagnosis = ''

    if st.button('📊 Diabetes Test Result'):
        diab_prediction = predict_diabetes(Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age)

        if diab_prediction[0] == 1:
            diab_diagnosis = 'The person is diabetic'
        else:
            diab_diagnosis = 'The person is not diabetic'

    st.success(diab_diagnosis)


# Heart Disease page
if(selection =='Heart Disease'):
    st.title('🫀 Heart Disease Prediction using ML model')
    # Example values for input fields
    example_values = {
        'age': 42,
        'sex': 1,
        'cp': 0,
        'trestbps': 140,
        'chol': 226,
        'fbs': 0,
        'restecg': 1,
        'thalach': 178,
        'exang': 0,
        'oldpeak': 1.2,
        'slope': 2,
        'ca': 0,
        'thal': 2
    }
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        age = st.text_input('Age',example_values['age'])
        
    with col2:
        sex = st.text_input('Sex (0: female, 1: male)',example_values['sex'])
        
    with col3:
        cp = st.text_input('Chest Pain types',example_values['cp'])
        
    with col1:
        trestbps = st.text_input('Resting Blood Pressure',example_values['trestbps'])
        
    with col2:
        chol = st.text_input('Serum Cholestoral in mg/dl',example_values['chol'])
        
    with col3:
        fbs = st.text_input('Fasting Blood Sugar > 120 mg/dl (0: false, 1: true)',example_values['fbs'])
        
    with col1:
        restecg = st.text_input('Resting Electrocardiographic results',example_values['restecg'])
        
    with col2:
        thalach = st.text_input('Maximum Heart Rate achieved',example_values['thalach'])
        
    with col3:
        exang = st.text_input('Exercise Induced Angina',example_values['exang'])
        
    with col1:
        oldpeak = st.text_input('ST depression induced by exercise',example_values['oldpeak'])
        
    with col2:
        slope = st.text_input('Slope of the peak exercise ST segment',example_values['slope'])
        
    with col3:
        ca = st.text_input('Major vessels colored by flourosopy',example_values['ca'])
        
    with col1:
        thal = st.text_input('thal: 1 = normal, 2 = fixed defect, 3 = reversable defect',example_values['thal'])
             
     
        
    def predict_heart_disease(age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal):
        input_values = [age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]
        # Ensure all input values are numeric
        if all(isinstance(val, (int, float)) for val in input_values):
            heart_prediction = heart_model.predict([input_values])
            return heart_prediction
        else:
            return "Invalid input values. Ensure all values are numeric."


    heart_diagnosis = ''

    if st.button('📊 Heart Disease Test Result'):
        heart_prediction = predict_heart_disease(age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal)

        if heart_prediction[0] == 1:
            heart_diagnosis = 'The person is having heart disease'
        else:
            heart_diagnosis = 'The person does not have any heart disease'

    st.success(heart_diagnosis)
    
# Parkinson's page
if selection == 'Parkinson\'s Disease':
    st.title('🧠 Parkinson\'s Disease Prediction using ML model')

    # Example values for input fields
    example_values = {
        'fo': 150,
        'fhi': 180,
        'flo': 120,
        'Jitter_percent': 0.5,
        'Jitter_Abs': 0.02,
        'RAP': 0.3,
        'PPQ': 0.25,
        'DDP': 0.9,
        'Shimmer': 0.03,
        'Shimmer_dB': 0.3,
        'APQ3': 0.02,
        'APQ5': 0.03,
        'APQ': 0.025,
        'DDA': 0.06,
        'NHR': 0.03,
        'HNR': 20,
        'RPDE': 0.5,
        'DFA': 0.6,
        'spread1': -6,
        'spread2': 0.2,
        'D2': 2.2,
        'PPE': 0.25
    }

    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        fo = st.text_input('MDVP : Fo(Hz)', value=example_values['fo'])

    with col2:
        fhi = st.text_input('MDVP : Fhi(Hz)', value=example_values['fhi'])

    with col3:
        flo = st.text_input('MDVP : Flo(Hz)', value=example_values['flo'])

    with col4:
        Jitter_percent = st.text_input('MDVP : Jitter(%)', value=example_values['Jitter_percent'])

    with col5:
        Jitter_Abs = st.text_input('MDVP : Jitter(Abs)', value=example_values['Jitter_Abs'])

    with col1:
        RAP = st.text_input('MDVP : RAP', value=example_values['RAP'])

    with col2:
        PPQ = st.text_input('MDVP : PPQ', value=example_values['PPQ'])

    with col3:
        DDP = st.text_input('Jitter : DDP', value=example_values['DDP'])

    with col4:
        Shimmer = st.text_input('MDVP : Shimmer', value=example_values['Shimmer'])

    with col5:
        Shimmer_dB = st.text_input('MDVP : Shimmer(dB)', value=example_values['Shimmer_dB'])

    with col1:
        APQ3 = st.text_input('Shimmer : APQ3', value=example_values['APQ3'])

    with col2:
        APQ5 = st.text_input('Shimmer : APQ5', value=example_values['APQ5'])

    with col3:
        APQ = st.text_input('MDVP : APQ', value=example_values['APQ'])

    with col4:
        DDA = st.text_input('Shimmer : DDA', value=example_values['DDA'])

    with col5:
        NHR = st.text_input('NHR', value=example_values['NHR'])

    with col1:
        HNR = st.text_input('HNR', value=example_values['HNR'])

    with col2:
        RPDE = st.text_input('RPDE', value=example_values['RPDE'])

    with col3:
        DFA = st.text_input('DFA', value=example_values['DFA'])

    with col4:
        spread1 = st.text_input('spread1', value=example_values['spread1'])

    with col5:
        spread2 = st.text_input('spread2', value=example_values['spread2'])

    with col1:
        D2 = st.text_input('D2', value=example_values['D2'])

    with col2:
        PPE = st.text_input('PPE', value=example_values['PPE'])

        
    
    def predict_parkinson(fo, fhi, flo, Jitter_percent, Jitter_Abs, RAP, PPQ, DDP, Shimmer, Shimmer_dB, APQ3, APQ5, APQ, DDA, NHR, HNR, RPDE, DFA, spread1, spread2, D2, PPE):
    
        input_values = [fo, fhi, flo, Jitter_percent, Jitter_Abs, RAP, PPQ, DDP, Shimmer, Shimmer_dB, APQ3, APQ5, APQ, DDA, NHR, HNR, RPDE, DFA, spread1, spread2, D2, PPE]
    # Ensure all input values are numeric
        if all(isinstance(val, (int, float)) for val in input_values):
            parkinsons_prediction = parkinson_model.predict([input_values])
            return parkinsons_prediction
        else:
            return "Invalid input values. Ensure all values are numeric."


    parkinsons_diagnosis = ''

    if st.button('📊 Parkinson\'s Test Result'):
        parkinsons_prediction = predict_parkinson(fo, fhi, flo, Jitter_percent, Jitter_Abs, RAP, PPQ, DDP, Shimmer, Shimmer_dB, APQ3, APQ5, APQ, DDA, NHR, HNR, RPDE, DFA, spread1, spread2, D2, PPE)

        if parkinsons_prediction[0] == 1:
            parkinsons_diagnosis = "The person has Parkinson's disease"
        else:
            parkinsons_diagnosis = "The person does not have Parkinson's disease"

    st.success(parkinsons_diagnosis)

