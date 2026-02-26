# IS320-Grocery-Order-System

A command-line grocery store ordering application developed as the final project for IS 320 – Fundamentals of Application Programming. Built in Python by Julie Mai, Nouryani Saleh, Matthew Chan, and Victor Man.

**Features**

The system supports two user roles — customers and managers — each with their own login and menu. Customers can browse available products, submit orders, and view their personal order history. Managers can view all orders across customers, edit product prices, and reorder stock. Inventory updates automatically as orders are placed.

**How to Run**

Requires Python 3. Clone the repository and run python FinalProject.py from your terminal. No external libraries required.

**Demo Login Credentials**

Customer IDs: 1001 (password: cpass1) and 1002 (password: cpass2). Manager ID: 9001 (password: mpass1).

**Project Structure**

Built around two core dictionaries — products (pre-loaded inventory) and orders (populated at runtime). Key functions include submit_order(), display_products(), display_orders(), edit_prices(), reorder_stock(), login(), customer_menu(), and manager_menu().

**Course**

IS 320 – Fundamentals of Application Programming


