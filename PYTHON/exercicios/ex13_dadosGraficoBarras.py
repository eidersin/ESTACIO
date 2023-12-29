# importando a classe, da forma mais usual
import matplotlib.pyplot as plt
import numpy as np

# x = ["a", "b", "c", "d"]
# y = [3, 8, 1, 10]
# plt.plot(x, y, 'k--')
# plt.plot(x, y, 'go')

x = np.array(["a", "b", "c", "d"])
y = np.array([3, 8, 1, 10])
plt.bar(x, y)
plt.title("Grafico do Exercício 13")
plt.show()






