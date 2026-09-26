def total_resistance(resistors):
    return sum(resistors)

def calculate_current(voltage, r_total):
    return voltage / r_total

def voltage_drops(current, resistors):
    return [current * r for r in resistors]

def main():
    print("Series Circuit Simulator")

    voltage = float(input("Enter source voltage (V): "))

    resistors = []
    num_resistors = int(input("How many resistors in series? "))
    for i in range(num_resistors):
        r = float(input(f"Enter resistance R{i+1} (ohms): "))
        resistors.append(r)

    r_total = total_resistance(resistors)
    current = calculate_current(voltage, r_total)
    drops = voltage_drops(current, resistors)

    print(f"\nTotal Resistance: {r_total} ohms")
    print(f"Current through circuit: {current:.3f} A")
    print("\nVoltage drop across each resistor:")
    for i, drop in enumerate(drops):
        print(f"  R{i+1} ({resistors[i]} ohms): {drop:.3f} V")

    print(f"\nSum of voltage drops: {sum(drops):.3f} V (should equal source voltage: {voltage} V)")

if __name__ == "__main__":
    main()