from flask import Blueprint, render_template


# Blueprint initialization



discover_blueprint = Blueprint(
    "discover", __name__, static_folder="static", template_folder="templates"
)

# DISCOVER
@discover_blueprint.route('/discover')
def discover():

    # LOGIC FOR DISCOVER

    # ref = db.reference("/users")
    # ref.update({"Chupapi": {"age": "6", "ball size": "2mm", "ball height": "0.1mm"}})

    return render_template("discover.html")