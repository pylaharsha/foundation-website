from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('base.html', page='home')

@app.route('/about')
def about():
    return render_template('base.html', page='about')

@app.route('/programs')
def programs():
    return render_template('base.html', page='programs')

@app.route('/events')
def events():
    return render_template('base.html', page='events')

@app.route('/donate')
def donate():
    return render_template('base.html', page='donate')

@app.route('/volunteer')
def volunteer():
    return render_template('base.html', page='volunteer')

@app.route('/contact')
def contact():
    return render_template('base.html', page='contact')

if __name__ == '__main__':
    app.run(debug=True)
