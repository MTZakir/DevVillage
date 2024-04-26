import uuid, pyrebase, os
from ast import literal_eval
from flask import Blueprint, render_template, redirect, url_for, session
from firebase_admin import db
from datetime import date
from discover_forms import CreateContract, ApplyContract
from firebase_admin import auth
from firebase_admin._auth_utils import UserNotFoundError
from datetime import date
from dashboard_routes import acc_nav_details

# Blueprint initialization
discover_blueprint = Blueprint(
    "discover", __name__, static_folder="static", template_folder="templates"
)

# Initializing pyrebase
pyrebase_config = {
    "apiKey": "AIzaSyDPEdHrwpZOvi0d1d1fUx1WOrX1RJ3TYHc",
    "authDomain": "codebase-93435.firebaseapp.com",
    "databaseURL": "https://codebase-93435-default-rtdb.europe-west1.firebasedatabase.app",
    "projectId": "codebase-93435",
    "storageBucket": "codebase-93435.appspot.com",
    "messagingSenderId": "580884701092",
    "appId": "1:580884701092:web:b4f7be265ee7ad59b9ab31",
    "measurementId": "G-JRZ98QNRSL"
}
firebase = pyrebase.initialize_app(pyrebase_config)

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
    # Call this function in every route, to ensure navbar details
    user_data = acc_nav_details(session.get("user_id"))


    contract_list = db.reference("/contracts").get()
    return render_template("indidiscover.html", contract_list = contract_list, user_data = user_data) 

@discover_blueprint.route('/discover/organization')
def companies():
    is_indi_or_org(False)
    # Call this function in every route, to ensure navbar details
    user_data = acc_nav_details(session.get("user_id"))

    
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
    return render_template("org_discover.html", ad_list=ad_list, user_data = user_data)




# ---------- CONTRACT PAGE ----------
@discover_blueprint.route("/contract/<string:contract_id>", methods = ["POST", "GET"])
def contract(contract_id):
    # If a user is logged in
    if session.get("user_id") is not None:
        # If user is a individual user
        if auth.get_user(session.get("user_id")[2:]).display_name in db.reference("/user_accounts").get():
            # Call this function in every route, to ensure navbar details
            user_data = acc_nav_details(session.get("user_id"))

            # Retrieve contract details
            contract_info = db.reference("/contracts").child(contract_id).get()
            company_info = db.reference("/org_accounts").child(contract_info["Author"]).get()
            
            # If user is applied to this contract or not
            applied = False
            if db.reference("/contracts").child(contract_id).child("Applied").get() != None:
                if session.get("user_id")[2:] in db.reference("/contracts").child(contract_id).child("Applied").get():
                    applied = True
    
            form = ApplyContract(contract_id, session.get("user_id")[2:])

            if form.validate_on_submit():
                
                if db.reference("/user_accounts").child(auth.get_user(session.get("user_id")[2:]).display_name).child("Resume").get() == None:
                    # Uploading contract image to cloud
                    storage = firebase.storage()
                    form.resume.data.save(form.resume.data.filename)
                    resume_upload = storage.child("files/resumes/" + str(session.get("user_id")[2:]) + ".pdf").put(form.resume.data.filename)
                    os.remove(form.resume.data.filename)

                    applicant_data = {
                        "Pay Requested": str(form.pay_range.data),
                        "Skill Level": form.capability.data,
                        "Message": form.message.data,
                        "Resume": storage.child("files/resumes/" + str(session.get("user_id")[2:]) + ".pdf").get_url(session.get("user_id")[2:])
                    }

                    db.reference("/contracts").child(contract_id).child("Applied").child(session.get("user_id")[2:]).update(applicant_data)

                    db.reference("/user_accounts").child(auth.get_user(session.get("user_id")[2:]).display_name).update({"Resume": storage.child("files/resumes/" + str(session.get("user_id")[2:]) + ".pdf").get_url(session.get("user_id")[2:])})

                else:
                    storage = firebase.storage()
                    
                    applicant_data = {
                        "Pay Requested": str(form.pay_range.data),
                        "Skill Level": form.capability.data,
                        "Message": form.message.data,
                        "Resume": storage.child("files/resumes/" + str(session.get("user_id")[2:]) + ".pdf").get_url(session.get("user_id")[2:])
                    }

                    db.reference("/contracts").child(contract_id).child("Applied").child(session.get("user_id")[2:]).update(applicant_data)

                return redirect(url_for('discover.individuals'))
        
        else:
            print("You are not an individual account. You do not have permission to view it.")
    else:
        print("You must be logged in to view this page.")
        return redirect(url_for('discover.individuals'))

    return render_template("contract.html", form = form, applied = applied, contract_info = contract_info, company_info = company_info, user_data = user_data)




