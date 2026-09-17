# Escreva um algoritmo em Python em que o usuário escolhe se quer comprar maçãs, laranjas ou bananas. 
# Deverá ser apresentado na tela um menu com as opções: 1 para maçã, 2 para laranja e 3 para banana

# Menuzinho
print("==============================")
print(" FRUTARIA LETTUCE DO NELSINHO ")
print("==============================")
print("Escolha qual fruta você quer comprar:")
print("1 - Maçã R$: 2,50 kg")
print("2 - Laranja R$: 1,80 kg")
print("3 - Banana R$: 1,20 kg")

# O banco de dados/"dicionário"
produtos = {
    1: ["Maçã", 2.50],
    2: ["Laranja", 1.80],
    3: ["Banana", 1.20]
}
# A cada repetição do for, a variável codigo segura o número da posição, e a variável info pega a pasta com a fruta e o preço
for codigo, info in produtos.items():
    print(f"{codigo} - {info[0]} R$: {info[1]:.2f} / kg")

print("------------------------------")
escolha = int(input("Qual fruta você quer comprar? (1, 2 ou 3): "))

# Verifica se o usuário digitou um número válido nos produtos
if escolha in produtos:

    # Buscando o nome e preço por kg da fruta de acordo com o código/número dela
    nome_fruta = produtos[escolha][0]
    preco_kg = produtos[escolha][1]
    
    # Pergunta a quantidade em kg (float porque pode ser números quebrados)
    peso = float(input(f"Quantos quilos de {nome_fruta} você quer? "))
    
    # Cálculo final
    total_pagar = peso * preco_kg
    
    print("------------------------------")
    print(f"Você comprou {peso:.2k}kg de {nome_fruta}(s)!")
    print(f"O total da sua compra deu R$: {total_pagar:.2f}")
else:
    print("------------------------------")
    print("Opção inválida! Produto não encontrado no sistema.")