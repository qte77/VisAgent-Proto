"""
# Image processing utilities

This module provides utility functions for image processing tasks.
"""

from typing import Any

import numpy as np
from vision_agent.tools import load_image, save_image

from .logging_config import logger


def load_and_process_image(image_path: str) -> np.ndarray:
    """
    # Load and process image

    Loads an image from the given path and performs initial processing.

    Args:
        image_path (str): Path to the input image

    Returns:
        np.ndarray: Processed image
    """
    logger.info(f"Loading image from {image_path}")
    return load_image(image_path)


def save_processed_image(image: np.ndarray, output_path: str) -> str:
    """
    # Save processed image

    Saves the processed image to the specified output path.

    Args:
        image (np.ndarray): Processed image
        output_path (str): Path to save the output image

    Returns:
        str: Path of the saved image
    """
    logger.info(f"Saving processed image to {output_path}")
    save_image(image, output_path)
    return output_path


def filter_detections(
    detections: list[dict[str, Any]], threshold: float = 0.5
) -> list[dict[str, Any]]:
    """
    # Filter detections

    Filters detections based on a confidence threshold.

    Args:
        detections (List[Dict[str, Any]]): List of detections
        threshold (float): Confidence threshold for filtering

    Returns:
        List[Dict[str, Any]]: Filtered list of detections
    """
    logger.info(f"Filtering detections with threshold {threshold}")
    return [d for d in detections if d["score"] > threshold]


def calculate_length(section: dict[str, Any], width: int, height: int) -> float:
    """
    # Calculate length

    Calculates the length of a section based on its bounding box and image dimensions.

    Args:
        section (Dict[str, Any]): Section data
        width (int): Image width
        height (int): Image height

    Returns:
        float: Calculated length
    """
    x1, y1, x2, y2 = section["bbox"]
    return ((x2 - x1) * width) ** 2 + ((y2 - y1) * height) ** 2
