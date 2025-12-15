# CÁLCULO IMC - Índice de Massa Corporal

# MENOR QUE 18,5 MAGREZA
# ENTRE 18,5 E 24,9 NORMAL
# ENTRE 25,0 E 29,9 SOBREPESO
# ENTRE 30,0 E 39,9 OBESIDADE
# MAIOR QUE 40,0 OBESIDADE GRAVE

Altura = float(input('Qual é a sua altura? '))
Peso = int(input('Qual é o seu peso em kg? '))

# IMC = peso / (altura x altura)

calculoIMC = Peso / (Altura* Altura)
if calculoIMC < 18.5:
    print('Abaixo do peso')
elif calculoIMC <=24.9:
    print('Peso normal')
elif calculoIMC <=29.9:
    print('Acima do peso')
elif calculoIMC <=39.9:
    print('Obesidade')
else:
    print('Obesidade grave')