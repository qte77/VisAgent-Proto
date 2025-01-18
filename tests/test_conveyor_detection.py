"""
This module contains tests for the conveyor detection functionality.
"""

import os
from src.utils.conveyor_detection import detect_conveyor_sections
from .test_utils import get_test_image_path


def test_detect_conveyor_sections():
    """
    Test the detect_conveyor_sections function.
    
    This test checks if the function correctly detects straight and curved
    conveyor sections in the given image.
    """
    test_image = "landing.ai_depositphotos_74665111-stock-photo-metal-roller-conveyor-system.jpg"
    image_path = get_test_image_path(test_image)
    result = detect_conveyor_sections(image_path)
    
    assert isinstance(result, dict), "Result should be a dictionary"
    assert "straight_sections_count" in result, "Result should contain 'straight_sections_count'"
    assert "curved_sections_count" in result, "Result should contain 'curved_sections_count'"
    assert "total_straight_length" in result, "Result should contain 'total_straight_length'"
    assert "total_curved_length" in result, "Result should contain 'total_curved_length'"
    assert "visualization_path" in result, "Result should contain 'visualization_path'"
    
    assert isinstance(result["straight_sections_count"], int), "straight_sections_count should be an integer"
    assert isinstance(result["curved_sections_count"], int), "curved_sections_count should be an integer"
    assert isinstance(result["total_straight_length"], (int, float)), "total_straight_length should be a number"
    assert isinstance(result["total_curved_length"], (int, float)), "total_curved_length should be a number"
    assert isinstance(result["visualization_path"], str), "visualization_path should be a string"
    assert os.path.exists(result["visualization_path"]), "Visualization image file should exist"
