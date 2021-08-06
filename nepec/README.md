## Noise-extended probabilistic error cancellation (NEPEC)

### [arXiv:2108.02237](https://arxiv.org/abs/2108.02237)

### Abstract

We propose a general framework for quantum error mitigation that combines and generalizes two techniques: probabilistic error cancellation (PEC) and zero-noise extrapolation (ZNE). Similarly to PEC, the proposed method represents ideal operations as linear combinations of noisy operations that are implementable on hardware. However, instead of assuming a fixed level of hardware noise, we extend the set of implementable operations by noise scaling. By construction, this method encompasses both PEC and ZNE as particular cases and allows us to investigate a larger set of hybrid techniques. For example, gate extrapolation can be used to implement PEC without requiring knowledge of the device's noise model, e.g., avoiding gate set tomography. Alternatively, probabilistic error *reduction* can be used to estimate expectation values at intermediate *virtual* noise strengths (below the hardware level), obtaining partially mitigated results at a lower sampling cost. Moreover, multiple results obtained with different noise reduction factors can be further post-processed with ZNE to better approximate the zero-noise limit.

### How to use
The code in this folder is organized in different Jupyter notebooks that can be used to reproduce the main results of the paper.

### Requirements
The code is written in Python. Notebooks can be visualized on GitHub (without execution) by just clicking on their file names.
Jupyter Notebook or JupyterLab should be [installed](https://jupyter.org/install) to execute the notebooks in your local machine. 
The quantum error mitigation library [Mitiq](https://github.com/unitaryfund/mitiq) is required. Please check all the other the `import` statements in each specific notebook for additional requirements.
