from threading import Thread


class ThreadLoop(Thread):

    def __init__(self, loop, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.running = False
        self.__loop = loop

    def start(self) -> None:
        self.running = True
        super().start()

    def run(self) -> None:
        while self.running:
            self.__loop()

    def stop(self):
        self.running = False
