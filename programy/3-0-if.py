def check_math_skills():
    answer = input('How many is 2 + 2 ?\n>>> ')
    if answer == "4":
        return True
    else:
        return False


if __name__ == "__main__":
    print(check_math_skills())
