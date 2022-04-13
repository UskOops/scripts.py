# scripts.py
<H2>Curso de python Gustavo Guanabara</H2>

-~-~-~-~-~-~-~-~- Tipos primitivos ~-~-~-~-~-~-~-~-~-

  int()  --> Para números inteiros ------------ 17, 21, 35, 42

  float() -> Números de ponto flutuante ---2.3, 1.6, 14.9, -67.1

  bool() --> Armazena True ou False --------True, False

  str() ----> Conjunto de caracteres -------- 'narigudo', 'Pedro', 'feioso'

  type() ---> Indica o tipo primitivo da var -  x = 'Sapo Tunado'   print(type(x)) logo seu tipo primitivo é string

-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-


-~-~-~-~-~-~-~- Operadores Aritméticos ~-~-~-~-~-~-~-

  + -> Adição              ** -> Potencia
  - -> Subtração           // -> Divisão inteira
  * -> Multiplicação        % -> Resto da divisão
  / > Divisão -


           Ordem de Precedência

  1° -> ()
  2° -> **
  3° -> *  /  //  %
  4° -> +  -

-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-


~-~-~-~-~-~-~--~-~-~ Módulos -~-~-~-~-~-~-~-~-~-~-~

  Import > Importa uma biblioteca - import math

  from math import cos -> Importa somente a funçao cos da biblioteca math

  math -> Biblioteca de operadores aritméticos {

     sqrt()  ---> Raiz Quadrada de um numero ------- raiz = math.sqrt(numero)
     floor() ---> Arredonda o numero para baixo ---- 5,23 fica 5,00
     ceil() -----> Retorna um valor inteiro ---------------- 5,23 fica 5
     hypot() ---> Retorna a hipotenusa dos catetos - math.hypot(co, ca)
     pow() ----> Potencia de um numero ---------------- pow(2, 3) = 2³ = 8
     radians()-> Converte em graus radianos ---------- print(math.radians(180))
     cos() -----> Retorne o cosseno em radianos --- print(math.cos(math.radians(x)))
     sin() ------> Retorne o seno em radianos --------- print(math.sin(math.radians(x)))
     tan() -----> Retorne a tangente em radianos---- print(math.tan(math.radians(x)))
  }

  random -> Gerar numeros pseudoaleatorios {

      randint() > Retorna um numero inteiro no range --------------- random.randint(1, 10)
      choice() --> Retorna um elemento aleatório da sequência - random.choice(x)
      shuffle() > Embaralha a sequência x no lugar ------------------- random.shuffle(y)
  }
-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-


-~-~-~-~-~-~-~-~- Manipulando Textos ~-~-~-~-~-~-~-~-

  frase = 'ESTOU APRENDENDO A PROGRAMAR EM PYHTON'

  frase[9] ------> Pega os caracteres das posições indicadas ------------------- letra E
  frase[9:13] -> Pega os caracteres das posições indicadas ------------------- ENDE
  frase[9:18:2]--> Pega os caracteres das posições indicadas pulando 2 - EDNOA
  len() -------------> Mostra quantos caracteres tem a frase -------------------------------- len(frase) = 38 letras
  count() ---------> Conta quantas vezes aparece a letra escolhida ----------- frase.count('s')
  find() ------------> Procura os caracteres escolhido ---------------------------------- frase.find('aprendendo')
  replace() ------> Troca uma palavra por outra na frase --------------------------- frase.replace('python','JavaScript')
  upper() ---------> Colocar todas as outras letras em maiúsculo -------------- frase.upper()
  lower() ---------> Colocar todas as outras letras em minusculo -------------- frase.lower()
  capilalize() ---> Coloca todas a frase em minusculo menos a 1 letra --- frase.capitalize()
  title() ------------> Todas as palavras começa com letra maiúscula --------- frase.title()
  strip() -----------> Tira o espaço do começo e no fim da frase ----------------- frase.strip()  frase.lstrip()  frase.rstrip()
  split() -----------> Vai ocorrer uma divisão entre os espaços da frase ----- frase.split()
  .join() -----------> Juntar uma coisa com a outra -------------------------------------- '-'.join.frase Estou-aprendendo-a-programar-em-python

