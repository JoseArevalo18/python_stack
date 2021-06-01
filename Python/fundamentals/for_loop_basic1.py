# #BASICO
for x in range (0,151,1):
    print(x)
# # #MULTIPLOS DE CINCO
for x in range (0,1001,5):
    print(x)
# #CONTAR,DOJO WAY
for x in range (1,101,1):
    if x % 10 == 0:
        print("Coding Dojo")
    elif x % 5 == 0:
        print("Coding")
    else:
        print(x)
#!UF, ESO ES BASTANTE GRANDE!
suma=0
for x in range (0,500000,1):
    if x % 2 == 1:
        suma= suma+x
print(suma)
#CUENTA REGRESIVA POR CUATRO
for x in range (2018,-1,-4):
    print(x)
#CONTADOR FLEXIBE
lowNum=2
highNum=9
mult=3
for x in range (lowNum,highNum + 1):
    if  x % mult ==0:
        print(x)


