import random
def odd():
      o,e,fl=[],[],[]
      for i in range(5):
            a=random.randrange(1,100,2)
            o.append(a)
      print(o)
      for i in range(4):
            a=random.randrange(0,100,2)
            e.append(a)
      print(e)
      o[2]=e
      print(o)
      o = [*o[:2], *e, *o[3:]]
      print(o)
      print(sorted(o))
      


odd()
      

