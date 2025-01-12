import requests

url = "https://meowfacts.herokuapp.com/"

lang = input("введите язик (наприклад, 'ukr', 'eng'): ")
count = input("введіть кількість фактів: ")


if not lang or not count.isdigit():
    print("неправильно ввів ввод! вкажи правильно язик і кількість.")
else:
    response = requests.get(url=url, params={
        'lang': lang,
        'count': count
    })

    if response.ok:
        as_json = response.json()
        facts = as_json.get('data', [])
        if facts:
            print('Случайні факты:')
            for fact in facts:
                print(f'- {fact}')
        else:
            print("факті неправильно ввів")
    else:
        print(f"Status code: {response.status_code}")
