import argparse
from typing import Optional

from pikepdf import Pdf, Encryption


def encrypt(filename: str, password: str, output: Optional[str] = None) -> None:
    with Pdf.open(filename) as pdf:
        pdf.save(output or f"encrypted_{filename}", encryption=Encryption(owner=password, user=password))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Encrypt pdf with passwords")
    parser.add_argument("filename", type=str, help="The name of the pdf to encrypt")
    parser.add_argument("password", type=str, help="The password for the encrypted file")
    parser.add_argument("-o", "--output", dest="output", type=str,
                        help="To change the output path for the encrypted pdf")

    args = parser.parse_args()
    encrypt(args.filename, args.password, args.output)
