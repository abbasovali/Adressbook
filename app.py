from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def display_form():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit_form():
    name = request.form['name']
    surname = request.form['surname']
    phone = request.form['phone']
    email = request.form['email']
    address = request.form['address']

    # Store the form data in a dictionary or a list
    data = {
        'name': name,
        'surname': surname,
        'phone': phone,
        'email': email,
        'address': address
    }

    return render_template('display.html', data=data)

if __name__ == '__main__':
    app.run()

