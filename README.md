# IS 320 Grocery Order System

A command-line grocery store ordering application developed as the final project for IS 320 – Fundamentals of Application Programming. Built in Python by Julie Mai, Nouryani Saleh, Matthew Chan, and Victor Man.

## Features

The system supports two user roles — customers and managers — each with their own login and menu.

- **Customers** can browse available products, submit orders, and view their personal order history.
- **Managers** can view all orders across customers, edit product prices, and reorder stock.
- Inventory updates automatically as orders are placed.

## How to Run

Requires Python 3. Clone the repository and run the following command from your terminal:

```bash
python FinalProject.py
```

No external libraries required — only the Python standard library is used.

## Demo Login Credentials

| Role     | ID   | Password |
|----------|------|----------|
| Customer | 1001 | cpass1   |
| Customer | 1002 | cpass2   |
| Manager  | 9001 | mpass1   |

## Project Structure

Built around two core dictionaries:

- `products` — pre-loaded with inventory data including name, unit price, and stock quantity
- `orders` — populated at runtime as customers place orders

### Key Functions

| Function | Description |
|---|---|
| `login()` | Handles customer and manager authentication |
| `customer_menu()` | Drives the customer session loop |
| `manager_menu()` | Drives the manager session loop |
| `submit_order()` | Prompts product selection, validates stock, and records an order |
| `display_products()` | Displays available products; supports stock view for managers |
| `display_orders()` | Shows order history; filtered by customer or all orders for managers |
| `edit_prices()` | Allows managers to update a product's unit price |
| `reorder_stock()` | Allows managers to add stock to a product |
| `compute_price()` | Calculates total order price from unit price and quantity |
| `print_order()` | Prints a formatted order confirmation |
| `get_date()` | Generates a randomized order date for simulation purposes |

## Course

IS 320 – Fundamentals of Application Programming
