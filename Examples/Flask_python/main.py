from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello world'



@app.route('/name/<name>/id/<number>/')
def func_name(name,number):
    number_user = int(number) * 100
    return f'<h1>Hello</h1>, <p><b>{name}</b> - <i>{number_user}<i></p>'

@app.route('/temp/')
def temp():
    return render_template('index.html')

if __name__ == '__main__':
    app.run()

