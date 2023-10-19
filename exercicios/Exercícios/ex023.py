#NOTAS DOS ALUNOS
nota_1 = float(input('1 nota: '))
nota_2 = float(input('2 nota: '))
media = (nota_1 + nota_2)/2

if media < 5.0:
    print('ALUNO \033[31mREPROVADO!\033[m')
    print('MÉDIA - \033[31m{:.2f}\033[m'.format(media))
elif media > 5.0 and media < 6.9:
    print('ALUNO APTO PARA \033[33mRECUPERAÇÃO\033[m')
    print('MÉDIA - \033[33m{:.2f}\033[m'.format(media))
elif media >= 7.0:
    print('ALUNO \033[32mAPROVADO!\033[m')
    print('MÉDIA - \033[32m{:.2f}\033[m'.format(media))