-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~--~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~--~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~--~-~-~-








~-~-~-~-~-~-~--~-~-~ FUNÇÕES (def) ~-~-~-~-~-~-~--~-~-~ 


*O que é uma FUNÇÃO no Python?
São blocos nomeados de um código designado para fazer um trabalho em específico. Elas permitem que você escreva o código uma vez que
 poderá ser usado a quantidade de vezes que você precisar para fazer uma mesma função. As funções podem pegar a informação que elas precisam e retornar a informação que elas geram. Então, basicamente é um jeito de tornar os programas fáceis de escrever, ler, testar, e consertar.


*Para definir uma função, a primeira linha dela é a sua definição, marcada pela palavra-chave DEF. O nome da função é seguido por um conjunto
 de parênteses e dois pontos. Uma DOCSTRING, em aspas triplas, descreve o que a função faz. O corpo da função ou o bloco de códigos dela é identado em um nível.

Exemplo:
def lin():
    """Mostra uma linha com trinta hífens seguidos."""
    print('-' * 30)

*Para chamar uma função, é só você digitar o nome da função seguido por um conjunto de parênteses, como por exemplo: lin()

*PARÂMETROS: INFORMAÇÃO QUE É RECEBIDA POR UMA FUNÇÃO, ESTÃO LISTADOS EM PARÊNTESES NA DEFINIÇÃO DA FUNÇÃO.

*ARGUMENTOS: INFORMAÇÃO QUE É PASSADA PARA UMA FUNÇÃO, SÃO INCLUÍDOS NOS PARÊNTESES DEPOIS DO NOME DA 
FUNÇÃO.
 
(Você pode tratar do jeito que você quiser, eu prefiro separar em parâmetros e argumentos.)

*Exemplo de argumentos e parâmetros em uma função:
def mostra_titulo(texto):    => texto nesse caso é o PARÂMETRO.
    """Mostra o título de forma elegante."""
    print(f'{"=-=" * 10}\n{texto.upper():^30}\n{"=-=" * 10}')


mostra_titulo('sistema de alunos')    => 'sistema de alunos' é uma string que eu defini como ARGUMENTO.

*Existem dois tipos de argumentos, que são os posicionais e os argumentos de palavra-chave. Quando você usa argumentos posicionais, Python 
corresponde ao primeiro argumento na chamada da função com o primeiro parâmetro na definição da função e assim por diante. Com os argumentos de palavra-chave, você específica com qual parâmetro o argumento deve ser atribuído na chamada da função. Quando os argumentos de palavra-chave são usados, a ordem dos argumentos não importa.


*Exemplos de argumentos posicionais e de palavra-chave:
def mostra_soma(a, b):
    """Mostra a soma de dois números."""
    print(f'A = {a} e B = {b}')
    s = a + b
    print(f'A soma A + B = {s}')

mostra_soma(4, 5)   => Argumentos posicionais.
mostra_soma(b=4, a=5)   => Argumentos de palavra-chave.

*Para passar um número arbitrário de argumentos para um parâmetro, usa-se o operador *. O parâmetro que deve aceitar um número arbitrário
 de argumentos deve ser o último na definição de uma função. 

Exemplo:
def contador(*num):
    """Mostra uma quantidade arbitrária de valores em uma tupla."""
    print(num)


contador(2, 1, 7)
contador(4, 4, 7, 6, 2)

*Você pode passar uma LISTA como argumento para uma função, e a função pode trabalhar com os valores na lista. Qualquer alteração feita na
 lista criada pela função afetará a lista original. Para impedir que uma função modifique a lista original, é só passar como argumento uma cópia da lista.

Exemplo, passando uma lista como argumento:
def dobra(lista):
    """Dobra os valores da lista."""
    pos = 0
    while pos < len(lista):
        lista[pos] *= 2
        pos += 1


valores = [6, 3, 9, 1, 0, 2]
valores_cópia = valores[:]
dobra(valores_cópia)
print(valores_cópia)
print(valores)


