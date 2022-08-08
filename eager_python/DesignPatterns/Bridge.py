from __future__ import annotations
from abc import ABC, abstractmethod


class WebPage(ABC):
    """
    اصلی ترین کلاس انتزاعی است
    """
    def __init__(self, theme: Theme) -> None:
        self.theme = theme

    def menu(self) -> str:
        return (f"WebPage: Base menu with:\n"
                f"{self.theme.CostumerNation()}")


class ExtendedWebPage(WebPage):
    def food(self) -> str:
        return (f"ExtendedWebPage: Extended menu with:\n"
                f"{self.theme.CostumerNation()}")


class Theme(ABC):
    """
    کلاس پیاده سازی ##
    """
    @abstractmethod
    def CostumerNation(self) -> str:
        pass


class ConcretTheme_IR(Theme):

    def CostumerNation(self) -> str:
        return "Iranian Food is here"


class ConcretTheme_IT(Theme):
    def CostumerNation(self) -> str:
        return "Italian Food is here"


def client(webpage: WebPage) -> None:
    """
    انتخاب کاربر را میگیرد و نتیجه را به او بر میگرداند
    """
    print(webpage.menu(), " ^_^ ")


if __name__ == "__main__":
    theme = ConcretTheme_IR()
    web = WebPage(theme)
    client(web)
    # print("\n")
    print("***##__##***")
    # print("   **##**   ")
    # print("    *#*     ")
    theme = ConcretTheme_IT()
    web = WebPage(theme)
    client(web)