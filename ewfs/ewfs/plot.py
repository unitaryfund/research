import numpy as np
from ewfs.ewfs import calculate_branch_factor


def plot_results(
    ax,
    results: dict, 
    friend_sizes: list[int], 
    plot_title: str,
    plot_error_bars: bool = False,
    color: str = "tab:blue",
    label: str | None = None,
    show_legend: bool = False,
    marker: str = "o",
    marker_size: float = 10,
    line_width: float = 2.5,
    y_min: float | None = None,
    y_max: float | None = None,
    optimal_threshold: float = 0.380364,
):
    # Compute averages and standard deviations
    avg_results = {}
    std_results = {}
    for fs in results:
        avg_results[fs] = {}
        std_results[fs] = {}
        for key in results[fs]:
            avg_results[fs][key] = np.mean(results[fs][key])
            if plot_error_bars:
                std_results[fs][key] = np.std(results[fs][key])

    for _, key in enumerate(["semi_brukner"]):
        means = [np.mean(results[fs][key]) for fs in friend_sizes]
        errors = [(3/np.sqrt(len(results[fs][key])))*np.std(results[fs][key]) for fs in friend_sizes] if plot_error_bars else None
        ax.plot(
            friend_sizes,
            means,
            label=label,
            marker=marker,
            markersize=marker_size,
            linestyle="-",
            linewidth=line_width,
            color=color,
        )
        if plot_error_bars:
            ax.errorbar(friend_sizes, means, yerr=errors, fmt="none", color=color, capsize=5, elinewidth=line_width)

    # ax.axhline(optimal_threshold, color="tab:green", linestyle="dashed", label="_nolegend_", linewidth=line_width)
    # ax.axhline(0, color="tab:red", linestyle="dotted", label="_nolegend_", linewidth=line_width)

    ax.set_xticks(friend_sizes)
    ax.set_title(plot_title)
    ax.grid(True)

    if y_min is not None and y_max is not None:
        ax.set_ylim(y_min, y_max)    

    if show_legend:
        ax.legend()


def add_branch_factor_axis(ax, friend_sizes, size="large"):
    """Function to create the second x-axis for branch factor at the bottom."""
    ax2 = ax.secondary_xaxis(-0.2)  # Place the second x-axis below the main one
    branch_factors = [calculate_branch_factor(fs) for fs in friend_sizes]
    ax2.set_xticks(friend_sizes)
    ax2.set_xticklabels(branch_factors)
    ax2.set_xlabel("Branch Factor", fontsize=size)
    ax2.tick_params(axis="x", labelsize=size)
    return ax2
