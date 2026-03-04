cliente=input("Qual é seu nome:")
doce=input("O que vc comprou:")
num=int(input("Quantas unidades:"))
val=float(input("Qual é o preço:"))

total=num*val

print("--------- RECIBO ---------")
print("Clinte:",cliente)
print("Item:",doce)
print("Total:",total)
print("--------------------------")