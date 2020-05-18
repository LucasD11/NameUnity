# Contributing Document

## Run unit tests

```shell
python -m unittest discover tests
```

## Build & Deploy

```shell
python setup.py sdist bdist_wheel
twine upload dist/*
```
