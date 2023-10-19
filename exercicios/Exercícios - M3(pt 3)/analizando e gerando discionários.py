def notas(*n, sit=False):
    """
    -> Verifica notas, dando a média, maior e menor nota.
    :param n: notas a serem cadastradas (aceita várias)
    :param situação: mostra a situação do aluno (opcional)
    :return: discionário com várias informações sobre a situação da turma.
    """
    #s = 0
    lista = dict()
    #numeros = list(n)
    lista['Quantidade de notas'] = len(n)
    lista['Mior'] = max(n)
    lista['Menor'] = min(n)

    #for c in numeros:
        #s += c

    lista['Média'] = sum(n) / len(n)

    if sit == True:
        if lista['Média'] < 6:
            lista['Situação'] = 'RUIM'
        elif lista['Média'] >= 6 and lista['Média'] < 7:
            lista['Situação'] ='RAZOÁVEL'
        else:
            lista['Situação'] = 'BOA'
    return lista

resposta = notas(10.0, 8.0, 6.5, 7.5, sit=True)
print(resposta)
#help(notas)
