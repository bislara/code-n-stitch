import platform
import subprocess
import ctypes
import time


def change_background(image_path: str):
    os = platform.system().lower()
    print(f'Setting background {image_path}')
    try:
        if 'darwin' in os:  # macOS
            from appscript import app, mactypes  # load only for macOS

            app('Finder').desktop_picture.set(mactypes.File(image_path))
        elif 'linux' in os:  # linux
            command = f"gsettings set org.gnome.desktop.background picture-uri '{image_path}'"
            subprocess.Popen(["/bin/bash", "-c", command])
        else:
            ctypes.windll.user32.SystemParametersInfoW(20, 0, image_path, 3)
    except Exception as e:
        print(f'Failed to set background at path {image_path}\n', e)


def background_selection() -> list:
    images = []
    while True:
        image = input('Provide image path to be set as background:')
        if not image:
            break
        images.append(image)
        print('If there are no more images, press Enter')
    return images


def set_interval() -> int:
    internal = input("You've selected multiple images, select time internal (in minutes) for images to change: ")
    while True:
        try:
            return int(internal) * 60  # internal in minutes
        except ValueError:
            internal = input('Internal should be a number: ')


def background_rotation(images: list):
    internal = 0 if len(images) == 1 else set_interval()
    while True:
        for image in images:
            change_background(image)
            time.sleep(internal)


if __name__ == '__main__':
    bg_images = background_selection()
    if not bg_images:
        print('No images selected')
        exit()
    background_rotation(bg_images)
