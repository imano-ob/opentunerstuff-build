
#TODO: FixImports
import opentuner

class skill:

    def __init__(self, name, pts):
        self.name = name
        self.max_pts = pts

    def addParams(self, manipulator):
        manipulator.add_parameter(
            IntegerParameter(self.name, 0, self.max_pts))

    def setRequirements(self, attribute_requirements, skill_requirements):
        self.attribute_requirements = attribute_requirements
        self.skill_requirements = skill_requirements

    def evalRequirements(self, cfg):
        #TODO: Figure the line of code below out
        stats = getStatsFromSomewhere()
        #TODO: Usar stats somehow?
        error = 0
        for skill, requirement in self.skill_requirements.items():
            if cfg[k] < requirement:
                error += requirement - cfg[k]

        return error
