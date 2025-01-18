"""
# Conveyor detection module

This module provides functions for detecting conveyor sections in images.
"""

from vision_agent.tools import (
    owl_v2_image,
    overlay_bounding_boxes
)
from .models import ConveyorSectionResult
from .image_processing import (
    load_and_process_image,
    save_processed_image,
    calculate_length,
)
from .logging_config import logger


def detect_conveyor_sections(image_path: str) -> ConveyorSectionResult:
    """
    # Detect conveyor sections

    Detects straight and curved conveyor sections in the given image.

    Args:
        image_path (str): Path to the input image

    Returns:
        ConveyorSectionResult: Result of conveyor section detection
    """
    logger.info("Starting conveyor section detection")
    image = load_and_process_image(image_path)
    height, width = image.shape[:2]

    detections = owl_v2_image(
        "straight conveyor belt, curved conveyor belt", image, box_threshold=0.1
    )
    straight_sections = [
        d for d in detections if d["label"] == "straight conveyor belt"
    ]
    curved_sections = [d for d in detections if d["label"] == "curved conveyor belt"]

    total_straight_length = sum(
        calculate_length(section, width, height) for section in straight_sections
    )
    total_curved_length = sum(
        calculate_length(section, width, height) for section in curved_sections
    )

    image_with_boxes = overlay_bounding_boxes(image, detections)
    visualization_path = save_processed_image(
        image_with_boxes, "conveyor_belt_detection.jpg"
    )

    return ConveyorSectionResult(
        straight_sections_count=len(straight_sections),
        curved_sections_count=len(curved_sections),
        total_straight_length=total_straight_length,
        total_curved_length=total_curved_length,
        visualization_path=visualization_path,
    )
