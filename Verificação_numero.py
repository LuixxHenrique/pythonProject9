entrada = '1.21+3*4+10-11/79'
entrada_mod_1 = entrada.replace('-', '|').replace('*', '|').replace('+', '|')
entrada_mod_2 = entrada_mod_1.split('|')
controle = 0
print(entrada)
print(entrada_mod_1)
print(entrada_mod_2)
print(controle)

for i in range(len(entrada_mod_2)):
    print(entrada_mod_2[i].replace('.', '1').isnumeric())
    if not entrada_mod_2[i].replace('.', '1', 1).isnumeric():
        controle = 1
        break
print(controle)
if controle == 0:
    print(eval(entrada))
else:
    print('Conta Invalida')

# print(entrada_mod_2[i].isnumeric())
# print(entrada_mod_2[i])