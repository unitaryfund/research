"""Functionality for saving and loading experiment data."""
import os
import pickle

from .ewfs import compute_violations


def save_data(
    results: dict,
    friend_size: int,
    trial: int,
    shots: int,
    data_path: str,
    backend_name: str | None = None,
) -> None:
    """Writes data to a file name format of `<MACHINE_NAME>_qubits_<NUM_QUBITS>_trial_<TRIAL>_shots_<NUM_SHOTS>`."""
    qubits = friend_size

    # If not output file name is given, use this format.
    output_file_name = f"{backend_name}_qubits_{qubits}_trial_{trial}_shots_{shots}.pickle"
    output_path = os.path.join(data_path, output_file_name)

    print(f"Writing data to: {output_path}")
    with open(output_path, "wb") as handle:
        pickle.dump(results, handle, protocol=pickle.HIGHEST_PROTOCOL)


def load_experiments(
    machine_name: str,
    friend_sizes: list[int],
    num_trials: int,
    shots: int,
    data_path: str,
    strategy: str,
) -> dict:
    """Load experiments from multiple files."""
    all_results = {
        fs: {inequality: [] for inequality in ["semi_brukner"]}
        for fs in friend_sizes
    }

    for friend_size in friend_sizes:
        for trial in range(1, num_trials+1):
            with open(os.path.join(data_path, f"{machine_name}_qubits_{friend_size}_trial_{trial}_shots_{shots}.pickle"), "rb") as file:
                results = pickle.load(file)
            violations = compute_violations(results=results, charlie_size=friend_size, debbie_size=1, strategy=strategy)
            for key in violations:
                all_results[friend_size][key].append(violations[key])
    return all_results
