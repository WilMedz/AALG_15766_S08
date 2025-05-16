cajas=[(10,4,"A"),(4,3,"B"),(7,3,"C"),(5,2,"D"),
       (3,1,"E"),(3,2,"F"),(2,1.8,"G"),(3,3,"H")]

for i in range(len(cajas)):
    for j in range(i+1,len(cajas)):
        precioKg_i=cajas[i][1] / cajas [i][0]
        precioKg_j=cajas[j][1] / cajas [j][0]
        if precioKg_i < precioKg_j:
            cajas[i],cajas[j]=cajas[j],cajas[i]

pesoMax=float(input("Ingrese el peso máximo que puede llevar la mochila: "))

peso_act=0
precio_total=0
cajas_seleccionadas=[]

for caja in cajas:
    if peso_act >= pesoMax:
        break
    
    peso,soles,denom=caja
    espacio=pesoMax-peso_act
    
    if peso <= espacio:
        fraccion=1
    else:
        fraccion=espacio/peso
        
    cajas_seleccionadas.append((denom,peso*fraccion,soles*fraccion))
    peso_act += peso*fraccion
    precio_total += soles*fraccion
       
print("Las cajas seleccionadas son: ")
for denom,peso,soles in cajas_seleccionadas:
    print(f"{denom}:{peso} (s/. {soles:.2f})")

print(f"Peso cargado:{peso_act:.2f} kg")
print(f"Precio total: s/.{precio_total:.2f}")