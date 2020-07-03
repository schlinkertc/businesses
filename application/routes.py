"""Core Flask app routes"""
from flask import render_template, redirect, url_for, session, g
from flask import current_app as app
from .forms import SubmitBusiness,ConfirmBusiness 
from config import Config
from application import yelp, parse_business
from .models import db,Business

@app.route('/')
def home():
    """Landing page."""
    return render_template('index.jinja2',
                          title='Black Owned Businesses',
                          template='home-template',
                          body='This is a homepage served with Flask')
@app.route('/submit/',methods=['GET','POST'])
def submit():
    business=''
    confirm=ConfirmBusiness()
    form = SubmitBusiness()
    if form.validate_on_submit():
        business_name = form.business_name.data
        business_location = form.business_location.data
        
        yelp_result = yelp(business_name,business_location)
        print(business_location)
        business = parse_business(yelp_result['businesses'][0])
        
        session['business']=business
        
        return render_template('submit.jinja2',
                               form=form,
                               business=business,
                               confirm=confirm)
    
    if confirm.validate_on_submit():
        #database operations
        try:
            biz_id = session['business']['id']
            existing_business = Business.query.filter_by(id=biz_id).first()
            if existing_business is None:
                record = Business(**session['business'])
                db.session.add(record)
                db.session.commit()
        except:
            pass
        
        return redirect(url_for('/dashapp/'))
    return render_template('submit.jinja2',form=form,
                           confirm=confirm,
                           business=business)