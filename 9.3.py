def create_array(x,y,z,value):
    return [[[value for i in range(z)]for i in range(y)]for i in range(x)]
array_3d=create_array(2,3,4,1)
print(array_3d)
