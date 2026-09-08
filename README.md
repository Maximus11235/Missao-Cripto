# Missão Cripto

Biblioteca educacional de funções matemáticas utilizadas em criptografia.

## Configuração no Windows

Instale o [Python](https://www.python.org/downloads/) e marque a opção
**Add Python to PATH** durante a instalação. Em seguida, execute no PowerShell:

```powershell
git clone https://github.com/Maximus11235/Missao-Cripto.git
cd Missao-Cripto
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -e .
```

Se o PowerShell impedir a ativação, libere scripts locais apenas para o seu
usuário e tente novamente:

```powershell
Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned
.\.venv\Scripts\Activate.ps1
```

No Prompt de Comando (`cmd.exe`), a ativação é feita com:

```bat
.venv\Scripts\activate.bat
```

## Rotina para desenvolver uma funcionalidade

Antes de começar, atualize a `main` e crie uma branch com um nome descritivo:

```powershell
git switch main
git pull origin main
git switch -c feature/nome-da-funcionalidade
```

Depois de alterar e testar os arquivos:

```powershell
git status
git add funcoes/SeuArquivo.py
git commit -m "feat: descreva a funcionalidade"
git push -u origin feature/nome-da-funcionalidade
```

Por fim, abra o repositório no GitHub e clique em **Compare & pull request**.
