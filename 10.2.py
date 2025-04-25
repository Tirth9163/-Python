f = open("marks.csv")
dic = {}
d = f.readline()
d = f.readline()
while d:
    parts = d.strip().split(",")  
    if len(parts) == 5:
        rlno, nm, cp, maths, eee = parts
        total = float(cp) + float(maths) + float(eee)
        dic[rlno] = [nm, float(cp), float(maths), float(eee), total]
        print(rlno, dic[rlno])
    d = f.readline()

f.close()
