# inventory-management-system-python
A console-based inventory management system with MySQL backend featuring product tracking, search, and stock alerts.

## Features
- Add/view/edit/delete products
- Search products by name
- Low stock alerts
- Simple text interface
  
## Setup
1. Create MySQL database:
   sql
   CREATE DATABASE my_db;
   USE my_db;
   CREATE TABLE inventory (
       product_ID INT PRIMARY KEY,
       product_Name VARCHAR(255),
       category VARCHAR(255),
       price DECIMAL(10,2),
       quantity INT
   );

## Requirements
- Python 3.x
- pymysql ('pip install pymysql')
- MySQL server

## Usage
Run mainprogram.py ,followed the menu prompts.


