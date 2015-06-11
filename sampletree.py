
from sampleskill import Skill
from skilltree import SkillTree


#Java feelings
class treeBuilder():
    def build(self, maxlv):
        sampletree = SkillTree()
        #Stuff sem dependencias
           
        deplessdmg = Skill("deplessdmg", maxlv, {})
        def f1(skill, cfg):
            skill_level = cfg[skill.getName()]
            return skill_level * 5, 0
        deplessdmg.setEvalFunction(f1)
        sampletree.addSkill(deplessdmg)
        
        deplessmix = Skill("deplessmix", maxlv, {})
        def f2(skill, cfg):
            skill_level = cfg[skill.getName()]    
            return skill_level * 2.5, skill_level * 0.1
        deplessmix.setEvalFunction(f2)
        sampletree.addSkill(deplessmix)
        
        deplessaps = Skill("deplessaps", maxlv, {})
        def f3(skill, cfg):
            skill_level = cfg[skill.getName()]
            return 0, skill_level * 0.2
        deplessaps.setEvalFunction(f3)
        sampletree.addSkill(deplessaps)
        
        #Dmg stuff
        
        dmg1 = Skill("dmg1", maxlv, {})
        def f4(skill, cfg):
            skill_level = cfg[skill.getName()]
            return skill_level * 2.5, 0
        dmg1.setEvalFunction(f4)
        sampletree.addSkill(dmg1)
        
        dmg2 = Skill("dmg2", maxlv, {"dmg1": 5})
        def f5(skill, cfg):
            skill_level = cfg[skill.getName()]
            return skill_level * 5, 0
        dmg2.setEvalFunction(f5)
        sampletree.addSkill(dmg2)
        
        dmg3 = Skill("dmg3", maxlv, {"dmg2": 5})
        def f6(skill, cfg):
            skill_level = cfg[skill.getName()]
            return skill_level * 10, 0
        dmg3.setEvalFunction(f6)
        sampletree.addSkill(dmg3)
        
        #Mix stuff
        
        mix1 = Skill("mix1", maxlv, {})
        def f7(skill, cfg):
            skill_level = cfg[skill.getName()]
            return skill_level * 1.25, skill_level * 0.05
        mix1.setEvalFunction(f7)
        sampletree.addSkill(mix1)
        
        mix2 = Skill("mix2", maxlv, {"mix1": 5})
        def f8(skill, cfg):
            skill_level = cfg[skill.getName()]
            return skill_level * 2.5, skill_level * 0.1
        mix2.setEvalFunction(f8)
        sampletree.addSkill(mix2)
        
        mix3 = Skill("mix3", maxlv, {"mix2": 5})
        def f9(skill, cfg):
            skill_level = cfg[skill.getName()]
            return skill_level * 5, skill_level * 0.2
        mix3.setEvalFunction(f9)
        sampletree.addSkill(mix3)
        
        #APS stuff
        
        aps1 = Skill("aps1", maxlv, {})
        def f10(skill, cfg):
            skill_level = cfg[skill.getName()]
            return 0, skill_level * 0.1
        aps1.setEvalFunction(f10)
        sampletree.addSkill(aps1)
        
        aps2 = Skill("aps2", maxlv, {"aps1": 5})
        def f11(skill, cfg):
            skill_level = cfg[skill.getName()]
            return 0, skill_level * 0.2
        aps2.setEvalFunction(f11)
        sampletree.addSkill(aps2)
        
        aps3 = Skill("aps3", maxlv, {"aps2": 5})
        def f12(skill, cfg):
            skill_level = cfg[skill.getName()]
            return 0, skill_level * 0.4
        aps3.setEvalFunction(f12)
        sampletree.addSkill(aps3)
        return sampletree
