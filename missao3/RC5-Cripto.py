"""RC5-w/r/b em Python puro (SecureDocs - Missão 3).
w = bits por palavra (16/32/64, bloco = 2w bits), r = rodadas, chave com b bytes."""
import os

# Constantes mágicas (P, Q) derivadas de e e da razão áurea
MAGIC = {16: (0xB7E1, 0x9E37), 32: (0xB7E15163, 0x9E3779B9),
         64: (0xB7E151628AED2A6B, 0x9E3779B97F4A7C15)}


class RC5:
    def __init__(self, chave: bytes, w=32, r=12):
        self.w, self.r = w, r
        self.mask = (1 << w) - 1
        self.u = w // 8                  # bytes por palavra
        self.bloco = 2 * self.u          # bytes por bloco
        self.S = self._expandir(chave)

    def _rotl(self, x, n):
        n %= self.w
        return ((x << n) | (x >> (self.w - n))) & self.mask

    def _rotr(self, x, n):
        n %= self.w
        return ((x >> n) | (x << (self.w - n))) & self.mask

    def _expandir(self, chave):
        """Expansão da chave: gera as t = 2(r+1) subchaves S[]."""
        m, u = self.mask, self.u
        c = max((len(chave) + u - 1) // u, 1)
        L = [0] * c
        for i in range(len(chave) - 1, -1, -1):          # chave -> palavras (little-endian)
            L[i // u] = ((L[i // u] << 8) + chave[i]) & m
        P, Q = MAGIC[self.w]
        t = 2 * (self.r + 1)
        S = [(P + i * Q) & m for i in range(t)]            # S[0]=P, S[i]=S[i-1]+Q
        i = j = A = B = 0
        for _ in range(3 * max(t, c)):                     # mistura chave e subchaves
            A = S[i] = self._rotl((S[i] + A + B) & m, 3)
            B = L[j] = self._rotl((L[j] + A + B) & m, A + B)
            i, j = (i + 1) % t, (j + 1) % c
        return S

    def cifrar_bloco(self, b: bytes) -> bytes:
        m, u, S = self.mask, self.u, self.S
        A = (int.from_bytes(b[:u], "little") + S[0]) & m
        B = (int.from_bytes(b[u:], "little") + S[1]) & m
        for i in range(1, self.r + 1):
            A = (self._rotl(A ^ B, B) + S[2 * i]) & m
            B = (self._rotl(B ^ A, A) + S[2 * i + 1]) & m
        return A.to_bytes(u, "little") + B.to_bytes(u, "little")

    def decifrar_bloco(self, b: bytes) -> bytes:
        m, u, S = self.mask, self.u, self.S
        A, B = int.from_bytes(b[:u], "little"), int.from_bytes(b[u:], "little")
        for i in range(self.r, 0, -1):
            B = self._rotr((B - S[2 * i + 1]) & m, A) ^ A
            A = self._rotr((A - S[2 * i]) & m, B) ^ B
        return ((A - S[0]) & m).to_bytes(u, "little") + ((B - S[1]) & m).to_bytes(u, "little")


# ---------- modo CBC + padding PKCS#7 (para cifrar arquivos de qualquer tamanho) ----------
def xor(a, b):
    return bytes(x ^ y for x, y in zip(a, b))


def cifrar(rc5: RC5, dados: bytes) -> bytes:
    """Retorna IV + texto cifrado."""
    n = rc5.bloco
    dados += bytes([n - len(dados) % n]) * (n - len(dados) % n)   # padding
    ant = iv = os.urandom(n)
    saida = [iv]
    for i in range(0, len(dados), n):
        ant = rc5.cifrar_bloco(xor(dados[i:i + n], ant))
        saida.append(ant)
    return b"".join(saida)


def decifrar(rc5: RC5, dados: bytes) -> bytes:
    n = rc5.bloco
    ant, saida = dados[:n], []
    for i in range(n, len(dados), n):
        bloco = dados[i:i + n]
        saida.append(xor(rc5.decifrar_bloco(bloco), ant))
        ant = bloco
    texto = b"".join(saida)
    return texto[:-texto[-1]]                                     # remove padding


def cifrar_arquivo(entrada, saida, chave, w=32, r=12):
    with open(entrada, "rb") as f, open(saida, "wb") as g:
        g.write(cifrar(RC5(chave, w, r), f.read()))


def decifrar_arquivo(entrada, saida, chave, w=32, r=12):
    with open(entrada, "rb") as f, open(saida, "wb") as g:
        g.write(decifrar(RC5(chave, w, r), f.read()))


# ---------- demonstração ----------
if __name__ == "__main__":
    # 1) Vetores de teste oficiais do artigo de Rivest (RC5-32/12/16): (chave, texto claro, cifrado)
    vetores = [
        ("00000000000000000000000000000000", "0000000000000000", "21A5DBEE154B8F6D"),
        ("915F4619BE41B2516355A50110A9CE91", "21A5DBEE154B8F6D", "F7C013AC5B2B8952"),
        ("783348E75AEB0F2FD7B169BB8DC16787", "F7C013AC5B2B8952", "2F42B3B70369FC92"),
        ("DC49DB1375A5584F6485B413B5F12BAF", "2F42B3B70369FC92", "65C178B284D197CC"),
        ("5269F149D41BA0152497574D7F153125", "65C178B284D197CC", "EB44E415DA319824"),
    ]
    print("=== Vetores de teste (Rivest) ===")
    for k, pt, ct in vetores:
        c = RC5(bytes.fromhex(k))
        ok = c.cifrar_bloco(bytes.fromhex(pt)).hex().upper() == ct and \
             c.decifrar_bloco(bytes.fromhex(ct)).hex().upper() == pt
        print(f"chave {k[:8]}... : {'OK' if ok else 'FALHOU'}")

    # 2) Experimento: original -> RC5 -> cifrado -> RC5 -> original
    print("\n=== Experimento com arquivo ===")
    with open("original.txt", "w", encoding="utf-8") as f:
        f.write("Contrato confidencial SecureDocs\nValor: R$ 1.000.000\n")
    chave = os.urandom(16)                       # chave de 128 bits
    print("Chave (hex):", chave.hex())
    cifrar_arquivo("original.txt", "cifrado.bin", chave)
    decifrar_arquivo("cifrado.bin", "recuperado.txt", chave)

    original = open("original.txt", "rb").read()
    cifrado = open("cifrado.bin", "rb").read()
    recuperado = open("recuperado.txt", "rb").read()
    print("Original  :", original.decode("utf-8").strip().replace("\n", " | "))
    print("Cifrado   :", cifrado.hex()[:64], "...")
    print("Recuperado:", recuperado.decode("utf-8").strip().replace("\n", " | "))
    print("Original == Recuperado ? ", original == recuperado)