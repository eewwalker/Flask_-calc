# Put your app in here.
from flask import Flask, request
from operations import add, sub, mult, div

app = Flask(__name__)


@app.get('/<operation>')
def calc_operations(operation):
    a_value = int(request.args['a'])
    b_value = int(request.args['b'])

    match operation:
        case 'add':
            return str(add(a_value, b_value))
        case 'sub':
            return str(sub(a_value, b_value))
        case 'mult':
            return str(mult(a_value, b_value))
        case 'div':
            return str(div(a_value, b_value))


