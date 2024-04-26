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

# Before request function
@dashboard_blueprint.before_request
def is_correct_user():
    if not session.get("user_id"):
        return redirect(url_for("auth.user_login"))
    
def is_indi_or_org(acc_type):
    if acc_type:
        return redirect(url_for("homecomp"))
    else:
        return redirect(url_for("home"))

# -------------------------------------------------------------------------------------------


# INDIVIDUAL DASHBOARD
@dashboard_blueprint.route('/individual/dashboard')
def individuals():
    is_indi_or_org(True)
    # Call this function in every route, to ensure navbar details
    user_data = acc_nav_details(session.get("user_id"))

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
                           recent_payments=recent_payments,
                           user_data = user_data, applicants=applicants)


# INDIVIDUAL PAYMENT HISTORY
@dashboard_blueprint.route('/individual/payments')
def payment_history():
    is_indi_or_org(True)
    # Call this function in every route, to ensure navbar details
    user_data = acc_nav_details(session.get("user_id"))

    payments = [
        {
            'comp_pic': '/static/images/netflix.png',
            'comp_name': 'Netflix',
            'status': 'Completed',
            'amount': 274,
            'date': '2018-07-05'
        },
        {
            'comp_pic': '/static/images/netflix.png',
            'comp_name': 'Netflix',
            'status': 'Completed',
            'amount': 534,
            'date': '2018-07-05'
        },
        {
            'comp_pic': '/static/images/netflix.png',
            'comp_name': 'Netflix',
            'status': 'Completed',
            'amount': 211,
            'date': '2018-07-05'
        },
        {
            'comp_pic': '/static/images/netflix.png',
            'comp_name': 'Netflix',
            'status': 'Completed',
            'amount': 114,
            'date': '2018-07-05'
        },
        {
            'comp_pic': '/static/images/netflix.png',
            'comp_name': 'Netflix',
            'status': 'Completed',
            'amount': 674,
            'date': '2018-07-05'
        },
        {
            'comp_pic': '/static/images/netflix.png',
            'comp_name': 'Netflix',
            'status': 'Completed',
            'amount': 904,
            'date': '2018-07-05'
        },
        {
            'comp_pic': '/static/images/netflix.png',
            'comp_name': 'Netflix',
            'status': 'Completed',
            'amount': 304,
            'date': '2018-07-05'
        },
        {
            'comp_pic': '/static/images/netflix.png',
            'comp_name': 'Netflix',
            'status': 'Completed',
            'amount': 274,
            'date': '2018-07-05'
        },
        {
            'comp_pic': '/static/images/netflix.png',
            'comp_name': 'Netflix',
            'status': 'Completed',
            'amount': 352,
            'date': '2018-07-05'
        },
        {
            'comp_pic': '/static/images/netflix.png',
            'comp_name': 'Netflix',
            'status': 'Completed',
            'amount': 156,
            'date': '2018-07-05'
        },
        {
            'comp_pic': '/static/images/netflix.png',
            'comp_name': 'Netflix',
            'status': 'Ongoing',
            'amount': 423,
            'date': '2018-07-05'
        },
        {
            'comp_pic': '/static/images/netflix.png',
            'comp_name': 'Netflix',
            'status': 'Ongoing',
            'amount': 690,
            'date': '2018-07-05'
        },
        {
            'comp_pic': '/static/images/netflix.png',
            'comp_name': 'Netflix',
            'status': 'Ongoing',
            'amount': 720,
            'date': '2018-07-05'
        },
    ]

    total_earned = 0
    for i in payments:
        total_earned += i['amount']

    return render_template("payments.html", payments=payments, total_earned=total_earned, user_data = user_data)


# INDIVIDUAL INVITES FROM COMPANY
@dashboard_blueprint.route('/individual/invites')
def invites():
    is_indi_or_org(True)
    # Call this function in every route, to ensure navbar details
    user_data = acc_nav_details(session.get("user_id"))

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
    return render_template("invites.html", company_hires=company_hires, user_data = user_data)

