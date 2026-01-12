"""
"""
"""
Конвертер валют
"""
import os
import requests
from dotenv import load_dotenv
import tkinter as tk
from tkinter import ttk, messagebox


# загружаем переменные из .env
load_dotenv()

# читаем API-ключ
API_KEY = os.getenv("API_KEY")

# проверяем, есть ли ключ
if not API_KEY:
    messagebox.showerror("Ошибка: API-ключ не найден. Проверьте файл .env")
    exit()

# Функция для получения списка валют
def get_currency_list():
    url = f"https://v6.exchangerate-api.com/v6/{API_KEY}/latest/USD"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()  # ответ на наш запрос в формате данных json (похоже на словарь)
        return list(data["conversion_rates"].keys())
    else:
        messagebox.showerror(title="Ошибка", message="Не удалось получить список валют")
        return []

# Функция для конвертации валют
def convert_currency():
    base_currency = base_currency_var.get()
    target_currency = target_currency_var.get()
    amount = amount_entry.get()

    # выбор валют происходит через выпадающие списки
    # ввод суммы через текстовое поле

    if not amount.isdigit():
        messagebox.showerror(title="Ошибка", message="Введите сумму корректно")
        return

    amount = float(amount)
    url = f"https://v6.exchangerate-api.com/v6/{API_KEY}/latest/{base_currency}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()

        if target_currency in data['conversion_rates']:
            rate = data['conversion_rates'][target_currency]
            converted_amount = amount * rate
            result_label.config(text=f"{amount} {base_currency} = {converted_amount:.2f} {target_currency}")
        else:
            messagebox.showerror(title="Ошибка", message="Целевая валюта не найдена")

    else:
        messagebox.showerror(title="Ошибка", message="Не удалось получить данные с API")


# Создаеем главное окно
root = tk.Tk()
root.title("Конвертер валют")
root.geometry("400x300")
root.resizable(width=False, height=False)
#root.config(bg="#E3D9F2")

# Получаем список валют
currencies = get_currency_list()

# Поля ввода
tk.Label(root, text="Сумма: ", bg="#B8B8B8").pack(pady=(15, 0))  # метка с надписью сумма, pack размещает элемент на экране
amount_entry = tk.Entry(root)   # поле для ввода суммы
amount_entry.pack(pady=(3, 0))

# создадим выпадающие списки
tk.Label(root, text="Исходная валюта: ", bg="#B8B8B8").pack(pady=(12, 3))
base_currency_var = tk.StringVar(value="USD")  # хранит выбранную валюту
base_currency_menu = ttk.Combobox(root, textvariable=base_currency_var, values=currencies)
base_currency_menu.pack()

tk.Label(root, text="Целевая валюта: ", bg="#B8B8B8").pack(pady=(12, 3))
target_currency_var = tk.StringVar(value="EUR")
target_currency_menu = ttk.Combobox(root, textvariable=target_currency_var, values=currencies)
target_currency_menu.pack()

# Кнопка для конвертации
convert_button = tk.Button(root, text="Конвертировать", command=convert_currency, bg="#66B2FF", activebackground="#939393")
convert_button.pack(pady=(10, 3))

# Поле для вывода результата
result_label = tk.Label(root, text="", font=("Arial", 12))
result_label.pack()

# Запуск главного цикла Tkinter
root.mainloop()

"""
Конвертер температур
"""
def convert_tempreture(base_temp, target_temp, num):
    # base_temp = base_temp_menu.get()
    # target_temp = target_temp_menu.get()
    # num = num_entry.get()

    # выбор температур происходит через выпадающие списки
    # ввод числа через текстовое пол

    if not num.isdigit():
        messagebox.showerror(title="Ошибка", message="Введите число корректно")
        return

    num = float(num)

    if base_temp == "Fahrenheit" and target_temp == "Fahrenheit":
        converted_num = num
        result_label2.config(text=f"{num} {base_temp} = {converted_num:.2f} {target_temp}")
        return converted_num

    elif (base_temp == "Fahrenheit") and (target_temp == "Celsius"):
        converted_num = (num - 32) * (5 / 9)
        result_label2.config(text=f"{num} {base_temp} = {converted_num:.2f} {target_temp}")
        return converted_num

    elif (base_temp == "Fahrenheit") and (target_temp == "Kelvin"):
        converted_num = (num + 459.67) * (5 / 9)
        result_label2.config(text=f"{num} {base_temp} = {converted_num:.2f} {target_temp}")
        return converted_num

    elif (base_temp == "Celsius") and (target_temp == "Fahrenheit"):
        converted_num = (num * 1.8) + 32
        result_label2.config(text=f"{num} {base_temp} = {converted_num:.2f} {target_temp}")
        return converted_num

    elif (base_temp == "Celsius") and (target_temp == "Celsius"):
        converted_num = num
        result_label2.config(text=f"{num} {base_temp} = {converted_num:.2f} {target_temp}")
        return converted_num

    elif (base_temp == "Celsius") and (target_temp == "Kelvin"):
        converted_num = num + 273
        result_label2.config(text=f"{num} {base_temp} = {converted_num:.2f} {target_temp}")
        return converted_num

    elif (base_temp == "Kelvin") and (target_temp == "Fahrenheit"):
        converted_num = 1.8 * (num - 273) + 32
        result_label2.config(text=f"{num} {base_temp} = {converted_num:.2f} {target_temp}")
        return converted_num

    elif (base_temp == "Kelvin") and (target_temp == "Celsius"):
        converted_num = num - 273
        result_label2.config(text=f"{num} {base_temp} = {converted_num:.2f} {target_temp}")
        return converted_num

    elif (base_temp == "Kelvin") and (target_temp == "Kelvin"):
        converted_num = num
        result_label2.config(text=f"{num} {base_temp} = {converted_num:.2f} {target_temp}")
        return converted_num


# Создаеем главное окно
root2 = tk.Tk()
root2.title("Конвертер температур")
root2.geometry("400x300")
root2.resizable(width=False, height=False)

# Список температур
temp_options = ["Celsius", "Fahrenheit", "Kelvin"]

# Поля ввода
tk.Label(root2, text="Число: ", bg="#B8B8B8").pack(pady=(15, 0))
num_entry = tk.Entry(root2)
num_entry.pack(pady=(3, 0))

# создадим выпадающие списки
tk.Label(root2, text="Исходная температура: ", bg="#B8B8B8").pack(pady=(12, 3))
base_temp_menu = ttk.Combobox(root2, values=temp_options)
base_temp_menu.pack()


tk.Label(root2, text="Целевая температура: ", bg="#B8B8B8").pack(pady=(12, 3))
target_temp_menu = ttk.Combobox(root2, values=temp_options)
target_temp_menu.pack()

# Кнопка для конвертации
convert_button2 = tk.Button(root2, text="Конвертировать", command=lambda: convert_tempreture(base_temp_menu.get(), target_temp_menu.get(), num_entry.get()), bg="#66B2FF", activebackground="#939393")
convert_button2.pack(pady=(10, 3))

# Поле для вывода результата
result_label2 = tk.Label(root2, text="", font=("Arial", 12))
result_label2.pack()

# Запуск главного цикла Tkinter
root2.mainloop()