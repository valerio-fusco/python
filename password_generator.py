import argparse
import random
import string


def get_args():
    args = argparse.ArgumentParser()
    args.add_argument("-n", action="store_true", dest="numbers",
                      default=False, help="Enable numbers")
    args.add_argument("-s", action="store_true", dest="symbols",
                      default=False, help="Enable symbols")
    args.add_argument("-l", type=int, dest="length",
                      default=16, help="Set password length")
    return vars(args.parse_args())


def generate_password(**kwargs):

    character_set = string.ascii_letters

    if kwargs.get("numbers"):
        character_set += string.digits

    if kwargs.get("symbols"):
        character_set += "\"|!\"£$%&/()[]{}=?^-_.:,;<>€@#°§*'"

    return "".join(random.choice(character_set) for _ in range(kwargs.get("length")))


if __name__ == "__main__":

    args = get_args()
    if args.get("length") < 8:
        print("Impostare una password con una lunghezza maggiore di 8 caratteri")
        exit(1)

    print(f"Generated password: {generate_password(**args)}")
    exit(0)
