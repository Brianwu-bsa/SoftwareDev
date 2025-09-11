def main():
    phone_book = {
        "Alice": "416-555-1234",
        "Bob": "647-555-5678",
        "Charlie": "905-555-2468",
        "Diana": "289-555-1357",
        "Ethan": "613-555-9876"
    }

    key = input("Person's name or 'q' for quit:").strip()
    if key.lower() == "q":
        print("Exiting...")
        return
    value = phone_book.get(key, None)  # default to None if not found

    if value is not None:
        print(value)
    else:
        print("The person doesn't exist in the phone book")


if __name__ == "__main__":
    main()
