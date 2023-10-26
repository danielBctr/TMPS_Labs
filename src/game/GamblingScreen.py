def screen_decorator(func):
    def wrapper(self, *args, **kwargs):
        # Additional functionality
        print("-" * 40)
        func(self, *args, **kwargs)
        print("-" * 40)
    return wrapper

class ScreenPrinter:
    def __init__(self, text):
        self.text = text

    @screen_decorator
    def print_screen(self):
        print(self.text)

class GamblingMachine(ScreenPrinter):
    def __init__(self):
        drawing = """
        _____   _____   _____
       /     \\ /     \\ /     \\
      |   7   |   7   |   7   |
       \\_____//_____//_____/
      """
        super().__init__(drawing)
