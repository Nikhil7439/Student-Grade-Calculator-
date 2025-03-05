from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    marks = int(request.form['marks'])
    
    if marks >= 90:
        grade = "A+"
    elif marks >= 75:
        grade = "A"
    elif marks >= 50:
        grade = "B"
    elif marks >= 45:
        grade = "C"
    elif marks >= 40:
        grade = "D"
    elif marks >= 35:
        grade = "E"
    else:
        grade = "Fail"
    
    return render_template('result.html', marks=marks, grade=grade)

if __name__ == '__main__':
    app.run(debug=True)