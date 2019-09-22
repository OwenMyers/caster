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

        "glass left": R(Key("c-w,h")),
        "glass right": R(Key("c-w,l")),
        "glass up": R(Key("c-w,k")),
        "glass down": R(Key("c-w,j")),
        "close lower": R(Key("escape,c-w,j,colon,q")),


        "fugitive status": R(Key("colon") + Text("Gstatus") + Key('enter')),
        "fugitive commit": R(Key("colon") + Text("Gcommit")),
        "insert": R(Key("i")),
        "leave insert": R(Key("escape")),

        "lower case": R(Key("u")),
        "upper case": R(Key("U")),
        "swap case": R(Key("tilde")),

        #"visual": Key("v"),
        "visual line": R(Key("s-v")),
        "visual block": R(Key("c-v")),

        #"brav [<n>]": Key("b:%(n)d"),
        #"whiskey [<n>]": Key("w:%(n)d"),
        #"echo [<n>]": Key("e:%(n)d"),

        "page center": R(Key("z,dot")),
        "text format": R(Key("g,q")),

        "next paragraph": R(Key("rbrace")),
        "previous paragraph": R(Key("lbrace")),
        "a paragraph": R(Key("a,p")),
        "inner paragraph": R(Key("i,p")),

        #"single [<n>]": Key("x:%(n)d"),
        #"backspace [<n>]": Key("backspace:%(n)d"),

        "Pete macro [<n>]": R(Key("at,at:%(n)d")),

        "join [<n>]": R(Key("J:%(n)d")),
        "rip": R(Key("d")),
        "rip [<n>] (whiskey|word)": R(Text("%(n)ddw")),
        "rip a (whiskey | word)": R(Key("d,a,w")),
        "rip inner (whiskey | word)": R(Key("d,i,w")),
        "rip a paragraph": R(Key("d,a,p")),
        "rip inner paragraph": R(Key("d,i,p")),
        "rip a (paren|parenthesis|raip|laip)": R(Key("d,a,rparen")),
        "rip inner (raip|laip)": R(Key("d,i,rparen")),
        "rip a (bracket|rack|lack)": R(Key("d,a,rbracket")),
        "rip inner (bracket|rack|lack)": R(Key("d,i,rbracket")),
        "rip a (bracket|race|lace)": R(Key("d,a,rbrace")),
        "rip inner (bracket|race|lace)": R(Key("d,i,rbrace")),

        "shift rip": R(Key("s-d")),
        "rip line [<n>]": R(Key("%(n)d,d,d")),

        "rice [<n>]": R(Key("u:%(n)d")),
        "role [<n>]": R(Key("c-r:%(n)d")),

        #'find [<n>] <letter>': Text('%(n)df') + Function(executeLetter),
        #'shift find [<n>] <letter>': Text('%(n)dF') + Function(executeLetter),

        #'[<n>] again': Text('%(n)d;'),
        #'[<n>] shift again': Text('%(n)d,'),

        #'until [<n>] <letter>': Text('%(n)dt') + Function(executeLetter),
        #'shift until [<n>] <letter>': Text('%(n)dT') + Function(executeLetter),

        "yank": R(Key("y")),
        "yank a paragraph": R(Key("y,a,p")),
        "yank inner paragraph": R(Key("y,i,p")),
        "yank a raip": R(Key("y,a,rparen")),
        "yank inner raip": R(Key("y,i,rparen")),
        "yank a rack": R(Key("y,a,rparen")),
        "yank inner rack": R(Key("y,i,rbracket")),
        "yank a race": R(Key("y,a,rparen")),
        "yank inner race": R(Key("y,i,rbrace")),
        "yank a rangle": R(Key("y,a,rparen")),
        "yank inner rangle": R(Key("y,i,rangle")),
        "yank line [<n>]": R(Key("%(n)d,y,y")),
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

        "kapa sink": R(Key("A,escape,o")),
        "kapa dock": R(Key("A,semicolon,escape,o")),
        "complete function": R(Key("escape,A,colon,enter")),

        "quick save": R(Key("colon,w,enter")),
        }

    extras = [
              Dictation("text"),
              Dictation("mim"),
              IntegerRefST("n", 1, 1000),
             ]
    defaults = {"n": 1, "mim": ""}

#---------------------------------------------------------------------------

control.nexus().merger.add_global_rule(Vim())