# ORGANIZATION DASHBOARD
@dashboard_blueprint.route('/org/dashboard')
def organization():
    is_indi_or_org(False)
    # Call this function in every route, to ensure navbar details
    user_data = acc_nav_details(session.get("user_id"))

    dashcontent = {
            'completed_contracts': 21,
            'ongoing_contracts': 4,
            'tokens_owned': 34,
        }
    
    recent_payments = [
        {
            'contractor_name': 'test',
            'status': 'Closed',
            'amount': 273,
        },
        {
            'contractor_name': 'test',
            'status': 'Closed',
            'amount': 273,
        },
        {
            'contractor_name': 'test',
            'status': 'Closed',
            'amount': 273,
        },
        {
            'contractor_name': 'test',
            'status': 'Closed',
            'amount': 273,
        },
        {
            'contractor_name': 'test',
            'status': 'Closed',
            'amount': 273,
        },
        {
            'contractor_name': 'test',
            'status': 'Closed',
            'amount': 273,
        },
        {
            'contractor_name': 'test',
            'status': 'Closed',
            'amount': 273,
        },
    ]

    applicants = [
        {
            'applicant': 'test',
            'title': 'Build website API for Banking',
            'suggested_pay': 120,
        },
        {
            'applicant': 'test',
            'title': 'Build website API for Banking',
            'suggested_pay': 120,
        },
        {
            'applicant': 'test',
            'title': 'Build website API for Banking',
            'suggested_pay': 120,
        },
        {
            'applicant': 'test',
            'title': 'Build website API for Banking',
            'suggested_pay': 120,
        },
        {
            'applicant': 'test',
            'title': 'Build website API for Banking',
            'suggested_pay': 120,
        },
        {
            'applicant': 'test',
            'title': 'Build website API for Banking',
            'suggested_pay': 120,
        },
        {
            'applicant': 'test',
            'title': 'Build website API for Banking',
            'suggested_pay': 120,
        },
        {
            'applicant': 'test',
            'title': 'Build website API for Banking',
            'suggested_pay': 120,
        },
        {
            'applicant': 'test',
            'title': 'Build website API for Banking',
            'suggested_pay': 120,
        },
        {
            'applicant': 'test',
            'title': 'Build website API for Banking',
            'suggested_pay': 120,
        },
        {
            'applicant': 'test',
            'title': 'Build website API for Banking',
            'suggested_pay': 120,
        },
        {
            'applicant': 'test',
            'title': 'Build website API for Banking',
            'suggested_pay': 120,
        },
        {
            'applicant': 'test',
            'title': 'Build website API for Banking',
            'suggested_pay': 120,
        },
        {
            'applicant': 'test',
            'title': 'Build website API for Banking',
            'suggested_pay': 120,
        },
        {
            'applicant': 'test',
            'title': 'Build website API for Banking',
            'suggested_pay': 120,
        },
        {
            'applicant': 'test',
            'title': 'Build website API for Banking',
            'suggested_pay': 120,
        },
        {
            'applicant': 'test',
            'title': 'Build website API for Banking',
            'suggested_pay': 120,
        },
        {
            'applicant': 'test',
            'title': 'Build website API for Banking',
            'suggested_pay': 120,
        },
        {
            'applicant': 'test',
            'title': 'Build website API for Banking',
            'suggested_pay': 120,
        },
        {
            'applicant': 'test',
            'title': 'Build website API for Banking',
            'suggested_pay': 120,
        },
        {
            'applicant': 'test',
            'title': 'Build website API for Banking',
            'suggested_pay': 120,
        },
        {
            'applicant': 'test',
            'title': 'Build website API for Banking',
            'suggested_pay': 120,
        },
        {
            'applicant': 'test',
            'title': 'Build website API for Banking',
            'suggested_pay': 120,
        },
        {
            'applicant': 'test',
            'title': 'Build website API for Banking',
            'suggested_pay': 120,
        },
        {
            'applicant': 'test',
            'title': 'Build website API for Banking',
            'suggested_pay': 120,
        },
        {
            'applicant': 'test',
            'title': 'Build website API for Banking',
            'suggested_pay': 120,
        },
        {
            'applicant': 'test',
            'title': 'Build website API for Banking',
            'suggested_pay': 120,
        },
        {
            'applicant': 'test',
            'title': 'Build website API for Banking',
            'suggested_pay': 120,
        },
        {
            'applicant': 'test',
            'title': 'Build website API for Banking',
            'suggested_pay': 120,
        },
    ]


    return render_template("dashboard.html", dashcontent=dashcontent, 
                           applicants=applicants, 
                           recent_payments=recent_payments,
                           user_data = user_data,)


