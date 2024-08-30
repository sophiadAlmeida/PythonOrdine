n1 = int (input('Digite um valor: '))
n2 = int (input('Digite um valor: '))

def maior_numero(n1, n2):
    """Retorna o maior entre dois números."""
    if n1 > n2:
        return n1
    else:
        return n2

print('O maior numero é: {}'.format(maior_numero(n1, n2)))