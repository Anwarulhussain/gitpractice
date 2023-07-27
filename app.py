### create a simple flask application
from flask import Flask
### create a flask app
app=Flask(__name__)
@app.route('/')
def home():
    return "Hello world"

@app.route('/success/<int:score>')
def success(score):
    return "the score is"+str(score)

if __name__=='__main__':
  app.run()



