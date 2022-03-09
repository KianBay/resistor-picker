

RESISTORS =     [1, 1.2, 1.5, 1.8, 2.2, 2.7, 3.3, 3.9, 4.7, 5.6, 
                6.8, 8.2, 10, 12, 15, 18, 22, 27, 33, 39, 
                47, 56, 68, 82, 100, 120, 150, 180, 220, 270, 
                330, 390, 470, 560, 680, 820, 1000, 1200, 1500, 1800,
                2200, 2700, 3300, 3900, 4700, 5600, 6800, 8200,
                10000, 12000, 15000, 18000, 22000, 27000, 33000,
                39000, 47000, 56000, 68000, 82000, 100000, 120000,
                150000, 180000, 220000, 270000, 330000, 390000, 470000,
                560000, 680000, 820000, 1000000, 1200000, 1500000,
                1800000, 2200000, 2700000, 3300000, 3900000,
                4700000, 5600000, 6800000, 8200000]

def pick(target_resistance, resistors_on_hand):
    resistors_on_hand.sort(reverse=True)
    current_resistance = 0
    dct = {}
    while current_resistance < target_resistance and resistors_on_hand[-1] + current_resistance < target_resistance:
        for resistor in resistors_on_hand:
            qty = (target_resistance - current_resistance) // resistor # Finding how many of the same resistors we can use
            if qty >= 1:
                current_resistance += qty * resistor
                dct[resistor] = round(qty)
    return dct, current_resistance

if __name__ == '__main__':
    pickpickpick, res = pick(3245, RESISTORS)
    print(pickpickpick)
    print('Actual resistance from picks:',res)
