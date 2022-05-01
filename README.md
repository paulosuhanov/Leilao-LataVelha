# Leilão Lata Velha

Template para o projeto da AC de DevOps (Terceiro Semestre)

## Instruções

Este repositório é um template de um projeto do Leião  
O programa se chama `latavelha` e está organizado com pastas
e módulos, porém a maioria dos arquivos encontra-se vazio.

## Requisitos

Este template utiliza o gerenciador de pacotes **poetry**

### Se estiver rodando no Linux no seu ambiente local

`execute o comando abaixo para instalar o Poetry no Linux`

```bash
curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -
```

`Em outros ambientes pode instalar com`

```bash
pip install --user poetry
```

> No replit.com o poetry já está disponível e no gitpod será instalado assim que o ambiente iniciar.

## Instalando o ambiente

O comando a seguir instala as dependências do projeto.

```bash
poetry install
```

O comando a seguir ativa o ambiente virtual do poetry

```bash
poetry shell
```

> **IMPORTANTE** o ambiente precisa estar ativado para o programa executar.  
> No terminal aparecerá algo como  
> `(latavelha-DlEBh_72-py3.8) $`

Executando o programa

```bash
latavelha
# ou
python -m latavelha
```

Se apareceu `Hello from latavelha` então está tudo certo.


## Está com problemas com instalação ou autocomplete no gitpod?

### Poetry

Para o programa rodar o ambiente poetry precisa estar ativado

```
pip install poetry
poetry install
poetry shell
```

Ou execute `source start_poetry` que é um script que automatiza os comandos acima.

### Autocomplete não funciona?

Após ativar o poetry digite no terminal

```
which python 
```
A saida será algo como

```
/home/gitpod/.cache/pypoetry/virtualenvs/beerlog-DlEBh_72-py3.8/bin/python
```

Copie este path ^

Agora digite `F1` no gitpod ou `Ctrl + Shift + P` no Vscode local e selectione a opção `Python: Select Interpreter`
Cole o path `/home/gitpod/.cache/pypoetry/virtualenvs/latavelha-DlEBh_72-py3.8/bin/python` e digite enter.

> **OBS**: Pode ser que o caminho seja outro, o importante é terminar com `/bin/python`