# Módulo RSA

O arquivo `rsa.py` contém a lógica central da criptografia.

## Classe `RSAKey`

Responsável por armazenar e manipular as chaves.

| Atributo | Descrição |
| :--- | :--- |
| `n` | O módulo (produto de $p$ e $q$). |
| `e` | O expoente público (padrão: 65537). |
| `d` | O expoente privado (calculado via inverso modular). Opcional. |

### Métodos Principais

* **`export_key()`**: Serializa a chave em um JSON codificado em Base64.
* **`import_key(key_str)`**: Reconstrói a instância `RSAKey` a partir da string Base64 exportada.

## Classe `RSA`

Métodos estáticos para operações criptográficas.

=== "Geração de Chaves"
    ```python
    key_pair = RSA.generate_keys()
    ```
    Gera primos $p$ e $q$, calcula $\phi(n)$ e determina $e$ e $d$.

=== "Encriptação"
    ```python
    ciphered = RSA.encrypt("Mensagem", key_pair)
    ```
    Converte a string para inteiro e aplica $c = m^e \pmod n$.

=== "Decriptação"

    ```python
    plaintext = RSA.decrypt(ciphered, key_pair)
    ```
    Aplica $m = c^d \pmod n$ e converte o obtem o inteiro decifrado.

    <br>


    ```python
    plaintext = RSA.decrypt_and_decode(ciphered, key_pair)
    ```
    Aplica $m = c^d \pmod n$ e converte o inteiro de volta para string.
    
