'''
Created on Sep 1, 2015

@author: synkarius
'''
from dragonfly import Key, Text

from caster.lib import control
from caster.lib.ccr.standard import SymbolSpecs
from caster.lib.dfplus.merge.mergerule import MergeRule
from caster.lib.dfplus.state.short import R


class Bash(MergeRule):
    mapping = {
        #"bash back [<n>]": R(Key(back "%(n)d,d,d")),
        "pock back": R(Text("cd ../") + Key("enter") + Text("ls") + Key("enter")),
        "pock slip": R(Text("../")),
        "pock change": R(Text("cd ")),
        "pock snake": R(Text("conda ")),
        "pock list": R(Text("ls") + Key("enter")),
        "pock pipe": R(Text(" | ")),

#        SymbolSpecs.IF:                 R(Text("if [[  ]]; ")+Key("left/5:5"), rdescript="Bash: If"),
#        SymbolSpecs.ELSE:               R(Text("else"), rdescript="Bash: Else"),
#        #
#        SymbolSpecs.SWITCH:             R(Text("case TOKEN in"), rdescript="Bash: Switch"),
#        SymbolSpecs.CASE:               R(Text("TOKEN)  ;;")+Key("left/5:2"), rdescript="Bash: Case"),
#        SymbolSpecs.BREAK:              R(Text("break"), rdescript="Bash: Break"),
#        SymbolSpecs.DEFAULT:            R(Text("*)  ;;"), rdescript="Bash: Default"),
#        #
#        SymbolSpecs.DO_LOOP:            R(Text("until [  ]; do")+Key("left/5:7"), rdescript="Bash: Do Loop"),
#        SymbolSpecs.WHILE_LOOP:         R(Text("while [  ]; do")+Key("left/5:7"), rdescript="Bash: While"),
#        SymbolSpecs.FOR_LOOP:           R(Text("for (( i=0; i<=TOKEN; i++ )); do"), rdescript="Bash: For i Loop"),
#        SymbolSpecs.FOR_EACH_LOOP:      R(Text("for TOKEN in TOKEN; do"), rdescript="Bash: For Each Loop"), 
#        #
#        # integers?
#        # strings?
#        # floats?
#        #
#        SymbolSpecs.AND:                R(Text(" && "), rdescript="Bash: And"),
#        SymbolSpecs.OR:                 R(Text(" || "), rdescript="Bash: Or"),
#        SymbolSpecs.NOT:                R(Text("!"), rdescript="Bash: Not"),
#        #
#        SymbolSpecs.SYSOUT:             R(Text("echo "), rdescript="Bash: Print"),
#        #
#        SymbolSpecs.IMPORT:             R(Text(". /path/to/functions"), rdescript="Bash: Import"), # (top of file, under #!/bin/bash)
#        # 
#        SymbolSpecs.FUNCTION:           R(Text("TOKEN(){}")+Key("left, enter/5:2"), rdescript="Bash: Function"),
#        # classes?
#        #
#        SymbolSpecs.COMMENT:            R(Text("# "), rdescript="Bash: Add Comment"),
#        # no multiline comment in bash
#        #
#        SymbolSpecs.NULL:               R(Text('-z "$var"')+Key("left/5:1"), rdescript="Bash: Null"),
#        #
#        SymbolSpecs.RETURN:             R(Text("return "), rdescript="Bash: Return"),
#        #
#        SymbolSpecs.TRUE:               R(Text("true"), rdescript="Bash: True"),
#        SymbolSpecs.FALSE:              R(Text("false"), rdescript="Bash: False"),
#        
      
        }

    extras   = []
    defaults = {}

control.nexus().merger.add_global_rule(Bash())
