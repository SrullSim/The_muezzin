from controller_loader import ControlLoader


class Main:

    def __init__(self):
        self.manager = ControlLoader()

    def run(self):
        self.manager.send_all_files_to_kafka()


run = Main()
run.run()