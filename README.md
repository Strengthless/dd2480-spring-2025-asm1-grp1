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
python3 -m src.main -i ./inputs/sample.txt
python3 -m unittest
python3 -m unittest -v
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

Some APIs can be located and re-used in the `src/modules` folder:

- The main decide function is stored in `decide.py`.
- The CMV (Conditions Met Vector) is derived in `cmv.py`
- The FUV (Final Unlocking Vector) is derived in `fuv.py`
- The PUM (Preliminary Unlocking Matrix) is derived in `pum.py`

## Statement of contributions

### Kam Ting Hoi

For this lab assignment, I mostly played the role of DevOps engineer & systems architect. I was responsible for:
- initializing the repository with a suitable architecture, implementing API interfaces, types and placeholder functions, etc.
- implementing core logic, e.g. handling of data inputs, high-level logic for `main.py` and `decide.py`, etc.
- improving developer experience by implementing CI checks, code formatter and linter, etc.
- refactoring of our codebase, e.g. extracting common arithmetic operations into their own functions, adding test fixtures and factory functions, fixing floating point error bugs, etc.
- integrating the final software, making sure that all modules are compatible with up-to-date function signatures.

### Johan Nilsson

- I wrote the solutions for LICs 5 to 9 with at least 3 tests for each. I wrote more than 400 lines of code and exclusively worked in modules/cmv.py and test.py.

### Marcello Krahforst

I was mainly responsible for implementing the _FUV_ and _PUM_ component, thus I mostly modified the _modules/pum.py_ and _modules/fuv.py_ files and created respective tests for the implemented functions in _test.py_. Besides that, I occasionally reviewed code in Pull Requests and suggested changes or tested the code that was about to be merged into the main branch. Finally, I helped in documenting our way-of-working.

### Arvid Hjort

For this lab assignment I worked on the LIC algorithms in the CMV function. Specifically I have coded LIC 10, 11, 12, 13 and 14 and the test cases for those functions. This means that I worked in the modules/cmv.py and test.py

### Olivia Aronsson

Implemented LIC 0, 1, 2, 3, 4 and corresponding tests, thus working solely in modules/cmv.py and test/test_CMV.py. Participated in reviewing pull request and wrote outline for assessment of WoW in accordance with Essensce standard.

## Way of working

We would argue that our ways of working are currently in the state “In Use” but almost in the state “In Place”. We have already achieved the first two states “Principles established” and “Foundations established” by having meetings where the group agreed to a shared approach to the project, established shared practices for the whole team and evaluated the tools available with the desired practices. Furthermore, once the practises and tools were approved by the team we have been using them to do real work on the project. We have continuously adapted our ways of working when presented with new feedback on improvements, and regularly evaluate in meetings if there are any gaps needed to be amended in order for everyone to adhere to the ways of working within the context of the project. This, in our opinion, means that we also have fulfilled the state “In Use”.

Lastly, the whole team is currently using the practices and tools in the day to day work within the project, however as of now, only few members of the group are modifying and improving the practices in the group. Although most of the criteria for the “In Place” state are fulfilled, we would categorize ourselves as being between the “In Use” state and the “In Place” state. To fully reach the “In Place” state, the entire group would have to be more involved in inspection and adaptation of the way-of-working.
