import pyotp
import os


auth_key = 'YOUR AUTH KEY'


def auth_pass(auth_key):
    totp = pyotp.TOTP(auth_key)
    return totp.now()


def paste_text_to_clipboard(text):
    cp_2_clipboard = 'echo %s | tr -d "\n" | pbcopy' % text
    os.system(cp_2_clipboard)


if __name__ == '__main__':
    otp_code = auth_pass(auth_key)
    paste_text_to_clipboard(otp_code)