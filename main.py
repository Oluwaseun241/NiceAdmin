from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def dashboard():
    return render_template('index.html')

@app.route('/profile')
def user_profile():
    return render_template('users-profile.html')

if __name__ == '__main__':
    app.run()