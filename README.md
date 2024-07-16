<p align="center">
    <h1 align="center"> Operations Research Codes</h1>
    <h4 align="center"><a href="docs/READMES.md">Readme en Español</a></h4>
</p>

> # [IMPORTANT]: The codes in this repository are written in spanish.

## Developers
<table align="center">
    <tbody>
        <tr>
            <td align="center"><a href="https://github.com/ImMamey" rel="nofollow"><img src="https://avatars.githubusercontent.com/u/32584037?v=4" width="150px;" alt="" style="max-width:100%;"><br><sub><b>Mamey</b></sub></a><br><a href="" title="Commits"><g-emoji class="g-emoji" alias="book" fallback-src="https://github.githubassets.com/images/icons/emoji/unicode/1f4d6.png">📖</g-emoji></a></td>
            <td align="center"><a href="https://github.com/Fussita" rel="nofollow"><img src="https://avatars.githubusercontent.com/u/110612202?v=4" width="150px;" alt="" style="max-width:100%;"><br><sub><b>Fussita</b></sub></a><br><a href="" title="Commits"><g-emoji class="g-emoji" alias="book" fallback-src="https://github.githubassets.com/images/icons/emoji/unicode/1f4d6.png">📖</g-emoji></a></td>
            <td align="center"><a href="https://github.com/C102002" rel="nofollow"><img src="https://avatars.githubusercontent.com/u/116277334?v=4" width="150px;" alt="" style="max-width:100%;"><br><sub><b>Alfredo Fung</b></sub></a><br><a href="" title="Commits"><g-emoji class="g-emoji" alias="book" fallback-src="https://github.githubassets.com/images/icons/emoji/unicode/1f4d6.png">📖</g-emoji></a></td>
            <td align="center"><a href="https://github.com/DanielBortot" rel="nofollow"><img src="https://avatars.githubusercontent.com/u/103535845?v=4" width="150px;" alt="" style="max-width:100%;"><br><sub><b>Daniel Borot</b></sub></a><br><a href="" title="Commits"><g-emoji class="g-emoji" alias="book" fallback-src="https://github.githubassets.com/images/icons/emoji/unicode/1f4d6.png">📖</g-emoji></a></td>
        </tr>
    </tbody>
</table>

## Description
This repository contains the codes of the Operations Research course at the University of Informatics Sciences. The codes are written in Python and are divided in two:
1. [Hungarian Algorithm.](https://en.wikipedia.org/wiki/Hungarian_algorithm)
2. [Revised Simplex Method.](https://en.wikipedia.org/wiki/Revised_simplex_method#:~:text=The%20revised%20simplex%20method%20is%20mathematically%20equivalent%20to%20the%20standard,the%20matrix%20representing%20the%20constraints.)

## Requirements
- Python 3.11+
- Pandas
- Tabulate
- Numpy
- Poetry (Optional)

## Installation
### a. If using Poetry:
1. `pip install poetry`
2. `poetry lock`
3. `poetry install`
4. Add the venv/lock as the project's interpreter.
5. Run the code.

### b. If not using Poetry:
1. Open the [`pyproject.toml`](pyproject.toml) file.
2. In the terminal, write `pip install <dependency name>` for each dependency listed under the `[tool.poetry.dependencies]` tag in the file from the previous step.
3. Run the code.

## Execution
### Hungarian Algorithm
1. Adapt `rest` with your matrix and `f_o` with your function (`"min"` or `"max"`)
```python
    rest = [
        [6, 2, 8, 5, 3, 0, 0],
        [5, 3, 9, 4, 2, 0, 0],
        [2, 3, 8, 4, 3, 0, 0],
        [4, 2, 6, 6, 5, 0, 0],
        [6, 1, 7, 6, 4, 0, 0],
        [0, 0, 0, 0, 0, -100, -100],
        [0, 0, 0, 0, 0, -100, -100],
    ]
    f_o = "max"  # min or max
```
2. Run the code.

## Legal


### Revised Simplex Method
1. Run the code.
2. The code will ask you for the number of variables, restrictions and matrix.
- - -
## Requisitos
Si quieres correr el codigo por tu cuenta, tienes dos opciones:
1. Usar el manejador de dependencias `Poetry` para crear un ambiente viretual-
2. Instalar todas las dependencias manualmente

#### Si vas a correr con poetry:
* [Python 3.11](https://www.python.org/downloads/release/python-3110/) 
* [Poetry](https://python-poetry.org/)
#### Si vas a correr sin poetry:
* [Python 3.11](https://www.python.org/downloads/release/python-3110/)
* Tienes que instalar todas las dependecias listadas en:  [`pyproject.toml`](pyproject.toml).

## Ejecucion:
#### Si vas a ejecutarlo con poetry:
1. En la terminal escribir `poetry lock`. (Esto crea el venv)
2. En la terminal escribir `poetry install`. (Esto instala las dependencias en el venv)
3. Añade el venv/lock como interprete dep projecto IDE.
> Para el caso de Pycharm: `Settings`→`Project`→`Python Interpreter`→`Add Interpreter`->`Add local Interpreter`-> `Poetry enviroment` ->`Existing enviroment`->Selecciona el `.lock` file.

#### Si vas a ejecutarlo sin poetry:
1. Abre [`pyproject.toml`](pyproject.toml).
2. En la terminal, escribir `pip install <nombre de la dependencia>` por cada dependencia escrita debalo del tag `[tool.poetry.dependencies]` en el archivo del paso anterior.

