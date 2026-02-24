# Faça um programa que leia um ângulo qualquer e mostre na tela o valor seno, cosseno e tangente desse ângulo.
import math

num = float(input('Digite o angulo que gostaria de encontar: '))


c = math.cos(math.radians(num))
s = math.sin(math.radians(num))
t = math.tan(math.radians(num))

print("cos {:.2f}, seno {:.2f}, tan {:.2f} e ângulo".format(c, s, t, ))