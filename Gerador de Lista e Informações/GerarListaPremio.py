import random
import os  

cont = 0
qtdpremio = 0
totalpremios = 0

premio1qtd = 0

premio2qtd = 0

premio3qtd = 0

premio4qtd = 0

premio5qtd = 0

premio6qtd = 0

premio7qtd = 0

premio8qtd = 0

premio9qtd = 0

vetorNomes = []
vetorGeral=[]
vetorFinal=[]

acumulador0 = 0
acumulador1 = 0
acumulador2 = 0
acumulador3 = 0
acumulador4 = 0
acumulador5 = 0
acumulador6 = 0
acumulador7 = 0
acumulador8 = 0

aux0 = ""
aux1 = ""
aux2 = ""
aux3 = ""
aux4 = ""
aux5 = ""
aux6 = ""
aux7 = ""
aux8 = ""



qtdpremio = int(input("Quantos prêmios serão inclusos na roleta? Digite apenas o numero e tecle enter:"))
print ("----------------------------------------------------")
print ("Importante! Ao colocar o nome do premio é necessario:")
print ("Abrir aspas, escrever o nome corretamente da imagem que será usada na roleta, fechar aspas e acrescentar virgula")
print ("Exemplo: 'mochila.png',")
print ("Nota-se que é importante adicionar corretamente a extensão do arquivo")
print ("É aconselhado que a extensão da imagem seja .png")
print ("----------------------------------------------------")
while qtdpremio > cont:
    nomepremio = str(input("Insira o nome do prêmio:"))
    quantidade = int(input("Insira quantos prêmios destes poderão ser entregues:"))
    vetorNomes.append(nomepremio)
    totalpremios+=quantidade
    
    if cont == 0:
        aux0 = nomepremio
        premio1qtd = quantidade
        for x in range (0, premio1qtd ,1):
            vetorGeral.append(vetorNomes[cont])
        
    if cont == 1:
        aux1 = nomepremio
        premio1qtd = quantidade
        for x in range (0, premio1qtd ,1):
            vetorGeral.append(vetorNomes[cont])
        
        
    if cont == 2:
        aux2 = nomepremio
        premio2qtd = quantidade
        for x in range (0, premio2qtd ,1):
            vetorGeral.append(vetorNomes[cont])
        
    if cont == 3:
        aux3 = nomepremio
        premio3qtd = quantidade
        for x in range (0, premio3qtd ,1):
            vetorGeral.append(vetorNomes[cont])
        
    if cont == 4:
        aux4 = nomepremio
        premio4qtd = quantidade
        for x in range (0, premio4qtd ,1):
            vetorGeral.append(vetorNomes[cont])
        
    if cont == 5:
        aux5 = nomepremio
        premio5qtd = quantidade
        for x in range (0, premio5qtd ,1):
            vetorGeral.append(vetorNomes[cont])
        
    if cont == 6:
        aux6 = nomepremio
        premio6qtd = quantidade
        for x in range (0, premio6qtd ,1):
            vetorGeral.append(vetorNomes[cont])
        
    if cont == 7:
        aux7 = nomepremio
        premio7qtd = quantidade
        for x in range (0, premio7qtd ,1):
            vetorGeral.append(vetorNomes[cont])
        
    if cont == 8:
        aux8 = nomepremio
        premio8qtd = quantidade
        for x in range (0, premio8qtd ,1):
            vetorGeral.append(vetorNomes[cont])
    
    cont+=1


for a in range (0,totalpremios,1):
      randomm = random.randint(0,totalpremios-1)
      vetorFinal.append(vetorGeral[randomm])
      print (vetorFinal[a])


for y in range (0,totalpremios,1):
    if vetorFinal[y] == aux0:
        acumulador0+=1
  
    if vetorFinal[y] == aux1:
        acumulador1+=1

    if vetorFinal[y] == aux2:
        acumulador2+=1
  
    if vetorFinal[y] == aux3:
        acumulador3+=1

    if vetorFinal[y] == aux4:
        acumulador4+=1
  
    if vetorFinal[y] == aux5:
        acumulador5+=1

    if vetorFinal[y] == aux6:
        acumulador6+=1
  
    if vetorFinal[y] == aux7:
        acumulador7+=1

    if vetorFinal[y] == aux8:
        acumulador8+=1

print ("\n\n--------------|RESULTADO-DA-LISTA|---------------")

