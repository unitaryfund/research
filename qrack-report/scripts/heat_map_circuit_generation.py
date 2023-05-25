import os
import math
import numpy as np
import random
from pyqrack import QrackCircuit

samples = 10
widths = [4, 9, 16, 25, 36, 49, 64]

def mcx(circ, c, q):
    circ.ucmtrx([c], [0, 1, 1, 0], q, 1)

def mcy(circ, c, q):
    circ.ucmtrx([c], [0, -1j, 1j, 0], q, 1)

def mcz(circ, c, q):
    circ.ucmtrx([c], [1, 0, 0, -1], q, 1)

def macx(circ, c, q):
    circ.ucmtrx([c], [0, 1, 1, 0], q, 0)

def macy(circ, c, q):
    circ.ucmtrx([c], [0, -1j, 1j, 0], q, 0)

def macz(circ, c, q):
    circ.ucmtrx([c], [1, 0, 0, -1], q, 0)

def rand_u3(circ, q):
    th = random.uniform(0, 4 * math.pi)
    ph = random.uniform(0, 4 * math.pi)
    lm = random.uniform(0, 4 * math.pi)

    c = math.cos(th / 2)
    s = math.sin(th / 2)

    op = []
    op.append(c)
    op.append(-np.exp(1j * lm) * s)
    op.append(np.exp(1j * ph) * s)
    op.append(np.exp(1j * (ph + lm)) * c)

    circ.mtrx(op, q)

def generate_circuits(width, depth):
    gateSequence = [ 0, 3, 2, 1, 2, 1, 0, 3 ]
    two_qubit_gates = mcx, mcy, mcz, macx, macy, macz
    
    colLen = math.floor(math.sqrt(width))
    while ((math.floor(width / colLen) * colLen) != width):
        colLen = colLen - 1
    rowLen = width // colLen

    time_results = []
    fidelity_results = []

    for t in range(samples):
        circ = QrackCircuit()
        d_time_results = []
        d_fidelity_results = []
        
        for i in range(depth):
            # Single bit gates
            for j in range(width):
                rand_u3(circ, j)

            gate = gateSequence[0]
            gateSequence.pop(0)
            gateSequence.append(gate)

            for row in range(1, rowLen, 2):
                for col in range(colLen):
                    tempRow = row
                    tempCol = col

                    tempRow = tempRow + (1 if (gate & 2) else -1);
                    if colLen != 1:
                        tempCol = tempCol + (1 if (gate & 1) else 0)

                    if (tempRow < 0) or (tempCol < 0) or (tempRow >= rowLen) or (tempCol >= colLen):
                        continue
                    
                    b1 = row * colLen + col
                    b2 = tempRow * colLen + tempCol

                    # Two bit gates
                    choice = random.choice(two_qubit_gates)
                    choice(circ, b1, b2)

            circ.out_to_file("heat_map_circuits/trial_" + str(t) + "_w" + str(width) + "_d" + str(i + 1))

if not os.path.exists("heat_map_circuits"):
   os.makedirs("heat_map_circuits")

for n in widths:
    generate_circuits(n, n)
