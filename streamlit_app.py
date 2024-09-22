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

# Set the title and favicon that appear in the Browser's tab bar.
st.set_page_config(
    layout='wide',
    page_title='One4All Rojo PE Charts',
    page_icon=':earth_americas:', # This is an emoji shortcode. Could be a URL too.
)

# Mostrar la imagen con Plotly
logo = Path(__file__).parent/'data/o4a_logo.gif'
#st.sidebar.image("logo")
#st.sidebar.image(load_image("logo"), use_column_width=True)


#DATA_FILENAME = Path(__file__).parent/'data/O4All_shipped.csv'
#df_1 = pd.read_csv(DATA_FILENAME)
#DATA_FILENAME_2 = Path(__file__).parent/'data/O4All_non_shipped.csv'
#df_2 = pd.read_csv(DATA_FILENAME_2)

with st.sidebar:
    #st.image(logo, width=100)
    selected = option_menu(
        menu_title = "Main Menu",
        options = ["SWBD","LVDO","MC-MCAR","SureSeT","Jobs Journey Map"],
        icons = ["activity","activity","activity","activity", "activity"],
        menu_icon = "cast",
        sidebarlogo = Image.open("logo")
        default_index = 0,
        #orientation = "horizontal",
)
