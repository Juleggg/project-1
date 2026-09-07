
#pole trojkata za pomoca herona

import math
print("obliczmy pole trojkata za pomoca wzoru herona")
a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))

p = (a+b+c)/2
P = math.sqrt(p*(p-a)*(p-b)*(p-c))
print(f"P = {P}")

#pole kwadratu 1 fig

print("obliczmy pole kwadratu")

a = float(input("a = "))
P = a*a
print(f"P = {P}")

#pole prostokąta 2 fig

print("teraz pole prost")

a = float(input("a = "))
b = float(input("b = "))
P = a*b
print(f"P = {P}")

#pole trojkata z wysokoscia 3 fig

print("obliczmy pole trokata z wysokoscia")

a = float(input("a = "))
h = float(input("h = "))
P = a*h/2
print(f"P = {P}")

#pole trapezu fig 4

print("obliczmy pole trapezu")

a = float(input("a = "))
b = float(input("b = "))
h = float(input("h = "))
P = ((a+b)*h)/2
print(f"P = {P}")

#pole rownolegloboka 5 fig

print("obliczmy pole rownolegloboka")

a = float(input("a = "))
h = float(input("h = "))
P = a*h
print(f"P = {P}")