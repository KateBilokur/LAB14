import pandas as pd
import matplotlib.pyplot as plt

# Завантаження даних з CSV файлу
file_path = 'data.csv'  
data = pd.read_csv(file_path)

# Припустимо, що стовпці CSV файлу мають структуру: 'Year', 'Country', 'Value'
# Фільтруємо дані для України та США 
country1 = 'Ukraine'
country2 = 'United States'

data_ukraine = data[data['Country'] == country1]
data_us = data[data['Country'] == country2]

# Побудова лінійного графіка
plt.figure(figsize=(14, 7))
plt.plot(data_ukraine['Year'], data_ukraine['Value'], label=country1, color='blue', linewidth=2)
plt.plot(data_us['Year'], data_us['Value'], label=country2, color='green', linewidth=2)

# Додавання підписів та легенди
plt.title('Динаміка показника для двох країн', fontsize=16)
plt.xlabel('Рік', fontsize=14)
plt.ylabel('Значення показника', fontsize=14)
plt.legend()
plt.grid(True)

# Відображення графіка
plt.show()

# Побудова стовпчастих діаграм для обраної країни
country_choice = input("Введіть назву країни для побудови стовпчастої діаграми (Ukraine або United States): ")

if country_choice in data['Country'].values:
    data_country = data[data['Country'] == country_choice]
    plt.figure(figsize=(14, 7))
    plt.bar(data_country['Year'], data_country['Value'], color='orange')

    # Додавання підписів та заголовка
    plt.title(f'Стовпчаста діаграма для {country_choice}', fontsize=16)
    plt.xlabel('Рік', fontsize=14)
    plt.ylabel('Значення показника', fontsize=14)
    plt.grid(axis='y')

    # Відображення діаграми
    plt.show()
else:
    print("Країну не знайдено у даних.")
