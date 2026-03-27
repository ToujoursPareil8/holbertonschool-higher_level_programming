#!/usr/bin/python3
"""Task_04_db.py module"""
import json
import csv
import sqlite3
from flask import Flask, render_template, request

app = Flask(__name__)


def read_json_file():
    with open('products.json') as f:
        return json.load(f)

def read_csv_file():
    products = []
    with open('products.csv', newline='') as f:
        reader = csv.DictReader(f)
        for row in reader:
            row['id'] = int(row['id'])
            row['price'] = float(row['price'])
            products.append(row)
    return products

def read_sqlite_data():
    try:
        conn = sqlite3.connect('products.db')
        cursor = conn.cursor()
        cursor.execute("SELECT id, name, category, price FROM Products")
        rows = cursor.fetchall()
        conn.close()

        products = [{'id': row[0], 'name': row[1], 'category': row[2], 'price': row[3]} for row in rows]
        return products
    except sqlite3.Error as e:
        return None

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/items')
def items():
    with open('items.json') as f:
        data = json.load(f)
    items = data.get("items", [])
    return render_template('items.html', items=items)

@app.route('/products')
def products():
    source = request.args.get('source')
    product_id = request.args.get('id', type=int)

    if source == 'json':
        products_list = read_json_file()
    elif source == 'csv':
        products_list = read_csv_file()
    elif source == 'sql':
        products_list = read_sqlite_data()
        if products_list is None:
            return render_template('product_display.html', error="Database error occurred.")
    else:
        return render_template('product_display.html', error="Wrong source. Please use 'json', 'csv', or 'sql'.")

    if product_id is not None:
        products_list = [product for product in products_list if product['id'] == product_id]
        if not products_list:
            return render_template('product_display.html', error="Product not found.")

    return render_template('product_display.html', products=products_list)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
