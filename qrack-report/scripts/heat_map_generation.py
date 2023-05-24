import click
import csv
import os
import time
from pyqrack import QrackSimulator, QrackCircuit

def create_csv(filename):
    file_exists = os.path.isfile(filename)
    csvfile = open(filename, 'a')

    headers = ['trial', 'width', 'depth', 'sdrp', 'time', 'fidelity']
    writer = csv.DictWriter(csvfile, delimiter=',', lineterminator='\n',fieldnames=headers)

    if not file_exists:
        writer.writeheader()  # file doesn't exist yet, write a header

    return writer

def write_csv(writer, data):
    writer.writerow(data)

@click.command()
@click.option('--trial', default=0, help='Which trial index to run (for depth and width)')
@click.option('--width', default=36, help='Which width to run (for trial and depth')
@click.option('--depth', default=36, help='Which depth to run (for trial and width')
@click.option('--sdrp', default=80, help='SDRP level setting for this case')
@click.option('--out', default='heat_map_data.csv', help='Where to store the CSV output of each test')
def bench(trial, width, depth, sdrp, out):
    sdrp = sdrp * 0.0125
    circ = QrackCircuit()

    # Load circuit definition from file
    circ.in_from_file("heat_map_circuits/trial_" + str(trial) + "_w" + str(width) + "_d" + str(depth))

    sim = QrackSimulator(width)
    if sdrp > 0:
        sim.set_sdrp(sdrp)

    start = time.perf_counter()
    circ.run(sim)
    end = time.perf_counter()

    writer = create_csv(out)

    write_csv(writer, { 'trial': trial, 'width': width, 'depth': depth, 'sdrp': sdrp, 'time': (end - start), 'fidelity': sim.get_unitary_fidelity() })

if __name__ == '__main__':
    bench()
