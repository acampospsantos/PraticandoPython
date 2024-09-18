#Operadores - Lógicos
# &&    AND  --> Só é true quando todos os valores de entrada são TRUE
# ||    OR   --> É true desde que um dos valores de entrada seja true
# !     NOT  --> Recebe um valor de entrada e inverte o valor lógico

#Trabalham com valores true e false

#Exemplo usando operador AND
idade = 25
altura = 1.81

resultado = (idade >=18) and (altura > 1.8)

print('Pode participar do evento? = ', resultado)


#Exemplo usando operador OR
#Vamos simular um programa de disparo de alarme
porta = False
janela = True

alarme = (porta == True) or (janela == True)

print('Alarme disparado? = ', str(alarme) ) #Converti alarme(boolean) para String


#Exemplo usando operador NOT

tem_dinheiro = False

tem_dinheiro = not tem_dinheiro #Ou seja, inverti o valor: era False e se tornou True

print('Tem dinheiro? = ', str(tem_dinheiro))