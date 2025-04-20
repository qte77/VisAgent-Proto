"""
# Main application file

This file serves as the entry point for the vision processing application.
It demonstrates the usage of various functions from the utils package.
"""

import argparse

from utils.conveyor_detection import detect_conveyor_sections
from utils.logging_config import logger
from utils.segmentation import (
    segment_and_visualize,
    segment_conveyor_belt,
    segment_conveyor_belts,
)


def process_image(image_path, tasks):
    """
    Process the image with the specified tasks.

    Args:
        image_path (str): Path to the input image
        tasks (list): List of tasks to perform
    """
    results = {}

    if "conveyor_detection" in tasks:
        results["conveyor_detection"] = detect_conveyor_sections(image_path)

    if "segment_visualize" in tasks:
        results["segment_visualize"] = segment_and_visualize(image_path)

    if "conveyor_belt_segment" in tasks:
        results["conveyor_belt_segment"] = segment_conveyor_belt(image_path)

    if "conveyor_belts_segment" in tasks:
        results["conveyor_belts_segment"] = segment_conveyor_belts(image_path)

    return results


def main():
    parser = argparse.ArgumentParser(description="Vision processing application")
    parser.add_argument("image_path", help="Path to the input image")
    parser.add_argument(
        "--tasks",
        nargs="+",
        choices=[
            "conveyor_detection",
            "segment_visualize",
            "conveyor_belt_segment",
            "conveyor_belts_segment",
        ],
        default=[
            "conveyor_detection",
            "segment_visualize",
            "conveyor_belt_segment",
            "conveyor_belts_segment",
        ],
        help="Tasks to perform on the image",
    )
    args = parser.parse_args()

    logger.info("Starting vision processing tasks")

    results = process_image(args.image_path, args.tasks)

    for task, result in results.items():
        logger.info(f"{task.replace('_', ' ').title()} result: {result}")

    logger.info("Vision processing tasks completed")


if __name__ == "__main__":
    main()
