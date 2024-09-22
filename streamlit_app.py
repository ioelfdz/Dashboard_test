import streamlit as st
import pandas as pd
import numpy as np
import snowflake.connector
import streamlit_option_menu
from streamlit_option_menu import option_menu
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import datetime
from datetime import datetime, timedelta
from pathlib import Path
from PIL import Image
import base64
import image

def img_to_base64(image_path):
    """Convert image to base64."""
    try:
        with open(image_path, "rb") as img_file:
            return base64.b64encode(img_file.read()).decode()
    except Exception as e:
        logging.error(f"Error converting image to base64: {str(e)}")
        return None

# Set the title and favicon that appear in the Browser's tab bar.
st.set_page_config(
    layout='wide',
    page_title='One4All Rojo PE Charts',
    #page_icon=':earth_americas:', # This is an emoji shortcode. Could be a URL too.
    page_icon="data/o4a_icon.jpg",
)

# Mostrar la imagen con Plotly
logo = Path(__file__).parent/'data/o4a_logo.png'
#st.sidebar.image("logo")
#st.sidebar.image(load_image("logo"), use_column_width=True)

st.sidebar.markdown(
        f'<img src="data/o4a_logo.png" >',
        unsafe_allow_html=True,
    )

# Load and display sidebar image
#img_path = "data/o4a_logo.png"
#img_base64 =img_to_base64(img_path)
#if img_base64:
#    st.sidebar.markdown(
#        f'<img src="data:image/png;base64,{img_base64}" >',
#        unsafe_allow_html=True,
#    )

#DATA_FILENAME = Path(__file__).parent/'data/O4All_shipped.csv'
#df_1 = pd.read_csv(DATA_FILENAME)
#DATA_FILENAME_2 = Path(__file__).parent/'data/O4All_non_shipped.csv'
#df_2 = pd.read_csv(DATA_FILENAME_2)

with st.sidebar:
    selected = option_menu(
        menu_title = "Main Menu",
        options = ["SWBD","LVDO","MC-MCAR","SureSeT","Jobs Journey Map"],
        icons = ["activity","activity","activity","activity", "activity"],
        menu_icon = "cast",
        default_index = 0,
        #orientation = "horizontal",
)
