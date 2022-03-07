import abc

import src.locomotion as mk  # move kind


class AbstractAnimal(abc.ABC):

    def __init__(self, locomotion_kind: mk.AbstractLocomotionKind):
        self.locomotion_kind: mk.AbstractLocomotionKind = locomotion_kind

    @abc.abstractmethod
    def eat(self) -> None:
        raise NotImplementedError()

    @abc.abstractmethod
    def sleep(self) -> None:
        raise NotImplementedError()

    def move(self) -> None:
        self.locomotion_kind.move()


class WalkingAnimal(AbstractAnimal):

    def __init__(self):
        super().__init__(mk.WalkingKind())


class FlyingAnimal(AbstractAnimal):

    def __init__(self):
        super().__init__(mk.FlyingKind())


class SwimmingAnimal(AbstractAnimal):

    def __init__(self):
        super().__init__(mk.SwimmingKind())
