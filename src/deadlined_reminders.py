from abc import ABCMeta, abstractmethod, ABC
from collections.abc import Iterable


class DeadlinedMetaReminder(Iterable, ABC):
    @abstractmethod
    def is_due(self):
        pass
