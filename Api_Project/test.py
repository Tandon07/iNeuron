from flask import Flask, request, jsonify

def test(a,b):
    return a+b

print(test(4,5))


app=Flask(__name__)  #creating objrct of Flask class

@app.route('/abc',methods=['Get','Post'])
def test1():
    if(request.method=='POST'):
        a=request.json['num1']       #Requesting a json data from the user
        b=request.json['num2']
        result=a+b
        return jsonify(str(result))


@app.route('/abc1/saur',methods=['Get','Post'])
def test2():
    a = request.json['num1']  # Requesting a json data from the user
    b = request.json['num2']
    result = a * b
    return jsonify(str(result))


if __name__=='__main__':
    app.run()


