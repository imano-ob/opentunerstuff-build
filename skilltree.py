
#import sampleskill

class SkillTree:

    def __init__(self):
        self.skills = []
    
    def addSkill(self, skill):
        self.skills.append(skill)

    def addParams(self, manipulator):
        for skill in self.skills:
            skill.addParams(manipulator)
        
    def evalRequirements(self, cfg, level):
        error = 0
        lvreq = 0
        for skill, lv in cfg.items():
            lvreq += lv
        if level < lvreq:
            return lvreq - level
        for skill in self.skills:
            error += skill.evalRequirements(cfg)
        return error

    def evalTree(self, cfg):
        total_dmg = 1
        total_aps = 1
        for skill in self.skills:
            dmg, aps = skill.evalSkill(cfg)
            total_dmg += dmg
            total_aps += aps
        return total_dmg * total_aps

    def setEvalFunction(self, f):
        self.evalTree = f
