from auth_routes import session_remove_if_not_verified
from flask import Blueprint, render_template
from datetime import date


# Blueprint initialization
discover_blueprint = Blueprint(
    "discover", __name__, static_folder="static", template_folder="templates"
)

# DISCOVER
@discover_blueprint.route('/discover')
def main():
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

    # ref = db.reference("/users")
    # ref.update({"Chupapi": {"age": "6", "ball size": "2mm", "ball height": "0.1mm"}})
    session_remove_if_not_verified()
    return render_template("discover.html", ad_details=ad_details)

@discover_blueprint.route("/contract")
def contractpage():
    session_remove_if_not_verified()
    return render_template("contract.html")