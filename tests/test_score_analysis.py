"""Tests for score analysis functions."""

import unittest
import music21
from src.score_analysis import load_score, extract_melody, identify_motifs


class TestScoreAnalysis(unittest.TestCase):
    def setUp(self):
        # Create a simple test score
        self.score = music21.stream.Score()
        part = music21.stream.Part()
        part.append(music21.note.Note("C4", quarterLength=1.0))
        part.append(music21.note.Note("D4", quarterLength=1.0))
        part.append(music21.note.Note("E4", quarterLength=1.0))
        self.score.append(part)

    def test_extract_melody(self):
        melody = extract_melody(self.score)
        self.assertEqual(len(melody.recurse().notes), 3)

    def test_identify_motifs(self):
        melody = extract_melody(self.score)
        motifs = identify_motifs(melody, min_length=2, max_length=3)
        # Should find 2 motifs of length 2 and 1 motif of length 3
        self.assertEqual(len(motifs), 3)


if __name__ == "__main__":
    unittest.main()
