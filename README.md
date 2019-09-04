# API Songs
API Flask que dado um artista retorna 10 músicas mais populares

Pré-requisitos:
- Python 2.7
- Pip
- Flask
- Pytest
- Requests

Para instalações dos pré-requisitos executem os seguintes comandos no Ubuntu:

### Instalação do Python

`$ apt-get install python`

### Instalação do Pip

`$ apt-get install python-pip`

### Instalação do Flask

`$ pip install -U Flask`

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

No navegador ou Postman por exemplo para chamar api temos que:
`http://localhost:5000/songs/[Nome do Artista]`

### Um exemplo simples

`http://localhost:5000/songs/Adele`

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

======================================== test session starts ========================================
platform linux2 -- Python 2.7.15+, pytest-4.6.5, py-1.8.0, pluggy-0.12.0
rootdir: /home/reinaldo/api_genius/api_songs
collected 1 item                                                                                    

test_app.py .                                                                                 [100%]

===================================== 1 passed in 3.84 seconds ======================================
