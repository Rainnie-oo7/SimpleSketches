import pyautogui
import math


def transform_coordinates(x, y):
    transformed_y = math.sqrt(x ** 2 + y ** 2)
    return (x, transformed_y)


def main():
    try:
        while True:
            # Mausposition lesen
            x, y = pyautogui.position()

            # Koordinaten transformieren
            new_x, new_y = transform_coordinates(x, y)

            # Mausmarkierung setzen (nur für Linux und macOS)
            pyautogui.mouseDown(x=new_x, y=new_y)

    except KeyboardInterrupt:
        print("\nProgramm beendet.")


if __name__ == "__main__":
    main()
