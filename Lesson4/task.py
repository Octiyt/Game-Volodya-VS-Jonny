def test(prompt):
    while True:
        try:
            user_input = input(prompt)
            number = float(user_input)
            return number
        except ValueError:
            print(f"Непраивльное значение: {user_input}. Пожалуйста введите число.")
result = test("введить число: ")
print(f"Ви ввели число: {result}")