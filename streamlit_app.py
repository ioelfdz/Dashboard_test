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

#DATA_FILENAME = Path(__file__).parent/'data/O4All_shipped.csv'
#df_1 = pd.read_csv(DATA_FILENAME)
#DATA_FILENAME_2 = Path(__file__).parent/'data/O4All_non_shipped.csv'
#df_2 = pd.read_csv(DATA_FILENAME_2)

data_files = {
    'df_1': Path(__file__).parent / 'data/O4All_LVDO_NS_C.csv',
    'df_2': Path(__file__).parent / 'data/O4All_LVDO_NS_DT.csv',
    'df_3': Path(__file__).parent / 'data/O4All_LVDO_NS_MR.csv',
    'df_4': Path(__file__).parent / 'data/O4All_LVDO_NS_TX.csv',
    'df_5': Path(__file__).parent / 'data/O4All_LVDO_S_C.csv',
    'df_6': Path(__file__).parent / 'data/O4All_LVDO_S_DT.csv',
    'df_7': Path(__file__).parent / 'data/O4All_LVDO_S_MR.csv',
    'df_8': Path(__file__).parent / 'data/O4All_LVDO_S_TX.csv',
    'df_9': Path(__file__).parent / 'data/O4All_MC_NS_C.csv',
    'df_10': Path(__file__).parent / 'data/O4All_MC_NS_DT.csv',
    'df_11': Path(__file__).parent / 'data/O4All_MC_NS_MR.csv',
    'df_12': Path(__file__).parent / 'data/O4All_MC_NS_TX.csv',
    'df_13': Path(__file__).parent / 'data/O4All_MC_S_C.csv',
    'df_14': Path(__file__).parent / 'data/O4All_MC_S_DT.csv',
    'df_15': Path(__file__).parent / 'data/O4All_MC_S_MR.csv',
    'df_16': Path(__file__).parent / 'data/O4All_MC_S_TX.csv',
    'df_17': Path(__file__).parent / 'data/O4All_SS_NS_C.csv',
    'df_18': Path(__file__).parent / 'data/O4All_SS_NS_DT.csv',
    'df_19': Path(__file__).parent / 'data/O4All_SS_NS_MR.csv',
    'df_20': Path(__file__).parent / 'data/O4All_SS_NS_TX.csv',
    'df_21': Path(__file__).parent / 'data/O4All_SS_S_C.csv',
    'df_22': Path(__file__).parent / 'data/O4All_SS_S_DT.csv',
    'df_23': Path(__file__).parent / 'data/O4All_SS_S_MR.csv',
    'df_24': Path(__file__).parent / 'data/O4All_SS_S_TX.csv',
    'df_25': Path(__file__).parent / 'data/O4All_SWBD_NS_C.csv',
    'df_26': Path(__file__).parent / 'data/O4All_SWBD_NS_DT.csv',
    'df_27': Path(__file__).parent / 'data/O4All_SWBD_NS_MR.csv',
    'df_28': Path(__file__).parent / 'data/O4All_SWBD_NS_TX.csv',
    'df_29': Path(__file__).parent / 'data/O4All_SWBD_S_C.csv',
    'df_30': Path(__file__).parent / 'data/O4All_SWBD_S_DT.csv',
    'df_31': Path(__file__).parent / 'data/O4All_SWBD_S_MR.csv',
    'df_32': Path(__file__).parent / 'data/O4All_SWBD_S_TX.csv'
}

dfs = {}
for key, file_path in data_files.items():
    dfs[key] = pd.read_csv(file_path)
#print(dfs)

