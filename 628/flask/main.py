import time


from flask import Flask
from flask import request,session, redirect, url_for, escape,send_from_directory,make_response

import pymysql
import json

app = Flask(__name__, static_url_path='')

# ?key=value&email=a@a.com


@app.route('/static/<path:path>')
def send_static(path):
    return send_from_directory('static', path)

@app.route("/process", methods=['GET','POST'])
def process():
    #request.args.get('action')
    print (request.form.get('email') )
    return 'email:'+ request.form.get('email')


@app.route("/", methods=['GET','POST'])
def data():
    return '''
    <form id="myform" action="/process" method="POST">
            Enter string<br>
            <input type="text" name="email" value="123"/>
            <br><br>
            <select name="choice">
                <option value="yes">yes</option>
                <option value="no">no</option>
                <option value="not sure">not sure</option>
            </select>
            <input type="submit" value="Submit"/>
        </form>'''


@app.route('/csv')
def download_csv():
    csv = 'a,b,c\n1,2,3\n'
    response = make_response(csv)
    cd = 'attachment; filename=mycsv.csv'
    response.headers['Content-Disposition'] = cd
    response.mimetype='text/csv'

    return response
@app.route('/date')
def pick_date():
    return '''
    <head>
    <link rel="stylesheet" href="static/jquery-ui.css">
      <link rel="stylesheet" href="static/style.css">
      <script src="static/jquery.js"></script>
      <script src="static/jquery-ui.min.js"></script>

       <link rel="stylesheet" href="static/jquery-ui-timepicker-addon.css">
      <script src="static/jquery-ui-timepicker-addon.js"></script>

      <script>
      $( function() {
        $( "#datepicker" ).datepicker();
        $('#datetimepicker').datetimepicker({
	timeFormat: "hh:mm tt"
});
      } );
      </script>
    </head>
    <body>
    <p>Date: <input type="text" id="datepicker"></p>
    <p>Datetime: <input type="text" id="datetimepicker"></p>
    </body>

    '''

if __name__ == "__main__":
    app.secret_key = '1234'
    app.run(debug=True)
