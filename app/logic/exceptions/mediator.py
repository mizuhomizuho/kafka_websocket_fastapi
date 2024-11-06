from dataclasses import dataclass


@dataclass(frozen=True, eq=False)
class EventHandlerNotRegisteredException(LogicException):
    event_type: type

    @property
    def message(self):
        return f'Event "{self.event_type}" handler not registered'


@dataclass(frozen=True, eq=False)
class CommandHandlerNotRegisteredException(LogicException):
    command_type: type

    @property
    def message(self):
        return f'Command "{self.command_type}" handler not registered'