# ---------- CREATE CONTRACT ----------
@discover_blueprint.route("/org/create_contract", methods = ["POST", "GET"])
def create_contract():
    is_indi_or_org(False)
    contract_ref = db.reference("/contracts")

    if check_if_user_is_company():
        # Call this function in every route, to ensure navbar details
        user_data = acc_nav_details(session.get("user_id"))
        form = CreateContract()

        if form.validate_on_submit():

            today = date.today().strftime("%d-%m-%Y")
            org_name = auth.get_user(session.get('user_id')[2:]).display_name

            uid = str(uuid.uuid4())

            # Uploading contract image to cloud
            storage = firebase.storage()
            form.contract_img.data.save(form.contract_img.data.filename)
            contract_img_upload = storage.child("images/contract_images/" + uid + "-" + form.contract_img.data.filename).put(form.contract_img.data.filename)
            os.remove(form.contract_img.data.filename)


            scope = [str(x.strip()) for x in form.scope.data[1:-1].split(',')]
            deliverables = [str(x.strip()) for x in form.deliverables.data[1:-1].split(',')]
            tech = [str(x.strip()) for x in form.tech_stack.data[1:-1].split(',')]
            notes = [str(x.strip()) for x in form.notes.data[1:-1].split(',')]


            contract_details = {
                    # Form data
                    "Title": form.title.data,
                    "Description": form.description.data,
                    "Min Price": form.min_price.data,
                    "Max Price": form.max_price.data,
                    "Duration": form.duration.data,
                    "Difficulty": form.difficulty.data,
                    "Contract Image": storage.child("images/contract_images/" + uid + "-" + form.contract_img.data.filename).get_url(session.get("user_id")[2:]),
                    "Scope": scope,
                    "Deliverables": deliverables,
                    "Technology Stack": tech,
                    "Payment Terms": ["Payment will be made every 15 days for a duration of " + str(payment_term_calc(form.duration.data))],
                    # Auto data
                    "Status": "Open",
                    "Company Name": org_name,
                    "Author": session.get('user_id')[2:],
                    "Date Posted": today
                }

            if form.notes.data != None:
                contract_details.update({"Notes": notes})

            contract_ref.update({uid: contract_details})

            return redirect(url_for("discover.create_contract"))
        
        else:
            print("Create contract form error: ", form.errors)

    else:
        print("You are not authorized to access this page.")
        return redirect(url_for('discover.individuals'))

    return render_template("create_contract.html", form = form, user_data = user_data)

# Helper function for create_contract()
def payment_term_calc(days):
    if days == "15":
        return "15 Days"
    elif days == "30":
        return "1 Month"
    elif days == "45":
        return "1 Month + 15 Days"
    elif days == "60":
        return "2 Months"
    elif days == "75":
        return "2 Months + 15 Days"
    elif days == "90":
        return "3 Months"
    



# ---------- EDIT CONTRACT ----------
@discover_blueprint.route("/edit_contract/<string:contract_id>", methods = ["POST", "GET"])
def edit_contract(contract_id):
    contract_ref = db.reference("/contracts").child("-" + contract_id)

    # Checking if user is an organization account AND if the current user is the author of the contract
    if contract_ref.child("Author").get() == session.get('user_id')[2:] and check_if_user_is_company():
        # Call this function in every route, to ensure navbar details
        user_data = acc_nav_details(session.get("user_id"))
        
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

    return render_template("temp/edit_contract.html", form = form, user_data = user_data)


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