import json as json
from com.deepvision.constants.ToolType import ToolType
from com.deepvision.input.CornerDetectionInput import CornerDetectionInput
from com.deepvision.input.TemplateMatchingInput import TemplateMatchingInput
from com.deepvision.input.DistanceDetectionInput import DistanceDetectionInput
from com.deepvision.input.AngleDetectionInput import AngleDetectionInput
from com.deepvision.input.EdgeDetectionInput import EdgeDetectionInput


class JobLoader(object):

    tool_list = []

    def loadJob(self):
        with open("job.json", "r") as read_file:
            test_obj = json.load(read_file)

        print('Job Name : ' + test_obj['job_name'])
        print('Job Description : ' + test_obj['job_description'])
        print('Job Created By :' + test_obj['created_by'])
        tools = test_obj['tools']
        for tool in tools:
            tool_type = tool['type']
            if (ToolType.CORNER_DETECTION.value == tool_type):
                input = createCornerDetectionInput(tool)
            if (ToolType.TEMPLATE_MATCHING.value == tool_type):
                input = createTemplateMatchingInput(tool)
            if (ToolType.ANGLE_DETECTION.value == tool_type):
                input = createAngleDetectionInput(tool)
            if (ToolType.DISTANCE_DETECTION.value == tool_type):
                input = createDistanceDetectionInput(tool)
            if (ToolType.EDGE_DETECTION.value == tool_type):
                input = createEdgeDetectionInput(tool)
            self.tool_list.append(input);


def createCornerDetectionInput(tool) -> CornerDetectionInput:
    input = CornerDetectionInput(tool['type'], tool['method'], tool['threshold'], tool['blockSize'],
                                 tool['apertureSize'], tool['k_size'],
                                 tool['max_thresholding'], tool['maxCorners'], tool['next_tool']);

    return input;


def createTemplateMatchingInput(tool) -> TemplateMatchingInput:
    input = TemplateMatchingInput(tool['type'], tool['method'], tool['main_img'], tool['temp_img'], tool['option'])
    return input


def createAngleDetectionInput(tool) -> AngleDetectionInput:
    input = AngleDetectionInput(tool['type'], tool['point_1'], tool['point_2'])
    return input


def createDistanceDetectionInput(tool) -> DistanceDetectionInput:
    input = DistanceDetectionInput(tool['type'], tool['method'], tool['point_1'], tool['point_2'])
    return input


def createEdgeDetectionInput(tool) -> EdgeDetectionInput:
    input = EdgeDetectionInput(tool['type'], tool['method'], tool['lower_threshold'], tool['upper_threshold'],
                               tool['k_sizeX'], tool['k_sizeY'], tool['edge_thickness'])
    return input