with st.sidebar:
    selected = option_menu(
    menu_title = "Main Menu",
    options = ["SWBD","LVDO","MC-MCAR","SureSeT","Jobs Journey Map"],
    icons = ["activity","activity","activity","activity", "activity"],
    menu_icon = "cast",
    default_index = 0,
    #orientation = "horizontal",
)
if selected == "SWBD":
    st.header('SWBD One4All')
    # Create a row layout
    c1, c2= st.columns(2)
    c3, c4= st.columns(2)
    c5, c6= st.columns(2)
    c7, c7a= st.columns((99,1))
    c8, c8a= st.columns((99,1))

 #   with st.container():
 #       c1.write("Digital Tools - Shipped Jobs")
 #       c2.write("Digital Tools - Non Shipped Jobs")

 #   with st.container():
 #       c3.write("Correlation - Shipped Jobs")
 #       c4.write("Correlation - Non Shipped Jobs")

 #   with st.container():
 #       c5.write("Reliability - Shipped Jobs")
 #       c6.write("Reliability - Non Shipped Jobs") 

 #   with st.container():
 #       c7.header("Reliability Data Table - Shipped Jobs") 

 #   with st.container():
 #       c8.header("Reliability Data Table - Non Shipped Jobs") 

    with c1:
        df_s = dfs['df_30']

        categories = ['Aid Mapics', 'Ampere Compare', 'CrossCheck', 'Mapics Compare', 'Reconfigure', 'Refresh']
        df_s['Type'] = df_s['Type'].astype(str)

        # Obtener los años únicos del DataFrame
        complexity = df_s['Type'].unique()
        
        fig = go.Figure()

        for index, row in df_s.iterrows():
            fig.add_trace(go.Scatterpolar(
                r=row.iloc[1:],  
                theta=categories,
                fill='toself',
                name=row.iloc[0], 
            ))
        fig.update_layout(
        template=None,
        #plot_bgcolor='white',
        title="Digital Tools - SWBD Shipped Jobs <br> (Current Month & M-1)", 
        font=dict(
                family="Arial",  
                size=12,  
                color="dark grey"),  
        polar=dict(
            radialaxis=dict(
            visible=True,
            range=[0, 100]
            )),
            width=400, 
        height=500, 
        showlegend=True,

        legend=dict(
                orientation="h",
                yanchor="top",
            ),
            annotations=[dict(text="Month - Complexity:", showarrow=False, x=0.7, y=-0.1, align="left", xanchor='right', yanchor='bottom')]
        )

        # Display the chart in Streamlit
        st.plotly_chart(fig)
           
    with c2:
        df_ns = dfs['df_26']
        
        categories = ['Aid Mapics', 'Ampere Compare', 'CrossCheck', 'Mapics Compare', 'Reconfigure', 'Refresh']
        df_ns['Type'] = df_ns['Type'].astype(str)

        # Obtener los años únicos del DataFrame
        complexity = df_ns['Type'].unique()

        fig = go.Figure()

        for index, row in df_ns.iterrows():
            fig.add_trace(go.Scatterpolar(
                r=row.iloc[1:],  
                theta=categories,
                fill='toself',
                name=row.iloc[0], 
            ))
        fig.update_layout(
        template=None,
        #plot_bgcolor='white',
        title="Digital Tools - SWBD Non Shipped Jobs <br> (Current Month & M+1)", 
        font=dict(
                family="Arial",  
                size=12,  
                color="dark grey"),  
        polar=dict(
            radialaxis=dict(
            visible=True,
            range=[0, 100]
            )),
            width=400, 
        height=500, 
        showlegend=True,

        legend=dict(
                orientation="h",
                yanchor="top",
            ),
            annotations=[dict(text="Month - Complexity:", showarrow=False, x=0.7, y=-0.1, align="left", xanchor='right', yanchor='bottom')]
        )

        # Display the chart in Streamlit
        st.plotly_chart(fig)
    with c3:
        df_s = dfs['df_29']

        fig = px.scatter_3d(df_s, x='Reliability Level', y='DPU_Percent', z='ANDON_Percent',
                   color='Job_Cx', size='Reliability Value',width=750, height=600, title="Correlation SWBD Shipped Jobs <br> (Current Month & M-1)",
                   category_orders={'Reliability Level': ['Good','Acceptable','Low','Extremely Low']})
        fig.update_layout(
            template=None,
            title_font=dict(family="Arial", size=16, weight="bold", color="dark grey" ),
            scene=dict(
                xaxis_title='Reliability Level',
                yaxis_title='DPU (%)',
                zaxis_title='ANDON (%)'
                
            )
)

        # Display the chart in Streamlit
        st.plotly_chart(fig)

    with c4:
        df_ns = dfs['df_25']
        fig = px.scatter_3d(df_ns, x='Reliability Level', y='Reliability Value', z='Complexity',
                   color='Job_Cx', size='Reliability Value',width=750, height=600, title="Correlation SWBD Non Shipped Jobs <br> (Current Month & M+1)",
                   category_orders={'Reliability Level': ['Good','Acceptable','Low','Extremely Low']})
        
        fig.update_layout(
            template=None,
            title_font=dict(family="Arial", size=16, weight="bold", color="dark grey" ),
            scene=dict(
                xaxis_title='Reliability Level',
                yaxis_title='Reliability',
                zaxis = dict(
                    title='Complexity',
                    dtick = 1)

            )
)
        # Display the chart in Streamlit
        st.plotly_chart(fig)

    with c5:
        df_s = dfs['df_31']
        color_palette = {'Good': 'green', 'Acceptable': 'yellow', 'Low': 'orange', 'Extremely Low': 'red'}

        fig = px.bar(df_s, y="Date", x='Reliability', color='Reliability Level', color_discrete_map=color_palette, title="Reliability SWBD Shipped Jobs <br> (Current Month & M-1)", 
                        barmode='stack'  # Utiliza el modo de gráficos apilados
        )
        fig.update_layout(
            template=None,
            title_font=dict(family="Arial", size=16, weight="bold", color="dark grey" ), 
            bargap=0.1, width=400, height=500)

        # Display the chart in Streamlit
        st.plotly_chart(fig)

    with c6:
        df_ns = dfs['df_27']
        color_palette = {'Good': 'green', 'Acceptable': 'yellow', 'Low': 'orange', 'Extremely Low': 'red'}

        fig = px.bar(df_ns, y="Date", x='Reliability', category_orders={"Date": df_ns['Date'].unique().tolist()}, color='Reliability Level', color_discrete_map=color_palette, title="Reliability SWBD Non Shipped Jobs <br> (Current Month & M+1)",
                    barmode='stack'  # Utiliza el modo de gráficos apilados
        )
        fig.update_layout(
            template=None,
            title_font=dict(family="Arial", size=16, weight="bold", color="dark grey" ), 
            bargap=0.1, width=400, height=500,)

        # Display the chart in Streamlit
        st.plotly_chart(fig)

    with c7:
        df_s = dfs['df_32']

        fig = go.Figure(go.Table(
            header={"values": df_s.columns},
            cells={"values": df_s.sort_values(by='Reliability Value', ascending=True).T.values},  # Sort the values before displaying
            columnwidth=[24, 24, 12, 6,6,6,25,25,12,12,12,12,6,6]
        ))

        fig.update_layout(
            updatemenus=[{
                "y": 1 - (i / 5),
                "buttons": [{
                    "label": c,
                    "method": "update",
                    "args": [{"cells": {"values": df_s.loc[df_s[menu].eq(c)].sort_values(by='Reliability Value', ascending=True).T.values}}],
                } for c in ["All"] + df_s[menu].unique().tolist()],
            } for i, menu in enumerate(["Reliability Level", "Complexity", "EE Name", "MD Name"])],

            annotations=[dict(text="Reliability Level:", showarrow=False,x=-0.05, y=1.06, align="left", xanchor='right', yanchor='top'),
                        dict(text="Complexity:", showarrow=False,x=-0.05, y=0.86, align="right", xanchor='right', yanchor='top'),
                        dict(text="Electrical Engineer:", showarrow=False,x=-0.05, y=0.68, align="right", xanchor='right', yanchor='top'),
                        dict(text="Mechanical Engineer:", showarrow=False,x=-0.05, y=0.48, align="right", xanchor='right', yanchor='top')],
        )
        fig.update_layout(title="SWBD Shipped Jobs - Reliability (Current Month & M-1)",
                        font=dict(
                                family="Arial",  
                                size=12,  
                                color="dark grey"),width=1600,height=500
                        )

        # Display the chart in Streamlit
        st.plotly_chart(fig)

    with c8:
        df_ns = dfs['df_28']

        fig = go.Figure(go.Table(
            header={"values": df_ns.columns},
            cells={"values": df_ns.sort_values(by='Reliability Value', ascending=True).T.values},  # Sort the values before displaying
            columnwidth=[24, 24, 12, 6,6,6,25,25,12,12,12,12,6,6]
        ))

        fig.update_layout(
            updatemenus=[{
                "y": 1 - (i / 5),
                "buttons": [{
                    "label": c,
                    "method": "update",
                    "args": [{"cells": {"values": df_ns.loc[df_ns[menu].eq(c)].sort_values(by='Reliability Value', ascending=True).T.values}}],
                } for c in ["All"] + df_ns[menu].unique().tolist()],
            } for i, menu in enumerate(["Reliability Level", "Complexity", "EE Name", "MD Name"])],
        
            annotations=[dict(text="Reliability Level:", showarrow=False,x=-0.05, y=1.06, align="left", xanchor='right', yanchor='top'),
                        dict(text="Complexity:", showarrow=False,x=-0.05, y=0.86, align="right", xanchor='right', yanchor='top'),
                        dict(text="Electrical Engineer:", showarrow=False,x=-0.05, y=0.68, align="right", xanchor='right', yanchor='top'),
                        dict(text="Mechanical Engineer:", showarrow=False,x=-0.05, y=0.48, align="right", xanchor='right', yanchor='top')],
        )


        fig.update_layout(title="SWBD Non Shipped Jobs - Reliability (Current Month & M+1)",
                        font=dict(
                                family="Arial",  
                                size=12,  
                                color="dark grey"),width=1600,height=500
                        )

        # Display the chart in Streamlit
        st.plotly_chart(fig)


