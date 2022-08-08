class Target:
    def request(self) -> str:
        return "some text in Target class"


class Adaptee:
    """the adaptee need som functions before client code use it"""

    def do_some_thing_on_adaptee(self):
        return "yeah I have some thing but client cant use me! adapter will be (Translate) me :)", \
               "ssalc eetpada ni txet emos"


class Adapter(Target, Adaptee):
    def request(self):
        msg, text = self.do_some_thing_on_adaptee()
        answer = text[::-1]
        answer.title()

        return f"yeah i can translate adaptee to client easily. adaptee said: {answer}"


def client_code(target: "Target") -> None:
    print(target.request())


if __name__ == "__main__":
    target_instance = Target()
    client_code(target_instance)
    adaptee = Adaptee()
    print(f"client:its weird I cant understand >> {adaptee.do_some_thing_on_adaptee()}")
    print("Client: But I can work with it via the Adapter:")
    adapter = Adapter()
    client_code(adapter)
