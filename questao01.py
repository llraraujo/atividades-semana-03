

PI = 3.141592

raio = float(input("Digite o raio: ").strip())

comprimento_circunferencia = 2 * PI * raio

area_circulo = PI * (raio ** 2)

area_esfera = 4* PI * (raio **2)

volume_esfera =  4/3 * PI * (raio ** 3)

print("Comprimento da circunferencia: %.6f" %(comprimento_circunferencia))
print("Área do círculo: %.6f" %(area_circulo ))
print("Área da esfera: %.6f" %(area_esfera ))
print("Volume da esfera: %.6f" %(volume_esfera ))