if selected == "LVDO":
    st.header('LVDO One4All')
    # Create a row layout
    c1, c2= st.columns(2)
    c3, c4= st.columns(2)
    c5, c6= st.columns(2)
    c7, c7a= st.columns((99,1))
    c8, c8a= st.columns((99,1))

    with c1:
        df_s = dfs['df_6']

        categories = ['Aid Mapics', 'Ampere Compare', 'CrossCheck', 'Mapics Compare', 'Reconfigure', 'Refresh']
        df_s['Type'] = df_s['Type'].astype(str)

        # Obtener los años únicos del DataFrame
        complexity = df_s['Type'].unique()
        
        fig = go.Figure()

        for index, row in df_s.iterrows():
            fig.add_trace(go.Scatterpolar(
                r=row.iloc[1:],  
                theta=categories,
                fill='toself',
                name=row.iloc[0], 
            ))
        fig.update_layout(
        template=None,
        #plot_bgcolor='white',
        title="Digital Tools - LVDO Shipped Jobs <br> (Current Month & M-1)",
        font=dict(
                family="Arial",  
                size=12,  
                color="dark grey"),  
        polar=dict(
            radialaxis=dict(
            visible=True,
            range=[0, 100]
            )),
            width=400, 
        height=500, 
        showlegend=True,

        legend=dict(
                orientation="h",
                yanchor="top",
            ),
            annotations=[dict(text="Month - Complexity:", showarrow=False, x=0.7, y=-0.1, align="left", xanchor='right', yanchor='bottom')]
        )

        # Display the chart in Streamlit
        st.plotly_chart(fig)
           
    with c2:
        df_ns = dfs['df_2']
        
        categories = ['Aid Mapics', 'Ampere Compare', 'CrossCheck', 'Mapics Compare', 'Reconfigure', 'Refresh']
        df_ns['Type'] = df_ns['Type'].astype(str)

        # Obtener los años únicos del DataFrame
        complexity = df_ns['Type'].unique()

        fig = go.Figure()

        for index, row in df_ns.iterrows():
            fig.add_trace(go.Scatterpolar(
                r=row.iloc[1:],  
                theta=categories,
                fill='toself',
                name=row.iloc[0], 
            ))
        fig.update_layout(
        template=None,
        #plot_bgcolor='white',
        title="Digital Tools - LVDO Non Shipped Jobs <br> (Current Month & M+1)", 
        font=dict(
                family="Arial",  
                size=12,  
                color="dark grey"),  
        polar=dict(
            radialaxis=dict(
            visible=True,
            range=[0, 100]
            )),
            width=400, 
        height=500, 
        showlegend=True,

        legend=dict(
                orientation="h",
                yanchor="top",
            ),
            annotations=[dict(text="Month - Complexity:", showarrow=False, x=0.7, y=-0.1, align="left", xanchor='right', yanchor='bottom')]
        )

        # Display the chart in Streamlit
        st.plotly_chart(fig)

    with c3:
        df_s = dfs['df_5']

        fig = px.scatter_3d(df_s, x='Reliability Level', y='DPU_Percent', z='ANDON_Percent',
                   color='Job_Cx', size='Reliability Value',width=750, height=600, title="Correlation LVDO Shipped Jobs <br> (Current Month & M-1)",
                   category_orders={'Reliability Level': ['Good','Acceptable','Low','Extremely Low']})
        fig.update_layout(
            template=None,
            title_font=dict(family="Arial", size=16, weight="bold", color="dark grey" ),
            scene=dict(
                xaxis_title='Reliability Level',
                yaxis_title='DPU (%)',
                zaxis_title='ANDON (%)'
                
            )
)

        # Display the chart in Streamlit
        st.plotly_chart(fig)

    with c4:
        df_ns = dfs['df_1']
        fig = px.scatter_3d(df_ns, x='Reliability Level', y='Reliability Value', z='Complexity',
                   color='Job_Cx', size='Reliability Value',width=750, height=600, title="Correlation LVDO Non Shipped Jobs <br> (Current Month & M+1)",
                   category_orders={'Reliability Level': ['Good','Acceptable','Low','Extremely Low']})

        fig.update_layout(
            template=None,
            title_font=dict(family="Arial", size=16, weight="bold", color="dark grey" ),
            scene=dict(
                xaxis_title='Reliability Level',
                yaxis_title='Reliability',
                zaxis = dict(
                    title='Complexity',
                    dtick = 1)

            )
)
        # Display the chart in Streamlit
        st.plotly_chart(fig)

    with c5:
        df_s = dfs['df_7']
        color_palette = {'Good': 'green', 'Acceptable': 'yellow', 'Low': 'orange', 'Extremely Low': 'red'}

        fig = px.bar(df_s, y="Date", x='Reliability', color='Reliability Level', color_discrete_map=color_palette, title="Reliability LVDO Shipped Jobs <br> (Current Month & M-1)", 
                    barmode='stack'  # Utiliza el modo de gráficos apilados
        )
        fig.update_layout(
            template=None,
            title_font=dict(family="Arial", size=16, weight="bold", color="dark grey" ), 
            bargap=0.1, width=400, height=500)

        # Display the chart in Streamlit
        st.plotly_chart(fig)

    with c6:
        df_ns = dfs['df_3']
        color_palette = {'Good': 'green', 'Acceptable': 'yellow', 'Low': 'orange', 'Extremely Low': 'red'}

        fig = px.bar(df_ns, y="Date", x='Reliability', category_orders={"Date": df_ns['Date'].unique().tolist()}, color='Reliability Level', color_discrete_map=color_palette, title="Reliability LVDO Non Shipped Jobs <br> (Current Month & M+1)", 
                    barmode='stack'  # Utiliza el modo de gráficos apilados
        )
        fig.update_layout(
            template=None,
            title_font=dict(family="Arial", size=16, weight="bold", color="dark grey" ), 
            bargap=0.1, width=400, height=500,)

        # Display the chart in Streamlit
        st.plotly_chart(fig)

    with c7:
        df_s = dfs['df_8']

        fig = go.Figure(go.Table(
            header={"values": df_s.columns},
            cells={"values": df_s.sort_values(by='Reliability Value', ascending=True).T.values},  # Sort the values before displaying
            columnwidth=[24, 24, 12, 6,6,6,25,25,12,12,12,12,6,6]
        ))

        fig.update_layout(
            updatemenus=[{
                "y": 1 - (i / 5),
                "buttons": [{
                    "label": c,
                    "method": "update",
                    "args": [{"cells": {"values": df_s.loc[df_s[menu].eq(c)].sort_values(by='Reliability Value', ascending=True).T.values}}],
                } for c in ["All"] + df_s[menu].unique().tolist()],
            } for i, menu in enumerate(["Reliability Level", "Complexity", "EE Name", "MD Name"])],
        
            annotations=[dict(text="Reliability Level:", showarrow=False,x=-0.05, y=1.06, align="left", xanchor='right', yanchor='top'),
                        dict(text="Complexity:", showarrow=False,x=-0.05, y=0.86, align="right", xanchor='right', yanchor='top'),
                        dict(text="Electrical Engineer:", showarrow=False,x=-0.05, y=0.68, align="right", xanchor='right', yanchor='top'),
                        dict(text="Mechanical Engineer:", showarrow=False,x=-0.05, y=0.48, align="right", xanchor='right', yanchor='top')],
        )
        fig.update_layout(title="LVDO Shipped Jobs - Reliability (Current Month & M-1)",
                          font=dict(
                                family="Arial",  
                                size=12,  
                                color="dark grey"),width=1600,height=500)

        # Display the chart in Streamlit
        st.plotly_chart(fig)

    with c8:
        df_ns = dfs['df_4']

        fig = go.Figure(go.Table(
            header={"values": df_ns.columns},
            cells={"values": df_ns.sort_values(by='Reliability Value', ascending=True).T.values},  # Sort the values before displaying
            columnwidth=[24, 24, 12, 6,6,6,25,25,12,12,12,12,6,6]
        ))

        fig.update_layout(
            updatemenus=[{
                "y": 1 - (i / 5),
                "buttons": [{
                    "label": c,
                    "method": "update",
                    "args": [{"cells": {"values": df_ns.loc[df_ns[menu].eq(c)].sort_values(by='Reliability Value', ascending=True).T.values}}],
                } for c in ["All"] + df_ns[menu].unique().tolist()],
            } for i, menu in enumerate(["Reliability Level", "Complexity", "EE Name", "MD Name"])],

            annotations=[dict(text="Reliability Level:", showarrow=False,x=-0.05, y=1.06, align="left", xanchor='right', yanchor='top'),
                        dict(text="Complexity:", showarrow=False,x=-0.05, y=0.86, align="right", xanchor='right', yanchor='top'),
                        dict(text="Electrical Engineer:", showarrow=False,x=-0.05, y=0.68, align="right", xanchor='right', yanchor='top'),
                        dict(text="Mechanical Engineer:", showarrow=False,x=-0.05, y=0.48, align="right", xanchor='right', yanchor='top')],
        )


        fig.update_layout(title="LVDO Non Shipped Jobs - Reliability (Current Month & M+1)",
                        font=dict(
                                family="Arial",  
                                size=12,  
                                color="dark grey"),width=1600,height=500)

        # Display the chart in Streamlit
        st.plotly_chart(fig)

