from flask import Flask, render_template

app = Flask(__name__)

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

@app.route('/applications')
def applications():
    return render_template('applications.html')

@app.route('/tasks')
def tasks():
    return render_template('tasks.html')

@app.route('/prof_chang')
def prof_chang():
    return render_template('prof_chang.html')

if __name__ == '__main__':
    app.run(debug=True)
