

RESISTORS = [2.2, 37, 220, 1800000, 2565, 2444]

def pick(target_resistance, resistors_on_hand):
    resistors_on_hand.sort(reverse=True)
    current_resistance = 0
    dct = {}
    while current_resistance < target_resistance and resistors_on_hand[-1] + current_resistance < target_resistance:
        for resistor in resistors_on_hand:
            qty = (target_resistance - current_resistance) // resistor # Finding how many of the same resistors we can use
            if qty >= 1:
                print(qty)
                current_resistance += qty * resistor
                dct[resistor] = round(qty)
                print(current_resistance)
    return dct

if __name__ == '__main__':
    pickpickpick = pick(3245, RESISTORS)
    print(pickpickpick)
