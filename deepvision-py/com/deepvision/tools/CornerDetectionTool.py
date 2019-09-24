import cv2
import numpy as np

from com.deepvision.constants import ToolType, Constant
from com.deepvision.exception.DataValidationException import DataValidationException
from com.deepvision.input.CornerDetectionInput import CornerDetectionInput
from com.deepvision.output.CornerDetectionOutput import CornerDetectionOutput
from com.deepvision.toolengine.ToolI import ToolI
from com.deepvision.util.displayutil import displayImageOutput


class CornerDetectionTool(ToolI):
    source_window = 'Source image'
    corners_window = 'Corners detected'
    max_thresh = 255

    def matches(type: ToolType) -> bool:
        return type == ToolType.ToolType.CORNER_DETECTION

    def process(self, input: CornerDetectionInput) -> CornerDetectionOutput:
        output = CornerDetectionOutput();

        if input.method == Constant.HARRIS_CORNER_DETECTION:
            output = self.harisCornerDetection(input.main_img, input.threshold, input.blockSize, input.apertureSize,
                                               input.k_size)
        elif input.method == Constant.SHI_TOMASI_AND_GOOD_FEATURES_TO_TRACK_CORNER_DETECTION:
            output = self.shiTomasiAndGoodFeaturesToTrack(input.main_img, input.maxCorners)
        else:
            output = ''
        return output;

    def harisCornerDetection(self, main_img, threshold, blockSize, apertureSize, k_size) -> CornerDetectionOutput:
        output = CornerDetectionOutput();
        try:
            # validation
            if main_img is None or threshold is None or blockSize is None or apertureSize is None or k_size is None:
                raise DataValidationException("main_img, threshold, blockSize, apertureSize or k_size is none")

            # reading the main image
            if isinstance(main_img, str):
                full = cv2.imread(main_img, cv2.IMREAD_GRAYSCALE)
            else:
                full = main_img

            # Detecting corners
            dst = cv2.cornerHarris(full, blockSize, apertureSize, k_size)
            # Normalizing
            dst_norm = np.empty(dst.shape, dtype=np.float32)
            cv2.normalize(dst, dst_norm, alpha=0, beta=255, norm_type=cv2.NORM_MINMAX)
            dst_norm_scaled = cv2.convertScaleAbs(dst_norm)

            # Drawing a circle around corners
            for i in range(dst_norm.shape[0]):
                for j in range(dst_norm.shape[1]):
                    if int(dst_norm[i, j]) > threshold:
                        output.corners.append([i, j])
                        cv2.circle(dst_norm_scaled, (j, i), 5, (0), 5)
            # Showing the result

            output.status = Constant.TOOL_PASS
            output.point_1 = output.corners[0]
            output.point_2 = output.corners[-1]

            if self.display:
                displayImageOutput(main_img=full, main_img_title=self.source_window, result_img=dst_norm_scaled,
                                   result_img_title=self.corners_window
                                   , title="Corner Detection" + " [" + output.status + "]")

        except DataValidationException as data_exp:
            print('DataValidationException :', data_exp.msg)
            output.status = Constant.TOOL_FAIL
        except Exception as exp:
            print('Exception : ', exp.args)
            output.status = Constant.TOOL_FAIL

        return output

    def shiTomasiAndGoodFeaturesToTrack(self, main_img, maxCorners) -> CornerDetectionOutput:
        output = CornerDetectionOutput()
        try:
            # validation
            if main_img is None or maxCorners is 0:
                raise DataValidationException("main_img or maxCorners is none")

            # reading the main image
            if isinstance(main_img, str):
                full_img = cv2.imread(main_img, cv2.IMREAD_GRAYSCALE)
            else:
                full_img = main_img

            corners = cv2.goodFeaturesToTrack(full_img, maxCorners, 0.01, 10)
            corners = np.int0(corners)

            # Drawing a circle around corners
            for i in corners:
                x, y = i.ravel()
                output.corners.append([x, y])
                cv2.circle(full_img, (x, y), 3, (0, 255, 0), 5)

            # Showing the result
            output.status = Constant.TOOL_PASS
            output.point_1 = output.corners[0]
            output.point_2 = output.corners[-1]

            if self.display:
                displayImageOutput(main_img=full_img, main_img_title="Original Image", result_img=full_img,
                                   result_img_title="Result Image"
                                   , title="Corner Detection" + " [" + output.status + "]")


        except DataValidationException as data_exp:
            print('DataValidationException :', data_exp.msg)
            output.status = Constant.TOOL_FAIL
        except Exception as exp:
            print('Exception : ', exp.args)
            output.status = Constant.TOOL_FAIL
        return output