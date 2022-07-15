valorTotal=0
valorTotalIva=0
n=int(input("Digite la cantidad del producto: "))
for i in range (n):
    codigo=int(input("Digite el codigo del producto: "))
    nombre=(input("Digite el nombre del producto: "))
    cantidad=float(input("Digite la cantidad comprada: "))
    unitario=float(input("Digite el valor Unitario: "))
    tipo=int(input("Digite el tipo de iva, que puede ser: 1: exento de iva, 2: Bienes\n"+"donde se aplica el iva del 5% y 3: General, Donde se aplica como iva del 19% "))

    if tipo==1:
        valorProducto=cantidad*unitario
        valorIva=0
        valorFinal=valorProducto+valorIva
    elif tipo==2:
        valorProducto=cantidad*unitario
        valorIva=valorProducto*0.05
        valorFinal= valorProducto+\
                    valorIva
    elif tipo==3:
        valorProducto=cantidad*unitario
        valorIva=valorProducto*0.19
        valorFinal=valorProducto+valorIva
    
    valorTotalIva=valorTotalIva+valorIva
    valorTotal=valorTotal+valorFinal

    print("El codigo es: ", codigo)
    print("El nombre es: ", nombre)
    print("El valor del producto es: ", valorProducto)
    print("El valor final es: ", valorFinal)

print("El valor total a pagar es: ", valorTotal)
print("El valor total del IVA es: ", valorTotalIva)





