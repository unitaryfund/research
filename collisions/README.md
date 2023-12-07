## Counting collisions in random circuit sampling for benchmarking quantum computers

### [arXiv:xxxx.xxxx](https://arxiv.org/abs/xxxx.xxxx)

### Abstract

We show that counting the number of collisions (re-sampled bitstrings) when measuring a random quantum circuit provides a practical benchmark for the quality of a quantum computer and a quantitative noise characterization method. We analytically estimate the difference in the expected number of collisions when sampling bitstrings from a pure random state and when sampling from the classical uniform distribution. We show that this quantity, if properly normalized, can be used as a _collision anomaly_ benchmark or as a _collision volume_ test which is similar to the well-known quantum volume test, with advantages (no classical computing cost) and disadvantages (high sampling cost).
We also propose to count the number of  cross-collisions between two independent quantum computers running the same random circuit in order to obtain a cross-validation test of the two devices.
Finally, we quantify the sampling cost of quantum collision experiments. We find that the sampling cost for running a collision volume test on state-of-the-art processors (e.g.~20 effective clean qubits) is quite small: less than $10^5$ shots. For large-scale experiments in the quantum supremacy regime the required number of shots for observing a quantum signal in the observed number of collisions is currently infeasible ($>10^{12}$), but not completely out of reach for near-future technology.

### Notebooks
1. [Counting collisions in random circuit sampling for benchmarking quantum computers](https://github.com/unitaryfund/research/blob/master/collisions/collisions.ipynb)

### How to use
The code is written in Python and is organized in a self-contained Jupyter notebook.
It can be visualized on GitHub (without execution) by just clicking on its file name.

### Requirements
Jupyter Notebook or JupyterLab should be [installed](https://jupyter.org/install) to execute the notebook in your local machine. 
The following Python packages are also required `numpy`, `matplotlib` and `qiskit`.
