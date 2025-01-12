"""
Functions for analyzing musical scores and identifying motifs.
"""

from typing import List, Optional
from pathlib import Path
import music21
import numpy as np
import matplotlib.pyplot as plt
import logging

# Configure logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
handler = logging.StreamHandler()
handler.setFormatter(
    logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
)
logger.addHandler(handler)


def load_score(file_path: Path | str) -> music21.stream.Score:
    """
    Load a MusicXML score file.

    Args:
        file_path: Path to the MusicXML file

    Returns:
        Parsed music21 Score object

    Raises:
        music21.exceptions.Music21Exception: If file cannot be parsed
        FileNotFoundError: If file does not exist
    """
    logger.info(f"Loading score from {file_path}")
    try:
        score = music21.converter.parse(str(file_path))
        logger.info(f"Successfully loaded score with {len(score.parts)} parts")
        return score
    except Exception as e:
        logger.error(f"Failed to load score: {str(e)}")
        raise


def extract_melody(score: music21.stream.Score) -> music21.stream.Part:
    """
    Extract the main melody from a score.

    Args:
        score: The music21 Score object

    Returns:
        The first part of the score (assumed to be the melody)

    Raises:
        IndexError: If score has no parts
    """
    logger.info("Extracting melody from score")
    try:
        melody_part = score.parts[0]
        n_notes = len(melody_part.recurse().notes)
        logger.info(f"Successfully extracted melody with {n_notes} notes")
        return melody_part
    except Exception as e:
        logger.error(f"Failed to extract melody: {str(e)}")
        raise


def identify_motifs(
    melody: music21.stream.Part, min_length: int = 3, max_length: int = 8
) -> List[List[music21.note.Note]]:
    """
    Identify potential motifs in a melody.

    Args:
        melody: music21.stream.Part object containing the melody
        min_length: Minimum number of notes in a motif
        max_length: Maximum number of notes in a motif

    Returns:
        List of identified motifs, where each motif is a list of notes

    Raises:
        ValueError: If min_length > max_length or either is negative
    """
    if min_length > max_length:
        raise ValueError("min_length must be less than or equal to max_length")
    if min_length < 1 or max_length < 1:
        raise ValueError("Length parameters must be positive")

    logger.info(f"Identifying motifs (length {min_length}-{max_length})")
    try:
        notes = [n for n in melody.recurse().notes]
        motifs = []

        for length in range(min_length, max_length + 1):
            logger.debug(f"Processing motifs of length {length}")
            for i in range(len(notes) - length + 1):
                motif = notes[i : i + length]
                motifs.append(motif)

        logger.info(f"Found {len(motifs)} potential motifs")
        return motifs
    except Exception as e:
        logger.error(f"Failed to identify motifs: {str(e)}")
        raise


def plot_motif_occurrences(
    score: music21.stream.Score,
    motifs: List[List[music21.note.Note]],
    output_path: Optional[str] = None,
) -> None:
    """
    Plot the occurrences of motifs in a score.

    Args:
        score: music21.stream.Score object
        motifs: List of identified motifs
        output_path: Optional path to save the plot

    Raises:
        ValueError: If motifs list is empty
    """
    if not motifs:
        raise ValueError("Motifs list cannot be empty")

    logger.info("Plotting motif occurrences")
    try:
        plt.figure(figsize=(12, 6))
        # Implementation details would depend on how you want to visualize the motifs
        # This is a placeholder for the actual visualization logic

        if output_path:
            plt.savefig(output_path)
            logger.info(f"Saved plot to {output_path}")
        plt.close()
    except Exception as e:
        logger.error(f"Failed to plot motif occurrences: {str(e)}")
        raise
