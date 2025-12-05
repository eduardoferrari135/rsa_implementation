# Bem-vindo ao Projeto RSA

Este projeto é uma implementação **educacional** do algoritmo de criptografia RSA em Python. Ele permite a geração de chaves, encriptação e decriptação de mensagens de texto.

!!! warning "Aviso de Segurança"
    Esta é uma implementação didática. Para ambientes de produção, utilize bibliotecas criptográficas padrão e auditadas.

## Funcionalidades Principais

* **Geração de Chaves**: Criação de pares de chaves pública e privada com primos grandes gerados via teste de Miller-Rabin.
* **Persistência**: Exportação e importação de chaves em formato JSON/Base64.
* **CLI**: Interface de linha de comando interativa para facilitar o uso.

## Começando

Para rodar o projeto, clone o repositório e execute o arquivo principal:

```bash
git clone https://github.com/eduardoferrari135/rsa_implementation && cd rsa_implementation
python src/main.py 
```
