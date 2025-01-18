"""
This module contains utility functions for testing.
"""

import os


def get_test_image_path(image_name):
    """
    Get the full path of a test image.

    Args:
        image_name (str): Name of the test image file.

    Returns:
        str: Full path to the test image.
    """
    return os.path.join(
        os.path.dirname(os.path.dirname(__file__)), "assets", "images", image_name
    )
