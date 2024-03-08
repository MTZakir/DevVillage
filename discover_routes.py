from auth_routes import session_remove_if_not_verified
from flask import Blueprint, render_template


# Blueprint initialization
discover_blueprint = Blueprint(
    "discover", __name__, static_folder="static", template_folder="templates"
)

# DISCOVER
@discover_blueprint.route('/discover')
def main():

    # LOGIC FOR DISCOVER

    # ref = db.reference("/users")
    # ref.update({"Chupapi": {"age": "6", "ball size": "2mm", "ball height": "0.1mm"}})
    session_remove_if_not_verified()
    return render_template("discover.html")