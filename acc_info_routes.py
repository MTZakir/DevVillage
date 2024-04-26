from flask import Blueprint, redirect, render_template, session, url_for
from firebase_admin import auth
from firebase_admin._auth_utils import UserNotFoundError
from dashboard_routes import acc_nav_details
from acc_info_forms import WalletTopup, AccountInfo, BuyTokens
from firebase_admin import db, auth

# Blueprint initialization
acc_info_blueprint = Blueprint(
    "accinfo", __name__, static_folder="static", template_folder="templates"
)

# Remove session if current user is unverified
# use this in the beginning of every route function
@acc_info_blueprint.before_request
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

@acc_info_blueprint.before_request
def is_correct_user():
    if not session.get("user_id"):
        return redirect(url_for("auth.org_login"))


def is_indi_or_org(acc_type):
    if acc_type:
        return redirect(url_for("homecomp"))
    else:
        return redirect(url_for("home"))




# TEST ROUTE - remove later
@acc_info_blueprint.route('/acc_info')
def acc_info():
    return render_template("accountinfo.html")



# ------------------------------------------------------------------------------------

# INDIVIDUAL ACCOUNT INFO
@acc_info_blueprint.route('/acc_info/profile/individual')
def individual_profile():
    is_indi_or_org(True)
    # Call this function in every route, to ensure navbar details
    # Contains first name, last name, display name, wallet amount, tokens and notifications
    user_data = acc_nav_details(session.get("user_id"))

    resume = False

    user_auth = auth.get_user(session.get("user_id")[2:])
    user_ref = db.reference("/user_accounts").child(user_auth.display_name).get()
    profile_info = {
        "Rating": user_ref["Rating"],
        "Expertise": user_ref["Expertise"],
        "Bio": user_ref["Bio"],
        "Phone": user_auth.phone_number,
        "Email": user_auth.email,
    }

    if "Resume" in user_ref:
        resume = True
        profile_info.update({"Resume": user_ref["Resume"]})


    return render_template("indiprofile.html", user_data = user_data, profile_info = profile_info, resume = resume)

# INDIVIDUAL ACCOUNT SETTINGS
@acc_info_blueprint.route('/acc_info/acc_settings/individual', methods=['GET', 'POST'])
def individual_settings():
    is_indi_or_org(True)
    # Call this function in every route, to ensure navbar details
    # Contains display name, first name, last name, wallet and tokens
    user_data = acc_nav_details(session.get("user_id"))

    user_auth = auth.get_user(session.get("user_id")[2:])
    user_ref = db.reference("/user_accounts").child(user_auth.display_name)

    user_info = {
        "Email": user_ref.get()["Email"],
        "Password": user_auth.email,
        "Phone": user_auth.phone_number,
        "Expertise": user_ref.get()["Expertise"],
        "DOB": user_ref.get()["DOB"],
        "Gender": user_ref.get()["Gender"],
        "Bio": user_ref.get()["Bio"]
    }

    form = AccountInfo()

    if form.validate_on_submit():
        # Updating any field
        # First name
        if form.first_name.data != user_data["First_name"]:
            user_ref.update({"First_name": form.first_name.data})
        # Last name
        if form.last_name.data != user_data["Last_name"]:
            user_ref.update({"Last_name": form.last_name.data})
        # Phone
        if form.phone.data != user_auth.phone_number:
            auth.update_user(session.get("user_id")[2:], phone_number = form.phone.data)
        # Expertise
        if form.expertise.data != user_info["Expertise"]:
            user_ref.update({"Expertise": form.expertise.data})
        # DOB
        if form.dob.data != user_info["DOB"]:
            user_ref.update({"DOB": form.dob.data})
        # Gender
        if form.gender.data != user_info["Gender"]:
            user_ref.update({"Gender": form.gender.data})
        # Bio
        if form.bio.data != user_info["Bio"]:
            user_ref.update({"Bio": form.bio.data})


    return render_template("indi_acc_settings.html", form=form, user_data = user_data, user_info = user_info)

