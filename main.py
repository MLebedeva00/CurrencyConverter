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

# Получаем список валют
currencies = get_currency_list()

# Поля ввода и выпадающие списки
tk.Label(root, text="Сумма: ").pack()  # метка с надписью сумма, pack размещает элемент на экране
amount_entry = tk.Entry(root)   # поле для ввода суммы
amount_entry.pack()

# создадим выпадающие списки
tk.Label(root, text="Исходная валюта: ").pack()
base_currency_var = tk.StringVar(value="USD")  # хранит выбранную валюту
base_currency_menu = ttk.Combobox(root, textvariable=base_currency_var, values=currencies)
base_currency_menu.pack()

tk.Label(root, text="Целевая валюта: ").pack()
target_currency_var = tk.StringVar(value="EUR")
target_currency_menu = ttk.Combobox(root, textvariable=target_currency_var, values=currencies)
target_currency_menu.pack()

# Кнопка для конвертации
convert_button = tk.Button(root, text="Конвертировать", command=convert_currency)
convert_button.pack()

# Поле для вывода результата
result_label = tk.Label(root, text="", font=("Arial", 12))
result_label.pack()

# Запуск главного цикла Tkinter
root.mainloop()
