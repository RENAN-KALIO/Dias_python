n1 = int(input("Digite um numero"))
n2 = int(input("Digite um numero"))
n3 = int(input("Digite um numero"))

menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3
print("O menor valor digitado foi {}".format(menor))