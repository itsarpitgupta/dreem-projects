from scipy.spatial import distance as dist

from com.deepvision.constants import ToolType, Constant
from com.deepvision.input.DistanceDetectionInput import DistanceDetectionInput
from com.deepvision.output.DistanceDetectionOutput import DistanceDetectionOutput
from com.deepvision.toolengine.ToolI import ToolI


class DistanceDetectionTool(ToolI):

    def matches(type: ToolType) -> bool:
        return type == ToolType.ToolType.DISTANCE_DETECTION

    def process(self, input: DistanceDetectionInput) -> DistanceDetectionOutput:
        output = self.distanceDetection(input.method,input.point_1,input.point_2)
        # if input.option == Constant.CANNY_EDGE_DETECTION:
        #     pass
        # else:
        #     output = ToolType.NO_TOOL
        return output;

    def distanceDetection(self, method, point_1, point_2) -> DistanceDetectionOutput:
        output = DistanceDetectionOutput()
        output.total_distance = dist.euclidean(point_1, point_2)
        output.status = Constant.RESULT_MATCH_FOUND
        print(output.total_distance)
        return output;