diccio = {0:"a", 1:"a", 2:"b", 3:"c", 4:"a"}
itera = 0
repe = []

for value in diccio.values():
    if value in diccio:
        print(value)
        itera +=1
    else:
        repe.append(value)
        repe.append(itera)

print(diccio)
print(repe)
