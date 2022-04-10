import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
import plotly.express as px 
import statsmodels.api as sm 
import io
from PIL import Image 
def app():
        # Web App Title
        st.markdown('''
        # **Home Page**
        This is the **Home page of our app** 
        - > This app will help you to perform multiple task 
        - > Main purpose of this app to make a combine app where can you do all the Analysis related to the Data Science on one Page
        - > This App will do plot animated graphs using Ploty
        - > Will do EDA Analysis Using Pandas-Profiling
        - > Will do Check the Correlation of the Data
        - > And Also check the Normality of the Data.
        ---
        ''')
        st.title("DATA SCIENCE LIFE CYCLE")
        image = Image.open('chart.png')
        st.image(image, caption="Data Science", width=1200, use_column_width=None, clamp=False, channels="RGB", output_format="auto")