"""
_______
set
______

immutable,unchangable,unordered,un indexed,duplicates not allowed

"""
set1 = {"safna",12,"python","BCA",12,"python"}
print(set1)
x=list(set1)
print(x)
print(x[3])

set1 = {"safna",12,"python","BCA",12,"python",(1,2,3),set["fghj",78,'fghj']}
print(set1)


set1 ={}
print(type(set1))

A = {"priya",12,"python","B-TECH"}
B = {"safna",12,"python","BCA","python"}
print(A.union(B))
print(A.intersection(B))
print(A.difference(B))
print(A.symmetric_difference(B))



