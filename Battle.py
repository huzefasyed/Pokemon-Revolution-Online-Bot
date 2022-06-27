import pyautogui
import time
import keyboard
import Travel

LOCATION_OF_FIGHT_BUTTON_X_POSITION = 1198
LOCATION_OF_FIGHT_BUTTON_Y_POSITION = 622

PIXEL_OF_FIGHT_BUTTON_WHEN_YOUR_TURN_R = 153
PIXEL_OF_FIGHT_BUTTON_WHEN_YOUR_TURN_G = 153
PIXEL_OF_FIGHT_BUTTON_WHEN_YOUR_TURN_B = 153

PIXEL_OF_FIGHT_BUTTON_WHEN_NOT_YOUR_TURN_R = 153
PIXEL_OF_FIGHT_BUTTON_WHEN_NOT_YOUR_TURN_G = 0
PIXEL_OF_FIGHT_BUTTON_WHEN_NOT_YOUR_TURN_B = 0

LOCATION_OF_FIRST_MOVE_X_POSITION = 0
LOCATION_OF_FIRST_MOVE_Y_POSITION = 0

FIRST_POKEMON_HEALTH_LOCATION = 56, 34, 85, 11
SECOND_POKEMON_HEALTH_LOCATION = 15, 66, 127, 43
THIRD_POKEMON_HEALTH_LOCATION = 15, 120, 127, 43


def startFight():
    print("Starting Fight")

    while checkIfInBattle():
        if checkIfPokemonFainted():
            # Press 2 to take the second PKMN in party out
            keyboard.press_and_release('2')
            time.sleep(0.2)
            # Press 3 to take third PKMN in party out if 2nd fainted.
            keyboard.press_and_release('3')

        if checkPPOfFirstMoveIsEmpty():
            time.sleep(2)
            keyboard.press_and_release('1')
            time.sleep(0.7)
            keyboard.press_and_release('2')
            time.sleep(0.3)
        else:
            keyboard.press_and_release('1')
            time.sleep(0.3)


def checkIf3PokemonAreFainted():
    firstPKMN = pyautogui.locateOnScreen('D:/PokemonRevoBot/assets/Health.PNG'
                                         , confidence=0.9,
                                         region=FIRST_POKEMON_HEALTH_LOCATION)

    secondPKMN = pyautogui.locateOnScreen('D:/PokemonRevoBot/assets/Health.PNG',
                                          confidence=0.9,
                                          region=FIRST_POKEMON_HEALTH_LOCATION)

    thirdPKMN = pyautogui.locateOnScreen('D:/PokemonRevoBot/assets/Health.PNG',
                                         confidence=0.9,
                                         region=FIRST_POKEMON_HEALTH_LOCATION)
    if firstPKMN != None:
        print("POKEMON FAINTED STOP EVERYTHING AND GO PKMN MARK")
        return True
    else:
        return False


def checkPPOfFirstMoveIsEmpty():
    if pyautogui.locateOnScreen('D:/PokemonRevoBot/assets/NoPPLeft.PNG', grayscale=True, confidence=0.8):
        print("No pp left")
        return True
    else:
        return False


def checkIfInBattle():
    if pyautogui.locateOnScreen('D:/PokemonRevoBot/assets/BattleScreenOutSideGreenLand.PNG', grayscale=True,
                                confidence=0.5):
        print("FOUND")
        return True
    else:
        print("Finding...")
        return False


def checkIfPokemonFainted():
    faintedWithText = pyautogui.locateOnScreen('assets\FaintedPokemon.PNG', confidence=0.8)
    faintedNoText = pyautogui.locateOnScreen('assets\FaintedPokemonNoText.PNG', confidence=0.8)
    if (faintedNoText or faintedWithText != None):
        print("PKMN Fainted")
        return True
    else:
        print("Checking If PKMN Fainted")
        return False


def moveHorizontalToFindEnemy():
    keyboard.press('a')
    time.sleep(1.5)
    keyboard.release('a')

    keyboard.press('d')
    time.sleep(1.5)
    keyboard.release('d')

    if checkIfInBattle():
        startFight()

    #  Once fight ended check if PKMN Fainted, if Faint then go POKE-Mart
    if checkIf3PokemonAreFainted():
        Travel.gotoPokeMarkFromCave()
        Travel.gotoNurseOnceEnteredAndHeal()
    else:
        moveHorizontalToFindEnemy()

