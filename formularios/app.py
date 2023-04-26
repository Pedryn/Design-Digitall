from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/index', methods=['GET', 'POST'])
def digite_numero():

    if request.method == 'POST':
        a=float(request.form["a"])
        b=float(request.form["b"])
        c=float(request.form["c"])
    return str(((a*2)+(b-2)+(c+3)))
        
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)