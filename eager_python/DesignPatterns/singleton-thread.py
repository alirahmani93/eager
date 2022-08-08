from threading import Lock, Thread


class SingletonMeta(type):
    _instance = {}
    _lock: Lock = Lock()

    def __call__(cls, *args, **kwargs):
        with cls._lock:
            if cls not in cls._instance:
                instance = super().__call__(*args, **kwargs)
                cls._instance[cls] = instance
        return cls._instance[cls]


class Singleton(metaclass=SingletonMeta):
    value: str = None

    def __init__(self, value):
        self.value = value

    def some_logic(self):
        print("cool_logic")


def test_singleton(value: str):
    singleton = Singleton(value)
    print(singleton.value)


if __name__ == "__main__":
    proc1 = Thread(target=test_singleton, args=("foo",))
    proc1.start()

    proc2 = Thread(target=test_singleton, args=("bar",))
    proc2.start()

    print("type(proc2): ", type(proc2))
    print("isinstance(proc1, type(proc2)): ", isinstance(proc1, type(proc2)))
