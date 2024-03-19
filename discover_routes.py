from auth_routes import session_remove_if_not_verified
from flask import Blueprint, render_template, redirect, url_for, session
from firebase_admin import db
from datetime import date
from discover_forms import CreateContract


# Blueprint initialization
discover_blueprint = Blueprint(
    "discover", __name__, static_folder="static", template_folder="templates"
)

# ---------- MAIN DISCOVER PAGE ----------
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
    "minprice": 46.05,
    "maxprice": 70.05,
    "company": "Google",
    "title": "Implement User Authentication using Firebase",
    "desc": "Our business website is using Firebase as its primary database, therefore, we need to implement login and registration functionality using Firebase Authentication to securely manage user access and authentication processes.",
    "time": today,
    "profileimg": "static/icons/person.svg",
    "profilename": "Victor Salazar"
    },]
    # {
    # "price": 46.05,
    # "title": "Implement Firebase Authentication",
    # "desc": "Our business website is using Firebase as its primary database; therefore, we need to implement login and registration functionality using Firebase Authentication to securely manage user access and authentication processes.",
    # "time": today,
    # "profileimg": "static/icons/person.svg",
    # "profilename": "Victor Salazar"
    # },
    # {
    # "price": 46.05,
    # "title": "Implement Firebase Authentication",
    # "desc": "Our business website is using Firebase as its primary database; therefore, we need to implement login and registration functionality using Firebase Authentication to securely manage user access and authentication processes.",
    # "time": today,
    # "profileimg": "static/icons/person.svg",
    # "profilename": "Victor Salazar"
    # },
    # {
    # "price": 46.05,
    # "title": "Implement Firebase Authentication",
    # "desc": "Our business website is using Firebase as its primary database; therefore, we need to implement login and registration functionality using Firebase Authentication to securely manage user access and authentication processes.",
    # "time": today,
    # "profileimg": "static/icons/person.svg",
    # "profilename": "Victor Salazar"
    # },
    # {
    # "price": 46.05,
    # "title": "Implement Firebase Authentication",
    # "desc": "Our business website is using Firebase as its primary database; therefore, we need to implement login and registration functionality using Firebase Authentication to securely manage user access and authentication processes.",
    # "time": today,
    # "profileimg": "static/icons/person.svg",
    # "profilename": "Victor Salazar"
    # },
    # {
    # "price": 46.05,
    # "title": "Implement Firebase Authentication",
    # "desc": "Our business website is using Firebase as its primary database; therefore, we need to implement login and registration functionality using Firebase Authentication to securely manage user access and authentication processes.",
    # "time": today,
    # "profileimg": "static/icons/person.svg",
    # "profilename": "Victor Salazar"
    # },
    # {
    # "price": 46.05,
    # "title": "Implement Firebase Authentication",
    # "desc": "Our business website is using Firebase as its primary database; therefore, we need to implement login and registration functionality using Firebase Authentication to securely manage user access and authentication processes.",
    # "time": today,
    # "profileimg": "static/icons/person.svg",
    # "profilename": "Victor Salazar"
    # },
    # {
    # "price": 46.05,
    # "title": "Implement Firebase Authentication",
    # "desc": "Our business website is using Firebase as its primary database; therefore, we need to implement login and registration functionality using Firebase Authentication to securely manage user access and authentication processes.",
    # "time": today,
    # "profileimg": "static/icons/person.svg",
    # "profilename": "Victor Salazar"
    # },
    # {
    # "price": 46.05,
    # "title": "Implement Firebase Authentication",
    # "desc": "Our business website is using Firebase as its primary database; therefore, we need to implement login and registration functionality using Firebase Authentication to securely manage user access and authentication processes.",
    # "time": today,
    # "profileimg": "static/icons/person.svg",
    # "profilename": "Victor Salazar"
    # },
    # {
    # "price": 46.05,
    # "title": "Implement Firebase Authentication",
    # "desc": "Our business website is using Firebase as its primary database; therefore, we need to implement login and registration functionality using Firebase Authentication to securely manage user access and authentication processes.",
    # "time": today,
    # "profileimg": "static/icons/person.svg",
    # "profilename": "Victor Salazar"
    # },
    # {
    # "price": 46.05,
    # "title": "Implement Firebase Authentication",
    # "desc": "Our business website is using Firebase as its primary database; therefore, we need to implement login and registration functionality using Firebase Authentication to securely manage user access and authentication processes.",
    # "time": today,
    # "profileimg": "static/icons/person.svg",
    # "profilename": "Victor Salazar"
    # },
    # {
    # "price": 46.05,
    # "title": "Implement Firebase Authentication",
    # "desc": "Our business website is using Firebase as its primary database; therefore, we need to implement login and registration functionality using Firebase Authentication to securely manage user access and authentication processes.",
    # "time": today,
    # "profileimg": "static/icons/person.svg",
    # "profilename": "Victor Salazar"
    # },
    # {
    # "price": 46.05,
    # "title": "Implement Firebase Authentication",
    # "desc": "Our business website is using Firebase as its primary database; therefore, we need to implement login and registration functionality using Firebase Authentication to securely manage user access and authentication processes.",
    # "time": today,
    # "profileimg": "static/icons/person.svg",
    # "profilename": "Victor Salazar"
    # },
    # {
    # "price": 46.05,
    # "title": "Implement Firebase Authentication",
    # "desc": "Our business website is using Firebase as its primary database; therefore, we need to implement login and registration functionality using Firebase Authentication to securely manage user access and authentication processes.",
    # "time": today,
    # "profileimg": "static/icons/person.svg",
    # "profilename": "Victor Salazar"
    # },
    # {
    # "price": 46.05,
    # "title": "Implement Firebase Authentication",
    # "desc": "Our business website is using Firebase as its primary database; therefore, we need to implement login and registration functionality using Firebase Authentication to securely manage user access and authentication processes.",
    # "time": today,
    # "profileimg": "static/icons/person.svg",
    # "profilename": "Victor Salazar"
    # },
    # {
    # "price": 46.05,
    # "title": "Implement Firebase Authentication",
    # "desc": "Our business website is using Firebase as its primary database; therefore, we need to implement login and registration functionality using Firebase Authentication to securely manage user access and authentication processes.",
    # "time": today,
    # "profileimg": "static/icons/person.svg",
    # "profilename": "Victor Salazar"
    # },
    # {
    # "price": 46.05,
    # "title": "Implement Firebase Authentication",
    # "desc": "Our business website is using Firebase as its primary database; therefore, we need to implement login and registration functionality using Firebase Authentication to securely manage user access and authentication processes.",
    # "time": today,
    # "profileimg": "static/icons/person.svg",
    # "profilename": "Victor Salazar"
    # }]

    return render_template("discover.html", ad_details=ad_details)




