import time
import Battle
import Travel


def main():
    time.sleep(2)
    # This depends on the location your going to.
    Travel.gotoCaveFromOutsidePokeMart()
    while True:
        Battle.moveHorizontalToFindEnemy()


main()
