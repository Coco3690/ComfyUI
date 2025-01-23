# coco_prefix.py

# 定义一个新的节点类
class CoCoPrefix:  # 修改这里
    # 定义节点的输入类型和默认值
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "width": ("INT", {"default": 512, "min": 1}),
                "height": ("INT", {"default": 512, "min": 1}),
                "a_string": ("STRING", {"default": "默认字符串", "multiline": False})
            }
        }

    # 定义节点的输出类型
    RETURN_TYPES = ("STRING",)

    # 定义节点的计算函数名称
    FUNCTION = "calculate_output_string"

    # 定义节点在ComfyUI中的分类
    CATEGORY = "Custom Nodes"

    # 定义计算函数，用于处理输入并返回输出
    def calculate_output_string(self, width, height, a_string):
        # 将width和height转换为字符串
        width_str = str(width)
        height_str = str(height)
        # 按照要求的格式计算输出字符串
        output_string = f"{width_str}x{height_str}~{a_string}"
        return (output_string,)

# 定义 NODE_CLASS_MAPPINGS 变量，将节点类名映射到节点类
NODE_CLASS_MAPPINGS = {
    "CoCoPrefix": CoCoPrefix  # 修改这里
}

# 定义 NODE_DISPLAY_NAME_MAPPINGS 变量，将节点类名映射到节点显示名称
NODE_DISPLAY_NAME_MAPPINGS = {
    "CoCoPrefix": "CoCoPrefix"  # 修改这里
}
