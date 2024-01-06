dict1 = {5:2,6:4,7:3,8:1,9:0}
val = list(dict1.items())
print(val)

newval = []

for i in val:
    irev= i[::-1]

    newval.append(irev)
print(newval)
val.clear()
newval.sort()
print(newval)

for i in newval:
    irevf = i[::-1]
    val.append(irevf)
print(val)

descending = val[::-1]
print(descending)
print("ascening order of value in the dictionary is:",dict(val))
print("descending order of the value in the dictionary is:",dict(descending))
