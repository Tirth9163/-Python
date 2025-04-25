def sorter(x):
   salaries={}
   for i in x:
     dept = i[0]  
     salary = x[i]  
    
     if dept not in salaries:
        salaries[dept] = []
     salaries[dept].append(salary)

   return salaries

x = {
    (1, "204"): 500,(1,"069"): 420,(1, "186"): 1000,(2, "167"): 750,(2, "179"): 1200,(3, "189"): 900,(3, "231"): 1100
}
salaries=sorter(x)
for dept in salaries:
     print("Department:", dept, "Min =", min(salaries[dept]), ", Max =", max(salaries[dept]))
