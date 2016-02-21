class Printer:
    def __init__(self, text):
        self.text = text + "a"

    def do_print(self):
        print(self.text)

if __name__ == "__main__":
    Printer("hahahah").do_print()