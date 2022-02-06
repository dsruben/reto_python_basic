billete_5 = 0
billete_10 = 0
billete_20 = 0
billete_50 = 0
billete_100 = 0
billete_200 = 0
billete_500 = 0
total_comida = 0

platos = ['pan','agua','arroz','curry','pollo','tandori']
precio = [2,3,4,8,10,6]
lista_pedido = []
cuenta = []

carta = dict(zip(platos,precio))
print(carta)


pedido = str(input("Que quiere para comer: "))
lista_pedido.append(pedido)
respuesta=int(input("Quiere algo mas SI=1, NO=0 : "))
if(respuesta == 1):
    y_luego  = True
else:
    y_luego = False



while y_luego == True:

    if respuesta == 1:
        pedido = str(input("Que mas quiere para comer: "))
        lista_pedido.append(pedido)
        respuesta = int(input("Quiere algo mas SI=1, NO=0 : "))
    else:
        y_luego = False

print(lista_pedido)
for plato in platos:

    for plato_pedido in lista_pedido:
        if plato_pedido == plato:
            print(plato_pedido)
            coste = carta[plato_pedido]
            cuenta.append(coste)
            break
total_comida = sum(cuenta)
bill=total_comida

while total_comida >= 500:
    billete_500 += 1
    total_comida -= 500

while total_comida >= 200:
    billete_200 += 1
    total_comida -= 200

while total_comida >= 100:
    billete_200 += 1
    total_comida -= 100

while total_comida >= 50:
    billete_50 += 1
    total_comida -= 50

while total_comida >= 20:
    billete_20 += 1
    total_comida -= 20

while total_comida >= 10:
    billete_10 += 1
    total_comida -= 10

while total_comida >= 5:
    billete_5 += 1
    total_comida -= 5

print("la cuenta total ha sido %d , se tiene que pagar con %d billetes de 500 , %d billetes de 200 , %d billetes de 100, "
      "%d billetes de 50 , %d billetes de 20 , %d billetes de 10 , %d billetes de 5  y %d monedas"
      % (bill,billete_500,billete_200,billete_100,billete_50,billete_20,billete_10,billete_5,total_comida))

