# from flask import Flask, render_template, make_response, request, jsonify, redirect, url_for
# from flaskext.mysql import MySQL
# from pymysql.cursors import DictCursor
# from forms import ListingForm
#
# app = Flask(__name__)
# app.config.from_pyfile('config.py')
#
# mysql = MySQL(cursorclass=DictCursor)
#
# app.config['MYSQL_DATABASE_HOST'] = 'db'
# app.config['MYSQL_DATABASE_USER'] = 'root'
# app.config['MYSQL_DATABASE_PASSWORD'] = 'root'
# app.config['MYSQL_DATABASE_PORT'] = 3306
# app.config['MYSQL_DATABASE_DB'] = 'housingPrices'
# app.config['SECRET_KEY'] = 'secret'
# mysql.init_app(app)
#
#
# @app.route('/', methods=['GET'])
# def home():
#     if request.method != 'GET':
#         return make_response('Malformed request', 400)
#     return render_template('home.html', title="Welcome Home", description="Your Resource For House Listings")
#
#
# @app.route('/table', methods=['GET'])
# def table():
#     if request.method != 'GET':
#         return make_response('Malformed request', 400)
#     cursor = mysql.get_db().cursor()
#     cursor.execute('SELECT * FROM zillow')
#     result = cursor.fetchall()
#     headers = {"Content-Type:": "application/json"}
#     return make_response(jsonify(result), 200, headers)
#
#
# @app.route('/zillow/<zipcode>', methods=['GET', 'POST'])
# def find_zipcode(zipcode):
#     cursor = mysql.get_db().cursor()
#     cursor.execute('SELECT * FROM zillow WHERE zip = %s', zipcode)
#     result = cursor.fetchall()
#     return render_template('table.html', houses=result)
#
#
# @app.route('/add_listing', methods=['GET', 'POST'])
# def add_listing():
#     form = ListingForm()
#     if form.validate_on_submit():
#         return redirect(url_for('success'))
#     return render_template('add.html', form=form)
#
#
# if __name__ == '__main__':
#     app.run(host='0.0.0.0')
