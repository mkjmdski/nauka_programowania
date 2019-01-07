def print_apples(apples):
    for apple in range(int(apples)):
        print(f"apple number: {apple} -> 🍏")


if __name__ == "__main__":
    print_apples(
        input('How many apples do you want?\n>>> '))
