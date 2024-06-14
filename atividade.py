import time
import getpass
cadastros = []
print('✨Bem vindo ao projeto Fitness‼✨')
time.sleep(1)
print('Como é sua primeira vez, é hora de se cadastrar!😃')
time.sleep(1)
username = input('Qual será seu nome de usuário? ')
cadastros.append(username)
password = getpass.getpass('Qual será a sua senha? ')
cadastros.append(password)
email = input('Digite seu email aqui: ')
cadastros.append(email)
print('🎊🎉Cadastrado com sucesso!🎉🎊')
print("")
time.sleep(1)
print('Vamos fazer o login e ver se suas informações estão corretas!')
username_login = str(input('Digite seu nome de usuário: '))
password_login = getpass.getpass('digite sua senha: ')
if username_login == cadastros[0] and password_login == cadastros[1]:
    print('Login realizado com sucesso!')
    print("")
    time.sleep(1)

while True:
  print('Vamos decidir o que você quer fazer hoje. Escolha uma das opções a seguir:')
  escolha = int(input('Digite 1 para descobrir seu peso ideal \nDigite 2 para descobrir sugestões de comidas para uma boa dieta: '))
  print("")
  if escolha == 1:
      print('Boa! Vamos descobrir seu IMC hoje.🙂')
      time.sleep(1)
      print('O cálculo do IMC é feito dividindo o seu peso, em Kg, pela a sua altura, em metros, ao quadrado. Por isso, vamos precisar dessas informações:')
      peso = float(input('Digite seu peso em Kg: '))
      altura = float(input('Digite sua altura em metros: '))
      imc = peso / (altura * altura)
      print("")
      if imc < 18.5:
        print('Oops! Parece que seu IMC está abaixo do normal.')
        print('O ideal é você procurar algum nutricionista para te orientar a sair dessa.')
        print(f'Seu imc é de {imc:.2f} Kg/m²')
        print("")
        continue
      if imc >= 18.5 and imc <= 24.9:
        print('🎉Parabéns! Você está no peso ideal. Continue assim.🎉')
        print(f'Seu imc é de {imc:.2f} Kg/m²')
        print("")
        continue
      if imc >= 25 and imc <= 29.9:
        print('Oops! Parece que seu IMC está acima do normal.')
        print('O ideal é você procurar algum nutricionista para te orientar a sair dessa, você pode estar com sobrepeso.')
        print(f'Seu imc é de {imc:.2f} Kg/m²')
        print("")
        continue
      if imc >= 30:
        print('Oops! Parece que seu IMC está muito acima do normal.')
        print('O ideal é você procurar algum nutricionista para te orientar a sair dessa. Você pode estar com obesidade, o que necessita de acompanhamento.')
        print(f'Seu imc é de {imc:.2f} Kg/m²')
        print("")
        continue
      if 30 < imc:
        print('Oops! Parece que seu IMC está muito acima do normal.')
        print('É necessário acompanhamento urgente, pois você pod eestar com algum problema sério')
        print(f'Seu imc é de {imc:.2f} Kg/m²')
        print("")
        continue
  if escolha == 2:
    print('🥪Boa! Vamos descobrir as sugestões de comidas para uma boa dieta.🥗')
    time.sleep(1)
    print('Vamos fazer isso calculando sua taxa metabólica basal, conhecido como TMB.')
    time.sleep(1)
    print('Para isso, vamos precisar do seu sexo, já que ele é importante nesse cálculo')
    sexo = input('Digite a primeira letra do seu sexo em letras maiúsculas: ')
    if sexo == "F":
      print('Beleza! Agora, vamos precisar de algumas informações: ')
      time.sleep(1)
      idade = int(input('Digite sua idade: '))
      peso = float(input('Digite seu peso em Kg: '))
      altura = float(input('Digite sua altura em metros: '))
      tmb = 655 + (9.56 * peso) + (1.85 * altura) - (4.68 * idade)
      print(f'Sua TMB é de {tmb:.2f} kcal')
      print("")
      time.sleep(1)
      print('Agora que você já sabe seu TMB, é importante que você coma alimentos que não ultrapassem essa linha')
      time.sleep(1)
      print('Isso não significa parar de comer, pois esse não é o que uma dieta é. Encontre um equilíbrio entre comer o que goste e não ultrapassar as calorias🍉')
      time.sleep(1)
      print('Tenho aqui alguns exemplos de comidas com suas respectivas calorias, ❕mas você deve procurar um nutricionista para te recomendar algo❕')
      comidas = ['abacate', 'aveia', 'macarrão com brócolis', 'arroz', 'Lasanha de berinjela', 'Filé de peixe', 'couveflor', 'frango grelhado'  ]
      calorias = [160, 53, 298,64, 130, 76,9, 200, 25, 146]
      for i in range(len(comidas)):
        print(comidas[i], 'tem', calorias[i], 'kcal')
        print("")
      continue
    if sexo == "M":
      print('Beleza! Agora, vamos precisar de algumas informações:')
      time.sleep(1)
      idade = int(input('Digite sua idade: '))
      peso = float(input('Digite seu peso em Kg: '))
      altura = float(input('Digite sua altura em metros: '))
      tmb = 66 + (13.75 * peso) + (5 * altura) - (6.76 * idade)
      print(f'Sua TMB é de {tmb:.2f} kcal')
      time.sleep(1)
      print('Agora que você já sabe seu TMB, é importante que você coma alimentos que não ultrapassem essa linha')
      time.sleep(1)
      print('Isso não significa parar de comer, pois esse não é o que uma dieta é. Encontre um equilíbrio entre comer o que goste e não ultrapassar as calorias')
      time.sleep(1)
      print('Tenho aqui alguns exemplos de comidas com suas respectivas calorias, mas você deve procurar um nutricionista para te recomendar algo')
      comidas = ['abacate', 'aveia', 'macarrão com brócolis', 'arroz', 'Lasanha de berinjela', 'Filé de peixe', 'couveflor', 'frango grelhado'  ]
      calorias = [160, 53, 298,64, 130, 76,9, 200, 25, 146]
      for i in range(len(comidas)):
        print(comidas[i], 'tem', calorias[i], 'kcal')
        print("")
