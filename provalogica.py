login = "lucas123"
senha = "12345"
contador_tentativa = 0




while contador_tentativa < 3:
        UserLogin = input('digite seu login:')
        UserPass = input('digite sua senha:')
        if UserLogin != login or UserPass != senha:
       
            print('Seu login ou senha estão errados')
        
            print(f'Você só tem  {2 - contador_tentativa} chance(s)')
            contador_tentativa +=1
        else:
            print('Seja bem vindo, login bem sucedido.')
            break


if contador_tentativa == 3:
        for tentativa in range(3):
              print("--------------------------")
              print('Acesso bloqueado')
              print('--------------------------')
  
