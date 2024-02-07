## Quantum error mitigation by layerwise Richardson extrapolation

### [arXiv:2402.04000](https://arxiv.org/abs/2402.04000)

### Abstract

A widely used method for mitigating errors in noisy quantum computers is Richardson extrapolation, a technique in which the overall effect of noise on the estimation of quantum expectation values is captured by a single parameter that, after being scaled to larger values, is eventually extrapolated to the zero-noise limit. We generalize this approach by introducing \emph{layerwise Richardson extrapolation (LRE)}, an error mitigation protocol in which the noise of different individual layers (or larger chunks of the circuit) is amplified and the associated expectation values are linearly combined to estimate the zero-noise limit. The coefficients of the linear combination are analytically obtained from the theory of multi-variate Lagrange interpolation. LRE leverages the flexible configurational space of layerwise unitary folding, allowing for a more nuanced mitigation of errors by treating the noise level of each layer of the quantum circuit as an independent variable. We provide numerical simulations demonstrating scenarios where LRE achieves superior performance compared to traditional (single-variable)  Richardson extrapolation.

### Notebooks
1. [Quantum error mitigation by layerwise Richardson extrapolation](https://github.com/unitaryfund/research/blob/master/lre/layerwise_richardson_extrapolation.ipynb)

### How to use
The code is written in Python and is organized in a self-contained Jupyter notebook.
It can be visualized on GitHub (without execution) by just clicking on its file name.

### Requirements
Jupyter Notebook or JupyterLab should be [installed](https://jupyter.org/install) to execute the notebook in your local machine. The following Python packages are required to run the notebook:

```
qiskit==0.44.1
qiskit-aer==0.12.2
mitiq==0.31.0
numpy==1.26.2
cirq==1.2.0
matplotlib==3.7.2
```