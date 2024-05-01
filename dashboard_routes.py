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
            'completed_contracts': 2,
            'total_earned': 3700,
            'tokens_owned': 30,
        }
    
    recent_payments = [
        {
            'company_name': 'Unreal Engine',
            'company_pic': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTb-r5Xf0pOtB3oJsJrvI9K4s5ho7qNpxWkjmETeIg5HA&s',
            'status': 'Ongoing',
            'amount': 600,
        },
        {
            'company_name': 'Unity',
            'company_pic': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSnquaZgwR8H2rYZUDcCi2sxjOqB1Wahz6sIoKuVc-xhYBuXeim1ZNhmYlz0pCV1WZ7yPA&usqp=CAU',
            'status': 'Completed',
            'amount': 1750,
        },
        {
            'company_name': 'Ionic',
            'company_pic': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRS230PJ4lEC5iEQpY6pFnB6ijvZlbX4UDw-U791RufDA&s',
            'status': 'Completed',
            'amount': 1350,
        }
    ]

    company_hires = [
        {
            'organization': 'Unreal Engine', 
            'title': 'Game Developer',
            'duration': '3 Months',
            'expected_pay': (800, 1200), 
        },
        {
            'organization': 'Unity', 
            'title': 'Mobile Game De...',
            'duration': '2 Months',
            'expected_pay': (1000, 2500), 
        },
        {
            'organization': 'Ionic', 
            'title': 'Mobile App Dev...',
            'duration': '1 Month 15 days',
            'expected_pay': (800, 1500), 
        }
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
            'comp_pic': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTb-r5Xf0pOtB3oJsJrvI9K4s5ho7qNpxWkjmETeIg5HA&s',
            'comp_name': 'Unreal Engine',
            'status': 'Ongoing',
            'amount': 600,
            'date': '24-04-2024'
        },
        {
            'comp_pic': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSnquaZgwR8H2rYZUDcCi2sxjOqB1Wahz6sIoKuVc-xhYBuXeim1ZNhmYlz0pCV1WZ7yPA&usqp=CAU',
            'comp_name': 'Unity',
            'status': 'Completed',
            'amount': 1750,
            'date': '01-05-2024'
        },
        {
            'comp_pic': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRS230PJ4lEC5iEQpY6pFnB6ijvZlbX4UDw-U791RufDA&s',
            'comp_name': 'Ionic',
            'status': 'Completed',
            'amount': 1350,
            'date': '18-04-2024'
        }
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
            'organization': 'Unreal Engine', 
            'title': 'Game Developer',
            'duration': '3 Months',
            'expected_pay': (800, 1200), 
        },
        {
            'organization': 'Unity', 
            'title': 'Mobile Game De...',
            'duration': '2 Months',
            'expected_pay': (1000, 2500), 
        },
        {
            'organization': 'Ionic', 
            'title': 'Mobile App Dev...',
            'duration': '1 Month 15 days',
            'expected_pay': (800, 1500), 
        }
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
            'tokens_owned': 20,
        }
    
    recent_payments = [
        {
            'contractor_name': '@markZoing534',
            'status': 'Ongoing',
            'amount': 220,
        },
        {
            'contractor_name': '@Sheinfactory',
            'status': 'Ongoing',
            'amount': 360,
        },
        {
            'contractor_name': '@liamJ5454',
            'status': 'Closed',
            'amount': 1750,
        }
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
            'contractor_name': '@markZoing534',
            'status': 'Ongoing',
            'amount': 220,
            'date': '2024-05-03'
        },
        {
            'contractor_name': '@Sheinfactory',
            'status': 'Ongoing',
            'amount': 360,
            'date': '2024-04-20'
        },        
        {
            'contractor_name': '@liamJ5454',
            'status': 'Closed',
            'amount': 1500,
            'date': '2024-04-15'
        }
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