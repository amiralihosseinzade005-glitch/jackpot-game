import random

while True:

    print("🎰 ماشین شانس 🎰")
    print("(1. Start    2. Exit)")

    x = input("انتخاب شما: ")

    if x == "1":
        print("به ماشین شانس خوش آمدید!")

        money = int(input("حساب خود را شارژ کنید: "))

        hazine = 10

        while money >= hazine:

            print("موجودی شما:", money)

            money = money - hazine

            print("هزینه بازی:", hazine)
            print("موجودی بعد از پرداخت:", money)

            namad = []

            namad.append("🍒")
            namad.append("🍋")
            namad.append("⭐")
            namad.append("💎")

            natije1 = random.choice(namad)
            natije2 = random.choice(namad)
            natije3 = random.choice(namad)

            print(natije1, "|", natije2, "|", natije3)

            if natije1 == natije2 and natije2 == natije3:
                money = money + 1000
                print("🎉 برنده شدید! 1000 دلار جایزه گرفتید!")
                print("موجودی شما:", money)

            else:
                print("😢 باختید!")

            again = input("دوباره بازی می‌کنید؟ (y/n): ")

            if again == "n":
                break

        print("موجودی شما برای بازی کافی نیست.")

    elif x == "2":
        print("Bye Bye")