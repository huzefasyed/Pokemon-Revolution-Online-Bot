import time
import keyboard
import Battle

# Mt Moon
def gotoPokeMarkFromCave():
    # Inside cave
    time.sleep(1.5)
    keyboard.press_and_release('a')
    time.sleep(1.5)
    while Battle.checkIfInBattle():
        keyboard.press_and_release('4')

    keyboard.press_and_release('a')
    time.sleep(1.5)
    while Battle.checkIfInBattle():
        keyboard.press_and_release('4')

    keyboard.press_and_release('a')
    time.sleep(1.5)
    while Battle.checkIfInBattle():
        keyboard.press_and_release('4')

    keyboard.press_and_release('d')
    time.sleep(1.5)
    while Battle.checkIfInBattle():
        keyboard.press_and_release('4')

    # Leaving Cave
    keyboard.press_and_release('s')
    time.sleep(1.5)

    # Enter outside
    keyboard.press_and_release('s')
    time.sleep(1)
    keyboard.press_and_release('s')
    time.sleep(1)
    keyboard.press_and_release('s')
    time.sleep(1)
    keyboard.press_and_release('s')
    time.sleep(1)
    keyboard.press_and_release('s')
    time.sleep(1)
    keyboard.press_and_release('s')
    time.sleep(1)
    keyboard.press_and_release('s')
    time.sleep(1)
    keyboard.press_and_release('s')
    time.sleep(1)
    keyboard.press_and_release('s')
    time.sleep(1)
    #     Left bridge

    keyboard.press_and_release('a')
    time.sleep(1)
    keyboard.press_and_release('a')
    time.sleep(1)
    keyboard.press_and_release('a')
    time.sleep(1)
    keyboard.press_and_release('a')
    time.sleep(1)

    keyboard.press_and_release('w')
    time.sleep(0.6)
    keyboard.press_and_release('w')
    time.sleep(0.6)
    keyboard.press_and_release('w')
    time.sleep(1)

    keyboard.press_and_release('w')
    time.sleep(0.5)
    keyboard.press_and_release('a')
    time.sleep(0.5)

    # Entering Poke Center
    keyboard.press_and_release('w')
    time.sleep(0.5)

    print("end")


def gotoCaveFromOutsidePokeMart():
    # Outside of PokeMart
    time.sleep(1)
    keyboard.press_and_release('s')
    time.sleep(0.4)
    keyboard.press_and_release('d')
    time.sleep(0.4)

    # Climbing ramp
    keyboard.press_and_release('s')
    time.sleep(0.4)
    keyboard.press_and_release('s')
    time.sleep(0.4)
    # Fin climbing ramp

    # Making way to bridge
    keyboard.press_and_release('s')
    time.sleep(0.4)

    # Aligning self with bridge to enter cave
    keyboard.press_and_release('d')
    time.sleep(0.4)
    keyboard.press_and_release('d')
    time.sleep(0.4)
    keyboard.press_and_release('d')
    time.sleep(0.4)
    keyboard.press_and_release('d')
    time.sleep(0.5)
    # Fin alignment

    # Climbing Bridge
    keyboard.press_and_release('w')
    time.sleep(0.4)
    keyboard.press_and_release('w')
    time.sleep(0.4)
    keyboard.press_and_release('w')
    time.sleep(0.4)
    keyboard.press_and_release('w')
    time.sleep(0.4)
    keyboard.press_and_release('w')
    time.sleep(0.4)
    keyboard.press_and_release('w')
    time.sleep(0.4)
    keyboard.press_and_release('w')
    time.sleep(0.4)
    keyboard.press_and_release('w')
    time.sleep(0.4)
    keyboard.press_and_release('w')
    time.sleep(0.4)
    # Ending bridge

    # Entering Cave
    keyboard.press_and_release('w')
    time.sleep(0.4)

def gotoNurseOnceEnteredAndHeal():
    # Once entered we start walking
    keyboard.press_and_release('w')
    time.sleep(0.4)

    keyboard.press_and_release('w')
    time.sleep(0.4)

    keyboard.press_and_release('w')
    time.sleep(0.4)

    keyboard.press_and_release('w')
    time.sleep(0.4)

    keyboard.press_and_release('w')
    time.sleep(0.4)

    keyboard.press_and_release('w')
    time.sleep(0.4)

    # Talk to nurse

    keyboard.press_and_release('space')
    time.sleep(1)

    # Confirm heal
    keyboard.press_and_release('1')
    time.sleep(1)

    keyboard.press_and_release('space')
    time.sleep(1)

    keyboard.press_and_release('space')
    time.sleep(1)

    # Finished healing

    # Leaving back to entrance
    keyboard.press_and_release('s')
    time.sleep(0.4)

    keyboard.press_and_release('s')
    time.sleep(0.4)

    keyboard.press_and_release('s')
    time.sleep(0.4)

    keyboard.press_and_release('s')
    time.sleep(0.4)

    keyboard.press_and_release('s')
    time.sleep(0.4)

    keyboard.press_and_release('s')
    time.sleep(2)

    gotoCaveFromOutsidePokeMart()
