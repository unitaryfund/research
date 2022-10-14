## Testing platform-independent quantum error mitigation on noisy quantum computers

### [arXiv:2210.07194](https://arxiv.org/abs/2210.07194)

### Abstract

We apply quantum error mitigation techniques to a variety of benchmark problems
and quantum computers to evaluate the performance of quantum error mitigation in
practice. To do so, we define an empirically motivated, resource-normalized
metric of the improvement of error mitigation which we call the improvement
factor, and calculate this metric for each experiment we perform.  The
experiments we perform consist of zero-noise extrapolation and probabilistic
error cancellation applied to two benchmark problems run on IBM, IonQ, and
Rigetti quantum computers, as well as noisy quantum computer simulators. Our
results show that error mitigation is on average more beneficial than no error
mitigation — even when normalized by the additional resources used — but also
emphasize that the performance of quantum error mitigation is closely tied to
the performance of the underlying computer.

### Notebooks
1. [Testing PEC and ZNE on noisy quantum computers](https://github.com/unitaryfund/research/blob/master/qem-on-hardware/pec_and_zne.ipynb)

### Experiment data

The data obtained from our experiments and used to generate the plots in our work can be found in

```
data/[TYPE]/[QEM]/[CIRCUIT]/[PLATFORM]/
```

where `[TYPE] = {'hardware', 'software'}` describes whether the experiment was
run on either an actual quantum device or a simulator, `[QEM] = {'pec', 'zne'}`
describes the error mitigation method that was applied, `[CIRCUIT] = {'mirror',
'rb'}` describes the circuit type considered and where `[PLATFORM] = {'rigetti',
'ibmq', 'ionq', 'depolarizing'}` describes on which platform the experimental
data was obtained from.

Contained in each such directory is a subfolder with the following form

```
[PLATFORM]_[QEM]_[CIRCUIT]_[QUBITS]_[MIN]_[MAX]_[SHOTS]_[TRIALS]
```

where `[QUBIT]` is the number of qubits used in the experiment, `[MIN]` is the
minimum Clifford depth, `[MAX]` is the maximum Clifford depth, `[SHOTS]` is the
total number of shots used in the experiment (this is 10,000 for all of our
experiments) and `[TRIALS]` is the total number of trials carried out per
experiment (this is 4 for all of our experiments).

In each such subfolder is a listing of files with the following prefixes:

- `cnot_counts`: The number of CNOT gates in the circuit.
- `noise_scaled_expectation_values`: Noise-scaled expectation values (for ZNE only).
- `noisy_values`: The non-scaled noisy expectation values (prior to applying error mitigation).
- `oneq_counts`: The number of circuit instructions (modulo the number of CNOT operations).
- `true_values`: The ideal values (these are always equal to 1).
- `mitigated_values`: The error-mitigated values. 

Each row represents the value obtained at the depth corresponding to the index
and each column represents the data obtained for a given trial.

The code in this folder is organized in different Jupyter notebooks that can be
used to reproduce the main results of the paper.

### Usage

Running the software that is responsible for capturing quantum device hardware
experiment data requires possessing an AWS Braket account (for IonQ and Rigetti)
an an IBM Quantum account (for IBM).  Running the software on exclusively
quantum simulators can be done without any such account access. 

To run the software on a simulator device the variable `use_noisy_simulator`
should be set to `True` (and alternatively, `False` if the desire is to run on
quantum device hardware). Setting the `mitigation_type` variable to either `pec`
and `zne` runs PEC or ZNE error mitigation, respectively. The type of circuit to
use can be set via the variable `circuit_type` to either `rb` for randomized
benchmarking circuits or `mirror` for mirror circuits. Specifying the target
platform can be done by setting the `hardware_type` variable to either `ibmq`,
`ionq`, or `rigetti` for IBM, IonQ, or Rigetti, respectively.

The present default setting in the `pec_and_zne.ipynb` notebook is to run a
3-qubit experiment on the IBM `FakeLima` simulator device using the ZNE error
mitigation method with randomized benchmarking circuits. There are 4 separate
trials run where each trial has a maximum Clifford depth of 20 with a step of 2.

Modifying the `use_noisy_simulator`, `mitigation_type`, `hardware_type`, and
`circuit_type` parameters as described above can produce experiment data for
other experimental scenarios of interest.

### Requirements
The code is written in Python. Notebooks can be visualized on GitHub (without
execution) by just clicking on their file names.  Jupyter Notebook or JupyterLab
should be [installed](https://jupyter.org/install) to execute the notebooks in
your local machine.  The quantum error mitigation library
[Mitiq](https://github.com/unitaryfund/mitiq) is required. Please check all the
other the `import` statements in each specific notebook for additional
requirements.
