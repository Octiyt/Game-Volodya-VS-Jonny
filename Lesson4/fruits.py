fruits = ["Яблука", "Банан", "апельсин", "Груша", "ківі"]

print("Список фруктів:")
i = 1
for fruit in fruits:
    print(f"{i}. {fruit}")
    i += 1

while True:
    try:
        indeh = int(input("Введіть номер фрукта: ")) - 1
        if 0 <= indeh < len(fruits):
            print(f"Ви вибрали: {fruits[indeh]}")
            break
        else:
            raise IndexError("Номер фрукта поза межами списку")
    except ValueError:
        print("Будь ласка, введіть число.")
    except IndexError as e:
        print(f"Помилка: {e}. Спробуйте ще раз.")
