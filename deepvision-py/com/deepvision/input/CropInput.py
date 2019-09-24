from com.deepvision.constants import Constant
from com.deepvision.constants.ToolType import ToolType
from com.deepvision.input.BaseInput import BaseInput


class CropInput(BaseInput):

    def __init__(self, main_ing, type, method, top_left, bottom_right, start_percentage, end_percentage, next_tool):
        self.type = type
        self.top_left = top_left
        self.bottom_right = bottom_right
        self.main_img = main_ing
        self.method = method
        self.start_percentage = start_percentage
        self.end_percentage = end_percentage
        self.next_tool = next_tool

    # default values
    type = ToolType.CROP
    method = Constant.CROP_BY_POINT
    top_left = []
    bottom_right = []
    start_percentage = 0.0
    end_percentage = 0.0
    next_tool = []