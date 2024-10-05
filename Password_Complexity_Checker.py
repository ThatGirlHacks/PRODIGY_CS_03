import re

while True:
    Password = input("Enter your Password (Enter q to quit):")
    if Password.lower() == 'q':
        break
    else:

        checks = {
            "uppercase": False,
            "lowercase": False,
            "length": False,
            "digit": False,
            "special_char": False,
        }

        Strength_score = 0
        if len(Password) >= 8:
            checks.update({"length": True})
            Strength_score += 1
        if re.search("[A-Z]", Password):
            checks.update({"uppercase": True})
            Strength_score += 1
        if re.search("[a-z]", Password):
            checks.update({"lowercase": True})
            Strength_score += 1
        if re.search("[0-9]", Password):
            checks.update({"digit": True})
            Strength_score += 1
        if re.search("[@#$%&]", Password):
            checks.update({"special_char": True})
            Strength_score += 1

        if Strength_score == 5:
            print("Strong Password!")
        elif 5 > Strength_score >= 3:
            print("Medium Strength: Your Password is not strong enough")
        else:
            print("Low Strength: Your password is weak")

        for key, value in checks.items():
            if value == False:
                if key == 'length':
                    print("Your password should be at least eight characters long")
                elif key == 'uppercase':
                    print("Your password should contain Uppercase Letters")
                elif key == 'lowercase':
                    print("Your password should contain Lowercase Letters")
                elif key == 'digit':
                    print("Your password should contain at least a number(0-9)")
                elif key == 'special_char':
                    print("Your password should contain at least one special character(@#$%&)")
