def convert(f):
    return (f - 32) * 5 / 9

fr,cs = [],[]

for i in range(5):
    t = float(input(f"Enter temperature {i+1} in Fahrenheit: "))
    fr.append(t)

for i in range(5):
    cs.append(convert(fr[i]))

print("Fahrenheit:", fr)
print("Celsius:", cs)