# ---------- CONTRACT PAGE ----------
@discover_blueprint.route("/contract")
def contractpage():
    session_remove_if_not_verified()

    return render_template("contract.html")




# ---------- CREATE CONTRACT ----------
@discover_blueprint.route("/create_contract", methods = ["POST", "GET"])
def create_contract():
    contract_ref = db.reference("/contracts")
    session_remove_if_not_verified()

    if check_if_user_is_company():
        form = CreateContract()

        if form.validate_on_submit():

            contract_ref.push(
                {
                    "Price": form.price.data,
                    "Title": form.title.data,
                    "Description": form.description.data,
                    "Contract Image": form.contract_img.data,
                    "Author": session.get('user_id')[2:]
                }
            )
        
        else:
            print("Create contract form error: ", form.errors)

    else:
        print("You are not authorized to access this page.")
        return redirect(url_for('discover.main'))

    return render_template("temp/create_contract.html", form = form)



# ---------- EDIT CONTRACT ----------
@discover_blueprint.route("/edit_contract/<string:contract_id>", methods = ["POST", "GET"])
def edit_contract(contract_id):
    session_remove_if_not_verified()
    contract_ref = db.reference("/contracts").child("-" + contract_id)

    # Checking if user is an organization account AND if the current user is the author of the contract
    if contract_ref.child("Author").get() == session.get('user_id')[2:] and check_if_user_is_company():
        form = CreateContract()

        # If form is submitted, apply changes
        if form.validate_on_submit():
            
            contract_ref.update(
                {
                    "Price": form.price.data,
                    "Title": form.title.data,
                    "Description": form.description.data,
                    "Contract Image": form.contract_img.data,
                }
            )
        
        # Else just display the contents
        else:
            form.price.data = contract_ref.child("Price").get()
            form.title.data = contract_ref.child("Title").get()
            form.description.data = contract_ref.child("Description").get()
            form.contract_img.data = contract_ref.child("Contract Image").get()
            
            print("Edit contract form error: ", form.errors)

    else:
        print("You are not authorized to access this page.")
        return redirect(url_for('discover.main'))

    return render_template("temp/edit_contract.html", form = form)



# ---------- DELETE CONTRACT ----------
# Logic for deleting contract:
# Only available in my contracts list/page
# Display all contracts made by current user
# On deleting a contract, get contract ID and pop or delete it from firebase real db



# ---------------------------
# Helper Functions
# ---------------------------

# Function that returns true if current user is org, else false.
def check_if_user_is_company():
    account_ref = db.reference("/")

    # If current user is org account
    if session.get('user_id')[0] == "O":
        return True
    
    # Any other account
    else:
        return False