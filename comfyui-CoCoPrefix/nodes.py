import numpy as np
import torch
from PIL import Image, ImageDraw, ImageFont

def pil2tensor(image):
    return torch.from_numpy(np.array(image).astype(np.float32) / 255.0).unsqueeze(0)

class PrintHelloWorld:
    """
    用于打印文本的节点类
    """
    @classmethod
    def INPUT_TYPES(cls):
        """
        定义节点的输入类型和默认值
        """
        return {
            "required": {
                "text": ("STRING", {"multiline": False, "default": "Hello World"}),
            }
        }

    RETURN_TYPES = ()
    FUNCTION = "print_text"
    OUTPUT_NODE = True
    CATEGORY = "🧩 Tutorial Nodes"

    def print_text(self, text):
        """
        打印文本的函数
        """
        print(f"Tutorial Text : {text}")
        return {}

class ConcatenateHelloWorld:
    """
    用于拼接两个文本的节点类
    """
    @classmethod
    def INPUT_TYPES(cls):
        """
        定义节点的输入类型和默认值
        """
        return {
            "required": {
                "text1": ("STRING", {"multiline": False, "default": "Hello"}),
                "text2": ("STRING", {"multiline": False, "default": "World"}),
            }
        }

    RETURN_TYPES = ("STRING",)
    FUNCTION = "concatenate_text"
    CATEGORY = "🧩 Tutorial Nodes"

    def concatenate_text(self, text1, text2):
        """
        拼接文本的函数
        """
        text_out = text1 + " " + text2
        return (text_out,)

class HelloWorldOverlayText:
    """
    用于在图像上叠加文本的节点类
    """
    @classmethod
    def INPUT_TYPES(cls):
        """
        定义节点的输入类型和默认值
        """
        return {
            "required": {
                "image_width": ("INT", {"default": 512, "min": 64, "max": 2048}),
                "image_height": ("INT", {"default": 512, "min": 64, "max": 2048}),
                "text": ("STRING", {"multiline": True, "default": "Hello World"}),
                "font_size": ("INT", {"default": 50, "min": 1, "max": 1024}),
                "font_color": (["white", "black", "red", "green", "blue", "yellow"],),
                "background_color": (["white", "black", "red", "green", "blue", "yellow"],),
            }
        }

    RETURN_TYPES = ("IMAGE",)
    # RETURN_NAMES = ("IMAGE",)
    FUNCTION = "draw_overlay_text"
    CATEGORY = "🧩 Tutorial Nodes"

    def draw_overlay_text(self, image_width, image_height, text,
                          font_size, font_color, background_color):
        """
        在图像上绘制叠加文本的函数
        """
        # based on https://stackoverflow.com/questions/1970807/center-middle-align-text-with-pil

        # Create a new PIL image
        new_img = Image.new("RGBA", (image_width, image_height), background_color)
        draw = ImageDraw.Draw(new_img)

        # Define font
        font = ImageFont.truetype("arial.ttf", size=font_size)

        # Get the image center
        image_center_x = image_width / 2
        image_center_y = image_height / 2

        # Draw the text, mm = text center
        draw.text((image_center_x, image_center_y), text, fill=font_color, font=font, anchor="mm")

        # Convert the PIL image to a torch tensor
        image_out = pil2tensor(new_img)

        return (image_out,)