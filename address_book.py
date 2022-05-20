import json


class User:
    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            self.__dict__[k] = v

    def __repr__(self) -> str:
        return "".join(f"{k}: {v}\n" for k, v in self.__dict__.items()) + "\n"


def read_json(file_path):
    with open(file_path) as f:
        return json.loads(f.read())


if __name__ == "__main__":

    users = []
    file = read_json("data.json")

    for i in file:
        users.append(User(**i))

    print("".join(f"{user}" for user in users))

    exit(0)
