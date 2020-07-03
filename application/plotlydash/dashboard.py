import dash
from dash.dependencies import Input,Output
import dash_table
import dash_html_components as html
import dash_core_components as dcc
import pandas as pd 
import numpy as np
from .layout import html_layout
import plotly.graph_objects as go
from application import db
from config import Config
from flask import g
from datetime import datetime as dt

mapbox_access_token = Config.mapbox_access_token

def serve_layout():
    return html.Div(
        children = [
            html.H1(dt.now()),
            dcc.Graph(
                id='map',
                figure=fig
            ),
        ],
    id='dash-container'
    )


def create_dashboard(server):
    """Create a Dash app"""
    dash_app = dash.Dash(server=server,
                        routes_pathname_prefix='/dashapp/',
                        external_stylesheets=['/static/dist/css/styles.css']
                        )
    
    # Custom HTML layout
    dash_app.index_sting = html_layout

    # Create layout 
    def serve_layout():
        # Query database
        df = pd.read_sql_table('businesses',db.engine.connect())
        
        fig = go.Figure(go.Scattermapbox(
            lat=df['latitude'],
            lon=df['longitude'],
            mode='markers',
            marker=go.scattermapbox.Marker(size=5),
            text=df['name'],
            customdata=df[['display_address','categories']],
            hovertemplate="<b>%{text}</b><br>%{customdata[0]}<br>%{customdata[1]}",
            hoverlabel=dict(bgcolor='white',font_size=12,font_family='Rockwell'),
        ))

        fig.update_layout(
            autosize=True,
            title='Black Owned Businesses',
            height=700,
            hovermode='closest',
            mapbox=dict(
                accesstoken=mapbox_access_token,
                bearing=0,
                center=dict(lat=40.7128,lon=-74.0060),
                pitch=3,
                zoom=10
            ),
        )
        return html.Div(
            children = [
                dcc.Graph(
                    id='map',
                    figure=fig
                ),
            ],
        id='dash-container'
        )
    dash_app.layout = serve_layout
    
    return dash_app.server

def create_data_table(df):
    """Create Dash datatable from Pandas DataFrame"""
    table = dash_table.DataTable(
        id='database-table',
        columns=[{'name':i,'id':i} for i in df.columns],
        data=df.to_dict('records'),
        sort_action='native',
        page_size=300
    )
    return table


    