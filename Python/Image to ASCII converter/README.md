# What does it do?
- It takes in path to an image and returns an ascii version of the image which can then be printed and copy-pasted
# Instructions
- Pass in the path to image file as parameter to `convert()` function
- Optionally tweak the `width` and `threshold value` (Default value for both variables is `100`) to get a nicer ascii version of the image.
- ### Usage
    - `>>> print(convert("path/to/the/image"))`
    - `>>> print(convert("path/to/the/image", width=50, threshold=200))`
    - `>>> print(convert("sample.png", width=60, threshold=150))`
# Requirements
- pillow

# Screenshots
![](https://i.imgur.com/Ey0teWG.png)
![](https://i.imgur.com/bSKULNa.png)
