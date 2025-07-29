import sqlite3
from datetime import datetime

from flask import Flask, flash, redirect, render_template, request, url_for

app = Flask(__name__)
app.secret_key = 'your-secret-key-here'

# Khởi tạo database
def init_db():
    conn = sqlite3.connect('products.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            price REAL NOT NULL,
            description TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    conn.commit()
    conn.close()

# Helper function để lấy kết nối database
def get_db_connection():
    conn = sqlite3.connect('products.db')
    conn.row_factory = sqlite3.Row
    return conn

# Trang chủ - hiển thị danh sách sản phẩm
@app.route('/')
def index():
    conn = get_db_connection()
    products = conn.execute('SELECT * FROM products ORDER BY created_at DESC').fetchall()
    conn.close()
    return render_template('index.html', products=products)

# Thêm sản phẩm mới
@app.route('/add', methods=['GET', 'POST'])
def add_product():
    if request.method == 'POST':
        name = request.form['name']
        price = request.form['price']
        description = request.form['description']
        
        if name and price:
            conn = get_db_connection()
            conn.execute(
                'INSERT INTO products (name, price, description) VALUES (?, ?, ?)',
                (name, float(price), description)
            )
            conn.commit()
            conn.close()
            flash('Sản phẩm đã được thêm thành công!', 'success')
            return redirect(url_for('index'))
        else:
            flash('Vui lòng điền đầy đủ thông tin!', 'error')
    
    return render_template('add.html')

# Xem chi tiết sản phẩm
@app.route('/product/<int:id>')
def view_product(id):
    conn = get_db_connection()
    product = conn.execute('SELECT * FROM products WHERE id = ?', (id,)).fetchone()
    conn.close()
    
    if product is None:
        flash('Không tìm thấy sản phẩm!', 'error')
        return redirect(url_for('index'))
    
    return render_template('view.html', product=product)

# Sửa sản phẩm
@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_product(id):
    conn = get_db_connection()
    product = conn.execute('SELECT * FROM products WHERE id = ?', (id,)).fetchone()
    
    if product is None:
        conn.close()
        flash('Không tìm thấy sản phẩm!', 'error')
        return redirect(url_for('index'))
    
    if request.method == 'POST':
        name = request.form['name']
        price = request.form['price']
        description = request.form['description']
        
        if name and price:
            conn.execute(
                'UPDATE products SET name = ?, price = ?, description = ? WHERE id = ?',
                (name, float(price), description, id)
            )
            conn.commit()
            conn.close()
            flash('Sản phẩm đã được cập nhật!', 'success')
            return redirect(url_for('index'))
        else:
            flash('Vui lòng điền đầy đủ thông tin!', 'error')
    
    conn.close()
    return render_template('edit.html', product=product)

# Xóa sản phẩm
@app.route('/delete/<int:id>')
def delete_product(id):
    conn = get_db_connection()
    conn.execute('DELETE FROM products WHERE id = ?', (id,))
    conn.commit()
    conn.close()
    flash('Sản phẩm đã được xóa!', 'success')
    return redirect(url_for('index'))

if __name__ == '__main__':
    init_db()
    app.run(debug=True)