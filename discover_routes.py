from auth_routes import session_remove_if_not_verified
from flask import Blueprint, render_template, redirect, url_for, session
from firebase_admin import db
from datetime import date
from discover_forms import CreateContract


# Blueprint initialization
discover_blueprint = Blueprint(
    "discover", __name__, static_folder="static", template_folder="templates"
)

# DISCOVER
@discover_blueprint.route('/discover')
def main():
    session_remove_if_not_verified()


    today = date.today().strftime("%d-%m-%Y")
    # LOGIC FOR DISCOVER
    ad_details = [{
    "price": 46.05,
    "title": "Implement Firebase Authentication",
    "desc": "Our business website is using Firebase as its primary database; therefore, we need to implement login and registration functionality using Firebase Authentication to securely manage user access and authentication processes.",
    "time": today,
    "profileimg": "static/icons/person.svg",
    "profilename": "Victor Salazar"
    },
    {
    "price": 46.05,
    "title": "Implement Firebase Authentication",
    "desc": "Our business website is using Firebase as its primary database; therefore, we need to implement login and registration functionality using Firebase Authentication to securely manage user access and authentication processes.",
    "time": today,
    "profileimg": "static/icons/person.svg",
    "profilename": "Victor Salazar"
    },
    {
    "price": 46.05,
    "title": "Implement Firebase Authentication",
    "desc": "Our business website is using Firebase as its primary database; therefore, we need to implement login and registration functionality using Firebase Authentication to securely manage user access and authentication processes.",
    "time": today,
    "profileimg": "static/icons/person.svg",
    "profilename": "Victor Salazar"
    },
    {
    "price": 46.05,
    "title": "Implement Firebase Authentication",
    "desc": "Our business website is using Firebase as its primary database; therefore, we need to implement login and registration functionality using Firebase Authentication to securely manage user access and authentication processes.",
    "time": today,
    "profileimg": "static/icons/person.svg",
    "profilename": "Victor Salazar"
    },
    {
    "price": 46.05,
    "title": "Implement Firebase Authentication",
    "desc": "Our business website is using Firebase as its primary database; therefore, we need to implement login and registration functionality using Firebase Authentication to securely manage user access and authentication processes.",
    "time": today,
    "profileimg": "static/icons/person.svg",
    "profilename": "Victor Salazar"
    }]

    return render_template("discover.html", ad_details=ad_details)

@discover_blueprint.route("/contract")
def contractpage():
    session_remove_if_not_verified()

    return render_template("contract.html")


@discover_blueprint.route("/create_contract", methods = ["POST", "GET"])
def create_contract():
    contract_ref = db.reference("/contracts")
    session_remove_if_not_verified()

    if check_if_user_is_company():
        form = CreateContract()

        if form.validate_on_submit():
            contract_ref.update({
                str(session.get('user_id')): {
                    "Price": form.price.data,
                    "Title": form.title.data,
                    "Description": form.description.data,
                    "Contract Image": form.contract_img.data
                }
            })
        
        else:
            print("Create contract form error: ", form.errors)

    else:
        print("You are not authorized to access this page.")
        return redirect(url_for('discover.main'))

    return render_template("temp/create_contract.html", form = form)




@discover_blueprint.route("/edit_contract", methods = ["POST", "GET"])
def edit_contract():
    pass




# ---------------------------
# Helper Functions
# ---------------------------

# Function that returns true if current user is org, else false.
def check_if_user_is_company():
    account_ref = db.reference("/")

    # If current user is org account
    if account_ref.child("org_accounts").get(session.get('user_id')) != None:
        return True
    
    # Any other account
    else:
        return False