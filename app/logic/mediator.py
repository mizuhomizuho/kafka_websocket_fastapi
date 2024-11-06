from cgitb import handler
from collections import defaultdict
from collections.abc import Iterable
from dataclasses import field

from domain.events.base import BaseEvent
from logic.commands.base import CT, CommandHandler, CR, BaseCommand
from logic.events.base import EventHandler, ET, ER
from logic.exceptions.mediator import EventHandlerNotRegisteredException, CommandHandlerNotRegisteredException


class Mediator:
    events_map: dict[type[ET], EventHandler] = field(default_factory=lambda: defaultdict(list))
    commands_map: dict[type[CT], CommandHandler] = field(default_factory=lambda: defaultdict(list))

    def register_event(self, event: ET, event_handler: EventHandler[ET, ER]):
        self.events_map[event.__class__].append(event_handler)

    def register_command(self, command: CT, command_handler: CommandHandler[CT, CR]):
        self.events_map[command.__class__].append(command_handler)

    def handler_event(self, event: BaseEvent) -> Iterable[ER]:
        event_type = event.__class__
        handlers = self.events_map.get(event_type)

        if not handlers:
            raise EventHandlerNotRegisteredException(event_type)

        return [handler_el.handle(event) for handler_el in handlers]

    def handler_commands(self, command: BaseCommand) -> Iterable[CR]:
        command_type = command.__class__
        handlers = self.commands_map.get(command_type)

        if not handlers:
            raise CommandHandlerNotRegisteredException(command_type)

        return [handler_el.handle(command) for handler_el in handlers]