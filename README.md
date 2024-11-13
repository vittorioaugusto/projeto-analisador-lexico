# Analisador Léxico em Python

Este projeto implementa um Analisador Léxico em Python que identifica e classifica tokens em códigos de entrada. Ele reconhece palavras-chave, operadores, identificadores, números, strings, delimitadores, e espaços em branco, categorizando cada elemento para uma análise lexical inicial de código-fonte.

# Funcionalidades

- Identificação de Tokens: Identifica e classifica tokens como palavras-chave, operadores, identificadores, números, strings, delimitadores, espaços em branco e tokens desconhecidos.

- Compatível com Python: Reconhece palavras-chave e operadores da linguagem Python, incluindo suporte para async, await, e outras palavras-chave atualizadas.

- Detecção de Erros: Lança uma mensagem de erro quando um token inválido é encontrado, facilitando a depuração de código.

# Estrutura do Projeto

- TOKENS: Lista de tuplas contendo os tipos de tokens e seus padrões em expressões regulares.

- analisador_lexico(): Função principal que recebe o código de entrada e analisa os tokens, retornando uma lista de tokens classificados.

- processar_codigo(): Função que solicita ao usuário o código de entrada, executa a análise léxica e exibe o resultado, incluindo o número total de tokens.