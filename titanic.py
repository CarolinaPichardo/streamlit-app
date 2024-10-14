import streamlit as st
import seaborn as sns
import plotly.express as px
import matplotlib.pyplot as plt
import pandas as pd
import time

# Load Titanic dataset from seaborn or a Kaggle CSV if downloaded
titanic = sns.load_dataset("titanic")  # You can also use a local CSV if preferred

# Set page title and layout
st.set_page_config(page_title="Titanic Data Dashboard", layout="wide")

# Define sidebar options for page navigation
page = st.sidebar.selectbox("Select a page", ["General view", "Passengers Information", "Who survived?", "Fare Analysis", "Class and Embarked"])

# Set color palette
color_palette = sns.color_palette("Set2")

# Custom colors for gender
gender_colors = {"male": "#ADD8E6", "female": "#FFB6C1"} 

# Page 1: Overview
if page == "General view":
    st.title("Titanic Dataset Overview")
    st.write("This dashboard visualizes key insights from the Titanic dataset. Use the sidebar to navigate between different sections.")
    
    st.subheader("General view")
    st.metric("Total Passengers", len(titanic))
    st.metric("Survived Passengers", titanic['survived'].sum())



# Page 2: Passenger Demographics
if page == "Passengers Information":
    st.title("Passengers Information")

    col1, col2 = st.columns(2)
    
    # Bar plot for gender distribution
    with col1:
        st.subheader("Gender Distribution")
        fig, ax = plt.subplots()
        sns.countplot(x="sex", data=titanic, palette=gender_colors, ax=ax)
        st.pyplot(fig)

    # Age distribution
    with col2:
        st.subheader("Age Distribution")
        fig, ax = plt.subplots()
        sns.histplot(titanic['age'].dropna(), bins=20, kde=True, color=color_palette[1], ax=ax)
        st.pyplot(fig)
    
    st.write("The dataset consists of more male passengers, and the age distribution shows a wide range of ages with many young and middle-aged passengers.")

# Page 3: Survival Rates
if page == "Who survived?":
    st.title("Who survived?")

    col1, col2 = st.columns(2)

    # Survival rate by gender
    with col1:
        st.subheader("Survival by Gender")
        fig, ax = plt.subplots()
        sns.barplot(x="sex", y="survived", data=titanic, palette=gender_colors, ax=ax)
        st.pyplot(fig)

    # Survival rate by class
    with col2:
        st.subheader("Survival by Passenger Class")
        fig, ax = plt.subplots()
        sns.barplot(x="pclass", y="survived", data=titanic, palette=color_palette, ax=ax)
        st.pyplot(fig)

    st.write("Women had a higher survival rate, and passengers in first class were more likely to survive compared to other classes.")

# Page 4: Fare Analysis
if page == "Fare Analysis":
    st.title("Fare Analysis")

    col1, col2 = st.columns(2)

    # Fare distribution
    with col1:
        st.subheader("Fare Distribution")
        fig, ax = plt.subplots()
        sns.histplot(titanic['fare'], bins=30, kde=True, color=color_palette[1], ax=ax)
        st.pyplot(fig)

    st.write("The fare distribution is heavily right-skewed, with a few passengers paying significantly higher amounts. Higher classes paid more for their tickets.")

# Page 5: Class and Embarked Analysis
if page == "Class and Embarked":
    st.title("Class and Embarked")

    col1, col2 = st.columns(2)

    # Passenger count by class
    with col1:
        st.subheader("Passenger Count by Class")
        fig, ax = plt.subplots()
        sns.countplot(x="pclass", data=titanic, palette=color_palette, ax=ax)
        st.pyplot(fig)

    # Passenger count by embarkation point
    with col2:
        st.subheader("Passenger Count by Embarkation Point")
        fig, ax = plt.subplots()
        sns.countplot(x="embarked", data=titanic, palette=color_palette, ax=ax)
        st.pyplot(fig)

    st.write("Most passengers boarded the Titanic in Southampton. Third class had the highest number of passengers.")
