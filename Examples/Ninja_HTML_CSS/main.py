from flask import Flask

app = Flask(__name__)

@app.route('/')
def say_hello():
    return 'Hello!'

@app.route('/buy/')
def say_by():
  return 'Buy!'

@app.route('/start/')
def say_start():
   return 'Start!'

@app.route('/stop/')
def say_stop():
   return 'Stop!'

if __name__ == '__main__':
    app.run()
