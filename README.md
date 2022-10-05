# CSC 510 Team 31 - HW 2, 3, 4 & 5
[![DOI](https://zenodo.org/badge/530464314.svg)](https://zenodo.org/badge/latestdoi/530464314)
[![Documentation Status](https://readthedocs.org/projects/ansicolortags/badge/?version=latest)](https://github.com/CSC-510-Team-31/CSC_510-Team-31_HW2345/blob/main/README.md)
[![GitHub language count](https://img.shields.io/github/languages/count/CSC-510-Team-31/CSC_510-Team-31_HW2345?style=flat-square)](https://docs.python.org/3/)
<a href="https://github.com/CSC-510-Team-31/CSC_510-Team-31_HW2345/actions"><img src="https://github.com/CSC-510-Team-31/CSC_510-Team-31_HW2345/actions/workflows/csv-test.yml/badge.svg"></a>
[![Coverage badge](https://raw.githubusercontent.com/CSC-510-Team-31/CSC_510-Team-31_HW2345/python-coverage-comment-action-data/badge.svg)](https://github.com/CSC-510-Team-31/CSC_510-Team-31_HW2345/tree/python-coverage-comment-action-data)
<br/>
This repo serves as a rewrite of Dr. Tim Menzies' [csv.lua](https://github.com/timm/lua/blob/main/src/csv.lua) implementation into Python. Apart from academic purposes, the goal is to showcase implementing a test frameworks from scratch, legacy refactorization, and learning more of the nuances of LUA as it's translated to (roughly equivalent) Python code.

## To Run
Requires Python 3 and nothing else. You don't need to install anything from requirements.txt; that's purely for our GitHub Actions CI to pick up code coverage on new changes.

From the root directory of this project, run `python src/csv.py`, followed by a number of options described by running `python src/csv.py -h`, or by viewing src/constants.py.

## To Test
For now, specify a valid `-e` argument when running the program. For instance, to run all the tests/examples for the functionality, please run `python src/csv.py -e ALL`.
