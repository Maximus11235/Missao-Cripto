# Descrição Detalhada da Implementação do Algoritmo DES

Este documento apresenta a especificação técnica e a documentação da implementação do algoritmo **DES (Data Encryption Standard)** desenvolvida na biblioteca Python do projeto, localizada no módulo `missao3/des.py`.

---

## 1. Visão Geral da Arquitetura

A implementação opera sobre **strings binárias** (sequências compostas por caracteres `'0'` e `'1'`), permitindo inspecionar diretamente a manipulação de bits exigida pelo padrão FIPS PUB 46-3.

O arquivo `missao3/des.py` está estruturado em quatro camadas funcionais:

```
┌─────────────────────────────────────────────────────────┐
│               Modos de Operação (Módulo 4)               │
│          (ECB, CBC, CFB, OFB - Encadeamento)            │
└────────────────────────────┬────────────────────────────┘
                             │
┌────────────────────────────▼────────────────────────────┐
│              Núcleo do DES (Módulo 3)                   │
│   (Permutação Inicial, Rede de Feistel e Função F)      │
└──────────────┬────────────────────────────┬─────────────┘
               │                            │
┌──────────────▼─────────────┐┌─────────────▼─────────────┐
│  Geração de Subchaves      ││  Operações Auxiliares     │
│  (Key Schedule - Módulo 2) ││  (Bitwise Helpers - Mod.1)│
└────────────────────────────┘└───────────────────────────┘

```

---

## 2. Operações de Manipulação de Bits (Módulo 1)

As funções auxiliares isolam os operadores primitivos necessários para transformar vetores binários.

### `aplicar_permutacao(bloco, tabela)`

Reordena e/ou redimensiona uma string de bits seguindo os índices definidos por uma matriz estática (como IP, $IP^{-1}$, PC-1, PC-2, E, P).

* **Entrada:** `bloco` (string de bits) e `tabela` (lista de inteiros indexada a partir de 1).


* **Mecânica:** Transforma o índice 1-based da especificação teórica no equivalente 0-based do Python (`i - 1`).



### `deslocamento_circular(bits, n)`

Executa a rotação circular à esquerda ($LS_i$) sobre as metades da chave ($C_i$ e $D_i$).

* **Entrada:** `bits` (string de 28 bits) e `n` (quantidade de posições: 1 ou 2).


* **Mecânica:** Realiza o fatiamento `bits[n:] + bits[:n]`, movendo os `n` bits mais significativos para o final.

### `operacao_xor(bits_a, bits_b)`

Computa o Ou-Exclusivo (soma módulo 2) entre duas strings de bits de mesmo comprimento.

* **Mecânica:** Compara caractere por caractere; resulta em `'1'` se os bits forem distintos e `'0'` se forem iguais.

### `formatar_binario(inteiro, tamanho)`

Converte o valor inteiro resultante das Caixas S em uma string binária de tamanho fixo de 4 bits.

---

## 3. Geração de Subchaves — Key Schedule (Módulo 2)

### `gerar_subchaves(chave_64bits)`

Prepara as 16 subchaves de 48 bits ($K_1$ a $K_{16}$) necessárias para cada rodada do algoritmo a partir da chave original de 64 bits.

```
Chave Original (64 bits)
          │
          ▼  (PC-1: Descarta 8 bits de paridade)
    Chave (56 bits)
     ┌────┴────┐
     ▼         ▼
  C0 (28b)  D0 (28b)
     │         │
 ┌───┴─────────┴───┐
 │   Para i = 1..16│ ──► LS_i (Rotaciona 1 ou 2 bits)
 └───┬─────────┬───┘
     ▼         ▼
  Ci (28b)  Di (28b)
     └────┬────┘
          ▼  (PC-2: Seleciona 48 bits)
       Subchave Ki (48 bits)

```

1. **Eliminação de Paridade (PC-1):** O vetor de 64 bits passa pela matriz `PC1`, descartando os bits 8, 16, 24, 32, 40, 48, 56 e 64, reduzindo o bloco para 56 bits úteis.


2. **Divisão:** A chave de 56 bits é dividida nas metades $C_0$ (28 bits superiores) e $D_0$ (28 bits inferiores).


3. **Ciclo de Rotação e Permutação PC-2:** Para cada uma das 16 rodadas:
* Aplica-se `deslocamento_circular` em $C$ e $D$ de acordo com o vetor `SHIFTS` (`1` bit nas rodadas 1, 2, 9 e 16; `2` bits nas demais).


* As metades rotacionadas são concatenadas e submetidas à permutação `PC2`, extraindo a subchave $K_i$ de 48 bits.





---

## 4. O Núcleo do DES (Módulo 3)

### `funcao_f(R, subchave)`

Processa a metade direita de 32 bits ($R_{i-1}$) em conjunto com a subchave $K_i$ da rodada.

