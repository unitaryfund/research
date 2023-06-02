# Expect to be able to use about 1-to-2 GB less than the total GPU VRAM
export QRACK_MAX_ALLOC_MB=79872
# This is >64 GB of general RAM "heap" for simulation, excluding operating system load.
export QRACK_MAX_PAGING_QB=33
# For FP32 precision, an A100 can do 31 qb in a single "page." (16 GB).
# Most or all NVIDIA GPUs have 4 "segments," so we can do 4 "pages."
# This is 33 qb in total, for "naive Schrödinger method."
export QRACK_MAX_CPU_QB=33
# Because GPUs can't generally handle the memory fragmentation multiple max-footprint pages,
# (31 qb being max for a page or segment, for the NVIDIA A100,)
# we instead do 8 pages of 30 qb, (still 33 qb in total).
export QRACK_MAX_PAGE_QB=30
for i in {1..100}; do
    ./benchmarks --optimal-single --single --max-qubits=54 --benchmark-depth=4 test_noisy_fidelity_2qb_nn_estimate
done >> test_noisy_fidelity_2qb_nn_estimate_m4.txt
for i in {1..100}; do
    ./benchmarks --optimal-single --single --max-qubits=54 --benchmark-depth=5 test_noisy_fidelity_2qb_nn_estimate
done >> test_noisy_fidelity_2qb_nn_estimate_m5.txt
for i in {1..100}; do
    ./benchmarks --optimal-single --single --max-qubits=54 --benchmark-depth=6 test_noisy_fidelity_2qb_nn_estimate
done >> test_noisy_fidelity_2qb_nn_estimate_m6.txt
for i in {1..100}; do
    ./benchmarks --optimal-single --single --max-qubits=54 --benchmark-depth=7 test_noisy_fidelity_2qb_nn_estimate
done >> test_noisy_fidelity_2qb_nn_estimate_m7.txt
for i in {1..100}; do
    ./benchmarks --optimal-single --single --max-qubits=54 --benchmark-depth=8 test_noisy_fidelity_2qb_nn_estimate
done >> test_noisy_fidelity_2qb_nn_estimate_m8.txt
for i in {1..100}; do
    ./benchmarks --optimal-single --single --max-qubits=54 --benchmark-depth=9 test_noisy_fidelity_2qb_nn_estimate
done >> test_noisy_fidelity_2qb_nn_estimate_m9.txt
for i in {1..100}; do
    ./benchmarks --optimal-single --single --max-qubits=54 --benchmark-depth=10 test_noisy_fidelity_2qb_nn_estimate
done >> test_noisy_fidelity_2qb_nn_estimate_m10.txt
for i in {1..100}; do
    ./benchmarks --optimal-single --single --max-qubits=54 --benchmark-depth=11 test_noisy_fidelity_2qb_nn_estimate
done >> test_noisy_fidelity_2qb_nn_estimate_m11.txt
for i in {1..100}; do
    ./benchmarks --optimal-single --single --max-qubits=54 --benchmark-depth=12 test_noisy_fidelity_2qb_nn_estimate
done >> test_noisy_fidelity_2qb_nn_estimate_m12.txt
for i in {1..100}; do
    ./benchmarks --optimal-single --single --max-qubits=54 --benchmark-depth=13 test_noisy_fidelity_2qb_nn_estimate
done >> test_noisy_fidelity_2qb_nn_estimate_m13.txt
for i in {1..100}; do
    ./benchmarks --optimal-single --single --max-qubits=54 --benchmark-depth=14 test_noisy_fidelity_2qb_nn_estimate
done >> test_noisy_fidelity_2qb_nn_estimate_m14.txt
for i in {1..100}; do
    ./benchmarks --optimal-single --single --max-qubits=54 --benchmark-depth=15 test_noisy_fidelity_2qb_nn_estimate
done >> test_noisy_fidelity_2qb_nn_estimate_m15.txt
for i in {1..100}; do
    ./benchmarks --optimal-single --single --max-qubits=54 --benchmark-depth=16 test_noisy_fidelity_2qb_nn_estimate
done >> test_noisy_fidelity_2qb_nn_estimate_m16.txt
for i in {1..100}; do
    ./benchmarks --optimal-single --single --max-qubits=54 --benchmark-depth=17 test_noisy_fidelity_2qb_nn_estimate
done >> test_noisy_fidelity_2qb_nn_estimate_m17.txt
for i in {1..100}; do
    ./benchmarks --optimal-single --single --max-qubits=54 --benchmark-depth=18 test_noisy_fidelity_2qb_nn_estimate
done >> test_noisy_fidelity_2qb_nn_estimate_m18.txt
for i in {1..100}; do
    ./benchmarks --optimal-single --single --max-qubits=54 --benchmark-depth=19 test_noisy_fidelity_2qb_nn_estimate
done >> test_noisy_fidelity_2qb_nn_estimate_m19.txt
for i in {1..100}; do
    ./benchmarks --optimal-single --single --max-qubits=54 --benchmark-depth=20 test_noisy_fidelity_2qb_nn_estimate
done >> test_noisy_fidelity_2qb_nn_estimate_m20.txt
