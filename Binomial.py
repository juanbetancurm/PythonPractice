n = int(input("Ingrese la fila por favor: "))
r = int(input("Ahora ingrese el término que necesita:" ))
row = 0
term = 0
d = n - r
outcome = 0

def factorial(a):

   if int(a) >= 1:
      for i in range (1, a):
         a = a * i
   if int(a) == 0:
         a = 1
   return a
"""      
def placeI(n, r):
   row = factorial(n)
   term = factorial(r)
   dif = factorial(n-r)

def place(row, n, r, dif):
   outcome = (row)/(term(dif))
"""
#print (d)
row = factorial(n)
term = factorial(r)
dif = factorial(d)

#print(row, term, dif)

outcome = (row)/(term*dif)
print(int(outcome))
#placeI(n, r)
#place(row, n, r, dif)
#print(outcome)
#print("El termino", r, "es: ")