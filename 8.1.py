def convert(a) :
  up = set()  
  for i in a:
    up.update(i.upper())
  return up

x = ["Manthan", "Vedaant", "Dhyan", "Utsav", "Nirmal"]
print(convert(x))
