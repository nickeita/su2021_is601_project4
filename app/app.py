from flask import Flask, render_template, make_response, request, jsonify
from flaskext.mysql import MySQL
from pymysql.cursors import DictCursor

app = Flask(__name__)
mysql = MySQL(cursorclass=DictCursor)

app.config['MYSQL_DATABASE_HOST'] = 'db'
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'root'
app.config['MYSQL_DATABASE_PORT'] = 3306
app.config['MYSQL_DATABASE_DB'] = 'housingPrices'
mysql.init_app(app)


@app.route('/', methods=['GET'])
def home():
    if request.method != 'GET':
        return make_response('Malformed request', 400)
    return render_template('home.html', title="Welcome Home", description="Your Resource For House Listings")


@app.route('/table', methods=['GET'])
def table():
    if request.method != 'GET':
        return make_response('Malformed request', 400)
    cursor = mysql.get_db().cursor()
    cursor.execute('SELECT * FROM zillow')
    result = cursor.fetchall()
    headers = {"Content-Type:": "application/json"}
    return make_response(jsonify(result), 200, headers)


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
