from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def dashboard():
    return render_template('index.html')

@app.route('/profile')
def user_profile():
    return render_template('users-profile.html')

@app.route('/contact')
def contact_form():
    return render_template('pages-contact.html')

@app.route('/faq')
def faq_page():
    return render_template('pages-faq.html')

if __name__ == '__main__':
    app.run()