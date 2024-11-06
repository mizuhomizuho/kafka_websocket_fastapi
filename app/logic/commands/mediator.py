from dataclasses import dataclass

from domain.entities.messages import Chat
from logic.commands.base import BaseCommand, CommandHandler


@dataclass(frozen=True)
class CreateChatCommand(BaseCommand):
    title: str


@dataclass(frozen=True)
class CreateChatCommandHandler(CommandHandler[CreateChatCommand]):
    title: str

    def handle(self, command: CreateChatCommand) -> Chat:
        ...