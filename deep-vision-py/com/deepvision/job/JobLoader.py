import json as json

from com.deepvision.constants.ToolType import ToolType
from com.deepvision.input.AngleDetectionInput import AngleDetectionInput
from com.deepvision.input.CornerDetectionInput import CornerDetectionInput
from com.deepvision.input.CropInput import CropInput
from com.deepvision.input.DistanceDetectionInput import DistanceDetectionInput
from com.deepvision.input.EdgeDetectionInput import EdgeDetectionInput
from com.deepvision.input.FixtureInput import FixtureInput
from com.deepvision.input.PixelCountInput import PixelCountInput
from com.deepvision.input.TemplateMatchingInput import TemplateMatchingInput


class JobLoader(object):
    tool_list = []
    jobJsonData = "";

    def loadJob(self):
        with open("..//job//job8.json", "r") as read_file:
            self.jobJsonData = json.load(read_file)

        # print('Job Name : ' + self.jobJsonData['job_name'])
        # print('Job Description : ' + self.jobJsonData['job_description'])
        # print('Job Created By :' + self.jobJsonData['created_by'])
        tools = self.jobJsonData['tools']
        for tool in tools:
            tool_type = tool['type']
            if (ToolType.CORNER_DETECTION.value == tool_type):
                input = self.createCornerDetectionInput(tool)
            if (ToolType.TEMPLATE_MATCHING.value == tool_type):
                input = self.createTemplateMatchingInput(tool)
            if (ToolType.ANGLE_DETECTION.value == tool_type):
                input = self.createAngleDetectionInput(tool)
            if (ToolType.DISTANCE_DETECTION.value == tool_type):
                input = self.createDistanceDetectionInput(tool)
            if (ToolType.EDGE_DETECTION.value == tool_type):
                input = self.createEdgeDetectionInput(tool)
            if (ToolType.PIXEL_COUNT.value == tool_type):
                input = self.createPixelCountInput(tool)
            if (ToolType.FIXTURE.value == tool_type):
                input = self.createFixtureInput(tool)

            self.tool_list.append(input)

    def createCornerDetectionInput(self, tool) -> CornerDetectionInput:
        input = CornerDetectionInput(tool['main_img'], tool['type'], tool['method'], tool['threshold'],
                                     tool['blockSize'],
                                     tool['apertureSize'], tool['k_size'],
                                     tool['max_thresholding'], tool['maxCorners'], tool['next_tool']);

        return input;

    def createTemplateMatchingInput(self, tool) -> TemplateMatchingInput:
        input = TemplateMatchingInput(tool['type'], tool['method'], tool['main_img'], tool['temp_img'], tool['option'],
                                      tool['next_tool'])
        return input

    def createAngleDetectionInput(self, tool) -> AngleDetectionInput:
        input = AngleDetectionInput(tool['type'], tool['point_1'], tool['point_2'], tool['next_tool'])
        return input

    def createDistanceDetectionInput(self, tool) -> DistanceDetectionInput:
        input = DistanceDetectionInput(tool['type'], tool['method'], tool['point_1'], tool['point_2'])
        return input

    def createEdgeDetectionInput(self, tool) -> EdgeDetectionInput:
        input = EdgeDetectionInput(tool['main_img'], tool['type'], tool['method'], tool['lower_threshold'],
                                   tool['upper_threshold'],
                                   tool['k_sizeX'], tool['k_sizeY'], tool['edge_thickness'], tool['next_tool'])
        return input

    def createCropInput(self, tool) -> CropInput:
        input = CropInput(tool['main_img'], tool['type'], tool['method'], tool['top_left'],
                          tool['bottom_right'],
                          tool['start_percentage'], tool['end_percentage'], tool['next_tool'])
        return input

    def createPixelCountInput(self, tool) -> PixelCountInput:
        input = PixelCountInput(tool['main_img'], tool['type'], tool['method'], tool['option'], tool['threshold'],
                                tool['max_value'], tool['block_size'], tool['constant'], tool['next_tool'])
        return input

    def createFixtureInput(self, tool):
        input = FixtureInput(tool['type'], tool['top_left_pnt'], tool['bottom_right_pnt'], tool['top_left_pnt_gape'],
                             tool['bottom_right_pnt_gape'], tool['next_tool'])
        return input
