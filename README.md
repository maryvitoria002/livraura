*Instalação local*

Caso queira rodar o Xtudent de forma local, segue as instruções:

    Clone o repositório

```git clone https://github.com/maryvitoria002/livraura.git```

    Crie um ambiente virtual e instale as dependencias

```
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

    Configuração do banco de dados
```
python3 manage.py makemigrations
python3 manage.py migrate
```

    Execute o servidor de desenvolvimento
```
python3 manage.py runserver
```