if selected == "MC-MCAR":
    st.header('MC-MCAR One4All')
    # Create a row layout
    c1, c2= st.columns(2)
    c3, c4= st.columns(2)
    c5, c6= st.columns(2)
    c7, c7a= st.columns((99,1))
    c8, c8a= st.columns((99,1))

    with c1:
        df_s = dfs['df_14']

        categories = ['Aid Mapics', 'Ampere Compare', 'CrossCheck', 'Mapics Compare', 'Reconfigure', 'Refresh']
        df_s['Type'] = df_s['Type'].astype(str)

        # Obtener los años únicos del DataFrame
        complexity = df_s['Type'].unique()
        
        fig = go.Figure()

        for index, row in df_s.iterrows():
            fig.add_trace(go.Scatterpolar(
                r=row.iloc[1:],  
                theta=categories,
                fill='toself',
                name=row.iloc[0], 
            ))
        fig.update_layout(
        template=None,
        #plot_bgcolor='white',
        title="Digital Tools - MC-MCAR Shipped Jobs <br> (Current Month & M-1)",
        font=dict(
                family="Arial",  
                size=12,  
                color="dark grey"),  
        polar=dict(
            radialaxis=dict(
            visible=True,
            range=[0, 100]
            )),
            width=400, 
        height=500, 
        showlegend=True,

        legend=dict(
                orientation="h",
                yanchor="top",
            ),
            annotations=[dict(text="Month - Complexity:", showarrow=False, x=0.7, y=-0.1, align="left", xanchor='right', yanchor='bottom')]
        )

        # Display the chart in Streamlit
        st.plotly_chart(fig)
           
    with c2:
        df_ns = dfs['df_10']
        
        categories = ['Aid Mapics', 'Ampere Compare', 'CrossCheck', 'Mapics Compare', 'Reconfigure', 'Refresh']
        df_ns['Type'] = df_ns['Type'].astype(str)

        # Obtener los años únicos del DataFrame
        complexity = df_ns['Type'].unique()

        fig = go.Figure()

        for index, row in df_ns.iterrows():
            fig.add_trace(go.Scatterpolar(
                r=row.iloc[1:],  
                theta=categories,
                fill='toself',
                name=row.iloc[0], 
            ))
        fig.update_layout(
        template=None,
        #plot_bgcolor='white',
        title="Digital Tools - MC-MCAR Non Shipped Jobs <br> (Current Month & M+1)", 
        font=dict(
                family="Arial",  
                size=12,  
                color="dark grey"),  
        polar=dict(
            radialaxis=dict(
            visible=True,
            range=[0, 100]
            )),
            width=400, 
        height=500, 
        showlegend=True,

        legend=dict(
                orientation="h",
                yanchor="top",
            ),
            annotations=[dict(text="Month - Complexity:", showarrow=False, x=0.7, y=-0.1, align="left", xanchor='right', yanchor='bottom')]
        )

        # Display the chart in Streamlit
        st.plotly_chart(fig)

    with c3:
        df_s = dfs['df_13']

        fig = px.scatter_3d(df_s, x='Reliability Level', y='DPU_Percent', z='ANDON_Percent',
                   color='Job_Cx', size='Reliability Value',width=750, height=600, title="Correlation MC-MCAR Shipped Jobs <br> (Current Month & M-1)",
                   category_orders={'Reliability Level': ['Good','Acceptable','Low','Extremely Low']})
        
        fig.update_layout(
            template=None,
            title_font=dict(family="Arial", size=16, weight="bold", color="dark grey" ),
            scene=dict(
                xaxis_title='Reliability Level',
                yaxis_title='DPU (%)',
                zaxis_title='ANDON (%)'
            )
)

        # Display the chart in Streamlit
        st.plotly_chart(fig)

    with c4:
        df_ns = dfs['df_9']

        fig = px.scatter_3d(df_ns, x='Reliability Level', y='Reliability Value', z='Complexity',
                   color='Job_Cx', size='Reliability Value',width=750, height=600, title="Correlation MC-MCAR Non Shipped Jobs <br> (Current Month & M+1)",
                   category_orders={'Reliability Level': ['Good','Acceptable','Low','Extremely Low']})

        fig.update_layout(
            template=None,
            title_font=dict(family="Arial", size=16, weight="bold", color="dark grey" ),
            scene=dict(
                xaxis_title='Reliability Level',
                yaxis_title='Reliability',
                zaxis = dict(
                    title='Complexity',
                    dtick = 1)
            )
)
        # Display the chart in Streamlit
        st.plotly_chart(fig)

    with c5:
        df_s = dfs['df_15']
        color_palette = {'Good': 'green', 'Acceptable': 'yellow', 'Low': 'orange', 'Extremely Low': 'red'}

        fig = px.bar(df_s, y="Date", x='Reliability', color='Reliability Level', color_discrete_map=color_palette, title="Reliability MC-MCAR Shipped Jobs <br> (Current Month & M-1)",
                    barmode='stack'  # Utiliza el modo de gráficos apilados
        )
        fig.update_layout(
            template=None,
            title_font=dict(family="Arial", size=16, weight="bold", color="dark grey" ), 
            bargap=0.1, width=400, height=500)

        # Display the chart in Streamlit
        st.plotly_chart(fig)

    with c6:
        df_ns = dfs['df_11']
        color_palette = {'Good': 'green', 'Acceptable': 'yellow', 'Low': 'orange', 'Extremely Low': 'red'}

        fig = px.bar(df_ns, y="Date", x='Reliability', category_orders={"Date": df_ns['Date'].unique().tolist()}, color='Reliability Level', color_discrete_map=color_palette, title="Reliability MC-MCAR Non Shipped Jobs <br> (Current Month & M+1)",
                    barmode='stack'  # Utiliza el modo de gráficos apilados
        )
        fig.update_layout(
            template=None,
            title_font=dict(family="Arial", size=16, weight="bold", color="dark grey" ), 
            bargap=0.1, width=400, height=500,)

        # Display the chart in Streamlit
        st.plotly_chart(fig)

    with c7:
        df_s = dfs['df_16']

        fig = go.Figure(go.Table(
            header={"values": df_s.columns},
            cells={"values": df_s.sort_values(by='Reliability Value', ascending=True).T.values},  # Sort the values before displaying
            columnwidth=[24, 24, 12, 6,6,6,25,25,12,12,12,12,6,6]
        ))

        fig.update_layout(
            updatemenus=[{
                "y": 1 - (i / 5),
                "buttons": [{
                    "label": c,
                    "method": "update",
                    "args": [{"cells": {"values": df_s.loc[df_s[menu].eq(c)].sort_values(by='Reliability Value', ascending=True).T.values}}],
                } for c in ["All"] + df_s[menu].unique().tolist()],
            } for i, menu in enumerate(["Reliability Level", "Complexity", "EE Name", "MD Name"])],
        
            annotations=[dict(text="Reliability Level:", showarrow=False,x=-0.05, y=1.06, align="left", xanchor='right', yanchor='top'),
                        dict(text="Complexity:", showarrow=False,x=-0.05, y=0.86, align="right", xanchor='right', yanchor='top'),
                        dict(text="Electrical Engineer:", showarrow=False,x=-0.05, y=0.68, align="right", xanchor='right', yanchor='top'),
                        dict(text="Mechanical Engineer:", showarrow=False,x=-0.05, y=0.48, align="right", xanchor='right', yanchor='top')],
        )
        fig.update_layout(title="MC-MCAR Shipped Jobs - Reliability (Current Month & M-1)",
                        font=dict(
                                family="Arial",  
                                size=12,  
                                color="dark grey"),width=1600,height=500)

        # Display the chart in Streamlit
        st.plotly_chart(fig)

    with c8:
        df_ns = dfs['df_12']

        fig = go.Figure(go.Table(
            header={"values": df_ns.columns},
            cells={"values": df_ns.sort_values(by='Reliability Value', ascending=True).T.values},  # Sort the values before displaying
            columnwidth=[24, 24, 12, 6,6,6,25,25,12,12,12,12,6,6]
        ))

        fig.update_layout(
            updatemenus=[{
                "y": 1 - (i / 5),
                "buttons": [{
                    "label": c,
                    "method": "update",
                    "args": [{"cells": {"values": df_ns.loc[df_ns[menu].eq(c)].sort_values(by='Reliability Value', ascending=True).T.values}}],
                } for c in ["All"] + df_ns[menu].unique().tolist()],
            } for i, menu in enumerate(["Reliability Level", "Complexity", "EE Name", "MD Name"])],

            annotations=[dict(text="Reliability Level:", showarrow=False,x=-0.05, y=1.06, align="left", xanchor='right', yanchor='top'),
                        dict(text="Complexity:", showarrow=False,x=-0.05, y=0.86, align="right", xanchor='right', yanchor='top'),
                        dict(text="Electrical Engineer:", showarrow=False,x=-0.05, y=0.68, align="right", xanchor='right', yanchor='top'),
                        dict(text="Mechanical Engineer:", showarrow=False,x=-0.05, y=0.48, align="right", xanchor='right', yanchor='top')],
        )


        fig.update_layout(title="MC-MCAR Non Shipped Jobs - Reliability (Current Month & M+1)",
                        font=dict(
                                family="Arial",  
                                size=12,  
                                color="dark grey"),width=1600,height=500)

        # Display the chart in Streamlit
        st.plotly_chart(fig)

