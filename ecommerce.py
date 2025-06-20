# 🛒 Simple E-commerce System in Python (CLI)
# Intern Name: NITIN NATH GOSWAMI
# Intern ID: 217256425
# Internship Task for @indolike
# Different Emojis picked From @emojipedia.org

print("👋 WELCOME to the Fashion Store!")

# 🧥 Sample Products - Clothing & Fashion Only
products = {
    1: {"name": "T-SHIRT", "price": 499},
    2: {"name": "SNEAKERS", "price": 1499},
    3: {"name": "WATCH", "price": 999},
    4: {"name": "TRAVELLING BACKPACK", "price": 799},
    5: {"name": "DENIM JEANS", "price": 999},
    6: {"name": "HOODIES", "price": 1199},
    7: {"name": "SUNGLASSES/SHADES", "price": 699},
    8: {"name": "KURTA SET", "price": 1499}
}

cart = {}

# 📦 Show All Products
def show_products():
    print("\n--- 🛍️ AVAILABLE PRODUCTS ---")
    for pid, item in products.items():
        print(f"{pid}. {item['name']} - ₹{item['price']}")

# ➕ Add Product to Cart
def add_to_cart():
    show_products()
    try:
        pid = int(input("Enter Product ID to add to cart: "))
        quantity = int(input("Enter quantity: "))
        if pid in products:
            cart[pid] = cart.get(pid, 0) + quantity
            print(f"✅ {quantity} x {products[pid]['name']} added to cart.")
        else:
            print("❌ Invalid Product ID.")
    except ValueError:
        print("⚠️ Please enter valid numbers only.")

# 🧾 View Cart Summary
def view_cart():
    if not cart:
        print("🛒 Your cart is empty.")
        return
    print("\n--- 🧾 YOUR CART ---")
    total = 0
    for pid, qty in cart.items():
        name = products[pid]['name']
        price = products[pid]['price']
        subtotal = qty * price
        total += subtotal
        print(f"{name} (x{qty}) - ₹{subtotal}")
    print(f"🧮 Total Amount: ₹{total}")

# 💳 Checkout and Clear Cart
def checkout():
    if not cart:
        print("🛒 Nothing to checkout.")
        return
    view_cart()
    confirm = input("Proceed to checkout? (yes/no): ").lower()
    if confirm == "yes":
        print("💸 Payment Successful! Thank you for shopping with us 🥳")
        cart.clear()
    else:
        print("❌ Checkout cancelled.")

# 📋 Show Main Menu
def show_menu():
    print("\n--- 📦 MAIN MENU ---")
    print("1. View Products")
    print("2. Add to Cart")
    print("3. View Cart")
    print("4. Checkout")
    print("5. Exit")

# 🎯 Main Program Loop
while True:
    show_menu()
    choice = input("Choose an option (1-5): ").strip()

    if choice == '1':
        show_products()
    elif choice == '2':
        add_to_cart()
    elif choice == '3':
        view_cart()
    elif choice == '4':
        checkout()
    elif choice == '5':
        print("👋 Thank you for visiting the Fashion Store. See you again!")
        break
    else:
        print("❌ Invalid choice. Please try again.")
