class Spell:

    def __init__(self, name, effect, wizard_name):  #constructor taking name of spell and effect on wizard
        self._name = name
        self._effect = effect
        self._wizard_name = wizard_name # 'V' for Voldemort, 'H' for Harry and 'A' for all

    def getName(self):
        return self._name

    def getEffect(self):
        return self._effect

    def getWizard(self):
        return self._wizard_name

