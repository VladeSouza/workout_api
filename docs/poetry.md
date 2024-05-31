# Poetry [pt]

## Setup Poetry

### 1. Instalação Oficial: 
LinK: https://python-poetry.org/docs/#installing-with-the-official-installer
```bash
curl -sSL https://install.python-poetry.org | python3 -

```

### 2. Instalação Usando Pipx :
Links:
- Pipx: https://pipx.pypa.io/stable/installation/
- Poetry: https://python-poetry.org/docs/#installing-with-pipx
```bash
python3 -m pip install --user pipx
python3 -m pipx ensurepath
sudo pipx ensurepath --global      # Opcional para deixar o pipx no escopo global
pipx install poetry                # Instala o Poetry caso opcional avançado com versão use pipx install poetry==1.2.0
pipx upgrade poetry                # Atualiza o Poetry
pipx uninstall poetry              # Desinstala o Poetry
```

### 3. Adicione o seguinte script no arquivo `~/.bashrc`

```bash
# Poetry
export PATH="/home/MEU_USUARIO/.local/bin:$PATH" # OBS. Use seu nome de usuario
```

### 4. Restart shell

### 5. Valide a instalação

```bash
poetry --version
poetry
```


## Comandos básicos
Link: https://python-poetry.org/docs/cli/
```bash
# Criar projeto
poetry new <nome_projeto>

# Ative o poetry em um projeto pré-existente
cd projeto_pré-existente
proetry init

# Abra como ambiente virtual
poetry shell

# Adicione as dependencias
poetry install
poetry add <dependencias> #Ex. poetry add fastapi uvicorn httpx 

# Adicione as dependencias de desenvolvimento
poetry add --group dev  #Adiciona um grupo como dev EX. poetry add --group dev pytest 
poetry add <--dev ou -D> <dependencia(s)> #
#Ex. poetry add -D pytest pytest-cov taskipy ruff httpx ipython

# Use o poetry para definir o caminho do ambiente virtual para interpretador de execução 
poetry env info -p
#OBS usando o VSCODE Ctrl + Shift + p e digita "Python: selector Interpreter" e cole o caminho Ex./home/meu_usuario/.cache/pypoetry/virtualenvs/workout-api-LbMsNJsC-py3.11

# Remover dependencias
poetry remove <dependencia>

# Mostra detalhes de dependencias
poetry show <dependencia>
```



Author: @Vlademir F Souza 

Github: @VladeSouza

Linkedin: https://www.linkedin.com/in/vlademir-souza-ads