fruits = ["Яблука", "Банан", "апельсин", "Груша", "ківі"]

print("Список фруктовв: ")
i = 1
for fruit in fruits:
    print(f"{i}. {fruit}")
    i += 1

while True:
    try:
        indeh = int(input("введи номер фрукта: ")) - 1
        if 0 <= indeh < len(fruits):
            print(f"Ви выбрали: {fruits[indeh]}")
            break
        else:
            print("Неправильний номер попробуй ще раз")
    except ValueError:
        print("пожалуйста введи число")
