fobj = open('C:\\Users\\karth\\emp.csv','r')
L = fobj.readlines()
fobj.close()

total = 0
for var in L:
    if 'sales' in var:
        var = var.strip()
        emp_list = var.split(",")
        ecost = emp_list[-1]
        total = total + int(ecost)
print(f"Sum of sales dept emp's cost:{total}")
 
 ## in Functional programming
"""
 >>> fobj = open('emp.csv','r')
>>>
>>> map(lambda a:a,open('emp.csv','r'))
<map object at 0x0000014A86B7DCC0>
>>>
>>> list(map(lambda a:a,open('emp.csv','r')))
['eid,ename,edept,ecity,ecost\n', '101,raj,sales,pune,1000\n', '102,leo,prod,bglore,2301\n', '230,raj,prod,pune,2300\n', '450,shan,sales,bglore,3401\n', '542,anu,HR,mumbai,4590\n', '321,bibu,sales,hyd,5419\n', '651,ram,hr,bglore,3130\n', '541,leo,admin,chennai,4913\n', '652,karthik,prod,bglore,3490\n', '742,anu,sales,mumbai,5901\n', '821,shan,prod,hyd,6000\n', '151,ram,prod,bglore,3000\n', '241,vijay,admin,chennai,3450\n', '252,anish,Hr,mumbai,5490']
>>>
>>> P1 = list(map(lambda a:a,open('emp.csv','r')))
>>>
>>> list(filter(lambda a:'sales' in a,P1))
['101,raj,sales,pune,1000\n', '450,shan,sales,bglore,3401\n', '321,bibu,sales,hyd,5419\n', '742,anu,sales,mumbai,5901\n']
>>>
>>>
>>> P1 = list(map(lambda a:a,open('emp.csv','r')))
>>> P2 = list(filter(lambda a:'sales' in a,P1))
>>>
>>> P3 = list(map(lambda a:a.split(",")[-1],P2))
>>> P3
['1000\n', '3401\n', '5419\n', '5901\n']
>>>
>>> functools.reduce(lambda a,b:int(a)+int(b),P3)
15721
>>>
>>> functools.reduce(lambda a,b:int(a)+int(b),map(lambda a:a.split(",")[-1],filter(lambda a:'sales' in a,map(lambda a:a,open('emp.csv','r'))))
... )
15721
>>>
"""
    