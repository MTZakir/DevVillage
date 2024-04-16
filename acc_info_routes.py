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

@acc_info_blueprint.route('/profile/individual')
def individual_profile():
    is_indi_or_org(True)

    return render_template("indiprofile.html")

@acc_info_blueprint.route('/profile/org')
def org_profile():
    is_indi_or_org(False)

    
    return render_template("org_profile.html")

@acc_info_blueprint.route('/acc_settings/individual')
def individual_settings():
    is_indi_or_org(True)


    return render_template("indi_acc_settings.html")

@acc_info_blueprint.route('/acc_settings/org')
def org_settings():
    is_indi_or_org(False)

    return render_template("org_acc_settings.html")