# Utilitários Matemáticos

O arquivo `utils.py` fornece as bases matemáticas para a segurança do RSA.

## Geração de Primos

A função `generate_prime(bits=1024)` utiliza o módulo `secrets` para gerar números aleatórios criptograficamente seguros e verifica a primalidade.

## Teste de primalidade

O algoritmo utilizado é o de Miller-Rabin, que baseia-se na propriedade de que $n-1$ pode ser fatorado como $2^r \cdot d$. O algoritmo verifica se a congruência de Fermat e as propriedades das raízes quadradas não triviais de 1 se mantêm para bases aleatórias.

### Passos Principais

1.  **Decomposição**: Escreve-se $n-1$ na forma $2^r \cdot d$, onde $d$ é ímpar, dividindo sucessivamente por 2.
2.  **Iterações (Rounds)**: Para cada rodada de teste $k$, escolhe-se uma base aleatória $a$ no intervalo $[2, n-2]$:
    * Calcula-se $x = a^d \pmod n$.
    * Se $x \equiv 1$ ou $x \equiv n-1$, a base $a$ não prova que $n$ é composto (continua para o próximo round).
    * Caso contrário, quadra-se $x$ sucessivamente ($x \leftarrow x^2 \pmod n$) até $r-1$ vezes:
        * Se $x$ tornar-se $n-1$, a base falha em provar que é composto (continua para o próximo round).
        * Se o loop terminar sem que $x$ atinja $n-1$, então $n$ é **definitivamente composto**.
3.  **Conclusão**: Se $n$ sobreviver a todos os $k$ rounds, é declarado **provavelmente primo**.

### Complexidade e Precisão

* **Complexidade**: $O(k \cdot \log^3 n)$.
* **Precisão**: A probabilidade de erro (falso positivo para um número composto) é de no máximo $4^{-k}$. Com $k=40$, essa probabilidade é infinitesimal.
Utilizamos o **Teste de Miller-Rabin** implementado na função `is_prime`.


## Algoritmo de Euclides (MDC)

O Algoritmo de Euclides é um método eficiente para calcular o **Máximo Divisor Comum (MDC)** entre dois números inteiros. É um dos algoritmos mais antigos ainda em uso comum.

### Lógica do Algoritmo

O método baseia-se no princípio de que o MDC de dois números não se altera se o maior número for substituído pelo resto da sua divisão pelo menor. Ou seja: 

$$
\gcd(a, b) = \gcd(b, a\pmod b)
$$

#### Execução

1.  **Iteração**: Enquanto o segundo valor ($b$) for diferente de zero.
2.  **Troca e Modulo**: Atualizam-se as variáveis simultaneamente:
    * $a$ assume o valor de $b$.
    * $b$ assume o valor do resto da divisão de $a$ por $b$.
3.  **Resultado**: Quando $b$ atingir 0, o valor contido em $a$ é o MDC.

