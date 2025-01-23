from .nodes import *
from .coco_prefix import CoCoPrefix  # 修改这里

NODE_CLASS_MAPPINGS = {
    "Print Hello World": PrintHelloWorld,
    "Concatenate Hello World": ConcatenateHelloWorld,
    "Hello World Overlay Text": HelloWorldOverlayText,
    "CoCoPrefix": CoCoPrefix,  # 修改这里
}

print("\033[34mComfyUI CoCo Prefix: \033[92mLoaded\033[0m")
