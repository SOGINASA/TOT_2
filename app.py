from flask import Flask, render_template

@app.route('/')
def main():
    return render_template('main.html')

@app.route('/about')
def about():
    return render_template('about.html')    

@app.route('/profile')
def profile():
    return render_template('profile.html')

@app.route('/tabs')
def tabs():
    return render_template('tabs.html')