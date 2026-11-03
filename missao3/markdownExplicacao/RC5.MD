# RC5 – Descrição e implementação (SecureDocs, Missão 3)

## 1. O que é

Cifra de bloco simétrica criada por Ronald Rivest em 1994. Seus parâmetros são ajustáveis, e por isso é escrita **RC5-w/r/b**:

| Parâmetro | Significado | Valores |
|-----------|-------------|---------|
| w | bits por palavra (bloco = 2w bits) | 16, 32 ou 64 |
| r | número de rodadas | 0 a 255 |
| b | tamanho da chave em bytes | 0 a 255 |

Configuração usada nos testes: **RC5-32/12/16** (bloco de 64 bits, 12 rodadas, chave de 128 bits).

Usa apenas três operações: soma módulo 2^w, XOR e **rotação dependente dos dados**. Essa rotação, cujo valor depende do conteúdo do outro meio bloco, é a fonte de não linearidade (no lugar das S-boxes do DES e do AES).

## 2. Algoritmo

Notação: `<<<` e `>>>` são rotações circulares, `⊕` é XOR, `+` e `−` são módulo 2^w.

**Constantes:** P e Q derivam de *e* e da razão áurea (32 bits: P = 0xB7E15163, Q = 0x9E3779B9).

**Expansão da chave** (gera t = 2(r+1) subchaves S[]):
1. converte a chave em palavras L[] (little-endian);
2. `S[0] = P` e `S[i] = S[i-1] + Q`;
3. repete 3·max(t, c) vezes (c = número de palavras da chave):
   `A = S[i] = (S[i] + A + B) <<< 3` e `B = L[j] = (L[j] + A + B) <<< (A + B)`.

**Cifragem** (bloco dividido em A e B):
```
A = A + S[0];  B = B + S[1]
para i = 1..r:
    A = ((A ⊕ B) <<< B) + S[2i]
    B = ((B ⊕ A) <<< A) + S[2i+1]
```

**Decifragem** (inverso, das rodadas finais para as iniciais):
```
para i = r..1:
    B = ((B − S[2i+1]) >>> A) ⊕ A
    A = ((A − S[2i])   >>> B) ⊕ B
B = B − S[1];  A = A − S[0]
```

## 3. Implementação (`rc5.py`, Python puro)

- `class RC5(chave, w, r)`: expande a chave no construtor e oferece `cifrar_bloco` e `decifrar_bloco`.
- **Modo CBC + padding PKCS#7** (`cifrar`, `decifrar`): permite cifrar arquivos de qualquer tamanho. Cada bloco sofre XOR com o cifrado anterior; o primeiro usa um **IV aleatório**, gravado no início do arquivo (`IV + cifrado`). Assim, blocos iguais não geram saídas iguais.
- `cifrar_arquivo` / `decifrar_arquivo`: aplicam o processo a arquivos.
- Ao executar `python rc5.py`, roda a demonstração completa.

## 4. Validação

- Os **5 vetores de teste do artigo de Rivest** (RC5-32/12/16) passaram na cifragem e na decifragem.
- Ida e volta em CBC testada com w = 16, 32 e 64.
- Experimento da missão: `original.txt → RC5 → cifrado.bin → RC5 → recuperado.txt`, com arquivos idênticos.

## 5. Segurança e comparação

- **Chave:** 128 bits inviabiliza a busca exaustiva (o DES, com 56 bits, já foi quebrado assim).
- **Bloco de 64 bits (RC5-32):** CBC fica vulnerável após cerca de 2^32 blocos com a mesma chave (ataque tipo Sweet32). O RC5-64 (bloco de 128 bits) evita isso.
- **Rodadas:** r = 12 é fraco contra criptoanálise diferencial (Biryukov e Kushilevitz, 1998); recomenda-se r ≥ 16.
- **Frente ao AES:** o AES é padrão NIST (FIPS 197), tem aceleração em hardware e muito mais análise pública. O RC5 é mais simples, mas menos estudado e não padronizado.

**Conclusão:** o RC5 com w = 64 e r ≥ 16 seria viável, mas para o SecureDocs o AES em modo autenticado (GCM) continua sendo a escolha mais forte e prática.