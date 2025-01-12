"""
Functions for visualizing musical analysis results.
"""

from typing import List, Optional, Any, Tuple
import matplotlib.pyplot as plt
import numpy as np
import music21


def plot_motif_distribution(
    motifs: List[Any],
    title: str = "Motif Distribution",
    output_path: Optional[str] = None,
) -> None:
    """
    Plot the distribution of motif lengths and occurrences.

    Args:
        motifs: List of identified motifs
        title: Plot title
        output_path: Optional path to save the plot

    Raises:
        ValueError: If motifs list is empty
    """
    if not motifs:
        raise ValueError("Motifs list cannot be empty")

    lengths = [len(m) for m in motifs]

    plt.figure(figsize=(10, 6))
    plt.hist(lengths, bins="auto")
    plt.title(title)
    plt.xlabel("Motif Length")
    plt.ylabel("Frequency")

    if output_path:
        plt.savefig(output_path)
    plt.close()


def plot_motif_timeline(
    score: music21.stream.Score,
    motifs: List[List[music21.note.Note]],
    output_path: Optional[str] = None,
) -> None:
    """
    Plot motifs along a timeline of the score.

    Args:
        score: music21.stream.Score object
        motifs: List of identified motifs
        output_path: Optional path to save the plot

    Raises:
        ValueError: If motifs list is empty or score has no parts
    """
    if not motifs:
        raise ValueError("Motifs list cannot be empty")
    if not score.parts:
        raise ValueError("Score must have at least one part")

    plt.figure(figsize=(15, 8))
    # Implementation would depend on how you want to visualize the timeline
    # This is a placeholder for the actual visualization logic

    if output_path:
        plt.savefig(output_path)
    plt.close()


def create_colormap(n_motifs: int) -> np.ndarray:
    """
    Create a colormap for visualizing different motifs.

    Args:
        n_motifs: Number of motifs to create colors for

    Returns:
        Array of RGBA color values

    Raises:
        ValueError: If n_motifs is less than 1
    """
    if n_motifs < 1:
        raise ValueError("Number of motifs must be positive")

    return plt.cm.viridis(np.linspace(0, 1, n_motifs))
