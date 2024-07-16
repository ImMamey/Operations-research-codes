<p align="center">
    <h1 align="center"> Códigos de Investigación de Operaciones</h1>
    <h4 align="center"><a href="docs/READMES.md">Leerme en Español</a></h4>
</p>

- - -
## Desarrolladores
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

 - - - 

## Descripción
Este repositorio contiene los códigos del curso de Investigación de Operaciones en la Universidad de Ciencias Informáticas. Los códigos están escritos en Python y se dividen en dos partes:
1. [Algoritmo Húngaro.](https://es.wikipedia.org/wiki/Algoritmo_h%C3%BAngaro)
2. [Método Simplex Revisado.](https://es.wikipedia.org/wiki/M%C3%A9todo_simplex_revisado)

## Requisitos
- Python 3.11+
- Pandas
- Tabulate
- Numpy
- Poetry (Opcional)

## Instalación
### a. Si estás utilizando Poetry:
1. `pip install poetry`
2. `poetry lock`
3. `poetry install`
4. Agrega venv/lock como intérprete del proyecto.
5. Ejecuta el código.

### b. Si no estás utilizando Poetry:
1. Abre el archivo [`pyproject.toml`](pyproject.toml).
2. En la terminal, escribe `pip install <nombre de la dependencia>` para cada dependencia listada bajo la etiqueta `[tool.poetry.dependencies]` en el archivo del paso anterior.
3. Ejecuta el código.

## Ejecución
### Algoritmo Húngaro
1. Adapta `rest` con tu matriz y `f_o` con tu función (`"min"` o `"max"`)
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
2. Ejecuta el código.
### Método Simplex Revisado
1. Ejecuta el código.
2. El código te pedirá el número de variables, restricciones y matriz.

- - -

## Contribuciones
**Este repositorio ya no está siendo mantenido.** Sin embargo, si deseas contribuir, puedes hacer un fork del repositorio y enviar un pull request.