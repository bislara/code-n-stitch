import platform
import subprocess
import ctypes
import time


def change_background(image_path):
    os = platform.system().lower()
    try:
        if 'darwin' in os:  # macOS
            from appscript import app, mactypes
            app('Finder').desktop_picture.set(mactypes.File(image_path))
        elif 'linux' in os:  # linux
            command = f"gsettings set org.gnome.desktop.background picture-uri '{image_path}'"
            subprocess.Popen(["/bin/bash", "-c", command])
        else:
            ctypes.windll.user32.SystemParametersInfoW(20, 0, image_path, 3)
    except Exception as e:
        print(f'Failed to set background at path {image_path}\n', e)


def images_selection():
    images = []
    while True:
        image = input('Provide image path to be set as background:')
        if not image:
            break
        images.append(image)
        print('If there are no more images, press Enter')
    return images


def internal_selection():
    internal = input("You've selected multiple images, select time internal (in minutes) for images to change: ")
    while True:
        try:
            return int(internal) * 60  # internal in minutes
        except ValueError:
            internal = input('Internal should be a number: ')


def images_rotation(images):
    internal = 0 if len(images) == 1 else internal_selection()
    for image in images:
        change_background(image)
        time.sleep(internal)


if __name__ == '__main__':
    images = images_selection()
    if not images:
        print('No images selected')
        exit()
    images_rotation(images)
