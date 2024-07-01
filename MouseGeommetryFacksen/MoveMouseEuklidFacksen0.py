import pyautogui
import math


def transform_coordinates(x, y):
    transformed_y = -math.sqrt(x ** 2 + y ** 2)
    return (x, transformed_y)


def main():
    try:
        while True:
            # Auf Mausklick warten
            pyautogui.click()

            # Mausposition lesen
            x, y = pyautogui.position()

            # Koordinaten transformieren
            new_x, new_y = transform_coordinates(x, y)

            # Mausmarkierung setzen
            pyautogui.moveTo(new_x, new_y)

    except KeyboardInterrupt:
        print("\nProgramm beendet.")


if __name__ == "__main__":
    main()