# INDIVUDUAL CONTRACT HISTORY
@acc_info_blueprint.route('/acc_info/contract_history/individual')
def contract_history():
    is_indi_or_org(True)
    # Call this function in every route, to ensure navbar details
    user_data = acc_nav_details(session.get("user_id"))

    contracts = [
        {
            'comp_name': 'Google',
            'start_date': '2024-04-05',
            'completion_date': '2024-04-09',
            'title': 'implement firebase Authentication', 
            'desc': 'This website need peoeple to code please send dudes and stuff',
            'price_range': (42, 90),
            'agreed_pay': 110,
            'total_earned': 1142,
            'status': 'Completed', 
        },
        {
            'comp_name': 'Google',
            'start_date': '2024-04-05',
            'completion_date': '',
            'title': 'implement firebase Authentication', 
            'desc': 'This website need peoeple to code please send dudes and stuff',
            'price_range': (42, 90),
            'agreed_pay': 110,
            'total_earned': None,
            'status': 'Ongoing', 
        },
        {
            'comp_name': 'Google',
            'start_date': '2024-04-05',
            'completion_date': '',
            'title': 'implement firebase Authentication', 
            'desc': 'This website need peoeple to code please send dudes and stuff',
            'price_range': (42, 90),
            'agreed_pay': 110,
            'total_earned': None,
            'status': 'Ongoing', 
        },
        {
            'comp_name': 'Google',
            'start_date': '2024-04-05',
            'completion_date': '2024-04-09',
            'title': 'implement firebase Authentication', 
            'desc': 'This website need peoeple to code please send dudes and stuff',
            'price_range': (42, 90),
            'agreed_pay': 110,
            'total_earned': 1142,
            'status': 'Completed', 
        },
        {
            'comp_name': 'Google',
            'start_date': '2024-04-05',
            'completion_date': '',
            'title': 'implement firebase Authentication', 
            'desc': 'This website need peoeple to code please send dudes and stuff',
            'price_range': (42, 90),
            'agreed_pay': 110,
            'total_earned': None,
            'status': 'Ongoing', 
        },
        {
            'comp_name': 'Google',
            'start_date': '2024-04-05',
            'completion_date': '2024-04-09',
            'title': 'implement firebase Authentication', 
            'desc': 'This website need peoeple to code please send dudes and stuff',
            'price_range': (42, 90),
            'agreed_pay': 110,
            'total_earned': 1142,
            'status': 'Completed', 
        },
        {
            'comp_name': 'Google',
            'start_date': '2024-04-05',
            'completion_date': '2024-04-09',
            'title': 'implement firebase Authentication', 
            'desc': 'This website need peoeple to code please send dudes and stuff',
            'price_range': (42, 90),
            'agreed_pay': 110,
            'total_earned': 1142,
            'status': 'Completed', 
        },
        {
            'comp_name': 'Google',
            'start_date': '2024-04-05',
            'completion_date': '2024-04-09',
            'title': 'implement firebase Authentication', 
            'desc': 'This website need peoeple to code please send dudes and stuff',
            'price_range': (42, 90),
            'agreed_pay': 110,
            'total_earned': 1142,
            'status': 'Completed', 
        },
        {
            'comp_name': 'Google',
            'start_date': '2024-04-05',
            'completion_date': '2024-04-09',
            'title': 'implement firebase Authentication', 
            'desc': 'This website need peoeple to code please send dudes and stuff',
            'price_range': (42, 90),
            'agreed_pay': 110,
            'total_earned': 1142,
            'status': 'Completed', 
        },
        {
            'comp_name': 'Google',
            'start_date': '2024-04-05',
            'completion_date': '2024-04-09',
            'title': 'implement firebase Authentication', 
            'desc': 'This website need peoeple to code please send dudes and stuff',
            'price_range': (42, 90),
            'agreed_pay': 110,
            'total_earned': 1142,
            'status': 'Completed', 
        },
        {
            'comp_name': 'Google',
            'start_date': '2024-04-05',
            'completion_date': '2024-04-09',
            'title': 'implement firebase Authentication', 
            'desc': 'This website need peoeple to code please send dudes and stuff',
            'price_range': (42, 90),
            'agreed_pay': 110,
            'total_earned': 1142,
            'status': 'Completed', 
        },
        {
            'comp_name': 'Google',
            'start_date': '2024-04-05',
            'completion_date': '2024-04-09',
            'title': 'implement firebase Authentication', 
            'desc': 'This website need peoeple to code please send dudes and stuff',
            'price_range': (42, 90),
            'agreed_pay': 110,
            'total_earned': 1142,
            'status': 'Completed', 
        },
    ]
    return render_template('contract_history.html', contracts=contracts, user_data = user_data)


# WALLET TOPUP
@acc_info_blueprint.route('/org/acc_info/wallet', methods = ["GET", "POST"])
def org_wallet():
    # Call this function in every route, to ensure navbar details
    is_indi_or_org(False)
    user_data = acc_nav_details(session.get("user_id"))

    form = WalletTopup()

    if form.validate_on_submit():
        # Organization Account
        org_wallet_db = db.reference("/org_accounts").child(session.get("user_id")[2:])

        if org_wallet_db.get()["Wallet"]:
            new_wallet_amount = org_wallet_db.get()["Wallet"] + int(form.amount.data)
            org_wallet_db.update({"Wallet": new_wallet_amount})

            return redirect(url_for('accinfo.org_wallet'))

    return render_template("wallet.html", form = form, user_data = user_data)

