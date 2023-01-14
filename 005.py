a, b, c = map(int, input().split())

d = b**2 - 4*a*c

root1 = (-b + d**0.5)/2*a
root2 = (-b - d**0.5)/2*a

print('The roots are {0} and {1}'.format(root1, root2))
