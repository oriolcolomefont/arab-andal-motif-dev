#!/usr/bin/env python3
"""
Basic example of analyzing motifs in a score.
"""

import logging
from pathlib import Path
from src.score_analysis import load_score, extract_melody, identify_motifs
from src.visualization import plot_motif_distribution, plot_motif_timeline

# Configure logging
logging.basicConfig(level=logging.INFO)


def main():
    # Load a score
    score_path = Path("scores/Btayhi_Iraq_Ajam.mxl")
    score = load_score(score_path)

    # Extract melody and identify motifs
    melody = extract_melody(score)
    motifs = identify_motifs(melody, min_length=3, max_length=8)

    # Create visualizations
    plot_motif_distribution(motifs, output_path="plots/motif_distribution.png")
    plot_motif_timeline(score, motifs, output_path="plots/motif_timeline.png")


if __name__ == "__main__":
    main()
