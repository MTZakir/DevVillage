from flask import Blueprint, redirect, render_template, session, url_for

# Blueprint initialization
prof_blueprint = Blueprint(
    "profile", __name__, static_folder="static", template_folder="templates"
)

@prof_blueprint.route('/profile/individual')
def individual_profile():
    if not session.get("user_id") or session.get("user_id")[:2] == "O-":
        return redirect(url_for("home"))
    
    return render_template("accountinfo.html")