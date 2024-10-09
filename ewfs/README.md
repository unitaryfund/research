# Extended Wigner's Friend Scenario (ewfs)

Supplemental code for [arXiv:2409.15302](https://arxiv.org/abs/2409.15302).

## Installation

Python 3.12 or higher and [poetry](https://python-poetry.org/) is required. 

```
poetry install
```

## Usage

In order to run the notebooks, you will need to unzip the `paper_data.zip` file.

Launch the virtual environment shell via poetry:

```
poetry shell
```

Next, launch a local Jupyter notebook server.


```
jupyter notebook
```

There are two Jupyter notebooks:

- `demo.ipynb`: Specifies a EWFS circuit and runs on an IBM simulator (or hardware) device.

- `plots.ipynb`: Uses the data generated on simulators and hardware to reproduce plots from the paper.

