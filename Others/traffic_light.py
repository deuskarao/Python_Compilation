import time


def main():
    count = 0
    light = ""
    lamps = {1: "RED", 30: "Yellow", 40: "GREEN"}

    while True:
        time.sleep(1)
        count += 1

        if lamps.get(count):
            light = lamps.get(count)

        print(f"\rLight : {light} | Count : {count}", end="")

        if count >= 60:
            count = 0


try:
    main()

except KeyboardInterrupt:
    time.sleep(1)
    print("\nTraffic Jam is coming!\n")
