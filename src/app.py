from flask import Flask, request, abort, jsonify, render_template
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/result',methods = ['POST', 'GET'])
def result():
   if request.method == 'POST':
      result = request.form
      return render_template("index.html",result = result)

@app.route('/test')
def test():
    payload = [{'Year': '2001', 'Month': '01'},
               {'Year': '2002', 'Month': '02'}]
    return render_template('index.html', payload = payload)

if __name__ == '__main__':
    app.run(debug=True, port=5001)