# shopping_cart.py

class Product:
    def __init__(self, product_id, name, price):
        self.product_id = product_id
        self.name = name
        self.price = price
        
    def __repr__(self):
        return f"Product({self.product_id}, {self.name}, {self.price})"


class Cart:
    def __init__(self):
        # Dictionary mapping product_id to a tuple (Product, quantity)
        self.items = {}
        
    def add_product(self, product, quantity=1):
        if quantity <= 0:
            raise ValueError("Quantity must be positive")
        if product.product_id in self.items:
            current_qty = self.items[product.product_id][1]
            self.items[product.product_id] = (product, current_qty + quantity)
        else:
            self.items[product.product_id] = (product, quantity)
            
    def remove_product(self, product, quantity=1):
        if product.product_id not in self.items:
            raise ValueError("Product not in cart")
        if quantity <= 0:
            raise ValueError("Quantity must be positive")
        current_qty = self.items[product.product_id][1]
        if quantity >= current_qty:
            del self.items[product.product_id]
        else:
            self.items[product.product_id] = (product, current_qty - quantity)
            
    def calculate_total(self):
        total = 0.0
        for product, quantity in self.items.values():
            total += product.price * quantity
        return total
        
    def apply_discount(self, discount_rate):
        if discount_rate < 0 or discount_rate > 100:
            raise ValueError("Discount rate must be between 0 and 100")
        total = self.calculate_total()
        discount_amount = total * (discount_rate / 100.0)
        return total - discount_amount


class Order:
    def __init__(self, cart, customer_name):
        self.cart = cart
        self.customer_name = customer_name
        self.total_amount = cart.calculate_total()
        self.status = "Pending"
        
    def process_order(self):
        if self.total_amount <= 0:
            raise ValueError("Cannot process order with zero total")
        self.status = "Processed"
        return True


class Inventory:
    def __init__(self):
        # Dictionary mapping product_id to available quantity
        self.stock = {}
        
    def add_stock(self, product, quantity):
        if quantity <= 0:
            raise ValueError("Quantity must be positive")
        if product.product_id in self.stock:
            self.stock[product.product_id] += quantity
        else:
            self.stock[product.product_id] = quantity
            
    def remove_stock(self, product, quantity):
        if product.product_id not in self.stock or self.stock[product.product_id] < quantity:
            raise ValueError("Insufficient stock")
        self.stock[product.product_id] -= quantity
        
    def check_stock(self, product):
        return self.stock.get(product.product_id, 0)


class Coupon:
    def __init__(self, code, discount_rate):
        if discount_rate < 0 or discount_rate > 100:
            raise ValueError("Invalid discount rate")
        self.code = code
        self.discount_rate = discount_rate
        
    def apply_coupon(self, cart):
        return cart.apply_discount(self.discount_rate)


# Test Cases
import unittest

class TestAShoppingCart(unittest.TestCase):
    def setUp(self):
        self.product1 = Product(1, "Widget", 10.0)
        self.product2 = Product(2, "Gadget", 20.0)
        self.cart = Cart()
        self.inventory = Inventory()
        self.inventory.add_stock(self.product1, 100)
        self.inventory.add_stock(self.product2, 50)

    def test_order_inventory_A(self):
        # Add products to cart and update inventory accordingly
        self.cart.add_product(self.product1, 2)
        self.cart.add_product(self.product2, 1)
        # Verify inventory before processing the order
        self.assertEqual(self.inventory.check_stock(self.product1), 100)
        self.assertEqual(self.inventory.check_stock(self.product2), 50)
        # Deduct inventory to simulate order placement
        self.inventory.remove_stock(self.product1, 2)
        self.inventory.remove_stock(self.product2, 1)

        # Create and process order
        order = Order(self.cart, "Alice")
        self.assertTrue(order.process_order())
        self.assertEqual(order.status, "Processed")
        self.assertEqual(self.inventory.check_stock(self.product1), 98)
        self.assertEqual(self.inventory.check_stock(self.product2), 49)
        
    def test_coupon_(self):
        self.cart.add_product(self.product1, 5)  # Total should be 50.0
        coupon = Coupon("SAVE20", 20)  # 20% discount
        discounted_total = coupon.apply_coupon(self.cart)
        self.assertAlmostEqual(discounted_total, 50.0 * 0.8)


class TestShoppingCart(unittest.TestCase):
    def test_full_order_flow(self):
        # Step 1: Initialize inventory and products
        inventory = Inventory()
        product1 = Product(1, "Widget", 15.0)
        product2 = Product(2, "Gadget", 25.0)
        inventory.add_stock(product1, 10)
        inventory.add_stock(product2, 5)
        
        # Step 2: User adds products to the cart
        cart = Cart()
        cart.add_product(product1, 3)  # Cost: 3 * 15.0 = 45.0
        cart.add_product(product2, 2)  # Cost: 2 * 25.0 = 50.0; Total = 95.0
        
        # Step 3: Apply a coupon for a 10% discount
        coupon = Coupon("DISCOUNT10", 10)
        total_after_discount = coupon.apply_coupon(cart)
        self.assertAlmostEqual(total_after_discount, 95 * 0.9)
        
        # Step 4: Update inventory based on purchased items
        inventory.remove_stock(product1, 3)
        inventory.remove_stock(product2, 2)
        self.assertEqual(inventory.check_stock(product1), 7)
        self.assertEqual(inventory.check_stock(product2), 3)
        
        # Step 5: Create and process the order
        order = Order(cart, "Bob")
        self.assertTrue(order.process_order())
        self.assertEqual(order.status, "Processed")
        self.assertAlmostEqual(order.total_amount, 95)


if __name__ == '__main__':
    unittest.main()