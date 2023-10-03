<div align="center">
  <h1>CSV Validator</h1>
  <img src="https://img.shields.io/badge/python-3.6%2B-blue" />
  <img src="https://img.shields.io/badge/license-MIT-green" />
  <img src="https://img.shields.io/badge/PRs-welcome-brightgreen" />
</div>

---

## Overview

This Python script processes CSV files in a specified input directory and writes only the valid rows to a new CSV file in an output directory. The script also logs the processing time, the files being processed, and any invalid rows that are skipped.

## Table of Contents

- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Options](#options)
- [Example](#example)
- [Contact](#contact)

## Prerequisites

- Python 3.6 or later

## Installation

1. Clone this repository or download the script `main.py`.
2. Make sure you have Python installed, or download it from [Python's official website](https://www.python.org/).

## Usage

Open a terminal and navigate to the directory containing the script. Then, run the following command:

```bash
python main.py
```

## Options

- This script doesn't have command-line options; it runs with default settings.

## Example

Let's say you have a directory `input` with the following CSV files:

- `sample1.csv`
- `sample2.csv`

After running the command:

```bash
python main.py
```

New CSV files (`sample1.csv`, `sample2.csv`) with only valid rows will be created in the `output` directory. Also, a log file named `log.txt` will be updated with processing details.

## Contact

- Website [carlos8a.com](https://carlos8a.com)
- GitHub [@CarlosUlisesOchoa](https://github.com/carlosulisesochoa)
- X [@Carlos8aDev](https://twitter.com/carlos8adev)
