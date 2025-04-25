import random
def find():
      a=[]
      s=0
      for i in range(20):
            m=random.randrange(1,100)
            a.append(m)
      print(a)
      x=int(input("Enter a number"))
      for i in a:
            if x==i:
                  print(a[s],s)
            s+=1
find()
