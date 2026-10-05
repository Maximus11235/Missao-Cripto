class StreamCipher:
    def __init__(self, key: bytes):
        """Inicializa o gerador de fluxo usando o Key-Scheduling Algorithm (KSA) do RC4."""
        self.S = list(range(256))
        j = 0
        for i in range(256):
            j = (j + self.S[i] + key[i % len(key)]) % 256
            self.S[i], self.S[j] = self.S[j], self.S[i]
            
        self.i = 0
        self.j = 0

    def _prga(self) -> int:
        """Pseudo-Random Generation Algorithm (PRGA) - Gera o próximo byte do keystream."""
        self.i = (self.i + 1) % 256
        self.j = (self.j + self.S[self.i]) % 256
        self.S[self.i], self.S[self.j] = self.S[self.j], self.S[self.i]
        
        K = self.S[(self.S[self.i] + self.S[self.j]) % 256]
        return K

    def process(self, data: bytes) -> bytes:
        """Cifra ou decifra os dados realizando a operação XOR com o keystream."""
        result = bytearray()
        for byte in data:
            keystream_byte = self._prga()
            result.append(byte ^ keystream_byte)
        return bytes(result)