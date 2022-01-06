class Spell():
    def __init__(self,name,range,desc,damage,hileveldamage,castTime,level):
        self.name = name
        self.range = range
        self.desc = desc
        self.damage = damage
        self.hileveldamge = hileveldamage
        self.castTime = castTime
        self.level = level

    

    def __str__(self):
        return self.name + " : " + "Cast Time : " + self.castTime + "at range " + self.range + "\n" + "Damage:" + self.damage + "(for high levels add" + self.hileveldamge +")" +"\n" + "Description: " + self.desc
    
    def getLevel(self):
        return self.level

    def rollSpell(self):
        pass