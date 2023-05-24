# python -m streamlit run main.py

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np



st.title("Streamlit Application for Data Analysis")

# Initialize data as an empty DataFrame
data = pd.DataFrame()

# 1. File uploader
uploaded_file = st.file_uploader("Upload a CSV file", type="csv")

# Check if data is not empty
if uploaded_file is not None:
    data = pd.read_csv(uploaded_file)

    # 2. Display relevant statistics
    st.write("Number of Rows:", data.shape[0])
    st.write("Number of Columns:", data.shape[1])
    st.write("Column Names:", data.columns.tolist())
    st.write("Numerical Columns:", data.select_dtypes(include=[int, float]).columns.tolist())
    st.write("Categorical Columns:", data.select_dtypes(include=[object]).columns.tolist())
    st.write("Boolean Columns:", data.select_dtypes(include=[bool]).columns.tolist())

    # 3. Select columns
    selected_columns = st.multiselect("Select columns", data.columns.tolist())

    # Check if a column has been selected
    if selected_columns is not None:
        for selected_column in selected_columns:
            st.subheader(f"Selected Column: {selected_column}")
            # 4. If numerical, display five number summary and distribution plot
            if np.issubdtype(data[selected_column].dtype, np.number):
                st.write("Five Number Summary")
                st.write("Min:", np.min(data[selected_column]))
                st.write("Q1:", np.percentile(data[selected_column], 25))
                st.write("Median:", np.median(data[selected_column]))
                st.write("Q3:", np.percentile(data[selected_column], 75))
                st.write("Max:", np.max(data[selected_column]))
                
                fig, ax = plt.subplots()
                sns.kdeplot(data[selected_column], fill = True)
                ax.set(title = f"KDE plot for {selected_column}")
                st.pyplot(fig)
                
            # 5. If categorical, display proportions and barplot
            elif np.issubdtype(data[selected_column].dtype, np.object):
                st.write("Category Proportions")
                st.write(data[selected_column].value_counts(normalize=True))

                fig, ax = plt.subplots()
                sns.countplot(data[selected_column], ax=ax)
                ax.set(title = f"Bar plot for {selected_column}")
                st.pyplot(fig)