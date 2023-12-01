import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn import metrics
from sklearn.preprocessing import OrdinalEncoder
import numpy as np
from PIL import Image
import joblib
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
import streamlit.components.v1 as components

_model = joblib.load('sales_.pkl')
st.set_page_config(page_title="Retails Sales Prediction", page_icon=None, layout="wide")


with st.sidebar:
    selected = option_menu("Menu", ["Retail Sales Prediction", "Data Visualization","About"],
                           icons=["house", "graph-up-arrow", "bar-chart-line", "exclamation-circle"],
                           menu_icon="menu-button-wide",
                           default_index=0,
                           styles={"nav-link": {"font-size": "15px", "text-align": "left", "margin": "-2px",
                                                "--hover-color": "#c44a2f"},
                                   "nav-link-selected": {"background-color": "#4a1252"}})
if selected == "Retail Sales Prediction":


    st.header(":rainbow[Retail Sales Prediction]")
    col1, col2 = st.columns(2)
    with col1:
            year = st.text_input('Enter the Year of sales')
            type_ = st.selectbox('Enter the Sales Type(A:1,B:0,C:-1)', (-1, 0, 1))
            dept = st.selectbox('Enter the Department code No',
                                (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 16, 17, 18,
                                 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35,
                                 36, 37, 38, 40, 41, 42, 44, 45, 46, 47, 48, 49, 51, 52, 54, 55, 56,
                                 58, 59, 60, 67, 71, 72, 74, 79, 80, 81, 82, 83, 85, 87, 90, 91, 92,
                                 93, 94, 95, 97, 98, 78, 96, 99, 77, 39, 50, 43, 65))
            cpi = st.text_input('CPI')
            fuel = st.text_input("Estimated Fuel Prize")
            m1 = st.text_input('Markdown Effect 1')
            m3 = st.text_input('Markdown Effect 3')
            m5 = st.text_input('Markdown Effect 5')
            size = st.text_input('Area size of the Shop {Generally 30K to 250K}')

    with col2:
            month = st.text_input('Enter the Month of sales')
            day = st.text_input('Enter the Day of the month')
            store = st.selectbox('Enter the Store No', (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17,
                                                        18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33,
                                                        34,
                                                        35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45))
            temp = st.text_input('Temperature')
            unemp = st.text_input('UnEmployment Rate {Generally ranges between 1 to 20}')
            holiday = st.selectbox('Is it a Holiday day {True:1,False:0} ', (0, 1))
            m2 = st.text_input('Markdown Effect 2')
            m4 = st.text_input('Markdown Effect 4')

    c1, c2, c3 = st.columns([3, 1, 3])
    with c2:
            submit = st.button("Predict")
            if submit:
                data = np.array(
                    [[store, temp, fuel, m1, m2, m3, m4, m5, cpi, unemp, holiday, dept, type_, size, year, month, day]])
                y_pred = _model.predict(data)
                # Assuming y_pred is a numeric value
                st.success("The Weekly sales are {}".format(y_pred))

