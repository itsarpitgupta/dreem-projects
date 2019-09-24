import cv2
import matplotlib.pyplot as plt
import numpy as np

from com.deepvision.constants import ToolType, Constant
from com.deepvision.exception.DataValidationException import DataValidationException
from com.deepvision.input.EdgeDetectionInput import EdgeDetectionInput
from com.deepvision.output.EdgeDetectionOutput import EdgeDetectionOutput
from com.deepvision.toolengine.ToolI import ToolI
from com.deepvision.util.displayutil import displayImageOutput


class EdgeDetectionTool(ToolI):

    def matches(type: ToolType) -> bool:
        return type == ToolType.ToolType.EDGE_DETECTION

    def process(self, input: EdgeDetectionInput) -> EdgeDetectionOutput:
        output = EdgeDetectionOutput();
        if input.method == Constant.CANNY_EDGE_DETECTION:
            output = self.cannyEdgeDetection(input.main_img, input.lower_threshold, input.upper_threshold,
                                             input.k_sizeX, input.k_sizeY, input.edge_thickness)
        else:
            output = ToolType.NO_TOOL
        return output;

    def cannyEdgeDetection(self, main_img, lower, upper, ksizX, ksizeY, edge_thickness) -> EdgeDetectionOutput:
        output = EdgeDetectionOutput()
        try:

            # validation
            if main_img is None or ksizX is None or ksizeY is None or edge_thickness is None:
                raise DataValidationException("main_img, ksizX, ksizeY or edge_thickness should not be none")

            if isinstance(main_img, np.ndarray):
                full_gray = main_img
            else:
                full_img = cv2.imread(main_img)
                full_gray = cv2.cvtColor(full_img, cv2.COLOR_BGR2GRAY)

            if lower is None or lower == 0:
                # LOWER THRESHOLD TO EITHER 0 OR 70% OF THE MEDIAN VALUE WHICH EVER IS GREATER
                lower = int(max(0, 0.7 * np.median(full_gray)))

            if upper is None or upper == 0:
                # UPPER THRESHOLD TO EITHER 130% OF THE MEDIAN VALUE OF THE 255, WHICH EVER IS SMALLER
                upper = int(min(255, 1.3 * np.median(full_gray)))

            blurred_img = cv2.blur(full_gray, ksize=(ksizX, ksizeY))

            edges = cv2.Canny(blurred_img, threshold1=lower, threshold2=upper)

            rows = edges[:, 1].size
            cols = edges[1, :].size

            count = 1
            for x in range(0, rows):
                for y in range(0, cols):
                    if edges[x, y] == 255:
                        for t in range(y + 1, y + edge_thickness):
                            if t < cols:
                                if edges[x, t] == 255:
                                    count += 1
                                else:
                                    break
                        if count >= edge_thickness:
                            output.points.append([x, y])
                    count = 1

            # Showing the result
            if self.display:
                displayImageOutput(main_img=full_gray, main_img_title="Original Image", result_img=edges,
                                   result_img_title='Edge Detection', title="")

            output.point_1 = output.points[0]
            output.point_2 = output.points[-1]
            output.point_mid = output.points[int(len(output.points) / 2)]
            output.status = Constant.TOOL_PASS

        except DataValidationException as data_exp:
            print('DataValidationException :', data_exp.msg)
            output.status = Constant.TOOL_FAIL
        except Exception as exp:
            print('Exception : ', exp.args)
            output.status = Constant.TOOL_FAIL

        return output