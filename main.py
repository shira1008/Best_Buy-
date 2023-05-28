import products
import store


def start(store_object):
    while True:
        print("********")
        print("Store Menu")
        print("----------")
        print("""1. List all products in store
2. Show total amount in store
3. Make an order
4. Quit """)

        user_input = input("Hello! Choose a number (1-4): ")
        print("_____")
        if user_input == "1":
            store_products = store_object.get_all_products()
            for i in range(len(store_products)):
                print(f"{i + 1}. {store_products[i].show()}")
            print("_____")

        elif user_input == "2":
            total_amount = store_object.get_total_quantity()
            print(f"Total of {total_amount} items in the store")

        elif user_input == "3":

            list_of_products = []
            print("When you want to finish the order, enter 'done'.")
            while True:
                try:
                    product_name = input("Which product # do you want? ")

                    if product_name == "done":
                        break

                    product_amount = int(input("What amount do you want? "))

                    found_product = False  # to track if a matching product is found
                    for i, product in enumerate(store_object.get_all_products()):
                        if str(i + 1) == product_name:
                            if product_amount > product.quantity:
                                # handling the Ordering a quantity too large, and Ordering
                                # limited products with over the limit quantity
                                print("_____")
                                print(
                                    f"There are less than {product_amount} items in stock, the limit is {product.quantity} please try again.")
                                found_product = True  # for the error handling
                            else:
                                list_of_products.append((product, product_amount))
                                found_product = True  # product is found

                    if not found_product:
                        print("____")
                        print("Product not found :( ")
                        print("____")
                except ValueError:
                    print("Invalid input, try again")

            total_cost = store_object.order(list_of_products)
            print("____")
            print(f"Order cost: {total_cost} dollars.")
            print("____")

        elif user_input == "4":
            print("Bye! ")
            break

        else:
            print("Invalid input. Please choose a number between 1 and 4.")


def main():
    # setup initial stock of inventory
    # handling products that is created with invalid parameters
    try:
        product_list = [
            products.Product("MacBook Air M2", price=1450, quantity=100),
            products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
            products.Product("Google Pixel 7", price=500, quantity=250)

        ]
        best_buy = store.Store(product_list)

        start(best_buy)
    except Exception as er:
        print(f"There was a problem, {er}")


if __name__ == "__main__":
    main()
