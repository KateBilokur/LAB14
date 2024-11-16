import numpy as np
import matplotlib.pyplot as plt

# Визначаємо діапазон x та обчислюємо значення функції Y(x)
x = np.linspace(-2, 5, 500)
y = x * np.sin(5 * x)

# Побудова графіка
plt.figure(figsize=(10, 6))
plt.plot(x, y, color='blue', linewidth=2, linestyle='-', label='Y(x) = x*sin(5x)')

# Додавання заголовка, позначення осей та легенди
plt.title('Графік функції Y(x) = x*sin(5x)', fontsize=16)
plt.xlabel('x', fontsize=14)
plt.ylabel('Y(x)', fontsize=14)
plt.grid(True)  # Додавання сітки для кращої візуалізації
plt.legend(loc='upper left')  # Вставка легенди у верхній лівий кут

# Відображення графіка
plt.show()
