from mini_sistema_de_cadastro import funcoes

def gerarArquivo(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print('Ouve um erro ao tentar cria um arquivo.')
    else:
        print(f'{funcoes.cores[3]}-- Arquivo {nome} criado com sucesso! --{funcoes.cores[0]}')


def arquivoExiste(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def lerArquivo(nome):
    global a
    try:
        a = open(nome, 'rt')
    except:
        print('ERRO ao tentar ler o arquivo!')
    else:
        funcoes.cabecalho('PESSOAS CADASTRADAS')
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<40}{dado[1]:>3} anos')
    finally:
        a.close()


def AdcionarPessoa(arq, nome='<desconhecido>', idade=0):
    funcoes.cabecalho('CADASTRO DE NOVA PESSOA')
    try:
        a = open(arq, 'a')
    except:
        print('ERRO na abertura do arquivo.')
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except:
            print('Ouve um ERRO ao adcionar os dados.')
        else:
            print(f'Cadastro de {nome} efetuado com sucesso!')
            a.close()
