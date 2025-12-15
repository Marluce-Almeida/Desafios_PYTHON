
# PROGRAMA QUE GERA LISTAS

#Lista1 = Funcionários que tem carro e trabalham a noite
#Lista2 = Funcionários que tem carro e trabalham durante o dia 
#Lista3 = Funcionários que não tem carro

# LISTAS
funcionarios = ('Jonas', 'Luiza', 'Joana', 'Larissa', 'Roberta', 'Carlos', 'Nadia')
turno_dia = ('Larissa', 'Luiza', 'Nadia', 'Joana')
turno_noite = ('Jonas', 'Roberta', 'Carlos')
tem_carro = ('Jonas', 'Carlos', 'Nadia')

# lista1
lista1 = set(tem_carro).intersection(turno_noite)
print(lista1)

# lista2
lista2 = set(tem_carro).intersection(turno_dia)
print(lista2)

# lista3
lista3 = set(funcionarios).difference(tem_carro)
print(lista3)