import  math

TamTab = int(input("Digite quantos valores tem a tabela: \n"))
Media = float(input("Qual a media? \n"))
DP = 0

for i in range(TamTab):
    calc = float(input("Digite o valor: "))
    x = (calc-Media)**2
    print("O valor deste calculo é: ")
    print(x)
    DP = x + DP
    print("\nOk, o proximo agora.")

print(DP)
s = math.sqrt(DP/TamTab)
print("\nO desvio padrão é igual a: ")
print(s)
