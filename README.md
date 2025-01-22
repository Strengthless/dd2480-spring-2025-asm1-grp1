# DD2480 Spring 2025 Assignment 1 - Group 1

## What is this?

This repository serves as the code base of a hypothetical anti-ballistic missile system.

For more information, please refer to the course [DD2480](https://www.kth.se/student/kurser/kurs/DD2480?startterm=20251&l=en).

## How to setup

### Prerequisites

You need to have Python3 installed. No external packages are required, as of the time of writing (22/1/2025).

### How to run the program

```
python3 main.py
python3 test.py -v
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

## Statement of contributions & Way of working

### Kam Ting Hoi

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aliquam nec eros orci. Nunc euismod et nulla eu pretium. Aenean vitae nisl dictum, semper nunc vel, faucibus velit. Proin eu viverra ante. Cras maximus enim odio, at pretium enim fermentum at. Nulla non ligula enim. Nullam eget lacus eget ex lacinia tempor sit amet quis est. Praesent eleifend erat eget magna feugiat congue. Cras accumsan neque eget erat consequat gravida. Cras posuere metus eget est tristique imperdiet.

### Johan Nilsson

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aliquam nec eros orci. Nunc euismod et nulla eu pretium. Aenean vitae nisl dictum, semper nunc vel, faucibus velit. Proin eu viverra ante. Cras maximus enim odio, at pretium enim fermentum at. Nulla non ligula enim. Nullam eget lacus eget ex lacinia tempor sit amet quis est. Praesent eleifend erat eget magna feugiat congue. Cras accumsan neque eget erat consequat gravida. Cras posuere metus eget est tristique imperdiet.

### Marcello Krahforst

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aliquam nec eros orci. Nunc euismod et nulla eu pretium. Aenean vitae nisl dictum, semper nunc vel, faucibus velit. Proin eu viverra ante. Cras maximus enim odio, at pretium enim fermentum at. Nulla non ligula enim. Nullam eget lacus eget ex lacinia tempor sit amet quis est. Praesent eleifend erat eget magna feugiat congue. Cras accumsan neque eget erat consequat gravida. Cras posuere metus eget est tristique imperdiet.

### Arvid Hjort

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aliquam nec eros orci. Nunc euismod et nulla eu pretium. Aenean vitae nisl dictum, semper nunc vel, faucibus velit. Proin eu viverra ante. Cras maximus enim odio, at pretium enim fermentum at. Nulla non ligula enim. Nullam eget lacus eget ex lacinia tempor sit amet quis est. Praesent eleifend erat eget magna feugiat congue. Cras accumsan neque eget erat consequat gravida. Cras posuere metus eget est tristique imperdiet.
