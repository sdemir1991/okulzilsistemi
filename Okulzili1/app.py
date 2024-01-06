from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return render_template('login.html')


@app.route('/dashboard', methods=['GET'])
def dashboard():
   return render_template('dashboard.html')



@app.route('/saatler',methods=['GET'])
def saatler():
    return  render_template('saatler.html')

@app.route('/zil',methods=['GET'])
def zil():
    return  render_template('zil.html')
@app.route('/toren',methods=['GET'])
def toren():
    return  render_template('toren.html')

if __name__ == '__main__':
    app.run()
