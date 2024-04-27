from flask import Blueprint, redirect, render_template, session, url_for
from firebase_admin import db, auth
from firebase_admin._auth_utils import UserNotFoundError
from discover_forms import ApplicantAcceptReject

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
                           user_data = user_data)


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
@dashboard_blueprint.route('/org/dashboard', methods=['GET', 'POST'])
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


    applicant_list = []
    for contract in db.reference("/contracts").get():
        contract_ref = db.reference("/contracts").child(contract)

        if session.get("user_id")[2:] == contract_ref.child("Author").get() and contract_ref.child("Applied").get() != None:
            applicant_list.append({
                "Contract ID": contract,
                "Applicant ID": next(iter(contract_ref.child("Applied").get().keys())),
                "Applicant Name": auth.get_user(next(iter(contract_ref.child("Applied").get().keys()))).display_name,
                "Title": contract_ref.child("Title").get(),
                "Pay": contract_ref.child("Applied").child(next(iter(contract_ref.child("Applied").get().keys()))).child("Pay Requested").get(),
                "Resume": db.reference("/user_accounts").child(auth.get_user(next(iter(contract_ref.child("Applied").get().keys()))).display_name).child("Resume").get()
            })


    form = ApplicantAcceptReject()

    if form.validate_on_submit():
        user_id = form.applicant.data[:-2]
        # If rejected
        if form.applicant.data[-1] == "0":
            # Send notification
            # Get the contract title first
            contract_title = db.reference("/contracts").child(form.contract.data).child("Title").get()

            # Construct the notification message separately
            notification_message = f"You did not qualify for the '{contract_title}' contract. Wish you the very best later on."

            # Push the notification to the database
            db.reference("/user_accounts").child(auth.get_user(user_id).display_name).child("Notifications").push(notification_message)

            # Refund user's tokens
            user_current = db.reference("/user_accounts").child(auth.get_user(user_id).display_name)
            user_current_token = user_current.child("Tokens").get()
            user_current.update({"Tokens": user_current_token + 10})
            # Remove user from applied list
            db.reference("/contracts").child(form.contract.data).child("Applied").child(user_id).delete()

        # If accepted
        if form.applicant.data[-1] == "1":
            # Send notification
            # Get the contract title first
            contract_title = db.reference("/contracts").child(form.contract.data).child("Title").get()

            # Construct the notification message separately
            notification_message = f"You have been accepted for the '{contract_title}' contract. Looking forward to working with you."

            # Push the notification to the database
            db.reference("/user_accounts").child(auth.get_user(user_id).display_name).child("Notifications").push(notification_message)

            # Update user wallet
            user_current = db.reference("/user_accounts").child(auth.get_user(user_id).display_name)
            user_current_wallet = user_current.child("Wallet").get()
            user_current.update({"Wallet": user_current_wallet + (int(applicant_list[0]["Pay"]) / (int(db.reference("/contracts").child(form.contract.data).child("Duration").get()) / 15))})
            # Update company wallet
            org_current = db.reference("/org_accounts").child(session.get("user_id")[2:])
            org_current_wallet = org_current.child("Wallet").get()
            org_current.update({"Wallet": org_current_wallet - (int(applicant_list[0]["Pay"]) / (int(db.reference("/contracts").child(form.contract.data).child("Duration").get()) / 15))})
            # Add user to contractor list
            db.reference("/contracts").child(form.contract.data).child("Contractors").child(user_id).update({
                "Contractor Name": auth.get_user(user_id).display_name,
                "Pay": applicant_list[0]["Pay"]
            })
            # Remove user from applied list
            db.reference("/contracts").child(form.contract.data).child("Applied").child(user_id).delete()

        return redirect(url_for("dashboard.organization"))

    return render_template("dashboard.html",
                            form = form,
                            dashcontent=dashcontent, 
                            applicant_list=applicant_list, 
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
        if (db.reference("/org_accounts").child(acc_id[2:]).child("Notifications").get() != None):
            noti = db.reference("/org_accounts").child(acc_id[2:]).child("Notifications").get()
            comp_data.update({"Notifications": noti.values()})

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
        if (db.reference("/user_accounts").child(user_db_auth.display_name).child("Notifications").get() != None):
            noti = db.reference("/user_accounts").child(user_db_auth.display_name).child("Notifications").get()
            user_data.update({"Notifications": noti.values()})

        return user_data