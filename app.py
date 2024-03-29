from flask import Flask, request, render_template

app = Flask(__name__)

class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            return 'Error! Division by zero.'
        else:
            return a / b

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    try:
        a = int(request.form['first_number'])
    except ValueError:
        try:
            a = float(request.form['first_number'])
        except ValueError:
            a = 0
    try:
        b = int(request.form['second_number'])
    except ValueError:
        try:
            b = float(request.form['second_number'])
        except ValueError:
            b = 0
    operation = request.form['operation']
    calculator = Calculator()
    if operation == 'add':
        result = calculator.add(a, b)
    elif operation == 'subtract':
        result = calculator.subtract(a, b)
    elif operation == 'multiply':
        result = calculator.multiply(a, b)
    elif operation == 'divide':
        result = calculator.divide(a, b)
    return render_template('index.html', result=result, first_number=a, second_number=b, operation=operation)
