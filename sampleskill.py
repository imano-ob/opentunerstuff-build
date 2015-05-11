
#TODO: FixImports
import opentuner
from opentuner import IntegerParameter

class Skill:

    def __init__(self, name, pts, skill_requirements):
        self.name = name
        self.max_pts = pts
        self.skill_requirements = skill_requirements

    def addParams(self, manipulator):
        manipulator.add_parameter(
            IntegerParameter(self.name, 0, self.max_pts))

#    Just in case
#    def setRequirement(self, skill_name, requirement):
#        self.skill_requirements[skill_name] = requirement
        
    def evalRequirements(self, cfg):
        error = 0
        for skill, requirement in self.skill_requirements.items():
            if cfg[skill] < requirement:
                error += (requirement - cfg[skill]) * cfg[self.name]
        return error

    def evalSkill(self, cfg):
        return self.cevalSkill(self, cfg)
    
    def setEvalFunction(self, f):
        print self.name
        self.cevalSkill = f
        
    def getName(self):
        return self.name
        
#    def __evalSkill(self, gambfiller, cfg):
#        print "dafuq"
#        pass
