dicti = {}
repeted = []
#valor = 0
itera = 0

wordy = input("Type the sentence: ")

HowMany = len(wordy)

def MakeDict(words):
    valor = 0
    for element in wordy:
        if element != " ":
            dicti[valor] = element
            valor = valor + 1
"""
def Counting(dicti):
    itera = 0
    for count, value in enumerate(dicti):
        if (value in dicti):
            itera +=1
            dicti[value] = count
        else:
            repeted.append(value)
            repeted.append(itera)
"""

def Counting(wordy):
    itera = 0
    for i in wordy:
        if dicti[i] in wordy:
            itera += 1
            i = i + 1
        else:
           i = i + 1
           repeted.append(dicti[i])
           repeted.append(itera)


#for count, value in enumerate(baldosa):
#if (value in diccionario):
#            defectuosas += 1
#        diccionario[value] = count

MakeDict(wordy)

Counting(wordy)

print(dicti)
print(itera)
print(repeted)