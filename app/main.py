import streamlit as st
import pandas as pd
import numpy as np
import utils

st.title("Data Visualization Dashboard")
st.markdown("This dashboard allows you to visualize data with various interactive features.")

# List of available datasets
datasets = {
    "Benin (Malanville)": "../data/benin-malanville.csv",
    "Sierra Leone (Bumbuna)": "../data/sierraleone-bumbuna.csv",
    "Togo (Dapaong QC)": "../data/togo-dapaong_qc.csv"
}

st.sidebar.header("Customize the Dashboard")
selected_dataset = st.sidebar.selectbox("Select Dataset", list(datasets.keys()))
plot_type = st.sidebar.selectbox("Select Plot Type", ["Line Plot", "Scatter Plot", "Box Plot", "Histogram"])

data_path = datasets[selected_dataset]
data = pd.read_csv(data_path)
data = utils.clean_data(data)

#  plot settings
x_column = st.sidebar.selectbox("X-Axis", data.columns)
y_column = st.sidebar.selectbox("Y-Axis", data.columns)

# Render the appropriate plot based on the selection
if plot_type == "Line Plot":
    utils.generate_line_plot(data, x_column, y_column, "Line Plot")

elif plot_type == "Scatter Plot":
    hue_column = st.sidebar.selectbox("Hue", ["None"] + list(data.columns))
    hue = None if hue_column == "None" else hue_column
    utils.generate_scatter_plot(data, x_column, y_column, "Scatter Plot", hue=hue)

elif plot_type == "Box Plot":
    utils.generate_box_plot(data, x_column, "Box Plot")

elif plot_type == "Histogram":
    utils.generate_histogram(data, x_column, "Histogram")

# Summary statistics
st.header("Summary Statistics")
st.write(utils.get_summary_stats(data))
