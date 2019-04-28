from com.deepvision.constants.ToolType import ToolType
from com.deepvision.input.BaseInput import BaseInput
from com.deepvision.constants import Constant


class CornerDetectionInput(BaseInput):
    type = ToolType.CONTOUR_DETECTION
    method = Constant.HARRIS_CORNER_DETECTION
    threshold = 100
    blockSize = 2
    apertureSize = 3
    k_size = 0.04
    max_thresholding = 100