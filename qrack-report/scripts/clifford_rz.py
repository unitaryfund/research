import math
import os
import random

import numpy as np
import tensorcircuit as tc
import tensorcircuit.compiler.simple_compiler as tcsc

from pyqrack import QrackSimulator


width = 6
max_magic = 8
sqrt1_2 = 1 / math.sqrt(2)


def x_to_y(circ, q):
    circ.s(q)
    return 1


def x_to_z(circ, q):
    circ.h(q)
    return 1


def y_to_z(circ, q):
    circ.adjs(q)
    circ.h(q)
    return 2


def y_to_x(circ, q):
    circ.adjs(q)
    return 1


def z_to_x(circ, q):
    circ.h(q)
    return 1


def z_to_y(circ, q):
    circ.h(q)
    circ.s(q)
    return 2


def cx(circ, q1, q2):
    circ.mcx([q1], q2)
    return 1


def cy(circ, q1, q2):
    circ.mcy([q1], q2)
    return 1


def cz(circ, q1, q2):
    circ.mcz([q1], q2)
    return 1


def acx(circ, q1, q2):
    circ.macx([q1], q2)
    return 1


def acy(circ, q1, q2):
    circ.macy([q1], q2)
    return 1


def acz(circ, q1, q2):
    circ.macz([q1], q2)
    return 1


def swap(circ, q1, q2):
    circ.swap(q1, q2)
    return 1


def nswap(circ, q1, q2):
    circ.mcz([q1], q2)
    circ.swap(q1, q2)
    circ.mcz([q1], q2)
    return 3


def pswap(circ, q1, q2):
    circ.mcz([q1], q2)
    circ.swap(q1, q2)
    return 2


def mswap(circ, q1, q2):
    circ.swap(q1, q2)
    circ.mcz([q1], q2)
    return 2


def iswap(circ, q1, q2):
    circ.iswap(q1, q2)
    return 1


def iiswap(circ, q1, q2):
    circ.adjiswap(q1, q2)
    return 1


def random_circuit(width, circ):
    t_count = 0
    gate_count = 0
    bit_depths = width * [0]

    single_bit_gates = { 0: (z_to_x, z_to_y), 1: (x_to_y, x_to_z), 2: (y_to_z, y_to_x) } 
    two_bit_gates = swap, pswap, mswap, nswap, iswap, iiswap, cx, cy, cz, acx, acy, acz
    
    # Nearest-neighbor couplers:
    gateSequence = [ 0, 3, 2, 1, 2, 1, 0, 3 ]
    row_len = math.ceil(math.sqrt(width))

    # Don't repeat bases:
    bases = [0] * width
    directions = [0] * width
    
    for i in range(3 * width):
        # Single bit gates
        for j in range(width):
            # Reset basis, every third layer
            if i % 3 == 0:
                bases[j] = random.randint(0, 2)
                directions[j] = random.randint(0, 1)
            
            # Sequential basis switch
            gate = single_bit_gates[bases[j]][directions[j]]
            g_count = gate(circ, j)
            gate_count += g_count
            bit_depths[j] += g_count

            # Cycle through all 3 Pauli axes, every 3 layers
            if directions[j]:
                bases[j] -= 1
                if bases[j] < 0:
                    bases[j] += 3
            else:
                bases[j] += 1
                if bases[j] > 2:
                    bases[j] -= 3
                
            # Rotate around local Z axis
            rnd = random.randint(0, 3)
            if rnd == 0:
                circ.s(j)
            elif rnd == 1:
                circ.z(j)
            elif rnd == 2:
                circ.adjs(j)
            # else - identity
            if rnd < 3:
                gate_count += 1
                bit_depths[j] += 1
            
            if (t_count < max_magic) and (width * width * random.random() / max_magic) < 1:
                circ.u(j, 0, random.uniform(0, 4 * math.pi), 0)
                gate_count += 1
                bit_depths[j] += 1
                t_count += 1
            
        # Nearest-neighbor couplers:
        ############################
        # gate = gateSequence.pop(0)
        # gateSequence.append(gate)
        # for row in range(1, row_len, 2):
        #     for col in range(row_len):
        #         temp_row = row
        #         temp_col = col
        #         temp_row = temp_row + (1 if (gate & 2) else -1);
        #         temp_col = temp_col + (1 if (gate & 1) else 0)
        #
        #         if (temp_row < 0) or (temp_col < 0) or (temp_row >= row_len) or (temp_col >= row_len):
        #             continue
        #
        #         b1 = row * row_len + col
        #         b2 = temp_row * row_len + temp_col
        #
        #         if (b1 >= width) or (b2 >= width):
        #             continue
        #
        #         g = random.choice(two_bit_gates)
        #         g_count = g(circ, b1, b2)
        #         gate_count += g_count
        #         bit_depths[b1] += g_count
        #         bit_depths[b2] += g_count

        # Fully-connected couplers:
        ###########################
        bit_set = [i for i in range(width)]
        while len(bit_set) > 1:
            b1 = random.choice(bit_set)
            bit_set.remove(b1)
            b2 = random.choice(bit_set)
            bit_set.remove(b2)
            g = random.choice(two_bit_gates)
            g_count = g(circ, b1, b2)
            gate_count += g_count
            bit_depths[b1] += g_count
            bit_depths[b2] += g_count

    # print("Gate count (before optimization): ", gate_count)
    # This might not be right:
    # print("Depth of critical path (before optimization): ", max(bit_depths))

    return circ


def main():
    qsim = QrackSimulator(width, isSchmidtDecomposeMulti=False, isSchmidtDecompose=False, isOpenCL=False)
    random_circuit(width, qsim)
    qsim.out_to_file('qrack_circuit.chp')
    circ = QrackSimulator.file_to_qiskit_circuit('qrack_circuit.chp')
    
    tc.set_dtype("complex64")
    net = tc.Circuit.from_qiskit(circ)
    for b in range(width, circ.width()):
        net.post_select(b, keep=0)
    net = tcsc.simple_compile(net)[0]

    print(net.sample(allow_state=True, batch=1024, format="count_dict_bin"))


if __name__ == "__main__":
    main()

