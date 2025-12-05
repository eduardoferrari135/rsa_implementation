# Guia de Uso

O projeto possui uma interface de linha de comando (CLI) definida em `main.py`. Ao executar o script, você terá duas opções principais.

## Fluxo Interativo

### 1. Encriptar Mensagem
Ao selecionar a opção `1`, o sistema irá:

1.  Solicitar o conteúdo a ser encriptado.
2.  Gerar um novo par de chaves RSA automaticamente.
3.  Salvar a chave (pública e privada) no arquivo `key.txt`.
4.  Exibir a mensagem cifrada (número inteiro).

```bash title="Exemplo de Saída"
Enter 1 to encrypt, 2 to decrypt: 1
Enter the content you want to encrypt: Olá Mundo
Enter the key.txt path (default: './key.txt'):
Key saved at $PATH.
Ciphered message: 123456789...
```

### 2. Decriptar Mensagem
Ao selecionar a opção 2, o sistema irá:

1. Solicitar o conteúdo cifrado (o número gerado no passo anterior).
2. Solicitar o caminho do arquivo de chave (padrão: ./key.txt).
3. Importar as chaves e realizar a decriptação.

!!! tip "Dica" Certifique-se de que o arquivo key.txt contém o campo d (chave privada) para que a decriptação funcione.

```bash
Enter 1 to encrypt, 2 to decrypt: 2
Enter the content you want to decipher: 123456789...
Enter the key.txt path (default: './key.txt'):
Deciphered message: Olá Mundo
```