@acc_info_blueprint.route('/org/acc_info/wallet', methods = ["GET", "POST"])
def indi_wallet():
    # Call this function in every route, to ensure navbar details
    is_indi_or_org(True)
    user_data = acc_nav_details(session.get("user_id"))

    form = WalletTopup()

    if form.validate_on_submit():
        # Individual Account
        user_wallet_db = db.reference("/user_accounts").child(auth.get_user(session.get("user_id")[2:]).display_name).child("Wallet").get()

        if user_wallet_db:
            new_wallet_amount = user_wallet_db + int(form.amount.data)
            db.reference("/user_accounts").child(auth.get_user(session.get("user_id")[2:]).display_name).update({"Wallet": new_wallet_amount})

            return redirect(url_for('accinfo.indi_wallet'))

    return render_template("wallet.html", form = form, user_data = user_data)


# BUY TOKENS
@acc_info_blueprint.route('/individual/buy_tokens', methods=['GET', 'POST'])
def buy_tokens():
    is_indi_or_org(True)
    # Call this function in every route, to ensure navbar details
    user_data = acc_nav_details(session.get("user_id"))
    form = BuyTokens()   
    # Individual Account
    user_ref = db.reference("/user_accounts").child(auth.get_user(session.get("user_id")[2:]).display_name)
    
    if form.validate_on_submit():
        # Reduce wallet balance
        user_ref.update({"Wallet": user_ref.get()["Wallet"] - int(form.token.data)})

        # Give tokens
        if form.token.data == "3":
            user_ref.update({"Tokens": user_ref.get()["Tokens"] + 10})
        if form.token.data == "7":
            user_ref.update({"Tokens": user_ref.get()["Tokens"] + 55})
        if form.token.data == "12":
            user_ref.update({"Tokens": user_ref.get()["Tokens"] + 120})

        return redirect(url_for('dashboard.individuals'))
        

    return render_template("buy_tokens.html", form = form, user_data = user_data)

@acc_info_blueprint.route('/org/buy_tokens', methods=['GET', 'POST'])
def org_buy_tokens():
    is_indi_or_org(False)
    # Call this function in every route, to ensure navbar details
    user_data = acc_nav_details(session.get("user_id"))
    form = BuyTokens()

    # Organization Account
    org_ref = db.reference("/org_accounts").child(session.get("user_id")[2:])

    if form.validate_on_submit():
        # Reduce wallet balance
        org_ref.update({"Wallet": org_ref.get()["Wallet"] - int(form.token.data)})

        # Give tokens
        if form.token.data == "3":
            org_ref.update({"Tokens": org_ref.get()["Tokens"] + 10})
        if form.token.data == "7":
            org_ref.update({"Tokens": org_ref.get()["Tokens"] + 55})
        if form.token.data == "12":
            org_ref.update({"Tokens": org_ref.get()["Tokens"] + 120})

        return redirect(url_for('dashboard.organization'))
      
    return render_template("buy_tokens.html", form = form, user_data = user_data)


@acc_info_blueprint.route('/acc_info/profile/organization')
def org_profile():
    is_indi_or_org(False)
    # Call this function in every route, to ensure navbar details
    user_data = acc_nav_details(session.get("user_id"))

    return render_template("org_profile.html", user_data = user_data)


# ORGANIZATION ACCOUNT SETTINGS
@acc_info_blueprint.route('/acc_info/acc_settings/org')
def org_settings():
    is_indi_or_org(False)
    # Call this function in every route, to ensure navbar details
    user_data = acc_nav_details(session.get("user_id"))

    return render_template("org_acc_settings.html", user_data = user_data)

