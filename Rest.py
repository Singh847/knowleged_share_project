import random

class Customer:
    def __init__(self, name, age, sex, contact):
        self.name = name
        self.age = age
        self.sex = sex
        self.contact = contact
        self.order_history = []

    def add_order(self, order):
        self.order_history.append(order)

    def show_history(self):
        if not self.order_history:
            print("No orders recorded yet.")
        else:
            print(f"Order History for {self.name}:")
            for order in self.order_history:
                print(order)


class Dish:
    def __init__(self, name, price, category):
        self.name = name
        self.price = price
        self.category = category

    def __str__(self):
        return f"{self.name} - {self.category} - ${self.price}"


class Menu:
    def __init__(self):
        self.dishes = []

    def add_dish(self, name, price, category):
        self.dishes.append(Dish(name, price, category))

    def show_menu(self):
        if not self.dishes:
            print("No dishes available.")
        else:
            print("Restaurant Menu:")
            for dish in self.dishes:
                print(dish)


class Payment:
    def __init__(self, amount):
        self.amount = amount

    def process_payment(self):
        print(f"Processing payment of ${self.amount}...")
        payment_status = random.choice(["Success", "Failure"])
        if payment_status == "Success":
            print(f"Payment of ${self.amount} successful!")
            return True
        else:
            print(f"Payment failed! Please try again.")
            return False


class DishCustomization:
    def __init__(self):
        self.customizations = []

    def add_customization(self, customization):
        self.customizations.append(customization)

    def show_customizations(self):
        if not self.customizations:
            return "No customizations."
        else:
            custom_str = "Customizations: " + ", ".join(self.customizations)
            return custom_str


class Feedback:
    def __init__(self):
        self.feedbacks = []

    def add_feedback(self, dish_name, rating, comment):
        self.feedbacks.append({"dish": dish_name, "rating": rating, "comment": comment})

    def show_feedback(self):
        if not self.feedbacks:
            print("No feedback available.")
        else:
            print("User Feedbacks:")
            for feedback in self.feedbacks:
                print(f"{feedback['dish']} - Rating: {feedback['rating']}/5 - Comment: {feedback['comment']}")


class RestaurantApp:
    def __init__(self):
        self.customer = None
        self.menu = Menu()
        self.populate_menu()
        self.feedback_system = Feedback()

    def register_customer(self):
        name = input("Enter your name: ")
        age = int(input("Enter your age: "))
        sex = input("Enter your gender (M/F): ")
        contact = input("Enter your contact number: ")
        self.customer = Customer(name, age, sex, contact)
        print(f"Welcome, {self.customer.name}! Enjoy your dining experience.\n")

    def populate_menu(self):
        # Add some default dishes to the menu
        self.menu.add_dish("Pizza", 12.99, "Main Course")
        self.menu.add_dish("Pasta", 10.99, "Main Course")
        self.menu.add_dish("Caesar Salad", 7.99, "Salad")
        self.menu.add_dish("Burger", 9.99, "Main Course")
        self.menu.add_dish("Cheesecake", 5.99, "Dessert")
        self.menu.add_dish("Ice Cream", 3.99, "Dessert")

    def generate_random_order(self):
        # Randomly select a dish from the menu
        chosen_dish = random.choice(self.menu.dishes)
        print(f"AI suggests: {chosen_dish.name} - ${chosen_dish.price}")
        self.customer.add_order(f"{chosen_dish.name} - ${chosen_dish.price}")

    def place_order(self):
        if not self.menu.dishes:
            print("No menu items available.")
            return

        print("Restaurant Menu:")
        self.menu.show_menu()

        dish_name = input("Enter the dish you want to order: ")
        selected_dish = None
        for dish in self.menu.dishes:
            if dish_name.lower() == dish.name.lower():
                selected_dish = dish
                break

        if selected_dish:
            print(f"You have ordered: {selected_dish.name} - ${selected_dish.price}")
            
            # Dish customization
            customization = input("Would you like to customize this dish? (yes/no): ")
            dish_customization = DishCustomization()
            if customization.lower() == "yes":
                while True:
                    customization_option = input("Enter customization (e.g., Extra Cheese, Extra Spicy) or 'done' to finish: ")
                    if customization_option.lower() == 'done':
                        break
                    else:
                        dish_customization.add_customization(customization_option)

            customizations = dish_customization.show_customizations()
            self.customer.add_order(f"{selected_dish.name} - ${selected_dish.price} ({customizations})")
            
            # Collect feedback after order
            rating = int(input(f"Rate your experience with {selected_dish.name} (1-5): "))
            comment = input(f"Leave a comment for {selected_dish.name}: ")
            self.feedback_system.add_feedback(selected_dish.name, rating, comment)

        else:
            print("Dish not found on the menu.")

    def process_payment(self):
        if self.customer:
            total_amount = sum([float(order.split('- $')[1].split()[0]) for order in self.customer.order_history])
            print(f"Total amount: ${total_amount}")
            payment = Payment(total_amount)
            payment_successful = payment.process_payment()
            if payment_successful:
                print("Order completed successfully!")
            else:
                print("Order failed due to payment issue.")
        else:
            print("No customer found. Please register first.")

    def show_feedback(self):
        self.feedback_system.show_feedback()

    def menu(self):
        while True:
            print("\n🍽️ Restaurant App 🍽️")
            print("1. Register Customer")
            print("2. Show Order History")
            print("3. Show Menu")
            print("4. Place an Order")
            print("5. Suggest a Random Dish")
            print("6. Process Payment")
            print("7. Show User Feedback")
            print("8. Exit")
            choice = input("Choose an option: ")

            if choice == "1":
                self.register_customer()
            elif choice == "2":
                if self.customer:
                    self.customer.show_history()
                else:
                    print("No customer found. Please register first.")
            elif choice == "3":
                self.menu.show_menu()
            elif choice == "4":
                if self.customer:
                    self.place_order()
                else:
                    print("No customer found. Please register first.")
            elif choice == "5":
                if self.customer:
                    self.generate_random_order()
                else:
                    print("No customer found. Please register first.")
            elif choice == "6":
                if self.customer:
                    self.process_payment()
                else:
                    print("No customer found. Please register first.")
            elif choice == "7":
                self.show_feedback()
            elif choice == "8":
                print("Exiting Restaurant App. Enjoy your meal!")
                break
            else:
                print("Invalid choice, please try again.")


if __name__ == "__main__":
    app = RestaurantApp()
    app.menu()
