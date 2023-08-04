from flask import Flask,request,render_template,jsonify
import json

app=Flask(__name__)

@app.route('/')
def welcome():
    return"welcome to the Flask"

@obj.route('/cal',methods=['GET'])
def math_op():
    operations=request.json["operation"]
    
    
    
    
    
    
    num1=request.json["operation1"]
    num2=request.json["operation2"]
    if operations=="add":
           result=num1+num2
    elif operations=="multiply":
        result=num1*num2
    elif operations=="division":
        result=num1/num2
    else:
        result=num1-num2
    return jsonify(result)
print(__name__)


if __name__=='__main__':

    app.run()