from personal import *;
import os
## Calcular IMC, recomendar deficit ou superavit calorico 
## Recomendar alimentação baseando-se na meta pessoal.
pessoa = Pessoa()
while True:
    print("Bem vindo!!\n Antes de começar preciso de algumas informações sobre você.")
    while True:
        try:
            nome = input("Como devo te chamar?: ").capitalize()
            validarNome(nome)
            pessoa.nome = nome
            break
        except ValueError: 
            print("Nome invalido. Tente novamente")

    print(f"Ótimo, {pessoa.nome}.")

    while True:
        sexo = input("Qual o seu sexo?\n 1 - Masculino\n 2 - Feminino\n R: ")
        teste = gosta(sexo)
        if teste is None:
            print("Resposta invalida. Tente novamente") 
        else:
            if sexo == "1":
                pessoa.sexo = "Masculino"
            else: 
                pessoa.sexo = "Feminino"
            break

    while True:
        try:
            idade = input("Sua idade: ")
            validarIdade(idade)
            pessoa.idade = idade
            break
        except ValueError:
            print("Digite uma idade válida.")

    while True:
        try:
            peso = input("Digite agora o seu peso: ")  
            peso_validado = validarMedidas(peso)
            if peso_validado is None:
                print("Peso inválido. Por favor, digite um peso válido.")
            else:
                pessoa.peso = float(peso_validado)
                break 
        except ValueError:
            print("Peso inválido. Por favor, digite um peso válido.")

    while True:
        try:
            altura = input("Digite agora a sua altura: ")  
            altura_validada = validarMedidas(altura)
            if altura_validada is None:
                print("Altura inválido. Por favor, digite um altura válido.")
            else:
                pessoa.altura = float(altura_validada)
                break 
        except ValueError:
            print("Altura inválido. Por favor, digite um peso válido.")
    print(pessoa.peso, pessoa.altura)
    pessoa.imc = calcular_imc(float(peso), float(altura))

    while True:
        meta = define_meta()
        if meta is None:
            print("Digite uma meta válida. Tente novamente.")
        else:
            if meta == "1":
                pessoa.meta = "Emagrecer"      
            else:
                pessoa.meta = "Engordar"
            break
    break  

print(f"Seu imc:{pessoa.imc:.2f}")

print("Certo, estamos quase lá!!\n")
print("Agora preciso saber com que frequencia voce costuma realizar atividade fisica:")
freq_atividade = ""
while True:
    atividade_fisica = input("1. Sedentário - Pouco ou nenhum exercício diário\n2. Levemente ativo - Exercício leve 1 a 3 dias na semana\n3. Exercício moderado 3 a 5 dias na semana\n4. Exercício pesado 6 a 7 dias na semana\n5. Exercício pesado todos dias da semana ou treinos 2x ao dia")
    lista_opcoes = ["Sedentário", "Levemente ativo", "Exercício moderado", "Exercício pesado", "Exercício pesado"]
    teste = check_num(atividade_fisica)
    if teste is None:
        print("Opção inválida. Tente novamente") 
    else:
        atividade_fisica = int(atividade_fisica) 
        freq_atividade = lista_opcoes[atividade_fisica - 1]
        break

pessoa.tmb = TMB(pessoa)
print(pessoa.tmb)
tmb_aprox = rotina(pessoa.tmb, freq_atividade)
pessoa.tmb = tmb_aprox
print(pessoa.tmb)
        

print(f"\nCerto {pessoa.nome}! Agora preciso de algumas informações sobre sua alimentação:")

info_nutricao = Nutricao()
while True:
    while True:
        verduras_legumes = input("Você gosta de legumes e verduras?\n 1 - SIM\n 2 - NÃO\n R: ")
        teste = gosta(verduras_legumes)
        if teste is None:
            print("Resposta invalida. Tente novamente") 
        else:
            info_nutricao.verduras_e_legumes = verduras_legumes
            break

    while True:
        frutas = input("Você gosta de frutas?\n 1 - SIM\n 2 - NÃO\n R: ")
        teste = gosta(frutas)
        if teste is None:
            print("Resposta invalida. Tente novamente") 
        else:
            info_nutricao.frutas = frutas
            break

    while True:
        carne_bovina = input("Você gosta de carne bovina?\n 1 - SIM\n 2 - NÃO\n R: ")
        teste = gosta(carne_bovina)
        if teste is None:
            print("Resposta inválida. Tente novamente") 
        else:
            info_nutricao.carne_bovina = carne_bovina
            break

    while True:
        carne_branca = input("Você gosta de carne branca(frango, peru, galinha)?\n 1 - SIM\n 2 - NÃO\n R: ")
        teste = gosta(carne_branca)
        if teste is None:
            print("Resposta inválida. Tente novamente") 
        else:
            info_nutricao.carne_branca = carne_branca
            break

    while True:
        frutos_do_mar = input("Você gosta de frutos do mar?\n 1 - SIM\n 2 - NÃO\n R: ")
        teste = gosta(frutos_do_mar)
        if teste is None:
            print("Resposta inválida. Tente novamente") 
        else:
            info_nutricao.frutos_do_mar = frutos_do_mar
            break

    print("Certo. Estamos quase lá")
    print("Agora preciso que me informe as coisas que você mais gosta de comer, separados por virgula.")

    while True:
            preferencias = input('Ex:(Arroz, feijão, carne, farofa...)\nR: ').replace(", ", ",")
            if not all(item.isalpha() for item in preferencias.split(",")):
                print("Digite apenas letras.")
            else:
                info_nutricao.preferencias = preferencias.split(",")
                print("Certo.")
                break

    print("Agora preciso que me informe as coisas que você não gosta, separados por virgula")
    while True:
        exclusoes = input("Ex:(Carne de porco, brocolis...)\nR: ").replace(", ", ",")
        if not all(item.isalpha() for item in exclusoes.split(",")):
                print("Digite apenas letras.")
        else:
            info_nutricao.exclusao = exclusoes.split(",")
            print("Certo.")
            break
    break




