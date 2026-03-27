#!/usr/bin/python3
"""Task_03_files.py module"""
import json
import csv
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
    else:
        return render_template('product_display.html', error="Wrong source. Please use 'json' or 'csv'.")

    if product_id is not None:
        products_list = [product for product in products_list if product['id'] == product_id]
        if not products_list:
            return render_template('product_display.html', error="Product not found.")

    return render_template('product_display.html', products=products_list)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
