import os

texto = "Cientista de Dados é a profissão que mais tem crescido em todo mundo.\n"
texto += "Esses profissionais precisam se especializar em Programação, Estatística e Machine Learning.\n"
texto += "E claro, em Big Data."

def criar_texto_em_linhas (texto_principal):
    texto_criado = ''
    print (texto_principal)
    print (texto_principal.split())
    for palavra in texto_principal.split():
        texto_criado += palavra
        texto_criado += "\n" 
    print (texto_criado)
    print ()
    print ("parte 2")
    print ()  
    novo = ''
    for palavra in texto_principal.split():
        novo += (palavra+' ')
    print (novo)
    return novo
texto2 = criar_texto_em_linhas(texto)

def criar_arquivo (texto):
    # Criando um arquivo 
    arquivo = open(os.path.join('Aula\Atividades\manipulacao_de_arquivos.txt'),'w')
    # Gravando os dados no arquivo  
    for palavra in texto.split():
        arquivo.write(palavra+' ')
    print ("\narquivo criado")
    arquivo.close()
criar_arquivo(texto)


def lendo_arquivo():
        # Lendo o arquivo
    arquivo = open('Aula\Atividades\manipulacao_de_arquivos.txt','r')
    conteudo = arquivo.read()
    arquivo.close()
    print(conteudo)
print ("\nlendo arquivo")
lendo_arquivo()

def lendo_arquivo_sem_close():
    # Com with, O método close() é executado automaticamente    
    with open('Aula\Atividades\manipulacao_de_arquivos.txt','r') as arquivo:
        conteudo = arquivo.read()

        print(len(conteudo))
        print(conteudo)

print("\nlendo arquivo com with. O método usa o close automaticamente")
lendo_arquivo_sem_close()


texto = 'podemos então abrir o arquivo para:\n'
texto += 'w = escrever\n'
texto += 'r = ler\n'
texto += 'a = adicionar\n'
texto += 'entre outros.'

import csv

def arquivo_csv ():    
    with open('Aula\Atividades\manipulacao_de_numeros.csv','w') as arquivo:
        writer = csv.writer(arquivo)
        writer.writerow(('primeira','segunda','terceira'))
        writer.writerow((55,93,76)) 
        writer.writerow((62,14,86))
   
    # Leitura de arquivos csv
    with open('Aula\Atividades\manipulacao_de_numeros.csv','r') as arquivo:
        leitor = csv.reader(arquivo)
        for x in leitor:
            print ('Número de colunas:', len(x))
            print(x)

print ("\nManipulando arquivos csv")
arquivo_csv ()

def arquivo_teste ():
    with open('Aula\Atividades\manipulacao_de_arquivos_teste.txt','w') as arquivo:
        posicao = 'primeira ','segunda ','terceira '
        for palavra in posicao:
            arquivo.write(palavra)
        numeros = "62 \n","            14       \n","86 \n           87"
        arquivo.writelines(numeros)
        # write lines faz a mesma coisa que a função for.

def arquivo_teste1 ():   
    with open('Aula\Atividades\manipulacao_de_arquivos_teste.txt','r') as arquivo:
        conteudo = arquivo.read()
        print(len(conteudo))
        print(conteudo)
        
        letras_separadas = []
        for x in conteudo:
            x = x.strip()
            letras_separadas.append(x)
        print ("arquivo teste 1, com tipo lista: = []")
        print (letras_separadas)

        letras_separadas2  = ''
        for x in conteudo:
            x = x.strip()
            letras_separadas2 += x
        print ("arquivo teste 2, com tipo literal: = ''")
        print (letras_separadas2)
        # quando vamos recriar o texto com "with as", o loop for fica em letras
        # ao contrario do open.
        palavras = ''
        y = open('Aula\Atividades\manipulacao_de_arquivos_teste.txt','r')
        for x in y:
            palavras += x.strip()
        y.close()
        print ()
        print ("arquivo teste 3, com tipo open e literal: = ''")
        print (palavras)

        palavras2 = []
        y = open('Aula\Atividades\manipulacao_de_arquivos_teste.txt','r')
        for x in y:
            x = x.strip()
            palavras2.append(x)
        y.close()
        print ("arquivo teste 4, com tipo open e lista: = []")
        return palavras2

print ()
print ("\nArquivo teste")
arquivo_teste()
print ()

nova = arquivo_teste1 ()
print ("retornando um loop for com arquivo reescrito em lista fica: {}" .format(nova))
print ()