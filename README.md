## Requisitos
Si quieres correr el codigo por tu cuenta, tienes dos opciones:
1. Usar el manejador de dependencias `Poetry` para crear un ambiente viretual-
2. Instalar todas las dependencias manualmente

#### Si vas a correr con poetry:
* [Python 3.11](https://www.python.org/downloads/release/python-3110/) 
* [Poetry](https://python-poetry.org/)
#### Si vas a correr sin poetry:
* [Python 3.11](https://www.python.org/downloads/release/python-3110/)
* All the dependencies listed in [`pyproject.toml`](pyproject.toml).

## Ejecucion:
#### Si vas a ejecutarlo con poetry:
1. En la terminal escribir `poetry lock`. (Esto crea el venv)
2. En la terminal escribir `poetry install`. (Esto instala las dependencias en el venv)
3. Añade el venv/lock como interprete dep projecto IDE.
> Para el caso de Pycharm: `Settings`→`Project`→`Python Interpreter`→`Add Interpreter`->`Add local Interpreter`-> `Poetry enviroment` ->`Existing enviroment`->Selecciona el `.lock` file.

#### Si vas a ejecutarlo sin poetry:
1. Abre [`pyproject.toml`](pyproject.toml).
2. En la terminal, escribir `pip install <nombre de la dependencia>` por cada dependencia escrita debalo del tag `[tool.poetry.dependencies]` en el archivo del paso anterior.

