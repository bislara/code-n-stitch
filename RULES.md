# Rules

## IMPORANT

Be sure to read the project structure and formatting rules given in the repo before commiting to the repository

## Project Structure

The project needs to defined in the following manner

- {Language}
  - {ProjectName} (This should be in CamelCase)
    - README.md
    - images (This is store images to be used with README or required by your application)
    - src (The source code for your application)
    - out (The build files your application)

Note: All the folders should be in lower case and the name should be plural noun.

In which the out folder should be excluded since the output files only clutter the system. Also provide your own .gitignore files if there are other clutter files. Also, the test folder can created inside the source for any test files.

### Example

- Python
  - HyperLinkExtractor
    - README.md
    - src
      - resources
        - code.js
        - test.txt
      - ui.py
      - links.py
      - links_test.py
    - images
      - cmd.png
      - gui.png

## Language Rules

### Python

The code for python should be formatted using [Black](https://black.readthedocs.io/en/stable/)

### HTML, CSS and Javascript

The code for above mentioned languages should by formatted by [Prettier](https://prettier.io/)

### Others

The code for all the others should be formatted by Google Style but using indent of 4 spaces

[https://github.com/google/styleguide]