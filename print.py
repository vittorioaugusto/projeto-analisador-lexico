import re

TOKENS = [
    (
        "palavra_chave",
        r"\b(print|if|else|elif|while|for|break|continue|return|def|class|try|except|finally|import|from|as|with|pass|yield|lambda|assert|raise|del|global|nonlocal|True|False|None|and|or|not|is|in|async|await)\b",
    ),
    ("operador", r"[+\-*/%<>!=]=?|&&|\|\||!|\->|\.|:"),
    ("identificador", r"\b[a-zA-Z_][a-zA-Z0-9_]*\b"),
    ("numero", r"\d+(\.\d*)?"),
    ("string", r'"[^"]*"|\'[^\']*\''),
    ("delimitador", r'[\'"\(\)\[\]\{\},;:.]'),
    ("espacos", r"[ \t]+"),
    ("desconhecido", r"."),
]

def analisador_lexico(code):
    tokens = []
    position = 0

    while position < len(code):
        match = None
        for token_type, pattern in TOKENS:
            regex = re.compile(pattern)
            match = regex.match(code, position)
            if match:
                if token_type != "WHITESPACE" and token_type != "COMMENT":
                    tokens.append((token_type, match.group(0)))
                position = match.end(0)
                break

        if not match:
            raise SyntaxError(f"Token inválido: {code[position]}")

    return tokens

def processar_codigo():
    code = input("Digite o código para análise: ").strip()
    try:
        tokens = analisador_lexico(code)
        print("Resultados:")
        for token_type, token_value in tokens:
            print(f"Tipo: {token_type}, Valor: {token_value}")
        print(f"\nTotal de tokens: {len(tokens)}")
    except SyntaxError as e:
        print(f"Erro de Sintaxe: {e}")

processar_codigo()
