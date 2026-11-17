def verificar_numero(numero):
    if not isinstance(numero, int):
        raise TypeError("é aceito apenas número")
    if numero % 2 == 0:
        return("Par")
    else:
        return("Impar")