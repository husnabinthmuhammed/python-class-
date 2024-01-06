listofdict = [{"V":"S001"},{"V":"S002"},{"V":"S001"},{"VI":"S005"},{"VII":"S005"},{"V":"S009"}]
unique_val = []
values = []
for i in listofdict:

    for value in i.values():
        values.append(value)
        if value not in unique_val:
            unique_val.append(value)
print(unique_val)