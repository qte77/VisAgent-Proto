"""
This module contains tests for the image segmentation functionality.
"""

import os

from utils.segmentation import (
    segment_and_visualize,
    segment_conveyor_belt,
    segment_conveyor_belts,
)

from .test_utils import get_test_image_path


def test_segment_conveyor_belt():
    """
    Test the segment_conveyor_belt function.

    This test checks if the function correctly segments a conveyor belt
    in the given image.
    """
    test_image = (
        "landing.ai_depositphotos_74665111-stock-photo-metal-roller-conveyor-system.jpg"
    )
    image_path = get_test_image_path(test_image)
    result = segment_conveyor_belt(image_path)

    assert isinstance(result, dict), "Result should be a dictionary"
    assert "segmentation" in result, "Result should contain 'segmentation' key"
    assert "output_image_path" in result, (
        "Result should contain 'output_image_path' key"
    )

    assert isinstance(result["segmentation"], list), "Segmentation should be a list"
    if result["segmentation"]:
        assert isinstance(result["segmentation"][0], dict), (
            "Segmentation items should be dictionaries"
        )
        assert "mask" in result["segmentation"][0], (
            "Segmentation items should contain 'mask' key"
        )

    assert isinstance(result["output_image_path"], str), (
        "Output image path should be a string"
    )
    assert result["output_image_path"].endswith(".jpg"), (
        "Output image should be a JPEG file"
    )
    assert os.path.exists(result["output_image_path"]), "Output image file should exist"


def test_segment_conveyor_belts():
    """
    Test the segment_conveyor_belts function.

    This test checks if the function correctly segments multiple conveyor belts
    and the spiral cooling system in the given image.
    """
    test_image = (
        "landing.ai_depositphotos_311935464-stock-photo-large-automated-round"
        "-conveyor-machine.jpg"
    )
    image_path = get_test_image_path(test_image)
    result = segment_conveyor_belts(image_path)

    assert isinstance(result, str), "Result should be a string (output path)"
    assert result.endswith(".jpg"), "Output image should be a JPEG file"
    assert os.path.exists(result), "Output image file should exist"


def test_segment_and_visualize():
    """
    Test the segment_and_visualize function.

    This test checks if the function correctly segments and visualizes
    objects in the given image.
    """
    test_image = (
        "landing.ai_depositphotos_119075536-stock-photo-loading"
        "-iron-ore-conveyor-machine.jpg"
    )
    image_path = get_test_image_path(test_image)
    result = segment_and_visualize(image_path)

    assert isinstance(result, dict), "Result should be a dictionary"
    assert "segmentation_results" in result, (
        "Result should contain 'segmentation_results'"
    )
    assert "visualized_image_path" in result, (
        "Result should contain 'visualized_image_path'"
    )
    assert isinstance(result["segmentation_results"], list), (
        "segmentation_results should be a list"
    )
    assert isinstance(result["visualized_image_path"], str), (
        "visualized_image_path should be a string"
    )
    assert os.path.exists(result["visualized_image_path"]), (
        "Output image file should exist"
    )
