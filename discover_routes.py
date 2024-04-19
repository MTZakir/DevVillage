import uuid
from flask import Blueprint, render_template, redirect, url_for, session
from firebase_admin import db
from datetime import date
from discover_forms import CreateContract, ApplyContract
from firebase_admin import auth
from firebase_admin._auth_utils import UserNotFoundError
from datetime import date

# Blueprint initialization
discover_blueprint = Blueprint(
    "discover", __name__, static_folder="static", template_folder="templates"
)

# Remove session if current user is unverified
# use this in the beginning of every route function
@discover_blueprint.before_request
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
    
def is_indi_or_org(acc_type):
    if acc_type:
        return redirect(url_for("homecomp"))
    else:
        return redirect(url_for("home"))

# ---------- MAIN DISCOVER PAGE ----------
@discover_blueprint.route('/discover/individual')
def individuals():
    is_indi_or_org(True)

    
    contract_list = db.reference("/contracts").get()
    print(contract_list.values())
    return render_template("indidiscover.html", contract_list = contract_list) 

@discover_blueprint.route('/discover/companies')
def companies():
    is_indi_or_org(False)

    
    posted_date = date.today()
    ad_list=[
        {
            'title': 'Design and develop a home page',
            'description': 'designer and developer needed to develop a homw page with react',
            'date':posted_date,
            'name': 'Victor Salazaar',
            'ratings': 4.3
        },
        {
            'title': 'Design and develop a home page',
            'description': 'designer and developer needed to develop a homw page with react',
            'date':posted_date,
            'name': 'Victor Salazaar',
            'ratings': 3.2
        },
        {
            'title': 'Design and develop a home page',
            'description': 'designer and developer needed to develop a homw page with react',
            'date':posted_date,
            'name': 'Victor Salazaar',
            'ratings': 3.6
        },
        {
            'title': 'Design and develop a home page',
            'description': 'designer and developer needed to develop a homw page with react',
            'date':posted_date,
            'name': 'Victor Salazaar',
            'ratings': 4.7
        },
        {
            'title': 'Design and develop a home page',
            'description': 'designer and developer needed to develop a homw page with react',
            'date':posted_date,
            'name': 'Victor Salazaar',
            'ratings': 4.1
        },
        {
            'title': 'Design and develop a home page',
            'description': 'designer and developer needed to develop a homw page with react',
            'date':posted_date,
            'name': 'Victor Salazaar',
            'ratings': 2.4
        },
        {
            'title': 'Design and develop a home page',
            'description': 'designer and developer needed to develop a homw page with react',
            'date':posted_date,
            'name': 'Victor Salazaar',
            'ratings': 2.4
        },
        {
            'title': 'Design and develop a home page',
            'description': 'designer and developer needed to develop a homw page with react',
            'date':posted_date,
            'name': 'Victor Salazaar',
            'ratings': 2.4
        },
        {
            'title': 'Design and develop a home page',
            'description': 'designer and developer needed to develop a homw page with react',
            'date':posted_date,
            'name': 'Victor Salazaar',
            'ratings': 2.4
        },
        {
            'title': 'Design and develop a home page',
            'description': 'designer and developer needed to develop a homw page with react',
            'date':posted_date,
            'name': 'Victor Salazaar',
            'ratings': 2.4
        },
        {
            'title': 'Design and develop a home page',
            'description': 'designer and developer needed to develop a homw page with react',
            'date':posted_date,
            'name': 'Victor Salazaar',
            'ratings': 2.4
        },
        {
            'title': 'Design and develop a home page',
            'description': 'designer and developer needed to develop a homw page with react',
            'date':posted_date,
            'name': 'Victor Salazaar',
            'ratings': 2.4
        },
        {
            'title': 'Design and develop a home page',
            'description': 'designer and developer needed to develop a homw page with react',
            'date':posted_date,
            'name': 'Victor Salazaar',
            'ratings': 2.4
        },
        {
            'title': 'Design and develop a home page',
            'description': 'designer and developer needed to develop a homw page with react',
            'date':posted_date,
            'name': 'Victor Salazaar',
            'ratings': 2.4
        },
        {
            'title': 'Design and develop a home page',
            'description': 'designer and developer needed to develop a homw page with react',
            'date':posted_date,
            'name': 'Victor Salazaar',
            'ratings': 2.4
        },
        {
            'title': 'Design and develop a home page',
            'description': 'designer and developer needed to develop a homw page with react',
            'date':posted_date,
            'name': 'Victor Salazaar',
            'ratings': 2.4
        },
        {
            'title': 'Design and develop a home page',
            'description': 'designer and developer needed to develop a homw page with react',
            'date':posted_date,
            'name': 'Victor Salazaar',
            'ratings': 2.4
        },
        {
            'title': 'Design and develop a home page',
            'description': 'designer and developer needed to develop a homw page with react',
            'date':posted_date,
            'name': 'Victor Salazaar',
            'ratings': 2.4
        },
        {
            'title': 'Design and develop a home page',
            'description': 'designer and developer needed to develop a homw page with react',
            'date':posted_date,
            'name': 'Victor Salazaar',
            'ratings': 2.4
        },
    ]
    return render_template("org_discover.html", ad_list=ad_list)




