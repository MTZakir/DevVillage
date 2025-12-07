# DevVillage

A comprehensive freelancing and contract management platform that connects skilled developers with organizations seeking technical expertise. DevVillage provides a seamless marketplace for contract-based work with integrated payment tracking, token-based application system, and real-time communication features.

## 📑 Table of Contents

- [Features](#-features)
  - [For Individuals](#for-individuals-developersfreelancers)
  - [For Organizations](#for-organizations)
  - [Security & Authentication](#security--authentication)
- [Technologies Used](#️-technologies-used)
- [Project Structure](#-project-structure)
- [Installation](#-installation)
- [Configuration](#️-configuration)
- [Usage](#-usage)
- [Key Features Explained](#-key-features-explained)
- [Important Notes](#️-important-notes)
- [Contributing](#-contributing)
- [License](#-license)

## 🚀 Features

### For Individuals (Developers/Freelancers)
- **User Registration & Authentication**: Secure account creation with email verification via OTP
- **Profile Management**: Create and manage professional profiles with expertise areas, bio, and resume uploads
- **Contract Discovery**: Browse and search available contracts posted by organizations
- **Application System**: Apply to contracts with custom pay requests, skill level ratings, and personalized messages
- **Token Economy**: Use tokens to apply for contracts (10 tokens per application)
- **Payment Tracking**: View payment history, earnings, and ongoing contracts
- **Dashboard**: Monitor completed contracts, total earnings, and token balance
- **Real-time Chat**: Communicate with organizations through integrated chat functionality
- **Contract History**: Track all past and current contracts with detailed information
- **Wallet System**: Manage earnings and top up wallet balance
- **Token Purchase**: Buy token packages (10, 55, or 120 tokens)

### For Organizations
- **Organization Registration**: Register company accounts with industry classification
- **Contract Creation**: Post detailed contracts with:
  - Title, description, and scope of work
  - Price range (min/max)
  - Duration options (15 days to 3 months)
  - Difficulty levels (Beginner to Master)
  - Technology stack requirements
  - Deliverables and additional notes
  - Contract images
- **Applicant Management**: Review applications, view resumes, and accept/reject applicants
- **Payment Management**: Track payments made to contractors
- **Contract History**: View all posted contracts with status tracking
- **Dashboard**: Monitor ongoing and completed contracts, token balance
- **Wallet System**: Top up wallet for contractor payments
- **Real-time Chat**: Communicate with contractors

### Security & Authentication
- **Email Verification**: OTP-based email verification system
- **Password Reset**: Secure password reset with email verification
- **Session Management**: Automatic session cleanup for unverified accounts
- **reCAPTCHA Integration**: Bot protection for organization registration
- **Phone Number Validation**: E.164 format validation for phone numbers
- **Password Strength Requirements**: Enforced strong password policies

## 🛠️ Technologies Used

### Backend
- **Flask**: Python web framework
- **Firebase Admin SDK**: Authentication and Realtime Database
- **Pyrebase4**: Firebase client library for authentication
- **Flask-SocketIO**: Real-time bidirectional communication
- **Flask-WTF**: Form handling and CSRF protection
- **Flask-Recaptcha**: reCAPTCHA integration
- **SQLite3**: Local chat history storage

### Frontend
- **HTML/CSS**: Frontend structure and styling
- **JavaScript**: Client-side interactivity
- **Jinja2**: Template engine

### Database
- **Firebase Realtime Database**: Primary database for user accounts, contracts, and application data
- **SQLite3**: Local database for chat message history

### Additional Libraries
- **email-validator**: Email validation
- **phonenumbers**: Phone number parsing and validation
- **APScheduler**: Task scheduling
- **requests**: HTTP library

## 📁 Project Structure

```
DevVillage/
│
├── app.py                      # Main Flask application entry point
├── database.py                 # SQLite database initialization and chat functions
├── requirements.txt            # Python dependencies
│
├── auth_routes.py             # Authentication routes (login, register, logout)
├── auth_forms.py              # Authentication form definitions
│
├── dashboard_routes.py        # Dashboard routes for individuals and organizations
│
├── discover_routes.py         # Contract discovery and creation routes
├── discover_forms.py          # Contract-related form definitions
│
├── acc_info_routes.py        # Account information and settings routes
├── acc_info_forms.py         # Account settings form definitions
│
├── verify_routes.py           # Email verification and password reset routes
│
├── static/                    # Static files
│   ├── css/                   # Stylesheets for all pages
│   ├── js/                    # JavaScript files for interactivity
│   ├── icons/                 # SVG icons
│   └── images/                # Image assets
│
└── templates/                 # HTML templates
    ├── home.html              # Landing page
    ├── user_login.html        # Individual login page
    ├── user_register.html       # Individual registration page
    ├── org_login.html         # Organization login page
    ├── org_register.html      # Organization registration page
    ├── dashboard.html         # Dashboard for both user types
    ├── indidiscover.html      # Contract discovery for individuals
    ├── org_discover.html      # Talent discovery for organizations
    ├── create_contract.html   # Contract creation form
    ├── contract.html          # Individual contract view and application
    ├── chat.html              # Real-time chat interface
    ├── payments.html          # Payment history
    ├── wallet.html            # Wallet top-up page
    ├── buy_tokens.html        # Token purchase page
    ├── profile pages          # Profile and settings pages
    └── ...
```

## 🔧 Installation

### Prerequisites
- Python 3.7 or higher
- Firebase project with Realtime Database enabled
- Firebase service account credentials JSON file
- reCAPTCHA v2 keys (for organization registration)

### Step 1: Clone the Repository
```bash
git clone https://github.com/yourusername/DevVillage.git
cd DevVillage
```

### Step 2: Create Virtual Environment
```bash
python -m venv venv

# On Windows
venv\Scripts\activate

# On macOS/Linux
source venv/bin/activate
```

### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 4: Firebase Configuration
1. Create a Firebase project at [Firebase Console](https://console.firebase.google.com/)
2. Enable Authentication (Email/Password)
3. Create a Realtime Database
4. Generate a service account key:
   - Go to Project Settings → Service Accounts
   - Click "Generate New Private Key"
   - Save the JSON file as `codebase-secret.json` in the project root
5. Update Firebase configuration in `app.py` and `auth_routes.py` with your project credentials

### Step 5: Environment Configuration
Update the following in `app.py`:
- Firebase database URL
- Service account credentials path
- Secret key for Flask sessions
- reCAPTCHA public and private keys

### Step 6: Run the Application
```bash
python app.py
```

The application will be available at `http://localhost:5000`

## ⚙️ Configuration

### Firebase Setup
The application uses Firebase for:
- **Authentication**: User registration and login
- **Realtime Database**: User accounts, contracts, applications, notifications
- **Storage**: Resume and contract image uploads

### Database Structure
```
Firebase Realtime Database:
├── user_accounts/
│   └── {username}/
│       ├── Email
│       ├── Expertise (array)
│       ├── First_name
│       ├── Last_name
│       ├── Wallet
│       ├── Tokens
│       ├── Bio
│       ├── DOB
│       ├── Gender
│       ├── Rating
│       ├── Resume (URL)
│       └── Notifications
│
├── org_accounts/
│   └── {uid}/
│       ├── Org name
│       ├── Email
│       ├── Org Website
│       ├── Contact Person Email
│       ├── Industry (array)
│       ├── Description
│       ├── Tokens
│       ├── Wallet
│       └── Notifications
│
├── contracts/
│   └── {contract_id}/
│       ├── Title
│       ├── Description
│       ├── Min Price
│       ├── Max Price
│       ├── Duration
│       ├── Difficulty
│       ├── Contract Image (URL)
│       ├── Scope (array)
│       ├── Deliverables (array)
│       ├── Technology Stack (array)
│       ├── Payment Terms (array)
│       ├── Notes (array)
│       ├── Status
│       ├── Company Name
│       ├── Author (org uid)
│       ├── Date Posted
│       ├── Applied/
│       │   └── {user_id}/
│       │       ├── Pay Requested
│       │       ├── Skill Level
│       │       ├── Message
│       │       └── Resume (URL)
│       └── Contractors/
│           └── {user_id}/
│               ├── Contractor Name
│               └── Pay
│
└── otp/
    └── {user_id}/ (OTP code, expires after 5 minutes)
```

### reCAPTCHA Configuration
1. Register at [Google reCAPTCHA](https://www.google.com/recaptcha/admin)
2. Add your domain
3. Copy public and private keys
4. Update in `app.py`:
   ```python
   app.config['RECAPTCHA_PUBLIC_KEY'] = 'your_public_key'
   app.config['RECAPTCHA_PRIVATE_KEY'] = 'your_private_key'
   ```

### Email Configuration (OTP System)
The application uses Gmail SMTP for sending OTP codes. Update email credentials in `auth_routes.py`:
```python
sender = 'your_email@gmail.com'
smtp.login(sender, 'your_app_password')
```

## 📖 Usage

### For Individuals

1. **Registration**
   - Navigate to `/user_register`
   - Fill in personal details, expertise areas, and create account
   - Verify email with OTP sent to your email
   - Login at `/user_login`

2. **Browse Contracts**
   - Visit `/discover/individual` to see available contracts
   - Filter and search contracts
   - Click on a contract to view details

3. **Apply to Contracts**
   - View contract details at `/contract/<contract_id>`
   - Upload resume (first time only, then it's saved)
   - Set your pay request within the allowed range
   - Rate your skill level
   - Submit application (costs 10 tokens)

4. **Manage Account**
   - Dashboard: `/individual/dashboard`
   - Profile: `/acc_info/profile/individual`
   - Settings: `/acc_info/acc_settings/individual`
   - Contract History: `/acc_info/contract_history/individual`
   - Payments: `/individual/payments`
   - Wallet: `/wallet/individual`
   - Buy Tokens: `/tokens/individual`

### For Organizations

1. **Registration**
   - Navigate to `/org_register`
   - Fill in organization details and industry
   - Complete reCAPTCHA verification
   - Verify email with OTP
   - Login at `/org_login`

2. **Create Contracts**
   - Visit `/org/create_contract`
   - Fill in contract details:
     - Title and description
     - Price range
     - Duration
     - Difficulty level
     - Scope of work
     - Deliverables
     - Technology stack
     - Optional contract image
   - Publish contract

3. **Manage Applications**
   - View dashboard at `/org/dashboard`
   - Review applicant list
   - Accept or reject applicants
   - Accepted applicants become contractors
   - Rejected applicants receive token refunds

4. **Manage Account**
   - Dashboard: `/org/dashboard`
   - Settings: `/acc_info/acc_settings/org`
   - Contract History: `/acc_info/contract_history/org`
   - Payments: `/organization/payments`
   - Wallet: `/wallet/organization`
   - Buy Tokens: `/tokens/organization`

## 🔑 Key Features Explained

### Token System
- New users receive 10 free tokens upon registration
- Applying to contracts costs 10 tokens
- Tokens can be purchased in packages:
  - $3 → 10 tokens
  - $7 → 55 tokens
  - $12 → 120 tokens
- Rejected applicants receive 10 tokens refunded

### Payment System
- Organizations maintain a wallet balance
- Payments are calculated based on contract duration and agreed pay
- Payments are made every 15 days during contract duration
- Individual wallets track earnings from completed contracts

### Application Workflow
1. Organization posts contract
2. Individual browses and applies (spends 10 tokens)
3. Organization reviews applications and resumes
4. Organization accepts or rejects:
   - **Accept**: Individual becomes contractor, tokens deducted
   - **Reject**: Individual receives 10 token refund, notification sent

### Email Verification
- OTP codes are generated and sent via email
- OTP expires after 5 minutes
- Unverified accounts are automatically deleted after OTP expiration
- Email verification required before accessing platform features

## 🚧 Important Notes

### Security Considerations
- **⚠️ Remove sensitive data before deploying**: The codebase contains hardcoded credentials (Firebase config, reCAPTCHA keys, email passwords). These should be moved to environment variables or a secure configuration file.
- Update `app.config['SECRET_KEY']` with a strong, randomly generated key
- Never commit `codebase-secret.json` to version control
- Use environment variables for all sensitive configuration

### Current Limitations
- Chat functionality uses SQLite for local storage (consider migrating to Firebase)
- Some mock data is still present in dashboard routes
- Payment processing is simulated (integrate real payment gateway for production)
- File uploads are stored in Firebase Storage (ensure proper security rules)

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

## 📝 License

This project is open source and available under the [MIT License](LICENSE).

## 👤 Author

**Taha Zakir**

## 🙏 Acknowledgments

- Firebase for backend services
- Flask community for excellent documentation
- All contributors and testers

---

**Note**: This is a development project. Ensure all security measures are properly implemented before deploying to production.

