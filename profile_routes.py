from flask import Blueprint, render_template

# Blueprint initialization
prof_blueprint = Blueprint(
    "profile", __name__, static_folder="static", template_folder="templates"
)

@prof_blueprint.route('/profile/individual')
def individual_profile():

    return render_template("accountnavbarlayout.html")