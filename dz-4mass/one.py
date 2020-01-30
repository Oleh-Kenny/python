mass = [1, 2, 5, 56, 7, 87, 98, 0, 34, 123, 545, 6, 7, 8888]
print(mass)
min_value = min(mass)
max_value = max(mass)
min_index = mass.index(min_value)
max_index = mass.index(max_value)
temp=mass[min_index]
mass[min_index] = mass[max_index]
mass[max_index] = temp
print("New Arr", mass)