def imc (peso, altura):

    print("Calculadora de IMC.")

    imc = peso/(altura*altura)

    print("O seu imc é: %.2f" % imc)

    if(imc < 18.4):
        print("Abaixo do peso normal.")
    elif(imc > 18.5 and imc < 24.9):
        print("Peso normal.")
    elif(imc > 25.0 and imc < 29.9):
        print("Excesso de peso.")
    elif(imc > 30 and imc < 34.9):
        print("Obesidade Classe 1")
    elif(imc > 35 and imc < 39.9):
        print("Obesidade Classe 2")
    else:
        print("Obesidade Classe 3")