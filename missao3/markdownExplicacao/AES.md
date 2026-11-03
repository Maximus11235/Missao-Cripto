# Algoritmo de Criptografia AES-128 (Advanced Encryption Standard)

Este documento apresenta uma visão detalhada do funcionamento do algoritmo **AES-128**, implementado como parte de um estudo prático de criptografia simétrica.

##  Visão Geral do AES-128
O **AES (Advanced Encryption Standard)** é um algoritmo de cifragem em bloco simétrico adotado globalmente para proteger dados confidenciais. A especificação **AES-128** utiliza:
* **Tamanho do bloco:** 16 bytes (128 bits).
* **Tamanho da chave:** 16 bytes (128 bits).
* **Número de rodadas (rounds):** 10 rodadas de processamento.

---

## Arquitetura e Funcionamento do Código

O algoritmo opera transformando uma matriz de estado de 4x4 bytes (chamada de *State*) através de quatro transformações principais distribuídas ao longo das rodadas.

### 1. Tratamento de Dados e Estrutura
* **`padding(mensagem)`**: Garante que o tamanho da mensagem seja um múltiplo exato de 16 bytes utilizando o padrão **PKCS#7**. Se faltarem 3 bytes, por exemplo, o valor `0x03` é replicado 3 vezes ao final do bloco.
* **`slice(padded)`**: Organiza o fluxo linear de bytes em matrizes bidimensionais 4x4 (*States*), ordenadas por colunas.

### 2. Funções de Rodada (Round Functions)
* **`subbyte(state)`**: Camada de confusão não-linear. Substitui cada byte do *State* por outro byte correspondente mapeado a partir de uma tabela estática conhecida como **SBOX**.
* **`shiftrows(state)`**: Camada de difusão linear. Desloca as linhas da matriz para a esquerda de forma cíclica: a linha 0 não se desloca, a linha 1 desloca 1 byte, a linha 2 desloca 2 bytes e a linha 3 desloca 3 bytes.
* **`mix_columns(state)`**: Multiplicação matricial operada no Campo de Galois GF(2^8) usando a função auxiliar **`gmull`**. Esta etapa mistura as informações de cada coluna, garantindo alta difusão.
* **`round_key(state, subkey)`**: Aplica uma operação XOR bit a bit entre o *State* atual e a chave da rodada específica (*Subkey*).

### 3. Expansão de Chave (`expand_key`)
A chave original de 128 bits é expandida usando o vetor **RCON** e a **SBOX** para gerar **11 subchaves** distintas (uma para o Round Inicial 0 e dez para as rodadas seguintes).

---

## 🔄 Fluxo de Execução por Bloco

A criptografia de cada bloco de 16 bytes segue estritamente a sequência descrita abaixo:

```text
[Dados Originais] ──> Padding (PKCS#7) ──> Criação do State (4x4)
                                  │
                                  ▼
                        ┌──────────────────┐
                        │    ROUND 0       │ ──> AddRoundKey (Chave 0)
                        └──────────────────┘
                                  │
                                  ▼
                        ┌──────────────────┐
                        │   ROUNDS 1 a 9   │ ──> SubBytes ──> ShiftRows ──> MixColumns ──> AddRoundKey
                        └──────────────────┘
                                  │
                                  ▼
                        ┌──────────────────┐
                        │    ROUND 10      │ ──> SubBytes ──> ShiftRows ──> AddRoundKey (Sem MixColumns)
                        └──────────────────┘
                                  │
                                  ▼
                           [Texto Cifrado]
```

---

## 📂 Extensão: Manipulação de Arquivos
A função integrada **`criptografar_arquivo`** mapeia este ecossistema para o armazenamento em disco:
1. Abre o arquivo desejado no modo de leitura binária (`rb`).
2. Transmite a cadeia de bytes pura para o motor do AES-128.
3. Salva a resposta cifrada em um novo arquivo com o modo de escrita binária (`wb`), preservando a integridade estrutural de qualquer formato (imagens, executáveis ou textos).
