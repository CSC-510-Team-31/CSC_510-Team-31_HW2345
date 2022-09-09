# CSC 510 Team 31 - HW 2, 3, 4 & 5

This repo serves as a rewrite of Dr. Tim Menzies' [csv.lua](https://github.com/timm/lua/blob/main/src/csv.lua) implementation into Python. Apart from academic purposes, the goal is to showcase implementing a test frameworks from scratch, legacy refactorization, and learning more the nuances of LUA as it's translated to (roughly equivalent) Python code.

## To Run
Requires Python 3.

From the root directory of this project, run `python src/__init__.py`, followed by a number of options described by running `python src/__init__.py -h`, or by viewing src/constants.py.

## To Test
For now, specify a valid `-e` argument when running the program. For instance, to run all the tests/examples for the functionality, please run `python src/__init__.py -e ALL`.