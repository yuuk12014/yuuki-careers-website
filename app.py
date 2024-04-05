from flask import Flask, jsonify, render_template, jsonify, request

app = Flask(__name__)

CONTACTS = [{
  'id': 1,
  'FName': 'John',
  'LName': 'Co',
  'Emailaddress': 'johndoe@gmail.com',
  'Address': '123 Main St, Anytown, USA'
},
{
  'id': 2,
  'FName': 'Jim',
  'LName': 'King',
  'Emailaddress': 'johndoe@gmail.com',
  'Address': '123 Main St, Anytown, USA'
},
{
  'id': 3,
  'FName': 'Jazz',
  'LName': 'Doe',
  'Emailaddress': 'johndoe@gmail.com',
  'Address': '123 Main St, Anytown, USA'
},
{
  'id': 4,
  'FName': 'John',
  'LName': 'Doe',
  'Emailaddress': 'johndoe@gmail.com',
  'Address': '123 Main St, Anytown, USA'
            }
]

@app.route('/')
def homepage():
  return render_template('index.html',
    contacts = CONTACTS)

@app.route('/contacts')
def contacts():
  return jsonify(CONTACTS)
  
if __name__ == '__main__':
  app.run(host='0.0.0.0', port=8080)