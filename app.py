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
        return a / b

@app.route('/')
def index():
    return render_template('index.html')
