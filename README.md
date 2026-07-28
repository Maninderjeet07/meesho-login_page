# meesho-login_page
> ⚠️ **Disclaimer**: This project is an educational phishing simulation and security awareness tool designed to demonstrate how credential harvesting attacks work and to help organizations test user awareness. It is not affiliated with Meesho or any of its affiliates.

## 🚀 Overview

This project is a high-fidelity login simulation built with Flask. It replicates the user interface and flow of Meesho's authentication system to demonstrate the mechanics of credential harvesting attacks targeting e-commerce platforms.

It features a **two-step authentication simulation**:

- **Step 1**: Captures user phone number (Mobile-first approach typical in Indian e-commerce).
- **Step 2**: Simulates a password entry gate with "Change" option to mimic real UX.

The primary goal of this project is to provide a safe, controlled environment for:

- Educating users on how phishing sites mimic legitimate Indian e-commerce services.
- Testing the effectiveness of security awareness training.
- Demonstrating the importance of URL verification and OTP-based authentication.
- Understanding mobile-first attack vectors.

## ⚠️ Important Security Warning

This project is for **educational and authorized testing purposes only**.

- 🛑 **Do not** use this project to maliciously steal credentials from individuals without their explicit consent.
- 🛑 **Do not** deploy this on a domain that infringes on trademarks (e.g., do not buy meesho-offers.com).
- ✅ **Do** use this to test your own security protocols or to educate others on phishing risks.
- ✅ **Do** ensure all participants are aware they are part of a security training exercise.

Misuse of this tool for unauthorized credential collection may violate local laws and regulations regarding data privacy, computer fraud, and telecommunications regulations.

## 🛡️ Features

- **High-Fidelity UI**: Replicates Meesho's visual style including the pink gradient banner, product showcases, and mobile-centric design.
- **Two-Step Flow**: Mimics the split authentication process (Phone first, Password second) used by Meesho and similar Indian e-commerce apps.
- **Session Management**: Uses secure Flask sessions to handle state between the two authentication steps.
- **Real-Time Logging**: Captures credentials with timestamps and IP addresses for analysis (visible in Render Logs or local console).
- **Responsive Design**: Fully responsive CSS that adapts to mobile and desktop views, matching Meesho's mobile-first approach.
- **Error Simulation**: Displays realistic "Session Expired" error before redirecting to the legitimate site.
- **CSS-Generated Assets**: Uses emoji and CSS gradients for product images (no external dependencies that could break).

## 📂 Project Structure
Meesho-Login-Phishing-Web-page/ ├── main.py # Main Flask application logic ├── requirements.txt # Python dependencies (Flask, Gunicorn) ├── README.md # This file ├── templates/ │ ├── index.html # Main login simulation (Phone/Password steps) │ └── error.html # Session expired error page with auto-redirect ├── static/ │ └── style.css # Meesho-themed CSS (pink/purple gradients) └── captured_data.txt # (Local only) Log file for captured credentials
Text

Unwrap

Copy

## 🛠️ Installation & Setup

### Prerequisites

- Python 3.8 or higher
- pip (Python package installer)
- A GitHub account (for hosting)
- (Optional) A Discord Webhook URL for real-time alerts

### 1. Clone the Repository

```bash
git clone <YOUR_REPOSITORY_URL>
cd Meesho-Login-Phishing-Web-page
```
2. Install Dependencies
```Bash

Copy
pip install -r requirements.txt
```
3. Configuration (Optional)
The application uses Flask's built-in session management. A random secret key is generated automatically, but for production deployments, set a fixed secret key via environment variable:
```Bash

Copy
# Linux/Mac
export SECRET_KEY="your-secret-key-here"

# Windows
set SECRET_KEY=your-secret-key-here
```
4. Run the Application
```Bash

Copy
python main.py
The application will start on http://127.0.0.1:8080.
```
🌐 Deployment
This project is optimized for deployment on cloud platforms for accessibility during authorized tests.
Render (Recommended)
Push code to GitHub
Connect repository to
Render
Use these settings:
Environment: Python 3
Build Command: pip install -r requirements.txt
Start Command: gunicorn main:app
Deploy and get your live URL
Note: On Render's free tier, file-based logging (captured_data.txt) is ephemeral. View captured credentials in the Logs tab where they are printed as:
Text

Unwrap

Copy
CAPTURED: Phone=9876543210 | Password=userpassword123
Replit
Create new Repl → Select Flask template
Upload files or import from GitHub
Click Run
Get live URL instantly
Local Testing
Running locally allows for file-based logging. Check the captured_data.txt file after testing:
Bash

Copy
cat captured_data.txt
🔒 Security & Privacy
Data Storage: Credentials are logged to console (visible in Render Logs) and optionally to captured_data.txt on local deployments. No database is used by default.
Session Safety: Uses Flask's secure session management with secret keys to prevent tampering.
Auto-Redirect: After capture, users are shown an error page and automatically redirected to the real Meesho website after 5 seconds.
No External Assets: Uses CSS-generated images and emojis to prevent broken image links.
🎓 Educational Use Cases
Security Awareness Training: Show employees how Indian e-commerce phishing attacks look different from Western counterparts (mobile-first, phone-based).
Red Team Exercises: Test if users verify URLs before entering phone numbers and passwords.
Mobile Security Training: Demonstrate how mobile-centric phishing pages exploit smaller screens and different UX patterns.
Cultural Context: Educate about region-specific phishing tactics targeting Indian users.
📝 How the Simulation Works
Landing Page: User sees Meesho-branded page with "Welcome to Meesho" or "Sign Up to view your profile"
Phone Entry: User enters Indian mobile number (+91 country code pre-selected)
Password Gate: System displays the entered phone number with "Change" option, asks for password
Data Capture: Both phone and password are logged with timestamp and IP
Error Display: Shows "Session Expired" or "Something went wrong" error
Redirect: Automatically redirects to https://www.meesho.com after 5 seconds
📜 License
This project is licensed under the MIT License. See the
LICENSE
file for details.
🤝 Contributing
Contributions are welcome! Please feel free to submit a Pull Request if you have improvements for:
Better security practices
Enhanced educational warnings
Additional regional e-commerce templates
Integration with alerting systems (Slack, Email, Discord)
📧 Contact
For questions regarding this project or security concerns, please open an issue on this repository.
Created for educational purposes. Always ensure you have explicit permission before testing phishing simulations on real users.
Stay Safe | Verify URLs | Enable 2FA
