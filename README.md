# Best practices for module

* __init__ makes the directory importable
* __main__ makes the main executable when i call it.

## Todo list

[ ] Task runner for python

## How to run

* run the module name
  * `python -m intro`
  * `poetry run python -m intro`
  * What's the difference?
    * nothing much as long as your python is in the same env space as your poetry.

## Double check your python dependencies per env

* code
  * `pip freeze | while IFS=  read -r line; do echo $line | sed -e 's/@.*$//'; done`
  * `poetry export --dev --without-hashes | while IFS=  read -r line; do  echo $line | sed -e 's/;.*$//' ; done`
* ELI5:
  * the top two should be the same.

<table>
<th><tr><td>pip</td><td>poetry</td></tr>
</th>
<td>
<pre>
attrs
importlib-metadata
intro==0.1.0
more-itertools
packaging
pluggy
py
pyparsing
pytest
typing_extensions
wcwidth
zipp
</pre>
</td>
<td>
<pre>
atomicwrites==1.4.0
attrs==21.4.0
colorama==0.4.4
importlib-metadata==4.11.2
more-itertools==8.12.0
packaging==21.3
pluggy==0.13.1
py==1.11.0
pyparsing==3.0.7
pytest==5.4.3
typing-extensions==4.1.1
wcwidth==0.2.5
zipp==3.7.0
</pre>
</td>
</table>

* atomicwrites, colorama is extra in poetry.
* `--dev                  Include development dependencies.`
* All these are dev dependencies.
* So a poetry install with just one dependency wont have such a large package.
  * it's cool!

## How to run tests

* poetry test with print statements
  * `poetry run pytest -s`
  * `poetry run pytest` (without statements)
* caveats
  * you got to run pytest from root
  * continiuous test mode
    * `poetry run ptw`
      * options are in the pytest.ini
        * defaulted it to spit out console logs
        * defaulted folder to only run tests when tests change
          * [ ] will add src in the future
    * `poetry run tox`
      * To test against multiple versions of python
      * defaulted it to run tests agains python 3.7 only

## Updating the rst

* `pandoc -t rst -o README.rst README.md`
  * because rst isnt mature yet, we first write to the md then generate changes to the rst
