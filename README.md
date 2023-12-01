# Retail_Sales_Forecast

# python packages:
  used:
  
    import pandas as pd 
    import numpy as np
    import streamlit as st
    from streamlit_option_menu import option_menu
    from PIL import Image
    import joblib
    from sklearn.ensemble import RandomForestRegressor
    import streamlit.components.v1 as components
    from sklearn.tree import DecisionTreeClassifier
    from sklearn.model_selection import train_test_split
    from sklearn import metrics
    from sklearn.preprocessing import OrdinalEncoder
# DATA CLEANING

Remove Duplicate Entries:

    Identify and remove duplicate records from the dataset. Duplicates can distort the analysis by inflating sales figures or creating inconsistencies.
    Handle Missing Values:

    Identify and address missing values in the dataset. Depending on the extent of missing data, you can either remove the records, fill in missing values using methods like mean or      median imputation, or employ more sophisticated techniques based on the nature of the data.
Standardize Data Formats:

    Ensure consistency in data formats, especially for fields like date, time, and currency. Standardizing formats facilitates accurate analysis and reporting.
Correct Inconsistent Data:

    Check for inconsistencies in data entry, such as variations in product names, category names, or units of measurement. Standardize these entries to maintain data integrity

# DATA Visualization:
1. Connect to Data:
Open Tableau and connect to your data source (Excel, CSV, database, etc.). Tableau supports a wide range of data formats.
2. Understand Data Structure:
Once connected, Tableau will display the data structure in the left pane. Familiarize yourself with the dimensions (categorical data) and measures (quantitative data).
3. Drag and Drop:
Start building your visualization by dragging and dropping fields onto the Rows and Columns shelves.
Rows Shelf: Typically holds dimensions (e.g., categories).
Columns Shelf: Typically holds measures (e.g., numeric values).
Marks Card: Define the type of visualization (bar chart, line chart, scatter plot, etc.).
4. Choose Visualization Type:
Tableau offers various visualization types. Choose the one that best suits your data and analysis goals. Right-click on the Marks Card or use the Show Me menu to change the visualization type.
5. Customize Your Visualization:
Customize the appearance and formatting of your visualization.
Color and Size: Use color and size encoding to highlight important information.
Labels and Tooltips: Add labels and tooltips to provide additional context.
Axes and Gridlines: Adjust axes, gridlines, and scales for clarity.
6. Create Dashboards:
Combine multiple visualizations into a dashboard for a comprehensive view.
Dashboard Tab: Create a new dashboard and drag visualizations onto it.
Arrange and Size: Arrange and size components to create a visually appealing layout.
7. Add Interactivity:
Tableau allows you to create interactive dashboards.
Filters: Apply filters to allow users to interactively explore the data.
Highlighting: Enable highlighting to emphasize specific data points.
8. Include Trend Lines and Reference Lines:
Add trend lines or reference lines to highlight patterns or key thresholds in your data.
9. Save and Share:
Save your Tableau workbook. You can also publish it to Tableau Server or Tableau Online for sharing with others.
