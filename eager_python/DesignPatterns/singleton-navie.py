# Naive

class SingletonMeta(type):
    _instance = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instance:
            instance = super().__call__(cls, *args, **kwargs)
            cls._instance = instance[cls]
        return cls._instance[cls]


class Singleton(metaclass=SingletonMeta):
    def business_logic(self):
        """
        define some business logic, which can be executed on its instance.
        """
        print("cool logic")


if __name__ == "__main__":
    s1, s2, s3 = Singleton, Singleton, Singleton.business_logic
    if id(s1) == id(s2):
        print("They are same instance")
        print(s1)
    else:
        print("They are different instance")
        print(s1, s2)

    print("isinstance(s2, type(s1)): ", isinstance(s2, type(s1)))
    print("isinstance(s3, type(s1)): ", isinstance(s3, type(s1)))
    print("issubclass(type(s3), type(s1)): ", issubclass(type(s3), type(s1)))
    print("issubclass(type(s3), type(s2)): ", issubclass(type(s3), type(s2)))
