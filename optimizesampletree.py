
from sampleskill import Skill
from skilltree import SkillTree

sampletree = SkillTree()

#Java feelings
class treeBuilder():
    def build(self, level):

        #Stuff sem dependencias

        #Otimizacoes marotas 
        #Mais do que isso, vale mais colocar na tree com dependencias
        maxdepless = min(level, 15)
        
        deplessdmg = Skill("deplessdmg", maxdepless, {})
        def f1(skill, cfg):
            skill_level = cfg[skill.getName()]
            return skill_level * 5, 0
        deplessdmg.setEvalFunction(f1)
        sampletree.addSkill(deplessdmg)
        
        deplessmix = Skill("deplessmix", maxdepless, {})
        def f2(skill, cfg):
            skill_level = cfg[skill.getName()]    
            return skill_level * 2.5, skill_level * 0.1
        deplessmix.setEvalFunction(f2)
        sampletree.addSkill(deplessmix)
        
        deplessaps = Skill("deplessaps", maxdepless, {})
        def f3(skill, cfg):
            skill_level = cfg[skill.getName()]
            return 0, skill_level * 0.2
        deplessaps.setEvalFunction(f3)
        sampletree.addSkill(deplessaps)
        
        #Dmg stuff
        
        dmg1 = Skill("dmg1", min(5, level), {})
        def f4(skill, cfg):
            skill_level = cfg[skill.getName()]
            return skill_level * 2.5, 0
        dmg1.setEvalFunction(f4)
        sampletree.addSkill(dmg1)

        if level > 5:
            dmg2 = Skill("dmg2", min(5, level - 5), {"dmg1": 5})
            def f5(skill, cfg):
                skill_level = cfg[skill.getName()]
                return skill_level * 5, 0
            dmg2.setEvalFunction(f5)
            sampletree.addSkill(dmg2)

        if level > 10:
            dmg3 = Skill("dmg3", level - 10, {"dmg2": 5})
            def f6(skill, cfg):
                skill_level = cfg[skill.getName()]
                return skill_level * 10, 0
            dmg3.setEvalFunction(f6)
            sampletree.addSkill(dmg3)
        
        #Mix stuff
        
        mix1 = Skill("mix1", min(5, level), {})
        def f7(skill, cfg):
            skill_level = cfg[skill.getName()]
            return skill_level * 1.25, skill_level * 0.05
        mix1.setEvalFunction(f7)
        sampletree.addSkill(mix1)

        if level > 5:
            mix2 = Skill("mix2", min(5, level - 5), {"mix1": 5})
            def f8(skill, cfg):
                skill_level = cfg[skill.getName()]
                return skill_level * 2.5, skill_level * 0.1
            mix2.setEvalFunction(f8)
            sampletree.addSkill(mix2)

        if level > 10:
            mix3 = Skill("mix3", level - 10, {"mix2": 5})
            def f9(skill, cfg):
                skill_level = cfg[skill.getName()]
                return skill_level * 5, skill_level * 0.2
            mix3.setEvalFunction(f9)
            sampletree.addSkill(mix3)
        
        #APS stuff
        
        aps1 = Skill("aps1", min(5, level), {})
        def f10(skill, cfg):
            skill_level = cfg[skill.getName()]
            return 0, skill_level * 0.1
        aps1.setEvalFunction(f10)
        sampletree.addSkill(aps1)

        if level > 5:
            aps2 = Skill("aps2", min(5, level - 5), {"aps1": 5})
            def f11(skill, cfg):
                skill_level = cfg[skill.getName()]
                return 0, skill_level * 0.2
            aps2.setEvalFunction(f11)
            sampletree.addSkill(aps2)

        if level > 10:
            aps3 = Skill("aps3", level - 10, {"aps2": 5})
            def f12(skill, cfg):
                skill_level = cfg[skill.getName()]
                return 0, skill_level * 0.4
            aps3.setEvalFunction(f12)
            sampletree.addSkill(aps3)
        return sampletree
