"""
__author__ = 'LexiconCode'
Command-module for Gitter
Official Site "https://gitter.im/"
"""
#---------------------------------------------------------------------------

from dragonfly import Dictation, Grammar, MappingRule

from castervoice.lib import control, settings
from castervoice.lib.actions import Key, Text
from castervoice.lib.context import AppContext
from castervoice.lib.dfplus.merge import gfilter
from castervoice.lib.dfplus.merge.mergerule import MergeRule
from castervoice.lib.dfplus.state.short import R


class GitterRule(MergeRule):
    pronunciation = "Gitter"

    mapping = {
        "bold":
            R(Text("****") + Key("left:2"), rdescript="Gitter: Bold"),
        "emphasize":
            R(Text("**") + Key("left"), rdescript="Gitter: Italicize"),
        # "header":           R(Text( "" ), rdescript="Gitter: Header"), # H1 ## H2 ### H3
        "insert item":
            R(Text("* "), rdescript="Gitter: Insert Item"),
        "block quote":
            R(Text("> "), rdescript="Gitter: Block Quote"),
        "mention":
            R(Text("@"), rdescript="Gitter: Mention"),
        "insert link":
            R(Text("[]()") + Key("left:3"), rdescript="Gitter: Insert Link"),
        "insert image":
            R(Text("![]()") + Key("left:3"), rdescript="Gitter: Insert Image"),
        "insert code":
            R(Text("``") + Key("left"), rdescript="Gitter: Insert Code"),
        "formatted code":
            R(Text("```") + Key("s-enter"), rdescript="Gitter: Formatted Code"),
    }
    extras = [
        Dictation("text"),
    ]
    Defaults = {}


#---------------------------------------------------------------------------

context = AppContext(executable="gitter")
control.non_ccr_app_rule(GitterRule(), context=context)