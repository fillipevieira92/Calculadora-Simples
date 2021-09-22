def soma(a,b):
    adicao = a + b
    return adicao

def sub(a,b):
    sub = a - b
    return sub

def mult(a,b):
    mult = a * b
    return mult

def divs(a,b):
    divs = a / b
    return divs

def divint(a,b):
    divint = a // b
    return divint

def resto(a,b):
    resto = a % b
    return resto

def unar(a,b):
    unar = -a
    return unar

def potenc(a,b):
    potenc = a ** b
    return potenc

def abertura():
    print('###############')
    print('# CALCULADURA #')
    print('###############')
    print()
    print('+ = Somar')
    print('- = Subtrair')
    print('* = Multiplicar')
    print('/ = Dividir')
    print('// = Divisão inteira')
    print('A- = Negativar o primeiro número')
    print('** = Elevar o primeiro número ao segundo')
    print()
    a = int(input("Digite o primeiro número a ser calculado: "))
    print()
    escolha = input('Digite o símbolo referente a função que você deseja: ')
    print()
    b = int(input("Digite o segundo número: "))
    print("-----------------------------------------------------")
    

    if escolha == "+":
        SOMA = soma(a,b)
        print("A soma dos números é = {}".format(SOMA))
        print("-----------------------------------------------------")
        reboot = input('Deseja calcular novamente? [s/n]: ')
        print("-----------------------------------------------------")
        if reboot == "s":
            abertura()
        else:
            print('Até a próxima!')

    if escolha == "-":
        SUB = sub(a,b)
        print("A subtração dos números é = {}".format(SUB))
        print("-----------------------------------------------------")
        reboot = input('Deseja calcular novamente? [s/n]: ')
        print("-----------------------------------------------------")
        if reboot == "s":
            abertura()
        else:
            print('Até a próxima!')

    if escolha == "*":
        MULT = mult(a,b)
        print("A multiplicação dos números é = {}".format(MULT))
        print("-----------------------------------------------------")
        reboot = input('Deseja calcular novamente? [s/n]: ')
        print("-----------------------------------------------------")
        if reboot == "s":
            abertura()
        else:
            print('Até a próxima!')

    if escolha == "/":
        DIVS = divs(a,b)
        print("A divisão dos números é = {}".format(DIVS))
        print("-----------------------------------------------------")
        reboot = input('Deseja calcular novamente? [s/n]: ')
        print("-----------------------------------------------------")
        if reboot == "s":
            abertura()
        else:
            print('Até a próxima!')
        
    if escolha == "//":
        DIVINT = divint(a,b)
        print("A divisão inteira dos números é = {}".format(DIVINT))
        print("-----------------------------------------------------")
        reboot = input('Deseja calcular novamente? [s/n]: ')
        print("-----------------------------------------------------")
        if reboot == "s":
            abertura()
        else:
            print('Até a próxima!')

    if escolha == "A-":
        UNAR = unar(a,b)
        print("A negativação do número primeiro número é = {}".format(UNAR))
        print("-----------------------------------------------------")
        reboot = input('Deseja calcular novamente? [s/n]: ')
        print("-----------------------------------------------------")
        if reboot == "s":
            abertura()
        else:
            print('Até a próxima!')

    if escolha == "**":
        POTENC = potenc(a,b)
        print("A potenciação é = {}".format(POTENC))
        print("-----------------------------------------------------")
        reboot = input('Deseja calcular novamente? [s/n]: ')
        print("-----------------------------------------------------")
        if reboot == "s":
            abertura()
        else:
            print('Até a próxima!')
abertura()




