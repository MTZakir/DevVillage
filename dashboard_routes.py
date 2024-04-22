from flask import Blueprint, redirect, render_template, session, url_for
from firebase_admin import db, auth
from firebase_admin._auth_utils import UserNotFoundError

dashboard_blueprint = Blueprint(
    "dashboard", __name__, static_folder="static", template_folder="templates"
)

# Remove session if current user is unverified
# use this in the beginning of every route function
@dashboard_blueprint.before_request
def session_remove_if_not_verified():
    if session.get('verify'):
        try:
            user = auth.get_user(session.get('verify'))
            if not user.email_verified:
                print("Deleting session verify of user", user.display_name)
                session.pop('verify', None)
        except UserNotFoundError:
            session.pop('verify', None)
    else:
        print("No session found.")

@dashboard_blueprint.before_request
def is_correct_user():
    if not session.get("user_id"):
        return redirect(url_for("auth.user_login"))
    
def is_indi_or_org(acc_type):
    if acc_type:
        return redirect(url_for("homecomp"))
    else:
        return redirect(url_for("home"))

# DISCOVER
@dashboard_blueprint.route('/dashboard/individual')
def individuals():
    is_indi_or_org(True)
    dashcontent = {
            'completed_contracts': 21,
            'total_earned': 6203.23,
            'tokens_owned': 34,
        }
    
    recent_payments = [
        {
            'company_name': 'Netflix',
            'company_pic': '/static/images/netflix.png',
            'status': 'Completed',
            'amount': 273,
        },
        {
            'company_name': 'Netflix',
            'company_pic': '/static/images/netflix.png',
            'status': 'Ongoing',
            'amount': 121,
        },
        {
            'company_name': 'Netflix',
            'company_pic': '/static/images/netflix.png',
            'status': 'Completed',
            'amount': 209,
        },
        {
            'company_name': 'Netflix',
            'company_pic': '/static/images/netflix.png',
            'status': 'Ongoing',
            'amount': 628,
        },
        {
            'company_name': 'Netflix',
            'company_pic': '/static/images/netflix.png',
            'status': 'Ongoing',
            'amount': 123,
        },
        {
            'company_name': 'Netflix',
            'company_pic': '/static/images/netflix.png',
            'status': 'Completed',
            'amount': 193,
        }
    ]

    company_hires = [
        {
            'organization': 'QVParts', 
            'title': 'build a website api for banking',
            'duration': '30 days',
            'expected_pay': (500, 700), 
        },
        {
            'organization': 'QVParts', 
            'title': 'build a website api for banking',
            'duration': '30 days',
            'expected_pay': (500, 700), 
        },
        {
            'organization': 'QVParts', 
            'title': 'build a website api for banking',
            'duration': '30 days',
            'expected_pay': (500, 700), 
        },
        {
            'organization': 'QVParts', 
            'title': 'build a website api for banking',
            'duration': '30 days',
            'expected_pay': (500, 700), 
        },
        {
            'organization': 'QVParts', 
            'title': 'build a website api for banking',
            'duration': '30 days',
            'expected_pay': (500, 700), 
        },
        {
            'organization': 'QVParts', 
            'title': 'build a website api for banking',
            'duration': '30 days',
            'expected_pay': (500, 700), 
        },
        {
            'organization': 'QVParts', 
            'title': 'build a website api for banking',
            'duration': '30 days',
            'expected_pay': (500, 700), 
        },
        {
            'organization': 'QVParts', 
            'title': 'build a website api for banking',
            'duration': '30 days',
            'expected_pay': (500, 700), 
        },
        {
            'organization': 'QVParts', 
            'title': 'build a website api for banking',
            'duration': '30 days',
            'expected_pay': (500, 700), 
        },
        {
            'organization': 'QVParts', 
            'title': 'build a website api for banking',
            'duration': '30 days',
            'expected_pay': (500, 700), 
        },
        {
            'organization': 'QVParts', 
            'title': 'build a website api for banking',
            'duration': '30 days',
            'expected_pay': (500, 700), 
        },
        
    ]

    return render_template("dashboard.html", dashcontent=dashcontent, 
                           company_hires=company_hires, 
                           recent_payments=recent_payments)

@dashboard_blueprint.route('/dashboard/org')
def organization():
    is_indi_or_org(False)
    
    return render_template("dashboard.html")