def cifrar(texto: str, chave: str) -> str:
    """
    Cifra uma mensagem utilizando a Cifra de Transposição Colunar Simples.
    Muda a ordem dos caracteres escrevendo o texto em uma grade e lendo coluna por coluna.
    """
    # Valida se a chave foi fornecida
    if not chave:
        raise ValueError("A chave não pode ser vazia.")

    # Filtra a chave mantendo apenas letras em maiúsculas
    chave_limpa = [caractere.upper() for caractere in chave if caractere.isalpha()]
    if not chave_limpa:
        raise ValueError("A chave deve conter pelo menos uma letra do alfabeto.")

    num_colunas = len(chave_limpa)

    # Preenche o final da mensagem com espaços caso não complete a última linha (padding)
    resto = len(texto) % num_colunas
    if resto != 0:
        texto += " " * (num_colunas - resto)

    # Obtém a ordem de leitura das colunas com base na ordem alfabética da chave
    # O sorted do Python é estável, lidando perfeitamente com letras repetidas na chave
    ordem_colunas = sorted(range(num_colunas), key=lambda i: chave_limpa[i])

    resultado = []
    # Para cada coluna na ordem alfabética, lê todos os caracteres daquela coluna (de cima para baixo)
    for col in ordem_colunas:
        resultado.append(texto[col::num_colunas])

    # Junta o texto cifrado em uma única string
    return "".join(resultado)


def decifrar(texto: str, chave: str) -> str:
    """
    Decifra uma mensagem cifrada pela Cifra de Transposição Colunar Simples.
    Reconstrói a grade original coluna por coluna na ordem da chave e lê linha por linha.
    """
    # Valida se a chave foi fornecida
    if not chave:
        raise ValueError("A chave não pode ser vazia.")

    # Filtra a chave mantendo apenas letras em maiúsculas
    chave_limpa = [caractere.upper() for caractere in chave if caractere.isalpha()]
    if not chave_limpa:
        raise ValueError("A chave deve conter pelo menos uma letra do alfabeto.")

    num_colunas = len(chave_limpa)

    # Valida se o texto cifrado é compatível com a largura da grade
    if len(texto) % num_colunas != 0:
        raise ValueError("O texto cifrado é inválido para esta chave (tamanho incompatível).")

    num_linhas = len(texto) // num_colunas

    # Obtém a mesma ordem alfabética das colunas utilizada na cifragem
    ordem_colunas = sorted(range(num_colunas), key=lambda i: chave_limpa[i])

    # Reconstrói cada coluna da grade fatiando o texto cifrado na ordem em que foram lidas
    colunas = {}
    indice_leitura = 0
    for col in ordem_colunas:
        colunas[col] = texto[indice_leitura : indice_leitura + num_linhas]
        indice_leitura += num_linhas

    # Lê a grade linha por linha para recuperar a ordem original da mensagem
    resultado = []
    for linha in range(num_linhas):
        for col in range(num_colunas):
            resultado.append(colunas[col][linha])

    # Retorna o texto original reconstruído
    return "".join(resultado)