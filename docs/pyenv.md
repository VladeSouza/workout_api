# Pyenv [pt]

## Setup Pyenv Debian(derivados)

### 1. Garanta que todas dependências necessárias estão instaladas

```bash
sudo apt-get update; sudo apt-get install make build-essential libssl-dev zlib1g-dev \
libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm \
libncursesw5-dev xz-utils tk-dev libxml2-dev libxmlsec1-dev libffi-dev liblzma-dev
```

### 2. Baixe e execute o script de instalação

```bash
curl https://pyenv.run | bash
```

### 3. Adicione o seguinte script no arquivo `~/.bashrc`

```bash
# pyenv
export PATH="$HOME/.pyenv/bin:$PATH"
eval "$(pyenv init --path)"
eval "$(pyenv virtualenv-init -)"
```

### 4. Restart shell

### 5. Valide a instalação

```bash
pyenv --version
```

## Setup Pyenv Mac com homebrew

### 1. Atualize brew e instale as dependências necessárias

```bash
brew update
brew install openssl readline sqlite3 xz zlib
```

**1.1 Se estiver usando uma versão do Mojava ou mais antiga são necessárias outras dependências**

```bash
$ sudo installer -pkg /Library/Developer/CommandLineTools/Packages/macOS_SDK_headers_for_macOS_10.14.pkg -target /
```

### 2. Instale o Pyenv

```bash
brew install pyenv
```

### 3. Atualize o shell

```bash
echo -e 'if command -v pyenv 1>/dev/null 2>&1; then\n  eval "$(pyenv init -)"\nfi' >> ~/.bash_profile
exec "$SHELL"
```

## Comandos básicos

```bash
# lista as versões de python disponíveis
pyenv install -l

# instala uma versão
pyenv install <version>

# mostra versão instalada
pyenv global

# define uma versão
pyenv global <version>

# lista versões instaladas
pyenv versions
```

Author: @Vlademir F Souza 

Github: @VladeSouza

Linkedin: https://www.linkedin.com/in/vlademir-souza-ads