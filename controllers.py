from flask import render_template, request, jsonify
from app.models.products import Product
from app import db
from . import main

# Scan barcode and retrieve product details
@main.route('/scan', methods=['POST'])
def scan():
    data = request.get_json()
    barcode = data['barcode']

    product = Product.query.filter_by(barcode=barcode).first()

    if not product:
        return jsonify({'status': 'error', 'message': 'Product not found.'})

    return jsonify({'status': 'success', 'data': {'name': product.name, 'description': product.description, 'expiry_date': product.expiry_date}})

# Add product to database
@main.route('/add', methods=['POST'])
def add():
    data = request.get_json()
    barcode = data['barcode']
    name = data['name']
    description = data['description']
    expiry_date = data['expiry_date']

    product = Product(barcode=barcode, name=name, description=description, expiry_date=expiry_date)

    db.session.add(product)
    db.session.commit()

    return jsonify({'status': 'success', 'message': 'Product added successfully.'})

# Render home page template
@main.route('/')
def index():
    return render_template('index.html')

# Render product details template
@main.route('/product/<barcode>')
def product(barcode):
    product = Product.query.filter_by(barcode=barcode).first()

    if not product:
        return render_template('error.html', message='Product not found.')

    return render_template('product.html', product=product)
