import random


def main():
    secret_password = str(random.randrange(0, 9999))

    for guess in range(0, 9999):
        print("Attempted:", guess)
        if str(guess) == secret_password:
            print(f"Found password: {guess}, took {guess + 1} tries")  # guess + 1 are the number of tries taken
            break


if __name__ == "__main__":
    main()
