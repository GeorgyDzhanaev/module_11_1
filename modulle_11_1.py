import numpy as np
import matplotlib.pyplot as plt
import requests

#1

arr = np.array([1, 2, 3, 4, 5])

mean = np.mean(arr)
sum_arr = np.sum(arr)
squared = arr ** 2

print("Mean:", mean)
print("Sum:", sum_arr)
print("Squared:", squared)

#2

x = np.linspace(0, 10, 100)
y = np.sin(x)


plt.plot(x, y, label='Sine Wave')
plt.title('Sine Wave Example')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.legend()
plt.grid(True)

plt.show()

#3

url = "https://jsonplaceholder.typicode.com/users"

response = requests.get(url)


if response.status_code == 200:
    data = response.json()
    for user in data:
        print(f"ID: {user['id']}, Name: {user['name']}, Email: {user['email']}")
else:
    print(f"Ошибка при получении данных: {response.status_code}")