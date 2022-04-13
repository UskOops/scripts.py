def write(text):
    size = len(text) + 4 #formatando o tamanho da borda texto
    print('~'*size)
    print(f'  {text}')
    print('~'*size)
write('Hello World')
write('This is a test')
write('This is another test')
write('and another')
