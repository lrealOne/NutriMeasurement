# Dados para Analise:

# Dados pessoais:
class Pessoa:
    def __init__(self):
        self.nome = ""
        self.sexo = ""
        self.idade = 0
        self.peso = 0
        self.altura = 0
        self.imc = 0
        self.meta = ""
        self.tmc = ""
        self.tmc_real = 0

    def __str__(self):
        return f"Nome: {self.nome}\nSexo: {self.sexo}\nIdade: {self.idade}\nPeso: {self.peso} kg\nAltura: {self.altura} m\nIMC: {self.imc:.2f}\nMeta: {self.meta}"

# Definindo IMC = peso / (altura x altura)
# imc < 18.5 = Magreza
# imc >= 18.5 and imc <= 24.9 = Normal
# imc > 24.9 and imc <= 29.9 = Sobrepeso
# imc > 29.9 and imc <= 39.9 = Obesidade
# imc > 40.0 = Obesidade grave

def calcular_imc(x: float, y: float) -> float:
    # A fórmula do IMC é: peso / (altura * altura)
    return x / (y ** 2)

def validarNome(nome):
    nome = nome.strip()  # Remove espaços extras
    if not nome.isalpha():  # Verifica se o nome contém apenas letras
        raise ValueError("O nome deve conter apenas letras e não pode ser vazio.")
    return nome  
    
    
def validarIdade(idade):
    idade = idade.strip()
    idades_invalidas = [0, ""]
    if int(idade) and idade not in idades_invalidas:
        return idade 
    
def validarMedidas(medida):
    medida = medida.strip()  
    medidas_invalidas = [0, ""]

    try:
        medida_float = float(medida)
    except ValueError:
        return None

    if medida_float not in medidas_invalidas and medida:
        return medida
    else:
        return None
    
def define_meta():
    meta = input("Qual a sua meta?\n 1 Emagrecer\n2 Engordar\n")
    values = ['1', '2']
    if meta in values:
        return meta
    else:
        return None
    

# Dados nutricionais
class Nutricao:
    def __init__(self):
        self.verduras_e_legumes = True
        self.frutas = True
        self.carne_bovina = True
        self.carne_branca = True
        self.frutos_do_mar = True
        self.preferencias = []
        self.exclusao = []

def gosta(meta):
    values = ['1', '2']
    if meta in values:
        return meta
    else:
        return None

# Informações consideraveis

# Calcular a taxa metabolica basal:
# 66 + (13,8 x peso em kg) + (5 x altura em cm) - (6,8 x idade em anos)

def TMB(pessoa):
    if pessoa.sexo == 'masculino':
        return 88.36 + (13.4 * pessoa.peso) + (4.8 * pessoa.altura) - (5.7 * int(pessoa.idade))
    else:
        return 447.6 + (9.2 * pessoa.peso) + (3.1 * pessoa.altura) - (4.3 * int(pessoa.idade))
    
# Verificar atividade fisica:

# Sedentário – Pouco ou nenhum exercício diário: Multiplique sua TMB por 1,20;
# Levemente Ativo – (Exercício leve/1 a 3 dias na semana): Multiplique sua TMB por 1,37;
# Moderadamente Ativo – (Exercício moderado/ 3 a 5 dias na semana): Multiplique sua TMB por 1,55;
# Bastante Ativo – (Exercício pesado 6 a 7 dias na semana): Multiplique sua TMB por 1,72;
# Muito Ativo (Exercício pesado todos dias da semana ou treinos 2x ao dia): Multiplique sua TMB por 1,90.

def rotina(tmb, exe):
    match exe:
        case "Sedentário":
            return tmb * 1.20
        case "Levemente ativo":
            return tmb * 1.37
        case "Moderadamente ativo":
            return tmb * 1.55
        case "Bastante ativo":
            return tmb * 1.72
        case "Muito ativo":
            return tmb * 1.90
        
def check_num(choice):
    numbers = ['1', '2', '3', '4', '5']
    if choice in numbers:
        return choice
    else:
        return None 
    


    