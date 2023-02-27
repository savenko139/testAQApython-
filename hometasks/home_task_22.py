"""

Выбрать паттерн проектирования и реализовать его на конкретном примере (паттерн из GoF,
который рассматривали или не рассматривали, но не Singleton, не Iterator, не Decorator).

"""


class Mediator:
    def __init__(self):
        self.colleagues = []

    def add_colleague(self, colleague):
        self.colleagues.append(colleague)

    def broadcast(self, message, sender):
        for colleague in self.colleagues:
            if colleague != sender:
                colleague.receive(message)


class Colleague:
    def __init__(self, mediator):
        self.mediator = mediator
        mediator.add_colleague(self)

    def send(self, message):
        self.mediator.broadcast(message, self)

    def receive(self, message):
        print(f"Received message: {message}")


# Example usage
mediator = Mediator()
colleague1 = Colleague(mediator)
colleague2 = Colleague(mediator)

colleague1.send("Hello from colleague 1!")
colleague2.send("Greetings from colleague 2!")