class Observer:
    #notifies program of death of Voldemort or Harry Potter

    def notifyProgram(self, Wizard1, Wizard2):
        if Wizard1.isAlive() == False or Wizard2.isAlive() == False:
            return True #someone died
        return False #no one died

    def whoWon(self, Wizard1, Wizard2):
        if Wizard1.isAlive() == False:
            return Wizard2.getName()
        elif Wizard2.isAlive() == False:
            return Wizard1.getName()
        else:
            return "error"


