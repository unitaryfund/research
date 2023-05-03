# qrack-report
Resources for report on Qrack

This is a repository of numerical data and analysis scripts for producing a report on the performance of Qrack, as a comparatively fast and efficient back end for exact simulation cases, and also as a cost-competitive option for reduced fidelity, high width simulation cases.

Currently, this repository contains a graph of comparative benchmark results on the ("exact" or "ideal") quantum Fourier transform algorithm, at [qft.png](https://github.com/unitaryfund/qrack-report/blob/main/qft.png), as well as high-width noisy simulation fidelity estimates from mirror circuit validation.

[marp_regression.ipynb](https://github.com/unitaryfund/qrack-report/blob/main/marp_regression.ipynb) contains bottom-line results distilled from "MARP search" to a single regression model of fidelity on a single A100 GPU, for circuits similar to "nearest-neighbor quantum volume."
