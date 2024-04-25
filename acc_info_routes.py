from flask import Blueprint, redirect, render_template, session, url_for
from firebase_admin import auth
from firebase_admin._auth_utils import UserNotFoundError

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

@acc_info_blueprint.route('/acc_info')
def acc_info():
    return render_template("accountinfo.html")

@acc_info_blueprint.route('/acc_info/profile/individual')
def individual_profile():
    is_indi_or_org(True)

    return render_template("indiprofile.html")

@acc_info_blueprint.route('/acc_info/profile/org')
def org_profile():
    is_indi_or_org(False)

    
    return render_template("org_profile.html")

@acc_info_blueprint.route('/acc_info/acc_settings/individual')
def individual_settings():
    is_indi_or_org(True)
    details=[
        {
            'firstname':'Dave',
            'lastname':'Batis',
            'email':'davebatis@gmail.com',
            'username':'Ballsmasher69',
            'phone':'+971-546329002',
            'profiencies':'',
            'password':'thisisballs69',
            'birth':'1999-07-05',
            'gender':'Nigga',
            'bio':'Before time began, there was the Cube. We know not where it comes from, only that it holds the power to create worlds and fill them with life. That is how our race was born. For a time, we lived in harmony, but like all great power, some wanted it for good, others for evil. And so began the war, a war that ravaged our planet until it was consumed by the death, and the Cube was lost to the far reaches of space. We scattered across the galaxy, hoping to find it and rebuild our home, searching every star, every world. And just when all hope seemed lost, message of a new discovery drew us to an unknown planet called Earth. But we were already too late.',

        }
    ]
    return render_template("indi_acc_settings.html", details=details)

@acc_info_blueprint.route('/acc_info/myadvertisement/individual')
def my_ads():
    is_indi_or_org(True)

    return render_template('myad.html')

@acc_info_blueprint.route('/acc_info/contract_history/individual')
def contract_history():
    is_indi_or_org(True)
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
    return render_template('contract_history.html', contracts=contracts)

@acc_info_blueprint.route('/buy_tokens/individual')
def buy_tokens():
    is_indi_or_org(True)

    return render_template("buy_tokens.html")


@acc_info_blueprint.route('/acc_info/acc_settings/org')
def org_settings():
    is_indi_or_org(False)

    return render_template("org_acc_settings.html")