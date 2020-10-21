from PIL import Image

def convert(image_path, width=100, threshold=100):
    """
    Takes in the path of the image [image_path] and converts it into ascii version of the image
    Optional paramaters:
        + width --> width of the ascii art
        + threshold --> value at which the pixels are differentiated into ascii characters

    Usage:
    >>> print(convert("path/to/the/image"))
    >>> print(convert("path/to/the/image", width=50, threshold=200))

    Example Usage:
    >>> print(convert("sample.png", width=60, threshold=150))
    """
    image = Image.open(image_path)
    og_width, og_height = image.size
    ratio = og_height / og_width
    height = int(width * ratio)//2
    image = image.resize((width, height)) # resizing the image

    image = image.convert("L")  # converting image to grayscale
    pixels = image.getdata()  # getting data of pixels in the grayscaled image
    characters = "".join(
        [" " if pixel < threshold else "." for pixel in pixels]
    )

    pixel_count = len(characters)
    ascii_image = "\n".join(
        [
            characters[index: index + width]
            for index in range(0, pixel_count, width)
        ]
    )
    return ascii_image
