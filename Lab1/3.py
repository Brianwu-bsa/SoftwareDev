def main():
    basket = {"apple", "banana"}

    while True:
        print(f"Current Basket: {basket}")
        query = input("Options: (q)uit, (a)dd, (r)remove, (c)heck: ").strip().lower()
        if query == "q":
            print("Exiting...")
            break

        if query == "a":
            fruit = input("Enter a fruit to add: ").strip()
            if fruit:  # as in not an empty string ""
                basket.add(fruit)
                print(f"Added {fruit} to the basket!")
            else:
                print("No fruit entered!")

        elif query == "r":
            fruit = input("Enter a fruit to remove: ").strip()
            if fruit in basket:
                basket.remove(fruit)
                print(f"Removed {fruit} from basket")
            else:
                print(f"{fruit} not found in basket!")

        elif query == "c":
            fruit = input("Enter fruit to check: ").strip()
            if fruit in basket:
                print(f"Yes, {fruit} is in the basket!")
            else:
                print(f"No, {fruit} is NOT in the basket!")
        else:
            print("Invalid option please try again!")
        print("-"*20)

if __name__ == "__main__":
    main()
