from flask import Blueprint, redirect, render_template, session, url_for
from firebase_admin import auth
from firebase_admin._auth_utils import UserNotFoundError
from dashboard_routes import user_nav_details
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



@acc_info_blueprint.route('/acc_info/profile/individual')
def individual_profile():
    is_indi_or_org(True)
    # Call this function in every route, to ensure navbar details
    # Contains first name, last name, display name, wallet amount, tokens and notifications
    user_data = user_nav_details(session.get("user_id")[2:])

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


@acc_info_blueprint.route('/acc_info/acc_settings/individual', methods=['GET', 'POST'])
def individual_settings():
    is_indi_or_org(True)
    # Call this function in every route, to ensure navbar details
    # Contains display name, first name, last name, wallet and tokens
    user_data = user_nav_details(session.get("user_id")[2:])

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

# CONTRACT HISTORY
@acc_info_blueprint.route('/acc_info/contract_history/individual')
def contract_history():
    is_indi_or_org(True)
    # Call this function in every route, to ensure navbar details
    user_data = user_nav_details(session.get("user_id")[2:])

    contracts = [
        {
            'comp_name': 'Google',
            'start_date': '2024-04-05',
            'completion_date': '2024-04-09',
            'title': 'implement firebase Authentication', 
            'desc': 'This website need peoeple to code please send dudes and stuff',
            'price_range': (42, 90),
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
            'total_earned': 1142,
            'status': 'Completed', 
        },
    ]
    return render_template('contract_history.html', contracts=contracts, user_data = user_data)


# WALLET TOPUP
@acc_info_blueprint.route('/acc_info/wallet/individual', methods = ["GET", "POST"])
def wallet():
    is_indi_or_org(True)
    # Call this function in every route, to ensure navbar details
    user_data = user_nav_details(session.get("user_id")[2:])

    form = WalletTopup()

    if form.validate_on_submit():
        user_wallet_db = db.reference("/user_accounts").child(auth.get_user(session.get("user_id")[2:]).display_name).child("Wallet").get()

        if (user_wallet_db):
            db.reference("/user_accounts").child(auth.get_user(session.get("user_id")[2:]).display_name).update({"Wallet": user_wallet_db + int(form.amount.data)})

    return render_template("wallet.html", form = form, user_data = user_data)


# BUY TOKENS
@acc_info_blueprint.route('/buy_tokens', methods=['GET', 'POST'])
def buy_tokens():
    is_indi_or_org(True)
    # Call this function in every route, to ensure navbar details
    user_data = user_nav_details(session.get("user_id")[2:])

    user_ref = db.reference("/user_accounts").child(auth.get_user(session.get("user_id")[2:]).display_name)

    form = BuyTokens()
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


@acc_info_blueprint.route('/acc_info/acc_settings/org')
def org_settings():
    is_indi_or_org(False)
    # Call this function in every route, to ensure navbar details
    user_data = user_nav_details(session.get("user_id")[2:])

    return render_template("org_acc_settings.html", user_data = user_data)