# DD2480 Spring 2025 Assignment 1 - Group 1

## What is this?

This repository serves as the code base of a hypothetical anti-ballistic missile system.

For more information, please refer to the course [DD2480](https://www.kth.se/student/kurser/kurs/DD2480?startterm=20251&l=en).

## How to setup

### Prerequisites

You need to have Python 3.11 installed, then run `pip3 install -r requirements.txt` to installed the required packages.

> Note that other Python3 versions might be supported, but this software has only been extensively tested on Python 3.11.

For developers, it is recommended to use [venv](https://docs.python.org/3/library/venv.html), to avoid conflicts in package resolution (as well as scenarios like "it works on my machine"). You can then run `pip install -r requirements-dev.txt` to install the required packages.

In additional, we use [Black](https://github.com/psf/black) as our formatter, and [Flake8](https://github.com/PyCQA/flake8) as our linter. Please run `pre-commit install` to setup your pre-commit hooks, which will run automatic checks on your file formats.

> If desired, you can find the VS code extensions for them [here](https://marketplace.visualstudio.com/items?itemName=ms-python.black-formatter), and [here](https://marketplace.visualstudio.com/items?itemName=ms-python.flake8) respectively.
>
> To run the formatter in CLI, simply do `python -m black .` to format all your files.

### How to use the program

```
python3 main.py --input sample.txt
python3 main.py --input sample.txt --verbose
python3 test.py --verbose
```

## Project specifications

The system takes in the following inputs:

- `NUMPOINTS` The number of planar data points.
- `POINTS` Array containing the coordinates of data points.
- `PARAMETERS` Struct holding parameters for LIC’s.
- `LCM` Logical Connector Matrix.
- `PUV` Preliminary Unlocking Vector.

And outputs the following data:

- `LAUNCH` Final launch / no launch decision encoded as ”YES”, ”NO” on the standard output.
- `CMV` Conditions Met Vector.
- `PUM` Preliminary Unlocking Matrix.
- `FUV` Final Unlocking Vector.

Some APIs can be located and re-used in the `modules` folder:

- The main decide function is stored in `decide.py`.
- The CMV (Conditions Met Vector) is derived in `cmv.py`
- The FUV (Final Unlocking Vector) is derived in `fuv.py`
- The PUM (Preliminary Unlocking Matrix) is derived in `pum.py`

## Statement of contributions

### Kam Ting Hoi

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aliquam nec eros orci. Nunc euismod et nulla eu pretium. Aenean vitae nisl dictum, semper nunc vel, faucibus velit. Proin eu viverra ante. Cras maximus enim odio, at pretium enim fermentum at. Nulla non ligula enim. Nullam eget lacus eget ex lacinia tempor sit amet quis est. Praesent eleifend erat eget magna feugiat congue. Cras accumsan neque eget erat consequat gravida. Cras posuere metus eget est tristique imperdiet.

### Johan Nilsson

- I wrote the solutions for LICs 5 to 9 with at least 3 tests for each. I wrote more than 400 lines of code and exclusively worked in modules/cmv.py and test.py.

### Marcello Krahforst

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aliquam nec eros orci. Nunc euismod et nulla eu pretium. Aenean vitae nisl dictum, semper nunc vel, faucibus velit. Proin eu viverra ante. Cras maximus enim odio, at pretium enim fermentum at. Nulla non ligula enim. Nullam eget lacus eget ex lacinia tempor sit amet quis est. Praesent eleifend erat eget magna feugiat congue. Cras accumsan neque eget erat consequat gravida. Cras posuere metus eget est tristique imperdiet.

### Arvid Hjort

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aliquam nec eros orci. Nunc euismod et nulla eu pretium. Aenean vitae nisl dictum, semper nunc vel, faucibus velit. Proin eu viverra ante. Cras maximus enim odio, at pretium enim fermentum at. Nulla non ligula enim. Nullam eget lacus eget ex lacinia tempor sit amet quis est. Praesent eleifend erat eget magna feugiat congue. Cras accumsan neque eget erat consequat gravida. Cras posuere metus eget est tristique imperdiet.

### Olivia Aronsson

Implemented LIC 0, 1, 2, 3, 4 and corresponding tests. Participated in reviewing pull request. Wrote outline for assessment of WoW according to Essensce.

## Way of working

We would argue that our ways of working are currently in the state “In Use” but almost in the state “In Place”. We have already achieved the first two states “Principles established” and “Foundations established” by having meetings where the group agreed to a shared approach to the project, established shared practices for the whole team and evaluated the tools available with the desired practices. Furthermore, once the practises and tools were approved by the team we have been using them to do real work on the project. We have continuously adapted our ways of working when presented with new feedback on improvements, and regularly evaluate in meetings if there are any gaps needed to be amended in order for everyone to adhere to the ways of working within the context of the project. This, in our opinion, means that we also have fulfilled the state “In Use”.

Lastly, the whole team is currently using the practices and tools in the day to day work within the project, however as of now, only few members of the group are modifying and improving the practices in the group. Although most of the criteria for the “In Place” state are fulfilled, we would categorize ourselves as being between the “In Use” state and the “In Place” state. To fully reach the “In Place” state, the entire group would have to be more involved in inspection and adaptation of the way-of-working.
