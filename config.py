from gpiozero import LED

# File paths of the core AI model, do not touch.
MODEL_NAME = "./"
GRAPH_NAME = "detect.tflite"
LABELMAP_NAME = "labelmap.txt"

# Decimal threshold which determines the needed confidence of an object's existence to acknowledge it.
min_conf_threshold = float(.5)

# Video resolution of our input
resW, resH = 640, 480
imW, imH = int(resW), int(resH)

# Do we have an accelerator? We don't btw.
use_TPU = False

# Webcam ID
device_id = 0

# device_id = "./vid_small.mp4" # Comment/uncomment this to use the testing video

# X-ranges for detected objects to light up LEDs.
center = (256, 384)
right = (384, 512)
far_right = (512, 640)
left = (128, 256)
far_left = (0, 128)

# How long a range needs to be active to trigger.
threshold = 2

# How big an object needs to appear
scale = 60

# How often we clear the ranges.
duration = 10

# Classes to acknowledge
detections = [
    "person",
    "bicycle",
    "car",
    "motorcycle",
    "bus",
    "truck"
]

# Turn this on if we are using this code on the raspberry pi.
rpi = False

if rpi:
    # LED config, assign GPIO pins
    pins = [LED(22), LED(27),  LED(17),  LED(23),  LED(24)]
