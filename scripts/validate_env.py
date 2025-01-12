#!/usr/bin/env python3
"""
Validate the environment setup for the Arab-Andalusian motif analysis project.
"""

import sys
import pkg_resources
import logging
from pathlib import Path

# Setup logging
logging.basicConfig(
    format="%(asctime)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)


def check_python_version():
    """Check if Python version meets requirements."""
    required_version = (3, 8)
    current_version = sys.version_info[:2]

    if current_version < required_version:
        logger.error(
            f"Python {required_version[0]}.{required_version[1]} or higher required"
        )
        return False

    logger.info(f"Python version OK: {sys.version}")
    return True


def check_dependencies():
    """Check if all required packages are installed with correct versions."""
    requirements_path = Path(__file__).parent.parent / "requirements.txt"

    try:
        with open(requirements_path) as f:
            requirements = [
                line.strip() for line in f if line.strip() and not line.startswith("#")
            ]

        pkg_resources.require(requirements)
        logger.info("All required packages are installed with correct versions")
        return True

    except pkg_resources.DistributionNotFound as e:
        logger.error(f"Missing package: {e}")
        return False
    except pkg_resources.VersionConflict as e:
        logger.error(f"Version conflict: {e}")
        return False


def check_directories():
    """Check if required directories exist."""
    root = Path(__file__).parent.parent
    required_dirs = ["scores", "plots", "src", "tests"]

    all_exist = True
    for dir_name in required_dirs:
        dir_path = root / dir_name
        if not dir_path.exists():
            logger.error(f"Required directory missing: {dir_name}")
            all_exist = False
        else:
            logger.info(f"Directory exists: {dir_name}")

    return all_exist


def main():
    """Run all validation checks."""
    checks = [
        ("Python version", check_python_version),
        ("Dependencies", check_dependencies),
        ("Directories", check_directories),
    ]

    all_passed = True
    for name, check in checks:
        logger.info(f"\nChecking {name}...")
        if not check():
            all_passed = False

    if all_passed:
        logger.info("\nAll checks passed! Environment is properly set up.")
        sys.exit(0)
    else:
        logger.error("\nSome checks failed. Please fix the issues above.")
        sys.exit(1)


if __name__ == "__main__":
    main()