if selected == "SureSeT":
    st.header('SureSeT One4All')
    # Create a row layout
    c1, c2= st.columns(2)
    c3, c4= st.columns(2)
    c5, c6= st.columns(2)
    c7, c7a= st.columns((99,1))
    c8, c8a= st.columns((99,1))

    with c1:
        df_s = dfs['df_22']

        categories = ['Aid Mapics', 'Ampere Compare', 'CrossCheck', 'Mapics Compare', 'Reconfigure', 'Refresh']
        df_s['Type'] = df_s['Type'].astype(str)

        # Obtener los años únicos del DataFrame
        complexity = df_s['Type'].unique()
        
        fig = go.Figure()

        for index, row in df_s.iterrows():
            fig.add_trace(go.Scatterpolar(
                r=row.iloc[1:],  
                theta=categories,
                fill='toself',
                name=row.iloc[0], 
            ))
        fig.update_layout(
        template=None,
        #plot_bgcolor='white',
        title="Digital Tools - SureSeT Shipped Jobs <br> (Current Month & M-1)", 
        font=dict(
                family="Arial",  
                size=12,  
                color="dark grey"),  
        polar=dict(
            radialaxis=dict(
            visible=True,
            range=[0, 100]
            )),
            width=400, 
        height=500, 
        showlegend=True,

        legend=dict(
                orientation="h",
                yanchor="top",
            ),
            annotations=[dict(text="Month - Complexity:", showarrow=False, x=0.7, y=-0.1, align="left", xanchor='right', yanchor='bottom')]
        )

        # Display the chart in Streamlit
        st.plotly_chart(fig)
           
    with c2:
        df_ns = dfs['df_18']
        
        categories = ['Aid Mapics', 'Ampere Compare', 'CrossCheck', 'Mapics Compare', 'Reconfigure', 'Refresh']
        df_ns['Type'] = df_ns['Type'].astype(str)

        # Obtener los años únicos del DataFrame
        complexity = df_ns['Type'].unique()

        fig = go.Figure()

        for index, row in df_ns.iterrows():
            fig.add_trace(go.Scatterpolar(
                r=row.iloc[1:],  
                theta=categories,
                fill='toself',
                name=row.iloc[0], 
            ))
        fig.update_layout(
        template=None,
        #plot_bgcolor='white',
        title="Digital Tools - SureSeT Non Shipped Jobs <br> (Current Month & M+1)", 
        font=dict(
                family="Arial",  
                size=12,  
                color="dark grey"),  
        polar=dict(
            radialaxis=dict(
            visible=True,
            range=[0, 100]
            )),
            width=400, 
        height=500, 
        showlegend=True,

        legend=dict(
                orientation="h",
                yanchor="top",
            ),
            annotations=[dict(text="Month - Complexity:", showarrow=False, x=0.7, y=-0.1, align="left", xanchor='right', yanchor='bottom')]
        )

        # Display the chart in Streamlit
        st.plotly_chart(fig)

    with c3:
        df_s = dfs['df_21']

        fig = px.scatter_3d(df_s, x='Reliability Level', y='DPU_Percent', z='ANDON_Percent',
                   color='Job_Cx', size='Reliability Value',width=750, height=600, title="Correlation SureSeT Shipped Jobs <br> (Current Month & M-1)",
                   category_orders={'Reliability Level': ['Good','Acceptable','Low','Extremely Low']})
        fig.update_layout(
            template=None,
            title_font=dict(family="Arial", size=16, weight="bold", color="dark grey" ),
            scene=dict(
                xaxis_title='Reliability Level',
                yaxis_title='DPU (%)',
                zaxis_title='ANDON (%)'
                
            )
)

        # Display the chart in Streamlit
        st.plotly_chart(fig)

    with c4:
        df_ns = dfs['df_17']
        fig = px.scatter_3d(df_ns, x='Reliability Level', y='Reliability Value', z='Complexity',
                   color='Job_Cx', size='Reliability Value',width=750, height=600, title="Correlation SureSeT Non Shipped Jobs <br> (Current Month & M+1)",
                    category_orders={'Reliability Level': ['Good','Acceptable','Low','Extremely Low']})

        fig.update_layout(
            template=None,
            title_font=dict(family="Arial", size=16, weight="bold", color="dark grey" ),
            scene=dict(
                xaxis_title='Reliability Level',
                yaxis_title='Reliability',
                zaxis = dict(
                    title='Complexity',
                    dtick = 1)

            )
)
        # Display the chart in Streamlit
        st.plotly_chart(fig)

    with c5:
        df_s = dfs['df_23']
        color_palette = {'Good': 'green', 'Acceptable': 'yellow', 'Low': 'orange', 'Extremely Low': 'red'}

        fig = px.bar(df_s, y="Date", x='Reliability', color='Reliability Level', color_discrete_map=color_palette, title="Reliability SureSeT Shipped Jobs <br> (Current Month & M-1)",
                    barmode='stack'  # Utiliza el modo de gráficos apilados
        )
        fig.update_layout(
            template=None,
            title_font=dict(family="Arial", size=16, weight="bold", color="dark grey" ), 
            bargap=0.1, width=400, height=500)

        # Display the chart in Streamlit
        st.plotly_chart(fig)

    with c6:
        df_ns = dfs['df_19']
        color_palette = {'Good': 'green', 'Acceptable': 'yellow', 'Low': 'orange', 'Extremely Low': 'red'}

        fig = px.bar(df_ns, y="Date", x='Reliability', category_orders={"Date": df_ns['Date'].unique().tolist()}, color='Reliability Level', color_discrete_map=color_palette, title="Reliability SureSeT Non Shipped Jobs <br> (Current Month & M+1)",
                    barmode='stack'  # Utiliza el modo de gráficos apilados
        )
        fig.update_layout(
            template=None,
            title_font=dict(family="Arial", size=16, weight="bold", color="dark grey" ), 
            bargap=0.1, width=400, height=500,)

        # Display the chart in Streamlit
        st.plotly_chart(fig)

    with c7:
        df_s = dfs['df_24']

        fig = go.Figure(go.Table(
            header={"values": df_s.columns},
            cells={"values": df_s.sort_values(by='Reliability Value', ascending=True).T.values},  # Sort the values before displaying
            columnwidth=[24, 24, 12, 6,6,6,25,25,12,12,12,12,6,6]
        ))

        fig.update_layout(
            updatemenus=[{
                "y": 1 - (i / 5),
                "buttons": [{
                    "label": c,
                    "method": "update",
                    "args": [{"cells": {"values": df_s.loc[df_s[menu].eq(c)].sort_values(by='Reliability Value', ascending=True).T.values}}],
                } for c in ["All"] + df_s[menu].unique().tolist()],
            } for i, menu in enumerate(["Reliability Level", "Complexity", "EE Name", "MD Name"])],
        
            annotations=[dict(text="Reliability Level:", showarrow=False,x=-0.05, y=1.06, align="left", xanchor='right', yanchor='top'),
                        dict(text="Complexity:", showarrow=False,x=-0.05, y=0.86, align="right", xanchor='right', yanchor='top'),
                        dict(text="Electrical Engineer:", showarrow=False,x=-0.05, y=0.68, align="right", xanchor='right', yanchor='top'),
                        dict(text="Mechanical Engineer:", showarrow=False,x=-0.05, y=0.48, align="right", xanchor='right', yanchor='top')],
        )
        fig.update_layout(title="SureSeT Shipped Jobs - Reliability (Current Month & M-1)",
                        font=dict(
                                family="Arial",  
                                size=12,  
                                color="dark grey"),width=1600,height=500)

        # Display the chart in Streamlit
        st.plotly_chart(fig)

    with c8:
        df_ns = dfs['df_20']

        fig = go.Figure(go.Table(
            header={"values": df_ns.columns},
            cells={"values": df_ns.sort_values(by='Reliability Value', ascending=True).T.values},  # Sort the values before displaying
            columnwidth=[24, 24, 12, 6,6,6,25,25,12,12,12,12,6,6]
        ))

        fig.update_layout(
            updatemenus=[{
                "y": 1 - (i / 5),
                "buttons": [{
                    "label": c,
                    "method": "update",
                    "args": [{"cells": {"values": df_ns.loc[df_ns[menu].eq(c)].sort_values(by='Reliability Value', ascending=True).T.values}}],
                } for c in ["All"] + df_ns[menu].unique().tolist()],
            } for i, menu in enumerate(["Reliability Level", "Complexity", "EE Name", "MD Name"])],

            annotations=[dict(text="Reliability Level:", showarrow=False,x=-0.05, y=1.06, align="left", xanchor='right', yanchor='top'),
                        dict(text="Complexity:", showarrow=False,x=-0.05, y=0.86, align="right", xanchor='right', yanchor='top'),
                        dict(text="Electrical Engineer:", showarrow=False,x=-0.05, y=0.68, align="right", xanchor='right', yanchor='top'),
                        dict(text="Mechanical Engineer:", showarrow=False,x=-0.05, y=0.48, align="right", xanchor='right', yanchor='top')],
        )


        fig.update_layout(title="SureSeT Non Shipped Jobs - Reliability (Current Month & M+1)",
                        font=dict(
                                family="Arial",  
                                size=12,  
                                color="dark grey"),width=1600,height=500)

        # Display the chart in Streamlit
        st.plotly_chart(fig)



