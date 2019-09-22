from dragonfly import (Grammar, AppContext, Dictation, Key, Text, MappingRule)

from caster.lib import control
from caster.lib import settings
from caster.lib.dfplus.additions import IntegerRefST
from caster.lib.dfplus.merge import gfilter
from caster.lib.dfplus.merge.mergerule import MergeRule
from caster.lib.dfplus.state.short import R


#class VimNon(MappingRule):


class Vim(MergeRule):

    pronunciation = "good key bind"
    mapping = {

        "fugitive data science": R(Text("~/repos/data_science/")),
        "fugitive service root": R(Text("~/repos/ds_score_api/")),
        "fugitive service chimera": R(Text("~/repos/ds_score_api/service_chimera/")),
        "fugitive service score": R(Text("~/repos/ds_score_api/service_score/")),
        "fugitive simulation": R(Text("~/repos/simulation/")),

        "fugitive left": R(Key("c-w,h")),
        "fugitive right": R(Key("c-w,l")),
        "fugitive up": R(Key("c-w,k")),
        "fugitive down": R(Key("c-w,j")),
        "fugitive close lower": R(Key("escape,c-w,j,colon,q")),
        "fugitive split": R(Key("escape,colon") + Text("vsplit ")),

        "fugitive status": R(Key("escape,colon") + Text("Gstatus") + Key('enter')),
        "fugitive commit": R(Key("escape,colon") + Text("Gcommit")),
        "fugitive tab edit": R(Key("escape,colon") + Text("tabe ")),
        "fugitive save quit": R(Key("escape,colon") + Text("wq")),

        "insert": R(Key("i")),
        "chook": R(Key("escape")),

        "lower case": R(Key("u")),
        "upper case": R(Key("U")),
        "swap case": R(Key("tilde")),

        #"visual": Key("v"),
        "visual line": R(Key("s-v")),
        "visual block": R(Key("c-v")),

        "blork [<n>]": Key("b:%(n)d"),
        "williams [<n>]": Key("w:%(n)d"),
        "eat [<n>]": Key("w:%(n)e"),
        "keeko [<n>]": Key("k:%(n)d"),
        "jannet [<n>]": Key("j:%(n)d"),

        "page center": R(Key("z,dot")),
        "text format": R(Key("g,q")),

        "next paragraph": R(Key("rbrace")),
        "previous paragraph": R(Key("lbrace")),
        "a paragraph": R(Key("a,p")),
        "inner paragraph": R(Key("i,p")),

        #"single [<n>]": Key("x:%(n)d"),
        #"backspace [<n>]": Key("backspace:%(n)d"),

        "suck [<n>]": R(Key("x:%(n)d")),

        "join [<n>]": R(Key("J:%(n)d")),
        "rip [<n>] (whiskey|word)": R(Text("%(n)ddw")),
        "rip inner (whiskey | word)": R(Key("d,i,w")),
        "rip inner paragraph": R(Key("d,i,p")),
        "rip inner (raip|laip)": R(Key("d,i,rparen")),
        "rip inner (bracket|rack|lack)": R(Key("d,i,rbracket")),
        "rip inner (bracket|race|lace)": R(Key("d,i,rbrace")),

        "shift rip": R(Key("s-d")),
        "rip line [<n>]": R(Key("%(n)d,d,d")),

        "rice [<n>]": R(Key("escape,u:%(n)d")),
        "role [<n>]": R(Key("escape,c-r:%(n)d")),

        #'find [<n>] <letter>': Text('%(n)df') + Function(executeLetter),
        #'shift find [<n>] <letter>': Text('%(n)dF') + Function(executeLetter),

        #'[<n>] again': Text('%(n)d;'),
        #'[<n>] shift again': Text('%(n)d,'),

        #'until [<n>] <letter>': Text('%(n)dt') + Function(executeLetter),
        #'shift until [<n>] <letter>': Text('%(n)dT') + Function(executeLetter),

        "yank a raip": R(Key("y,a,rparen")),
        "yank inner raip": R(Key("y,i,rparen")),
        "yank inner rack": R(Key("y,i,rbracket")),
        "yank inner race": R(Key("y,i,rbrace")),
        "yank inner rangle": R(Key("y,i,rangle")),
        "yank line": R(Key("y,y")),

        "yank inner word": R(Key("y,i,w")),
        "yank word": R(Key("y,w")),

        "squirt": R(Key("p")),
        "sprout": R(Key("P")),

        "replace": Key("r"),
        "shift replace": R(Key("R")),

        "shift left": R(Key("langle,langle")),
        "shift right": R(Key("rangle,rangle")),

        #"fuzzy find": Key("backslash,t"),

        # Python specific macros that work together with certain plug-ins

        # used in Jedi vim
        #"go to definition": Key("backslash,d"),

        # Pete is shorthand for repeat
        "[<n>] Pete": R(Key("dot:%(n)d")),

        #"mimic <text>": release + Mimic(extra="text"),
        "complete function": R(Key("escape,A,colon,enter")),

        "quick save": R(Key("escape,colon,w,enter")),
        }

    extras = [
              Dictation("text"),
              Dictation("mim"),
              IntegerRefST("n", 1, 1000),
             ]
    defaults = {"n": 1, "mim": ""}

#---------------------------------------------------------------------------

control.nexus().merger.add_global_rule(Vim())

