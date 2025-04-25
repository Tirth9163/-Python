def modify():
    names = set()

    names.update(["Manthan", "Dhyan", "Vedaant", "Utsav", "Nirmal"])
    print("adding names:", names)

    if "Dhyan" in names:
        names.remove("Dhyan")
        names.add("Nishant")
    print("modifying name:", names)

    names.remove("Manthan")  
    names.remove("Vedaant")    
    print("deleting two names:", names)

modify()
