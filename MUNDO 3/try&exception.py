try: #tenta executar o bloco de código abaixo
    a = int(input("Enter a number: "))
    b = int(input("Denominator: "))
    r = a/b
except Exception as error: #se ocorrer um erro, executa o bloco abaixo
    print(f'The problem found is {error.__class__.__name__}') #printa o nome da classe do erro
else: #se não ocorrer erro, executa o bloco abaixo (tratamento de erro)
    print(f'The result is {r:.2f}')
finally: #vai acontecer independente de ocorrer erro ou não
    print("Back soon!")