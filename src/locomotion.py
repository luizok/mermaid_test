import abc


class AbstractLocomotionKind(abc.ABC):

    @abc.abstractmethod
    def move(self):
        ...


class WalkingKind(AbstractLocomotionKind):

    def move(self) -> None:
        self.walk()

    def walk(self) -> None:
        print('Walking')


class FlyingKind(AbstractLocomotionKind):

    def move(self) -> None:
        self.fly()

    def fly(self) -> None:
        print('Flying')


class SwimmingKind(AbstractLocomotionKind):

    def move(self) -> None:
        self.swim()

    def swim(self) -> None:
        print('Swimming')