if selected == "Jobs Journey Map":
    st.header('Jobs Journey Map One4All')
    # Create a row layout
    c1, c2= st.columns((99,1))

    with c1:

        DATA_FILENAME = Path(__file__).parent/'data/O4All_WIYO_XTENDED.csv'
        df = pd.read_csv(DATA_FILENAME)

        today = df['Refresh_Date'].unique()
        
        # Prepare data for sorting Label
        unique = df['Job'].unique()
        unique = sorted(unique, reverse=False)
        
        fig = px.scatter(df, x="X", y="Y", color="Product Line", size="Risk Weight", category_orders={"Job": unique}, hover_data={"X": False,"Y": False, "Product Line": True, "Stage": True,"Job": True,"Job Name": True,"VIP Flag": True,"NET_USD": True,"Bays": True,"Cx": True,"OCN": True,"ANDON": True, "Reliability": True})
        #fig.update_traces(marker=dict(size=12, line=dict(width=1, color='DarkSlateGrey')), selector=dict(mode='markers'))
        fig.update_xaxes(showline=False, showgrid=False, zeroline=False, showticklabels=False, title_text="")
        fig.update_yaxes(showline=False, showgrid=False, zeroline=False, showticklabels=False, title_text="")
        fig.update_layout(
            title=f'Glass Factory (inside Rojo plant)<br><i><span style="font-size: 50%">{today}</i>',
            plot_bgcolor='rgba(0, 0, 0, 0)',  # Hace el fondo del gráfico transparente
            paper_bgcolor='rgba(0, 0, 0, 0)',  # Hace el fondo del área del papel transparente
            hoverlabel=dict(bgcolor="white", font_size=16, font_family="Rockwell"),
            font_color="white",
            title_font_color="green",
            legend_font_color="grey",
        
        )
        # Mostrar la imagen con Plotly
        ruta_imagen = Path(__file__).parent/'data/Layout.png'
        imagen = Image.open(ruta_imagen)

        fig.update_layout(xaxis=dict(range=[0.0, 10.0], dtick=0.25), yaxis=dict(range=[0.0, 8.0], dtick=0.25),
                        )
        
        fig.add_layout_image(
                dict(
                    source=imagen,
                    xref="x",
                    yref="y",
                    x=0,
                    y=8,
                    sizex=10,
                    sizey=8,
                    sizing="stretch",
                    opacity=0.5,
                    layer="below")
        )
        fig.update_layout()
        # Display the chart in Streamlit
        st.plotly_chart(fig)

