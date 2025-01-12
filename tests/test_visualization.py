"""Tests for visualization functions."""

import unittest
import numpy as np
from src.visualization import create_colormap, plot_motif_distribution
import tempfile
import os


class TestVisualization(unittest.TestCase):
    def test_create_colormap(self):
        n_motifs = 5
        colors = create_colormap(n_motifs)
        self.assertEqual(len(colors), n_motifs)
        self.assertEqual(colors.shape, (n_motifs, 4))  # RGBA values

    def test_plot_motif_distribution(self):
        # Create dummy motifs
        class DummyMotif:
            def __init__(self, length):
                self.length = length

            def __len__(self):
                return self.length

        motifs = [DummyMotif(i) for i in range(3, 6)]

        # Test plotting to a temporary file
        with tempfile.NamedTemporaryFile(suffix=".png", delete=False) as tmp:
            plot_motif_distribution(motifs, output_path=tmp.name)
            self.assertTrue(os.path.exists(tmp.name))
            self.assertTrue(os.path.getsize(tmp.name) > 0)
            os.unlink(tmp.name)


if __name__ == "__main__":
    unittest.main()
