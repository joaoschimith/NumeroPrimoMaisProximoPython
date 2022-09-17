def maiorPrimo(num):
    for num in reversed(range(1,num+1)):
        if all (num%i!=0 for i in range(2,num)):
            return num
n=int(input("Digite o valor de n>= 2."))#100

print(maiorPrimo(n))#97

// Para calcular o número primo mais próximmo do número digitado do usuário 