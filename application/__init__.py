
"""Initialize Flask app."""
from flask import Flask, g
from flask_assets import Environment
from flask_sqlalchemy import SQLAlchemy
from config import Config
import requests
import json
import pandas as pd

db = SQLAlchemy()

def create_app():
    """Construct core Flask application with embedded Dash app."""
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object('config.Config')
    
    db.init_app(app)
    
    assets = Environment()
    assets.init_app(app)

    with app.app_context():
        # Import parts of our core Flask app
        from . import routes
        from .assets import compile_static_assets

        # Import Dash application
        from .plotlydash.dashboard import create_dashboard
        app = create_dashboard(app)

        # Compile static assets
        compile_static_assets(assets)
        
        # Database tables
        db.create_all()
        
        return app
    
def yelp(term,location,limit=1):
    api_key = Config.yelp_api_key
    url = 'https://api.yelp.com/v3/businesses/search'
    headers = {'Authorization': 'Bearer {}'.format(api_key)}
    url_params = {'term':term.replace(' ','+'),'location':location.replace(' ','+'),'limit':limit}
    
    response = requests.get(url, headers=headers, params=url_params)
    
    results = json.loads(response.content)
    
    return results

def parse_business(result):
    out = {}
    keys = [k for k,v in result.items() if type(v)==str]
    for k in keys:
        out[k]=result[k]
    
    out['latitude'],out['longitude'] = result['coordinates'].values()
    
    for k,v in result['location'].items():
        out[k]=v
    
    out['display_address'] = "".join(
        [x+' ' for x in out['display_address']]
    ).strip()
    
    out['categories']="".join(
        [x['title']+', ' for x in result['categories']]
    ).strip(', ')
    
    for transaction in ['pickup','delivery']:
        if transaction in result['transactions']:
            out[transaction]=True
        else:
            out[transaction]=False
    
    return out