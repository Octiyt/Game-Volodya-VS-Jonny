def task(prompt, min_value=None, max_value=None):


    while True:

        try:
            user_input = input(prompt)
            number = float(user_input)
            if min_value is not None and number < min_value:
                print(f"число должно быти не меньше {min_value}.")
                continue
            if max_value is not None and number > max_value:
                print(f"число должно быть не больше {max_value}.")
                continue
            return number

        except ValueError:
            print("Неверное значение ведите число")


result = task("Введіть число (від 0 до 100): ", min_value=0, max_value=100)
print(f"Ви вели число: {result}")
