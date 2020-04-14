# Main script for detect, track and count object in real time 


# video stream 

# object detection deep CNN + tracking algorithms

import argparse

import cv2
import numpy as np

from classes import CLASSES_90
from sort import Sort  # Sort tracker 




parser = argparse.ArgumentParser()
parser.add_argument("-i", "--input",
                    help="Video path, stream URI, or camera ID ", default="demo.mkv")
parser.add_argument("-t", "--threshold", type=float, default=0.3,
                    help="Minimum score to consider")
parser.add_argument("-m", "--mode", choices=['detection', 'tracking'], default="tracking",
                    help="Either detection or tracking mode")

args = parser.parse_args()


# Open CV - add Camera 
if args.input.isdigit():
    args.input = int(args.input)


# Const
TRACKED_CLASSES = ["car", "person"]
BOX_COLOR = (23, 230, 210)
TEXT_COLOR = (255, 255, 255)
INPUT_SIZE = (300,300)

# Protobuf format 
config = "./ssd_mobilenet_v1_coco_2017_11_17.pbtxt.txt"
model = "frozen_inference_graph.pb"
detector = cv2.dnn.readNetFromTensorflow(model,config)


# Start 

# single bounding box 

def illustrate_box(image: np.ndarray, box: np.ndarray, caption: str) -> None:

    # extract size of image
    rows, cols = frame.shape[:2]

    points = box.reshape((2, 2)) * np.array([cols, rows])
    p1, p2 = points.astype(np.int32)


    # draw rectangle 
    cv2.rectangle(image, tuple(p1), tuple(p2), BOX_COLOR, thickness=4)


    # put caption 
    cv2.putText(
    image,
    caption,
    tuple(p1),
    cv2.FONT_HERSHEY_SIMPLEX,
    0.75,
    TEXT_COLOR,
    2)

    