```
       R_{i-1} (32 bits)
              │
              ▼  Expansão (E)
        E(R) (48 bits) ───⊕─── Subchave Ki (48 bits)
              │
              ▼
        Bloco de 48 bits
              │
  ┌───┬───┬───┼───┬───┬───┬───┐  (Divide em 8 blocos de 6 bits)
  ▼   ▼   ▼   ▼   ▼   ▼   ▼   ▼
 B1  B2  B3  B4  B5  B6  B7  B8
  │   │   │   │   │   │   │   │
  ▼   ▼   ▼   ▼   ▼   ▼   ▼   ▼
 S1  S2  S3  S4  S5  S6  S7  S8  (Substituição S-Box)
  │   │   │   │   │   │   │   │
  ▼   ▼   ▼   ▼   ▼   ▼   ▼   ▼
 C1  C2  C3  C4  C5  C6  C7  C8  (8 blocos de 4 bits = 32 bits)
              │
              ▼  Permutação (P)
         f(R, K) (32 bits)

```

1. **Expansão (E):** `aplicar_permutacao(R, E_BOX)` expande os 32 bits para 48 bits, duplicando 16 posições estáticas.


2. **Mistura:** `operacao_xor` combina os 48 bits expandidos com a subchave $K_i$ de 48 bits.


3. **Substituição (Caixas S):** O bloco de 48 bits é fatiado em 8 substrings de 6 bits ($B_1$ a $B_8$). Para cada fragmento $B_j = b_1b_2b_3b_4b_5b_6$:


* Linha $r$: bits $b_1b_6$ convertidos para decimal ($0 \le r \le 3$).


* Coluna $c$: bits $b_2b_3b_4b_5$ convertidos para decimal ($0 \le c \le 15$).


* O valor $S_j[r][c]$ é lido da matriz $S_j$ correspondente e convertido para 4 bits binários via `formatar_binario`.




4. **Permutação P:** A concatenação dos 32 bits oriundos das 8 Caixas S é reordenada pela matriz `P_BOX`.



### `processar_bloco_64bits(bloco, chave, decifrar=False)`

Executa o fluxo completo do algoritmo DES sobre um único bloco de 64 bits:

1. **Permutação Inicial (IP):** Submete o bloco de entrada de 64 bits à matriz `IP` e divide a saída em $L_0$ (32 bits) e $R_0$ (32 bits).


2. **Ordem das Subchaves:** Invoca `gerar_subchaves(chave)`. Caso `decifrar=True`, a lista de subchaves é invertida ($K_{16}, K_{15}, \dots, K_1$).


3. **Rede de Feistel (16 Rodadas):** Para $i = 1 \dots 16$:

$$L_i = R_{i-1}$$


$$R_i = L_{i-1} \oplus f(R_{i-1}, K_i)$$


4. **Troca Final (Swap) e Permutação Inversa ($IP^{-1}$):** Une as metades na ordem $R_{16}L_{16}$ e aplica `aplicar_permutacao(..., IP_INV)`, retornando o bloco de 64 bits transformado.



---

## 5. Modos de Operação em Bloco (Módulo 4)

Permitem aplicar o cifrador de bloco sobre mensagens de qualquer extensão divididas em blocos de 64 bits.

| Modo | Função de Cifragem | Função de Decifragem | Característica Principal |
| --- | --- | --- | --- |
| **ECB** (*Electronic Codebook*) | $C_n = \text{DES}(P_n, K)$ | $P_n = \text{DES}^{-1}(C_n, K)$ | Processamento independente de cada bloco.

 |
| **CBC** (*Cipher Block Chaining*) | $C_n = \text{DES}(P_n \oplus C_{n-1}, K)$ | $P_n = \text{DES}^{-1}(C_n, K) \oplus C_{n-1}$ | Encadeia os blocos usando XOR; exige Vetor de Inicialização ($IV = C_0$).

 |
| **CFB** (*Cipher Feedback*) | $C_n = P_n \oplus \text{DES}(R_{n-1}, K)$ | $P_n = C_n \oplus \text{DES}(R_{n-1}, K)$ | Converte o cifrador de bloco em cifrador de fluxo; a decifragem usa o modo de cifragem do DES.

 |
| **OFB** (*Output Feedback*) | $O_n = \text{DES}(O_{n-1}, K)$<br>

<br>$C_n = P_n \oplus O_n$ | $O_n = \text{DES}(O_{n-1}, K)$<br>

<br>$P_n = C_n \oplus O_n$ | Gera um fluxo de chaves independente do texto claro.

 |

### Funções Implementadas

* **`pad_texto(texto)`:** Aplica preenchimento com o caractere `'0'` até que o tamanho total da string binária seja um múltiplo exato de 64 bits.
* **`fragmentar(texto)`:** Divide o texto em uma lista de blocos de 64 bits.
* **`cifrar_ecb` / `decifrar_ecb`:** Processa cada bloco de 64 bits isoladamente por `processar_bloco_64bits`.


* **`cifrar_cbc` / `decifrar_cbc`:** Aplica a operação de XOR entre o bloco atual e o bloco cifrado anterior antes da cifragem (ou após a decifragem).


* **`cifrar_cfb` / `decifrar_cfb`:** Cifra o registrador de estado (iniciado pelo IV) e faz XOR com o bloco de texto.


* **`cifrar_ofb` / `decifrar_ofb`:** Atualiza o registrador cifrando-o sucessivamente, tornando a cifragem e a decifragem operações idênticas de XOR.