from typing import List, Dict
import mysql.connector
import simplejson as json
from flask import Flask, Response
from flask import render_template

app = Flask(__name__)


def cities_import() -> List[Dict]:
    config = {
        'user': 'root',
        'password': 'root',
        'host': 'db',
        'port': '3306',
        'database': 'citiesData'
    }
    connection = mysql.connector.connect(**config)
    cursor = connection.cursor(dictionary=True)

    cursor.execute('SELECT * FROM tblCitiesImport')
    result = cursor.fetchall()

    cursor.close()
    connection.close()

    return result


def cities_import2() -> List[Dict]:
    config = {
        'user': 'root',
        'password': 'root',
        'host': 'db',
        'port': '3306',
        'database': 'citiesData'
    }
    connection = mysql.connector.connect(**config)
    cursor = connection.cursor(dictionary=True)

    cursor.execute('SELECT * FROM tblCitiesImport WHERE fldPopulation > 10000000')
    result = cursor.fetchall()

    cursor.close()
    connection.close()

    return result





@app.route('/')
def index():
    user = {'username': 'Eric'}
    cities_data = cities_import()

    return render_template('index.html', title='Home', user=user, cities=cities_data)


@app.route('/api/cities')
def cities() -> str:
    js = json.dumps(cities_import())
    resp = Response(js, status=200, mimetype='application/json')
    return resp


@app.route('/LargeCities')
def tryPage():
    user = {'username': 'Eric'}
    LargeCities_data = cities_import2()

    return render_template('index.html', title='Home', user=user, cities=LargeCities_data)


if __name__ == '__main__':
    app.run(host='0.0.0.0')
