#Funciones
def ordenamiento(n,codigo,cantidad,unitario,iva,nombre,valor_producto,valor_final):
    for i in range(0,n-1):
        for j in range(i+1,n):
            if(nombre[i] > nombre[j]):
                t=codigo[i]
                codigo[i]=codigo[j]
                codigo[j]=t
                t=nombre[i]    
                nombre[i]=nombre[j]
                nombre[j]=t
                t=cantidad[i]
                cantidad[i]=cantidad[j]
                cantidad[j]=t
                t=unitario[i]
                unitario[i]=unitario[j]
                unitario[j]=t
                t=iva[i]
                iva[i]=iva[j]
                iva[j]=t
                t=valor_producto[i]
                valor_producto[i]=valor_producto[j]
                valor_producto[j]=t
                t=valor_final[i]
                valor_final[i]=valor_final[j]
                valor_final[j]=t
    return (codigo,nombre,cantidad,unitario,iva,valor_producto,valor_final)

#Cuerpo del programa
n=int(input("n: "))
total_venta=0
total_iva=0
codigo=[]
nombre=[]
cantidad=[]
unitario=[]
tipo=[]
valor_producto=[]
iva=[]
valor_final=[]
for i in range(n):
    codigo.append(int(input("codigo: ")))
    nombre.append(input("nombre: "))
    cantidad.append(float(input("cantidad: ")))
    unitario.append(float(input("unitario: ")))
    tipo.append(int(input("tipo: ")))

for i in range(n):
    valor_producto.append(cantidad[i]*unitario[i])
    if tipo[i]==1:
        iva.append(0)
    elif tipo[i]==2:
        iva.append(valor_producto[i]*0.05)
    else:
        iva.append(valor_producto[i]*0.19)
    valor_final.append(valor_producto[i]+iva[i])
    total_iva=total_iva+iva[i]
    total_venta=total_venta+valor_final[i]

codigo,nombre,cantidad,unitario,iva,valor_producto,valor_final=ordenamiento(n,codigo,nombre,cantidad,unitario,iva,valor_producto,valor_final)

for i in range(n):
    print(codigo[i])
    print(nombre[i])
    print(valor_producto[i])
    print(valor_final[i])

print(total_venta)
print(total_iva)