def pin_generator(pin):
    current_pin = '0000'
    while current_pin != pin:
        yield current_pin
        current_pin = str(int(current_pin) + 1).zfill(4)

PIN = '0549'
generator = pin_generator(PIN)

for pin in generator:
    print(pin)

print("PIN is " + PIN)


