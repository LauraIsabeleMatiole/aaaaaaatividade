

print ('💪projeto fitness🥗')

     print('Bem vindo!✨tela inicial✨')
     opcao = int (input('digite a opção que você deseja escolher (1: peso ideal, 2:, 3:  '))
 
    if opcao == (1):
      print('peso ideal')
    elif opcao == (2):
     print('lista de calorias dos doces!🍭')
     doces = ['chocolate','sorvete', 'bolo', 'jujubas', 'pão de mel', 'cookies', 'ovo de pascoa inteiro']
     calorias = [546, 207, 257, 375, 263, 502, 1500]
     for i, doces in enumerate(doces):
      print(f'{doces} tem {calorias[i]}')