if qtdpremio == 0:
    print("Erro, é necessário de pelo menos 1 premio")
elif qtdpremio == 1:
    print (acumulador0,aux0,"foram adicionados a lista de prêmios.")
elif qtdpremio == 2:
    print (acumulador0,aux0,"foram adicionados a lista de prêmios.\n")
    print (acumulador1,aux1,"foram adicionados a lista de prêmios.")
elif qtdpremio == 3:
    print (acumulador0,aux0,"foram adicionados a lista de prêmios.\n")
    print (acumulador1,aux1,"foram adicionados a lista de prêmios.\n")
    print (acumulador2,aux2,"foram adicionados a lista de prêmios.")
elif qtdpremio == 4:
    print (acumulador0,aux0,"foram adicionados a lista de prêmios.\n")
    print (acumulador1,aux1,"foram adicionados a lista de prêmios.\n")
    print (acumulador2,aux2,"foram adicionados a lista de prêmios.\n")
    print (acumulador3,aux3,"foram adicionados a lista de prêmios.")
elif qtdpremio == 5:
    print (acumulador0,aux0,"foram adicionados a lista de prêmios.\n")
    print (acumulador1,aux1,"foram adicionados a lista de prêmios.\n")
    print (acumulador2,aux2,"foram adicionados a lista de prêmios.\n")
    print (acumulador3,aux3,"foram adicionados a lista de prêmios.\n")
    print (acumulador4,aux4,"foram adicionados a lista de prêmios.")
elif qtdpremio == 6:
    print (acumulador0,aux0,"foram adicionados a lista de prêmios.\n")
    print (acumulador1,aux1,"foram adicionados a lista de prêmios.\n")
    print (acumulador2,aux2,"foram adicionados a lista de prêmios.\n")
    print (acumulador3,aux3,"foram adicionados a lista de prêmios.\n")
    print (acumulador4,aux4,"foram adicionados a lista de prêmios.\n")
    print (acumulador5,aux5,"foram adicionados a lista de prêmios.")
elif qtdpremio == 7:
    print (acumulador0,aux0,"foram adicionados a lista de prêmios.\n")
    print (acumulador1,aux1,"foram adicionados a lista de prêmios.\n")
    print (acumulador2,aux2,"foram adicionados a lista de prêmios.\n")
    print (acumulador3,aux3,"foram adicionados a lista de prêmios.\n")
    print (acumulador4,aux4,"foram adicionados a lista de prêmios.\n")
    print (acumulador5,aux5,"foram adicionados a lista de prêmios.\n")
    print (acumulador6,aux6,"foram adicionados a lista de prêmios.")
elif qtdpremio == 8:
    print (acumulador0,aux0,"foram adicionados a lista de prêmios.\n")
    print (acumulador1,aux1,"foram adicionados a lista de prêmios.\n")
    print (acumulador2,aux2,"foram adicionados a lista de prêmios.\n")
    print (acumulador3,aux3,"foram adicionados a lista de prêmios.\n")
    print (acumulador4,aux4,"foram adicionados a lista de prêmios.\n")
    print (acumulador5,aux5,"foram adicionados a lista de prêmios.\n")
    print (acumulador6,aux6,"foram adicionados a lista de prêmios.\n")
    print (acumulador7,aux7,"foram adicionados a lista de prêmios.")
elif qtdpremio == 8:
    print (acumulador0,aux0,"foram adicionados a lista de prêmios.\n")
    print (acumulador1,aux1,"foram adicionados a lista de prêmios.\n")
    print (acumulador2,aux2,"foram adicionados a lista de prêmios.\n")
    print (acumulador3,aux3,"foram adicionados a lista de prêmios.\n")
    print (acumulador4,aux4,"foram adicionados a lista de prêmios.\n")
    print (acumulador5,aux5,"foram adicionados a lista de prêmios.\n")
    print (acumulador6,aux6,"foram adicionados a lista de prêmios.\n")
    print (acumulador7,aux7,"foram adicionados a lista de prêmios.\n")
    print (acumulador8,aux8,"foram adicionados a lista de prêmios.")
print ("-------------------------------------------------\n")

print ("\n_______________________________|ATENÇÃO|_____________________________")
print ("Como os itens foram adicionados com probabilidade, existe uma certa margem de erro")
print ("Ao copiar todos os valores, tirar os itens excedentes e adicionar os faltantes")
print ("_______________________________________________________________________")


os.system("pause")
