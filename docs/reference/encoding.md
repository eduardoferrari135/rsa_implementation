# Codificação de Texto

O arquivo `encoding.py` trata a conversão entre texto legível e números inteiros processáveis pelo RSA.

Esta implementação trata a string como um número em **base 256**.

## Funções

### `encode(text: str) -> int`

Itera sobre cada caractere da string, pegando seu valor ASCII (`ord(c)`) e acumulando no resultado:

$$
\text{final_message} = \text{final_message} \cdot 256 + \text{ASCII}(c)
$$

### `decode(number: int) -> str`

Realiza o processo inverso, extraindo o resto da divisão por 256 repetidamente para recuperar os bytes originais.
