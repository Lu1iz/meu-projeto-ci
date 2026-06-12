import os


def somar(a, b):
    return a + b


def subtrair(a, b):
    return a - b


def obter_api_key():
    api_key = os.environ.get("MINHA_API_SECRET")
    if not api_key:
        raise ValueError(
            "A variável de ambiente MINHA_API_SECRET não foi definida."
        )
    return api_key


if __name__ == "__main__":
    print("Soma:", somar(3, 5))
    print("Subtração:", subtrair(10, 4))
    print("API Key carregada:", obter_api_key())
    