from evennia import Command, CmdSet
from evennia.utils.evmenu import EvMenu


class CommandSetProductionFocus(Command):
    """
    Sets planet production focus on specific sector

    Usage:
        set_prod_focus [civilian|naval]

    This will direct the planets economical focus in specified direction.
    """
    key = "set_prod_focus"
    aliases = ["spf"]

    def func(self):
        caller = self.caller
        location = caller.location
        self.args = self.args[1:]

        if not self.args:
            message = "You must specify production focus for it to work!"
            location.msg_contents(message)
            return

        if self.args not in ["civilian", "naval"]:
            message = "Focus must be either civilian or naval! %s provided" % \
                      self.args[0]
            location.msg_contents(message)
            return

        message = "Great, planet focus set to %s" % self.args
        location.msg_contents(message)


class CommandShowMenu(Command):
    """
    Displays menu for managing and adjusting planets

    Usage:
        show_menu
    """
    key = "show_menu"
    aliases = "sm"

    def func(self):
        EvMenu(self.caller, "world.planet_administration",
               startnode="main_menu", cmdset_mergetype="Union")


class PlanetCommandSet(CmdSet):
    key = "planetcommandset"

    def at_cmdset_creation(self):
        self.add(CommandSetProductionFocus())
