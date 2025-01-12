"""
Configuration settings for the Arab-Andalusian motif analysis project.
"""

from pathlib import Path

# Project paths
PROJECT_ROOT = Path(__file__).parent
SCORES_DIR = PROJECT_ROOT / "scores"
PLOTS_DIR = PROJECT_ROOT / "plots"

# Analysis settings
MIN_MOTIF_LENGTH = 3
MAX_MOTIF_LENGTH = 8
MIN_MOTIF_OCCURRENCES = 2

# Visualization settings
FIGURE_DPI = 300
FIGURE_FORMAT = "png"
DEFAULT_FIGSIZE = (12, 6)

# Logging settings
LOG_FORMAT = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
LOG_LEVEL = "INFO"

# Color settings
COLORMAP = "viridis"
ALPHA = 0.7  # Transparency for plot elements