# ---------- CONTRACT PAGE ----------
@discover_blueprint.route("/contract/<string:contract_id>", methods = ["POST", "GET"])
def contract(contract_id):
    # WORK IN PROGESS

    # contract_data = db.reference("/contracts").child(contract_id).get()

    # Creating and loading the list of all applicants in the contract
    applicants_list = []
    if db.reference("/contracts/"+contract_id).child("Applied").get():
        applicants_list = db.reference("/contracts/"+contract_id+"/Applied").get()

    # Preventing reapplication of contract if already applied
    if session.get("user_id")[2:] in applicants_list:
        print("You have already applied for this contract")
        return redirect(url_for('discover.individuals'))
    
    form = ApplyContract()

    if form.validate_on_submit():
        contract_ref = db.reference("/contracts")

        # Adding new applicant to list of applicants
        applicants_list.append(session.get("user_id")[2:])
        contract_ref.child(contract_id).update(
            {"Applied": applicants_list}
        )

        return redirect(url_for('discover.individuals'))

    return render_template("temp/temp_contract.html", form = form)




# ---------- CREATE CONTRACT ----------
@discover_blueprint.route("/create_contract", methods = ["POST", "GET"])
def create_contract():
    contract_ref = db.reference("/contracts")

    if check_if_user_is_company():
        form = CreateContract()

        if form.validate_on_submit():

            today = date.today().strftime("%d-%m-%Y")
            org_name = auth.get_user(session.get('user_id')[2:]).display_name

            uid = str(uuid.uuid4())

            contract_details = {
                    "Min Price": form.min_price.data,
                    "Max Price": form.max_price.data,
                    "Title": form.title.data,
                    "Description": form.description.data,
                    "Contract Image": form.contract_img.data,
                    "Company Name": org_name,
                    "Author": session.get('user_id')[2:],
                    "Date Posted": today
                }

            contract_ref.update({uid: contract_details})
        
        else:
            print("Create contract form error: ", form.errors)

    else:
        print("You are not authorized to access this page.")
        return redirect(url_for('discover.main'))

    return render_template("temp/create_contract.html", form = form)



# ---------- EDIT CONTRACT ----------
@discover_blueprint.route("/edit_contract/<string:contract_id>", methods = ["POST", "GET"])
def edit_contract(contract_id):
    contract_ref = db.reference("/contracts").child("-" + contract_id)

    # Checking if user is an organization account AND if the current user is the author of the contract
    if contract_ref.child("Author").get() == session.get('user_id')[2:] and check_if_user_is_company():
        form = CreateContract()

        # If form is submitted, apply changes
        if form.validate_on_submit():
            
            contract_ref.update(
                {
                    "Min Price": form.min_price.data,
                    "Max Price": form.max_price.data,
                    "Title": form.title.data,
                    "Description": form.description.data,
                    "Contract Image": form.contract_img.data,
                    "Company Name": form.company_name.data
                }
            )
        
        # Else just display the contents
        else:
            form.min_price.data = contract_ref.child("Min Price").get()
            form.max_price.data = contract_ref.child("Max Price").get()
            form.title.data = contract_ref.child("Title").get()
            form.description.data = contract_ref.child("Description").get()
            form.contract_img.data = contract_ref.child("Contract Image").get()
            form.company_name.data = contract_ref.child("Company Name").get()
            
            print("Edit contract form error: ", form.errors)

    else:
        print("You are not authorized to access this page.")
        return redirect(url_for('discover.main'))

    return render_template("temp/edit_contract.html", form = form)

@discover_blueprint.route("/applicants", methods = ["POST", "GET"])

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