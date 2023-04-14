from flask import Flask, request, jsonify, render_template
import subprocess

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    # Get the values from the AJAX request
    num1 = request.form.get('num1')
    num2 = request.form.get('num2')

    # Call the do_calculation.py script using subprocess
    result = subprocess.check_output(['python', 'utils/do_calculation.py', num1, num2])

    # Convert the result to a string and return it as an AJAX response
    result_str = result.decode('utf-8').strip()
    response = {'result': result_str}
    return jsonify(response)

if __name__ == '__main__':
    app.run()