# ORGANIZATION CONTRACT HISTORY
@acc_info_blueprint.route('/acc_info/contract_history/org')
def contract_history_org():
    is_indi_or_org(False)
    # Call this function in every route, to ensure navbar details
    user_data = acc_nav_details(session.get("user_id"))
    contracts = [
        {
            'indi_username': 'test',
            'start_date': '2024-04-05',
            'completion_date': '2024-04-09',
            'title': 'Implement Firebase Authentication', 
            'desc': 'This website need peoeple to code please send dudes and stuff',
            'price_range': (42, 90),
            'total_payed': 1142,
            'status': 'Closed', 
        },
        {
            'indi_username': 'test',
            'start_date': '2024-04-05',
            'completion_date': '2024-04-09',
            'title': 'Implement Firebase Authentication', 
            'desc': 'This website need peoeple to code please send dudes and stuff',
            'price_range': (42, 90),
            'total_payed': 1142,
            'status': 'Ongoing', 
        },
        {
            'indi_username': 'test',
            'start_date': '2024-04-05',
            'completion_date': '2024-04-09',
            'title': 'Implement Firebase Authentication', 
            'desc': 'This website need peoeple to code please send dudes and stuff',
            'price_range': (42, 90),
            'total_payed': 1142,
            'status': 'Open', 
        },
        {
            'indi_username': 'test',
            'start_date': '2024-04-05',
            'completion_date': '2024-04-09',
            'title': 'Implement Firebase Authentication', 
            'desc': 'This website need peoeple to code please send dudes and stuff',
            'price_range': (42, 90),
            'total_payed': 1142,
            'status': 'Closed', 
        },
        {
            'indi_username': 'test',
            'start_date': '2024-04-05',
            'completion_date': '2024-04-09',
            'title': 'Implement Firebase Authentication', 
            'desc': 'This website need peoeple to code please send dudes and stuff',
            'price_range': (42, 90),
            'total_payed': 1142,
            'status': 'Ongoing', 
        },
        {
            'indi_username': 'test',
            'start_date': '2024-04-05',
            'completion_date': '2024-04-09',
            'title': 'Implement Firebase Authentication', 
            'desc': 'This website need peoeple to code please send dudes and stuff',
            'price_range': (42, 90),
            'total_payed': 1142,
            'status': 'Open', 
        },
        {
            'indi_username': 'test',
            'start_date': '2024-04-05',
            'completion_date': '2024-04-09',
            'title': 'Implement Firebase Authentication', 
            'desc': 'This website need peoeple to code please send dudes and stuff',
            'price_range': (42, 90),
            'total_payed': 1142,
            'status': 'Closed', 
        },
        {
            'indi_username': 'test',
            'start_date': '2024-04-05',
            'completion_date': '2024-04-09',
            'title': 'Implement Firebase Authentication', 
            'desc': 'This website need peoeple to code please send dudes and stuff',
            'price_range': (42, 90),
            'total_payed': 1142,
            'status': 'Ongoing', 
        },
        {
            'indi_username': 'test',
            'start_date': '2024-04-05',
            'completion_date': '2024-04-09',
            'title': 'Implement Firebase Authentication', 
            'desc': 'This website need peoeple to code please send dudes and stuff',
            'price_range': (42, 90),
            'total_payed': 1142,
            'status': 'Open', 
        },
        {
            'indi_username': 'test',
            'start_date': '2024-04-05',
            'completion_date': '2024-04-09',
            'title': 'Implement Firebase Authentication', 
            'desc': 'This website need peoeple to code please send dudes and stuff',
            'price_range': (42, 90),
            'total_payed': 1142,
            'status': 'Closed', 
        },
        {
            'indi_username': 'test',
            'start_date': '2024-04-05',
            'completion_date': '2024-04-09',
            'title': 'Implement Firebase Authentication', 
            'desc': 'This website need peoeple to code please send dudes and stuff',
            'price_range': (42, 90),
            'total_payed': 1142,
            'status': 'Ongoing', 
        },
        {
            'indi_username': 'test',
            'start_date': '2024-04-05',
            'completion_date': '2024-04-09',
            'title': 'Implement Firebase Authentication', 
            'desc': 'This website need peoeple to code please send dudes and stuff',
            'price_range': (42, 90),
            'total_payed': 1142,
            'status': 'Open', 
        },
        {
            'indi_username': 'test',
            'start_date': '2024-04-05',
            'completion_date': '2024-04-09',
            'title': 'Implement Firebase Authentication', 
            'desc': 'This website need peoeple to code please send dudes and stuff',
            'price_range': (42, 90),
            'total_payed': 1142,
            'status': 'Closed', 
        },
        {
            'indi_username': 'test',
            'start_date': '2024-04-05',
            'completion_date': '2024-04-09',
            'title': 'Implement Firebase Authentication', 
            'desc': 'This website need peoeple to code please send dudes and stuff',
            'price_range': (42, 90),
            'total_payed': 1142,
            'status': 'Ongoing', 
        },
        {
            'indi_username': 'test',
            'start_date': '2024-04-05',
            'completion_date': '2024-04-09',
            'title': 'Implement Firebase Authentication', 
            'desc': 'This website need peoeple to code please send dudes and stuff',
            'price_range': (42, 90),
            'total_payed': 1142,
            'status': 'Open', 
        },
    ]
    return render_template("org_contract_history.html", user_data = user_data, contracts=contracts)