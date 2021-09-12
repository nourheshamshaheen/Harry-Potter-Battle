class Wizard:

    def __init__(self, name): #constructor taking name of wizard and setting all values to default
        self._name = name
        self._health = 100
        self._energy = 500
        self._shield = 3

    def isAlive(self):
        if self._health > 0 and self._energy > 0:
            return True
        else:
            return False

    def hasShield(self):
        if self._shield == 0:
            return False
        else:
            return True

    def castSpell(self, spell_casted, spell_received):  #normal spell match
        self._energy = self._energy - spell_casted.getEffect() #own energy is decreased by spell_casted's effect
        if(spell_received.getEffect() > spell_casted.getEffect()): #own health is decreased if received effect is bigger than casting effect
            self._health = self._health - (spell_received.getEffect() - spell_casted.getEffect())

    def castUselessSpell(self, spell_casted): #spell if the other wizard has a shield, doesn't depend on other wizard
            self._energy = self._energy - spell_casted.getEffect()


    def getName(self):
        return self._name

    def getHealth(self):
        return self._health

    def getEnergy(self):
        return self._energy

    def getShield(self):
        return self._shield

    def setName(self, name):
        self._name = name

    def setHealth(self, health):
        self._health = health

    def setEnergy(self, energy):
        self._energy = energy

    def setShield(self, shield):
        self._shield = shield
