# PDF watermaker

Code to Create add a watermark to a PDF. It accept img or pdf for watermark.

## Pre requirements

- [Pipenv](https://pipenv-es.readthedocs.io/es/latest/)

## Quick start

```sh
pipenv install
pipenv shell
```

## Installing with pip

```sh
pip install -r requirements.txt
```

## CLI

- Simple command

```sh
python main.py <path_to_pdf> <path_to_watermark> # Output path optional
```

- Help command

```sh
python main.py --help
```

## Example

### Watermarked PDF

![Alt text](./pdf_in.png?raw=true "original pdf")

### Orginal PDF

![Alt text](./pdf_out.png?raw=true "watermarked pdf")
