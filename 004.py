# Take 3 sides as input

a = int(input())
b = int(input())
c = int(input())

s = (a + b + c)/2

area = (s * (s - a) * (s - b) * (s - c)) **(0.5)

print(round(area, 2))

