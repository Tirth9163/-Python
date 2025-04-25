def counter (l):
    c,d=0,0
    for i in l:
        if isinstance(i,tuple):
            for j in i:
                c+=1
        else:
            d+=1
    print(f"There are {c} boys")
    print(f"There are {d} girls")

l=["sita","laxmi",("manthan","dhyan"),"jigna",("utsav","vedaaant","niru")]
counter(l)

 
