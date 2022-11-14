from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)  
app.secret_key = "My secret key!"

@app.route('/')         
def index():
    if 'counter' not in session:
        session['counter'] = 0
        return render_template("index.html", counter = session)
    if 'visits' not in session:
        session['visits'] = 0
        return render_template("index.html", counter = session)
    session['counter'] += 1
    session['visits'] += 1
    return render_template("index.html", counter = session)

@app.route('/destroy_session')
def destroy():
    session.pop('counter')
    return redirect('/')

@app.route('/increment', methods = ['POST'])
def increment2():
    if 'counter' in session:
        session['counter'] +=2
    return redirect('/')

@app.route('/reset', methods=['POST'])
def reset():
    session['counter'] = 0
    return redirect('/')

@app.route('/addNum', methods = ['POST'])
def addNum():
    num = request.form['number']
    if 'counter' in session:
        session['counter'] += int(num, 10)
    return redirect('/')

if __name__=="__main__":   
    app.run(debug=True)    