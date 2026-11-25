import fa_console
while True:
    print("\n===  کتابخانه مدرسه ===")
    print("1. ثبت کتاب جدید")
    print("2. دیدن همه کتاب‌ها")
    print("3. خروج")

    entekhab = input("چی می‌خوای انجام بدی؟ (1/2/3): ")

    # --- ثبت کتاب جدید ---
    if entekhab == "1":
        name_ketab = input("اسم کتاب: ")
        nevisande = input("نویسنده: ")

        with open("ketabkhane.txt", "a", encoding="utf-8") as file:
            file.write(f"کتاب: {name_ketab} | نویسنده: {nevisande}\n")

        print(" ثبت شد!")

    # --- نمایش کتاب‌ها ---
    elif entekhab == "2":
        print("\n لیست کتاب‌ها:")
        try:
            with open("ketabkhane.txt", "r", encoding="utf-8") as file:
                shomare = 1
                for line in file:
                    print(f"{shomare}. {line.strip()}")
                    shomare += 1
        except FileNotFoundError:
            print(" هنوز هیچ کتابی ثبت نشده!")

    # --- خروج ---
    elif entekhab == "3":
        print("خداحافظ!")
        break

    else:
        print(" گزینه اشتباه! دوباره امتحان کن.")