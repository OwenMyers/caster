from dragonfly import (Grammar, AppContext, Dictation, Key, Text, MappingRule)

from caster.lib import control
from caster.lib import settings
from caster.lib.dfplus.additions import IntegerRefST
from caster.lib.dfplus.merge import gfilter
from caster.lib.dfplus.merge.mergerule import MergeRule
from caster.lib.dfplus.state.short import R


#class VimNon(MappingRule):


class Tmux(MergeRule):

    pronunciation = "multiplex"
    mapping = {
        "plex": R(Key("c-b")),
        "plex pain": R(Key("c-b,q")),
        "plex flip": R(Key("c-b,o")),
        "plex flip run": R(Key("c-b,o") + Key("up") + Key("enter") + Key("c-b,o")),
        "plex flop": R(Key("c-b,l")),
        "plex new tab": R(Key("c-b,c")),
        "plex rename tab": R(Key("c-b,comma")),
        }

    extras = [
              Dictation("text"),
              Dictation("mim"),
              IntegerRefST("n", 1, 1000),
             ]
    defaults = {"n": 1, "mim": ""}

#---------------------------------------------------------------------------

control.nexus().merger.add_global_rule(Tmux())

