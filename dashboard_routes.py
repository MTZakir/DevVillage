from flask import Blueprint, render_template, session
from firebase_admin import db, auth
from firebase_admin._auth_utils import UserNotFoundError

dashboard_blueprint = Blueprint(
    "dashboard", __name__, static_folder="static", template_folder="templates"
)

# Remove session if current user is unverified
# use this in the beginning of every route function
@dashboard_blueprint.before_request
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

# DISCOVER
@dashboard_blueprint.route('/dashboard')
def discover():
    org_name = db.reference("/org_accounts")
    company_hires = [
        {
            'Organization': org_name.order_by_child('Org Website').equal_to('asd.com'),
            'Contract Title': 'designer and developer needed to develop a homw page with react',
            'Contract Time':posted_date,
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
    return render_template("temp/dashboard_temp.html")