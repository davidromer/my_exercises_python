
n=int(input("Numero de producto: "))
listaCodigo=[]
listaNombre=[]
listaCantidad=[]
listaUnitario=[]
listaTipo=[]

for i in range(n):
    codigo=int(input("Digite el codigo: "))
    nombre=str(input("Digite el nombre: "))
    cantidad=int(input("Digite la Cantidad: "))
    unitario=float(input("Digite Unitario: "))
    tipoIva=int(input("Digite tipo de IVA: "))

    listaCodigo.append(codigo)
    listaNombre.append(nombre)
    listaCantidad.append(cantidad)
    listaUnitario.append(unitario)
    listaTipo.append(tipoIva)

cod=len(listaCodigo)
nom=len(listaNombre)
can=len(listaCantidad)
uni=len(listaUnitario)
tip=len(listaTipo)
print(cod)
print(nom)
print(can)
print(uni)
print(tip)

valorTotalIva=0
valorTotal=0
listaValorProducto=[]
listaValorIva=[]
listaValorFinal=[]

for j in range(n):
    codigo=listaCodigo[j]
    nombre=listaNombre[j]
    cantidad=listaCantidad[j]
    unitario=listaUnitario[j]
    tipoIva=listaTipo[j]

    valorProducto=cantidad*unitario

    if tipoIva==1:
        iva=0
        valorFinal=valorProducto+iva
    elif tipoIva==2:
        iva=valorProducto*0.05
        valorFinal=valorProducto+iva
    elif tipoIva==3:
        iva=valorProducto*0.19
        valorFinal=valorProducto+iva

    valorTotalIva=valorTotalIva+iva
    valorTotal=valorTotal+valorFinal

    listaValorProducto.append(valorProducto)
    listaValorIva.append(valorTotalIva)
    listaValorFinal.append(valorTotal)

    print(codigo)
    print(nombre)
    print(valorProducto)
    print(valorFinal)
print("Total de la compra: ", valorTotal)
print("Valor Total del IVA: ", valorTotalIva)

