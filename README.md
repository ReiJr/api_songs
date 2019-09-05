# API Songs

## API Flask 
Dado um artista retorna 10 músicas mais populares.

Pré-requisitos:
- Python 2.7
- Pip
- Flask
- Pytest
- Requests

Para instalações dos pré-requisitos executem os seguintes comandos:

### Instalação do Python
- Ubuntu
`$ apt-get install python`

- Windows

https://www.python.org/ftp/python/2.7.16/python-2.7.16.msi


1. Abra o painel de controle e navegue até as configurações de sistema
2. Selecione as configurações avançadas do sistema
3. Clique em variáveis de ambiente
4. Procure nas variáveis do sistema pela variável Path
5. Clique em editar
6. Verifique se os valores C:\Python27 e C:\Python26\Scripts existem no campo de valor da variável, caso não exista adicione ao final dos valores separando cada valor com ;. 
7. Clique em OK
### Instalação do Pip
- Ubuntu
`$ apt-get install python-pip`

- Windows


### Instalação do Flask
- Ubuntu
`$ pip install -U Flask`

- Windows

### Instalação do Pytest

`$ pip install pytest`

### Instalação do Requests

`$ pip install requests`

Para iniciar a aplicação temos que executar o seguinte comandos no Ubuntu

`python app.py`

* Debug mode: on
* Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
* Restarting with stat
* Debugger is active!
* Debugger PIN: 420-572-100

## Utilização da API

No navegador ou Postman(Método GET) por exemplo para chamar api temos que:

`http://localhost:5000/songs/[Nome do Artista]`

### Um exemplo simples

http://localhost:5000/songs/Adele

{
    "Hello",
    "Someone Like You",
    "All I Ask",
    "When We Were Young",
    "Rolling in the Deep",
    "Send My Love (To Your New Lover)",
    "Set Fire to the Rain",
    "Water Under the Bridge",
    "Make You Feel My Love",
    "Chasing Pavements"
}

## Teste

Para executar o teste execute o seguinte comando:

`python -m pytest test_app.py`

==================== test session starts ====================


platform linux2 -- 

Python 2.7.15+, 

pytest-4.6.5,

py-1.8.0, pluggy-0.12.0

rootdir: /home/reinaldo/api_genius/api_songs

collected 1 item                                                                                    

test_app.py .                                                [100%]

==================== 1 passed in 3.84 seconds ====================