if selected == "Data Visualization":
    st.header(":rainbow[Tabelau mode using data Visualization]")
    tab1,tab2,tab3,tab4=st.tabs(["EDA ANALYSIS","DEPARTMENT WISE AVG SALES AND TOTAL SALES" ,"STORE WISE AVG SALES AND TOTAL SALES","HOLIDAYS BASED SALES"])
    with tab1:
        with st.container():
            i = Image.open('/Users/rajesh/Desktop/Screenshot 2023-12-01 at 3.50.53 AM.png')
            st.image(i, use_column_width='always')
    with tab2:


        # Define the HTML code for the Tableau visualization
        tableau_html_code = """
        <div class='tableauPlaceholder' id='viz1701407437381' style='position: relative'>
          <noscript><a href='#'><img alt='Dashboard 7' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;RE&#47;RETAIL_STORE_DATA_ANALYSIS&#47;Dashboard7&#47;1_rss.png' style='border: none' /></a></noscript>
          <object class='tableauViz' style='display:none;'>
            <param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' />
            <param name='embed_code_version' value='3' />
            <param name='site_root' value='' />
            <param name='name' value='RETAIL_STORE_DATA_ANALYSIS&#47;Dashboard7' />
            <param name='tabs' value='no' />
            <param name='toolbar' value='yes' />
            <param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;RE&#47;RETAIL_STORE_DATA_ANALYSIS&#47;Dashboard7&#47;1.png' />
            <param name='animate_transition' value='yes' />
            <param name='display_static_image' value='yes' />
            <param name='display_spinner' value='yes' />
            <param name='display_overlay' value='yes' />
            <param name='display_count' value='yes' />
            <param name='language' value='en-GB' />
            <param name='filter' value='publish=yes' />
          </object>
        </div>
        <script type='text/javascript'>
          var divElement = document.getElementById('viz1701407437381');
          var vizElement = divElement.getElementsByTagName('object')[0];
          if (divElement.offsetWidth > 800) {
            vizElement.style.width='100%';
            vizElement.style.height=(divElement.offsetWidth*0.75)+'px';
          } else if (divElement.offsetWidth > 500) {
            vizElement.style.width='100%';
            vizElement.style.height=(divElement.offsetWidth*0.75)+'px';
          } else {
            vizElement.style.width='100%';
            vizElement.style.height='827px';
          }
          var scriptElement = document.createElement('script');
          scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';
          vizElement.parentNode.insertBefore(scriptElement, vizElement);
        </script>
        """

        # Use streamlit.components.v1.html to embed HTML code
        st.components.v1.html(tableau_html_code, height=1000, width=1000)
    with tab3:


        # Define the HTML code for the Tableau visualization
        tableau_html_code1 = """
        <div class='tableauPlaceholder' id='viz1701407903438' style='position: relative'>
          <noscript><a href='#'><img alt='Dashboard 7' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;ST&#47;STORE_WISE&#47;Dashboard7&#47;1_rss.png' style='border: none' /></a></noscript>
          <object class='tableauViz' style='display:none;'>
            <param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' />
            <param name='embed_code_version' value='3' />
            <param name='site_root' value='' />
            <param name='name' value='STORE_WISE&#47;Dashboard7' />
            <param name='tabs' value='no' />
            <param name='toolbar' value='yes' />
            <param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;ST&#47;STORE_WISE&#47;Dashboard7&#47;1.png' />
            <param name='animate_transition' value='yes' />
            <param name='display_static_image' value='yes' />
            <param name='display_spinner' value='yes' />
            <param name='display_overlay' value='yes' />
            <param name='display_count' value='yes' />
            <param name='language' value='en-GB' />
          </object>
        </div>
        <script type='text/javascript'>
          var divElement = document.getElementById('viz1701407903438');
          var vizElement = divElement.getElementsByTagName('object')[0];
          if (divElement.offsetWidth > 800) {
            vizElement.style.width='1000px';
            vizElement.style.height='827px';
          } else if (divElement.offsetWidth > 500) {
            vizElement.style.width='1000px';
            vizElement.style.height='827px';
          } else {
            vizElement.style.width='100%';
            vizElement.style.height='727px';
          }
          var scriptElement = document.createElement('script');
          scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';
          vizElement.parentNode.insertBefore(scriptElement, vizElement);
        </script>
        """

        # Use streamlit.components.v1.html to embed HTML code
        st.components.v1.html(tableau_html_code1, height=1000, width=1000)
    with tab4:


        # Define the HTML code for the Tableau visualization
        tableau_html_code2 = """
        <div class='tableauPlaceholder' id='viz1701408188543' style='position: relative'>
          <noscript><a href='#'><img alt='Dashboard 7' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;ho&#47;holidays_17014081620510&#47;Dashboard7&#47;1_rss.png' style='border: none' /></a></noscript>
          <object class='tableauViz' style='display:none;'>
            <param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' />
            <param name='embed_code_version' value='3' />
            <param name='site_root' value='' />
            <param name='name' value='holidays_17014081620510&#47;Dashboard7' />
            <param name='tabs' value='no' />
            <param name='toolbar' value='yes' />
            <param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;ho&#47;holidays_17014081620510&#47;Dashboard7&#47;1.png' />
            <param name='animate_transition' value='yes' />
            <param name='display_static_image' value='yes' />
            <param name='display_spinner' value='yes' />
            <param name='display_overlay' value='yes' />
            <param name='display_count' value='yes' />
            <param name='language' value='en-GB' />
          </object>
        </div>
        <script type='text/javascript'>
          var divElement = document.getElementById('viz1701408188543');
          var vizElement = divElement.getElementsByTagName('object')[0];
          if (divElement.offsetWidth > 800) {
            vizElement.style.width='1000px';
            vizElement.style.height='827px';
          } else if (divElement.offsetWidth > 500) {
            vizElement.style.width='1000px';
            vizElement.style.height='827px';
          } else {
            vizElement.style.width='100%';
            vizElement.style.height='727px';
          }
          var scriptElement = document.createElement('script');
          scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';
          vizElement.parentNode.insertBefore(scriptElement, vizElement);
        </script>
        """

        # Use streamlit.components.v1.html to embed HTML code
        st.components.v1.html(tableau_html_code2, height=1000, width=1000)



if selected=="About":
    st.header(":rainbow[Retail Sales Analysis]")
    st.write("""
    Retail sales data analysis involves examining and interpreting data related to the performance of retail businesses.
    It encompasses evaluating sales trends, customer behavior, and product performance to make informed business decisions.
    Through techniques such as data visualization and statistical analysis, retailers gain insights into consumer preferences, inventory management, and marketing effectiveness.
    This analytical process aids in optimizing pricing strategies, identifying growth opportunities, and enhancing overall operational efficiency.
    Retailers leverage data-driven insights to stay competitive, improve customer satisfaction, and adapt to evolving market dynamics.""")
    i = Image.open('/Users/rajesh/Desktop/Image.png')
    st.image(i, use_column_width='always')
    st.write("**:rainbow[My Project GitHub link]** ⬇️")
    st.write("https://github.com/Rajeshk513/Retail_Sales_Forecast")