#Realistically, Harry Potter wouldn't use the forbidden curses even when fighting Voldemort :(

from Wizard import Wizard
from Spell import Spell
from Observer import Observer


def getSpellData():
    # getting spell data from text file
    try:
        spell_file = open("spells.txt", "r")
    except IOError:
        print("File not found or path is incorrect")
        exit(1)

    Lines = spell_file.readlines()
    spell_list = []

    # creating a new object Spell for each spell in the file
    for line in Lines:
        res = line.split()
        spell_list.append(Spell(res[1], int(res[2]), res[0]))

    # making a dict for easy access of spells by their name
    spell_dict = dict()
    for spell in spell_list:
        spell_dict[spell.getName()] = spell

    return spell_dict


if __name__ == '__main__':

    #initializing both wizards
    Voldemort = Wizard("Voldemort")
    Harry = Wizard("Harry")

    #initialize observer to get notified of deaths
    obs = Observer()

    #creating a spell dictionary
    spell_dict = getSpellData()

    #WAR!
    print("THE WAR IS STARTING")

    while(obs.notifyProgram(Voldemort, Harry) == False):
        buffer = input("Enter the two spells (Harry then Voldemort):\n")
        buff = buffer.split()

        #Check if input is correct: spells exist and every wizard is using his own spells
        everything_is_correct = True

        if buff[0] not in spell_dict or buff[1] not in spell_dict:
            print("WRONG SPELLS.")
            continue

        if(spell_dict[buff[0]].getWizard() != 'H' and spell_dict[buff[0]].getWizard() != 'A'):
            print("Harry can't use this spell. This spell can only be used by Voldemort.")
            everything_is_correct = False

        if (spell_dict[buff[1]].getWizard() != 'V' and spell_dict[buff[1]].getWizard() != 'A'):
            print("Voldemort can't use this spell. This spell can only be used by Harry.")
            everything_is_correct = False

        if(everything_is_correct == False):
            continue

        if buff[0] == "sheild" and Harry.hasShield():
            Harry.setShield(Harry.getShield() - 1)
            Voldemort.castUselessSpell(spell_dict[buff[1]])
        elif buff[1] == "sheild" and Voldemort.hasShield():
            Voldemort.setShield(Voldemort.getShield() - 1)
            Harry.castUselessSpell(spell_dict[buff[0]])
        else:
            Harry.castSpell(spell_dict[buff[0]], spell_dict[buff[1]])
            Voldemort.castSpell(spell_dict[buff[1]], spell_dict[buff[0]])

        print("\t\tHarry \t Voldemort")
        print("Health: " +str(Harry.getHealth()) + "\t\t " + str(Voldemort.getHealth()))
        print("Energy: " +str(Harry.getEnergy()) + "\t\t " + str(Voldemort.getEnergy()))

    if obs.notifyProgram(Voldemort, Harry) == True:
        print("\t\t"+obs.whoWon(Voldemort, Harry)+" is the winner... ")


