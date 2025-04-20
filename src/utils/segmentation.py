"""
# Segmentation module

This module provides functions for image segmentation tasks.
"""

import numpy as np
from vision_agent.tools import florence2_sam2_image, overlay_segmentation_masks

from .image_processing import (
    filter_detections,
    load_and_process_image,
    save_processed_image,
)
from .logging_config import logger
from .models import BoundingBox, Segmentation, SegmentationResult


def segment_and_visualize(image_path: str) -> SegmentationResult:
    """
    # Segment and visualize

    Segments and visualizes objects in the given image.

    Args:
        image_path (str): Path to the input image

    Returns:
        SegmentationResult: Result of segmentation and visualization
    """
    logger.info("Starting segmentation and visualization")
    image = load_and_process_image(image_path)

    segmentation_results = florence2_sam2_image(
        "stacker reclaimer, iron ore piles", image
    )
    filtered_results = filter_detections(segmentation_results)

    merged_results = []
    iron_ore_masks = []
    for result in filtered_results:
        if result["label"] == "iron ore piles":
            iron_ore_masks.append(result["mask"])
        else:
            merged_results.append(result)

    if iron_ore_masks:
        merged_iron_ore_mask = np.logical_or.reduce(iron_ore_masks)
        merged_results.append(
            {
                "label": "iron ore piles",
                "mask": merged_iron_ore_mask,
                "score": 1.0,
                "bbox": BoundingBox(x1=0, y1=0, x2=1, y2=1),
            }
        )

    visualized_image = overlay_segmentation_masks(image, merged_results)
    output_path = save_processed_image(visualized_image, "segmentation_result.jpg")

    return SegmentationResult(
        segmentation_results=[Segmentation(**result) for result in merged_results],
        visualized_image_path=output_path,
    )


def segment_conveyor_belt(image_path: str) -> dict[str, list[Segmentation] | str]:
    """
    # Segment conveyor belt

    Segments the conveyor belt in the given image.

    Args:
        image_path (str): Path to the input image

    Returns:
        Dict[str, Union[List[Segmentation], str]]:
        Segmentation result and output image path
    """
    logger.info("Starting conveyor belt segmentation")
    image = load_and_process_image(image_path)

    detections = florence2_sam2_image("conveyor belt", image)

    if len(detections) > 1:
        largest_segment = max(detections, key=lambda x: np.sum(x["mask"]))
        detections = [largest_segment]

    highlighted_image = overlay_segmentation_masks(image, detections)
    output_path = save_processed_image(highlighted_image, "segmented_conveyor_belt.jpg")

    return {
        "segmentation": [Segmentation(**detection) for detection in detections],
        "output_image_path": output_path,
    }


def segment_conveyor_belts(image_path: str) -> str:
    """
    # Segment conveyor belts and spiral cooling system

    Segments conveyor belts and spiral cooling system in the given image.

    Args:
        image_path (str): Path to the input image

    Returns:
        str: Path to the output image with highlighted segments
    """
    logger.info("Starting conveyor belts and spiral cooling system segmentation")
    image = load_and_process_image(image_path)

    segmentations = florence2_sam2_image("conveyor belts, spiral cooling system", image)
    filtered_segmentations = filter_detections(segmentations)

    highlighted_image = overlay_segmentation_masks(
        image, filtered_segmentations, draw_label=True
    )
    return save_processed_image(highlighted_image, "highlighted_conveyor_belts.jpg")