# ORGANIZATION PAYMENT HISTORY
@dashboard_blueprint.route('/organization/payments')
def org_payment_history():
    is_indi_or_org(True)
    # Call this function in every route, to ensure navbar details
    user_data = acc_nav_details(session.get("user_id"))

    payments = [
        {
            'contractor_name': 'test',
            'status': 'Closed',
            'amount': 273,
            'date': '1984-05-03'
        },
        {
            'contractor_name': 'test',
            'status': 'Ongoing',
            'amount': 273,
            'date': '1984-05-03'
        },
        {
            'contractor_name': 'test',
            'status': 'Ongoing',
            'amount': 273,
            'date': '1984-05-03'
        },
        {
            'contractor_name': 'test',
            'status': 'Closed',
            'amount': 273,
            'date': '1984-05-03'
        },
        {
            'contractor_name': 'test',
            'status': 'Ongoing',
            'amount': 273,
            'date': '1984-05-03'
        },
        {
            'contractor_name': 'test',
            'status': 'Ongoing',
            'amount': 273,
            'date': '1984-05-03'
        },
        {
            'contractor_name': 'test',
            'status': 'Closed',
            'amount': 273,
            'date': '1984-05-03'
        },
        {
            'contractor_name': 'test',
            'status': 'Ongoing',
            'amount': 273,
            'date': '1984-05-03'
        },
        {
            'contractor_name': 'test',
            'status': 'Ongoing',
            'amount': 273,
            'date': '1984-05-03'
        },
        
    ]

    total_payed = 0
    for i in payments:
        total_payed += i['amount']

    return render_template("payments.html", payments=payments, total_payed=total_payed, user_data = user_data)

# ORGANIZATION APPLICANTS LIST
@dashboard_blueprint.route('/organization/applicants')
def applicants():
    is_indi_or_org(False)
    # Call this function in every route, to ensure navbar details
    user_data = acc_nav_details(session.get("user_id"))

    return render_template('applicants.html', user_data=user_data)





# ---------------------------
# Helper Functions
# ---------------------------

# Return User details from database for navbar
def acc_nav_details(acc_id):

    # Organization Account
    if acc_id[0] == "O":
        comp_db_auth = auth.get_user(acc_id[2:])
        comp_db_ref = db.reference("/org_accounts").child(acc_id[2:]).get()

        comp_data = {
            "Company_name": comp_db_auth.display_name,
            "Wallet": "$ {:,.2f}".format(comp_db_ref["Wallet"]),
            "Tokens": comp_db_ref["Tokens"],
            "Email": comp_db_ref["Email"]
        }

        # Any notification messages
        if (comp_db_ref["Notifications"] != None):
            comp_data.update({"Notifications": comp_db_ref["Notifications"]})

        return comp_data

    # Individual Account
    elif acc_id[0] == "I":
        user_db_auth = auth.get_user(acc_id[2:])
        user_db_ref = db.reference("/user_accounts").child(user_db_auth.display_name).get()

        # Getting base account dropdown info
        user_data = {
            "Display_name": user_db_auth.display_name,
            "First_name": user_db_ref["First_name"],
            "Last_name": user_db_ref["Last_name"],
            "Wallet": "$ {:,.2f}".format(user_db_ref["Wallet"]),
            "Tokens": user_db_ref["Tokens"]
        }

        # Any notification messages
        if (user_db_ref["Notifications"] != None):
            user_data.update({"Notifications": user_db_ref["Notifications"]})

        return user_data