import  math

TamTab = int(input("Digite quantos valores tem a tabela: \n"))
Media = float(input("Qual a media? \n"))
DP = 0

for i in range(TamTab):
    calc = int(input("Digite o valor: \n"))
    x = (calc-Media)**2
    DP = x + DP
    print("Ok, o proximo agora.\n")

s = math.sqrt(DP/TamTab)
print("O valor é igual a: \n")
print(s)
