def exercicio2():
    num = int(input("Escolha um numero: "))
    a, b = 0, 1
    while b < num:
        a, b = b, a+b
    if b == num:
        print("O numero pertence a sequencia fibonacci")
    else:
        print("O numero nao pertence a sequencia fibonacci")

def exercicio3():
    faturamento = [
	{
		"dia": 1,
		"valor": 22174.1664
	},
	{
		"dia": 2,
		"valor": 24537.6698
	},
	{
		"dia": 3,
		"valor": 26139.6134
	},
	{
		"dia": 4,
		"valor": 0.0
	},
	{
		"dia": 5,
		"valor": 0.0
	},
	{
		"dia": 6,
		"valor": 26742.6612
	},
	{
		"dia": 7,
		"valor": 0.0
	},
	{
		"dia": 8,
		"valor": 42889.2258
	},
	{
		"dia": 9,
		"valor": 46251.174
	},
	{
		"dia": 10,
		"valor": 11191.4722
	},
	{
		"dia": 11,
		"valor": 0.0
	},
	{
		"dia": 12,
		"valor": 0.0
	},
	{
		"dia": 13,
		"valor": 3847.4823
	},
	{
		"dia": 14,
		"valor": 373.7838
	},
	{
		"dia": 15,
		"valor": 2659.7563
	},
	{
		"dia": 16,
		"valor": 48924.2448
	},
	{
		"dia": 17,
		"valor": 18419.2614
	},
	{
		"dia": 18,
		"valor": 0.0
	},
	{
		"dia": 19,
		"valor": 0.0
	},
	{
		"dia": 20,
		"valor": 35240.1826
	},
	{
		"dia": 21,
		"valor": 43829.1667
	},
	{
		"dia": 22,
		"valor": 18235.6852
	},
	{
		"dia": 23,
		"valor": 4355.0662
	},
	{
		"dia": 24,
		"valor": 13327.1025
	},
	{
		"dia": 25,
		"valor": 0.0
	},
	{
		"dia": 26,
		"valor": 0.0
	},
	{
		"dia": 27,
		"valor": 25681.8318
	},
	{
		"dia": 28,
		"valor": 1718.1221
	},
	{
		"dia": 29,
		"valor": 13220.495
	},
	{
		"dia": 30,
		"valor": 8414.61
	}
]
    soma = 0
    count = 0
    maior = 0
    diamaior = 0
    menor = 0
    diamenor = 0

    for i in faturamento:
        if i["valor"] != 0:
            soma += i["valor"]
            count += 1
        if i["valor"] > maior:
            maior = i["valor"]
            diamaior = i["dia"]
        if i["valor"] != 0:
            if i["valor"] < menor:
                menor = i["valor"]
                diamenor = i["dia"]

    media = soma/count
    diamedia = 0

    for i in faturamento:
        if i["valor"] > media:
            diamedia += 1

    print("Maior faturamento: dia: ", diamaior, " valor: ", maior)
    print("Menor faturamento: dia: ", diamenor, " valor: ", menor)
    print("Dias com faturamento superior a media: ", diamedia)

def exercicio4():
    faturamento = [
        {"estado" : "sp",
         "valor" : 67836.43},
        {"estado": "rj",
         "valor": 36678.66},
        {"estado": "mg",
         "valor": 29229.88},
        {"estado": "es",
         "valor": 27165.48},
        {"estado": "outros",
         "valor": 19849.53}
    ]
    total = 0
    media = 0

    for i in faturamento:
        total += i["valor"]
    for i in faturamento:
        media = i["valor"]/total * 100
        print("A media de ", i["estado"], " foi de ", media, "%")

def exercicio5():
    string = input("Insira uma string: ")
    invertido = string[::-1]
    print (invertido)


exercicio2()
print('')
exercicio3()
print('')
exercicio4()
print('')
exercicio5()
