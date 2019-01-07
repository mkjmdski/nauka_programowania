from time import sleep
from math import ceil


def greeting():
    print("🍵🍵🍵🍵🍵 SUPER ADVANCED TEA CREATOR 🍵🍵🍵🍵🍵")
    print("Welcome to tea creator")
    print("It is five o'clock, you need some tea my lord")


def choose_tea():
    teas = ['green', 'black']
    print(f"You can have one of {len(teas)} types of tea: {teas}")
    tea = input("Which one would you like?")
    while tea not in teas:
        tea = input("Which one would you like?")
    return tea


def count_people():
    teas = input("how many teas do you want to prepare? (max 4)")
    while teas not in ['1', '2', '3', '4']:
        teas = input("how many teas do you want to prepare? (max 4)")
    return teas


def time_to_boil(teas, tea_type):
    boiling = {
        'black': 100,
        'green': 70} # celcius
    # kittle_power = 2000  # watt
    # with this kittle we can warm up 1 litr of water in 1 second for 0.5 grade
    mug_volume = 0.25  # litr
    initial_water_temperature = 20  # celcius

    celcius_to_warm = boiling[tea_type] - initial_water_temperature
    water_ammount = int(teas) * mug_volume
    time_needed = water_ammount * celcius_to_warm * 2
    return time_needed


def boil_water(time_to_boil, how_many_teas):
    for i in range(ceil(time_to_boil*10)):
        print(f' ☕ 🌡 Temperature: {20 + (float(i) * 0.05 / (0.25 * float(how_many_teas)))}')
        sleep(0.1)


if __name__ == "__main__":
    greeting()
    tea = choose_tea()
    how_many_teas = count_people()
    time = time_to_boil(how_many_teas, tea)
    boil_water(time, how_many_teas)
    print("Water boiled! Make your tea")
