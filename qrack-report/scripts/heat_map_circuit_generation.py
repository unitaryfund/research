import os
import math
import numpy as np
import random
from pyqrack import QrackCircuit

samples = 10
widths = [25, 36, 49, 64]

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

    # Nearest-neighbor couplers:
    row_len = math.ceil(math.sqrt(width))

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
            
            # Nearest-neighbor couplers:
            ############################
            gate = gateSequence.pop(0)
            gateSequence.append(gate)

            for row in range(1, row_len, 2):
                for col in range(row_len):
                    temp_row = row
                    temp_col = col
                    temp_row = temp_row + (1 if (gate & 2) else -1);
                    temp_col = temp_col + (1 if (gate & 1) else 0)
                    
                    if (temp_row < 0) or (temp_col < 0) or (temp_row >= row_len) or (temp_col >= row_len):
                        continue

                    b1 = row * row_len + col
                    b2 = temp_row * row_len + temp_col
                    
                    if (b1 >= width) or (b2 >= width):
                        continue

                    choice = random.choice(two_qubit_gates)
                    choice(circ, b1, b2)

            # Fully-connected couplers:
            ###########################
            # unused_bits = list(range(width))
            # while len(unused_bits) > 1:
            #     b1 = random.choice(unused_bits)
            #     unused_bits.remove(b1)
            #     b2 = random.choice(unused_bits)
            #     unused_bits.remove(b2)
            #
            #     # Two bit gates
            #     choice = random.choice(two_qubit_gates)
            #     choice(circ, b1, b2)

            circ.out_to_file("heat_map_circuits/trial_" + str(t) + "_w" + str(width) + "_d" + str(i + 1))

if not os.path.exists("heat_map_circuits"):
   os.makedirs("heat_map_circuits")

for n in widths:
    generate_circuits(n, n)
