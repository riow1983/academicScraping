from flask import Flask, render_template
import os
import logging

app = Flask(__name__)

#log = logging.getLogger('werkzeug')
#log.setLevel(logging.ERROR)



@app.route("/")
def hello():
    return render_template('index.html')
  

if __name__ == '__main__':
    #app.run(host=os.environ["CDSW_IP_ADDRESS"],port=int(os.environ["CDSW_PUBLIC_PORT"]))
    app.run(host='0.0.0.0', debug=True)