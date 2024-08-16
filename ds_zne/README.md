## Zero noise extrapolation on logical qubits by scaling the error correction code distance

### [arXiv:2304.14985](https://arxiv.org/abs/2304.14985)

### Abstract

In this work, we migrate the quantum error mitigation technique of Zero-Noise Extrapolation (ZNE) to fault-tolerant quantum computing. We employ ZNE on logically encoded qubits rather than physical qubits. This approach will be useful in a regime where quantum error correction (QEC) is implementable but the number of qubits available for QEC is limited. Apart from illustrating the utility of a traditional ZNE approach (circuit-level unitary folding) for the QEC regime, we propose a novel noise scaling ZNE method specifically tailored to QEC: distance scaled ZNE (DS-ZNE). DS-ZNE scales the distance of the error correction code, and thereby the resulting logical error rate, and utilizes this code distance as the scaling `knob' for ZNE. Logical qubit error rates are scaled until the maximum achievable code distance for a fixed number of physical qubits, and lower error rates (i.e., effectively higher code distances) are achieved via extrapolation techniques migrated from traditional ZNE. Furthermore, to maximize physical qubit utilization over the ZNE experiments, logical executions at code distances lower than the maximum allowed by the physical qubits on the quantum device are parallelized to optimize device utilization. We validate our proposal with numerical simulation and confirm that ZNE lowers the logical error rates and increases the effective code distance beyond the physical capability of the quantum device. For instance, at a physical code distance of 11, the DS-ZNE effective code distance is 17, and at a physical code distance of 13, the DS-ZNE effective code distance is 21. When the proposed technique is compared against unitary folding ZNE under the constraint of a fixed number of executions of the quantum device, DS-ZNE outperforms unitary folding by up to 92\% in terms of the post-ZNE logical error rate.

### Notebooks
- [DS-ZNE data generation](https://github.com/unitaryfund/research/blob/main/ds_zne/ds-zne-data-generation.ipynb)
- [DS-ZNE data processing](https://github.com/unitaryfund/research/blob/main/ds_zne/ds-zne-data-processing.ipynb)
- [DS-ZNE data generation on deeper circuits](https://github.com/unitaryfund/research/blob/main/ds_zne/ds_zne_data_gen_deeper_circs.ipynb)
- [DS-ZNE data processing on deeper circuits](https://github.com/unitaryfund/research/blob/main/ds_zne/ds_zne_data_proc_deep_circs.ipynb)

### How to use
The code in this folder is contained in a Jupyter notebook which, along with the data in the [ds_zne/data](./data/) folder, can be used to reproduce the main results of the paper.

### Requirements
The code is written in Python. Notebooks can be visualized on GitHub (without execution) by just clicking on their file names.
Jupyter Notebook or JupyterLab should be [installed](https://jupyter.org/install) to execute the notebooks in your local machine. 
The quantum error mitigation library [Mitiq](https://github.com/unitaryfund/mitiq) is required. Please check all the other the `import` statements in each specific notebook for additional requirements.
