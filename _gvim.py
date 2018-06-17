#
# This file is a command-module for Dragonfly.
# (c) Copyright 2008 by Christo Butcher
# Licensed under the LGPL, see <http://www.gnu.org/licenses/>
#
# Modified by David Gessner
# Contains some code obtained from
# https://github.com/danielgm/JarvisGrammars/blob/master/vim.py

"""
Command-module for the vim editor
============================================================================

This module allows the user to control the vim text editor.


Discussion of this module
----------------------------------------------------------------------------

This command-module creates a powerful voice command for
editing and cursor movement.  This command's structure can
be represented by the following simplified language model:

 - *CommandRule* -- top-level rule which the user can say
    - *repetition* -- sequence of actions (name = "sequence")
       - *NormalModeKeystrokeRule* -- rule that maps a single
         spoken-form to an action
    - *optional* -- optional specification of repeat count
       - *integer* -- repeat count (name = "n")
       - *literal* -- "times"

The top-level command rule has a callback method which is
called when this voice command is recognized.  The logic
within this callback is very simple:

1. Retrieve the sequence of actions from the element with
   the name "sequence".
2. Retrieve the repeat count from the element with the name
   "n".
3. Execute the actions the specified number of times.

"""

try:
    import pkg_resources
    pkg_resources.require("dragonfly >= 0.6.5beta1.dev-r99")
except ImportError:
    pass

from dragonfly import *


#---------------------------------------------------------------------------
# Here we globally defined the release action which releases all
#  modifier-keys used within this grammar.  It is defined here
#  because this functionality is used in many different places.
#  Note that it is harmless to release ("...:up") a key multiple
#  times or when that key is not held down at all.

release = Key("shift:up, ctrl:up")

class LetterRule(MappingRule):
    exported = True
    mapping = {
        'blank nothing ignore': Key('a', static=True),

        #'arch': Key('a', static=True),
        #'brav': Key('b', static=True),
        #'char': Key('c', static=True),
        #'delta': Key('d', static=True),
        #'echo': Key('e', static=True),
        #'foxy': Key('f', static=True),
        #'goof': Key('g', static=True),
        #'hotel': Key('h', static=True),
        #'india': Key('i', static=True),
        #'julia': Key('j', static=True),
        #'kilo': Key('k', static=True),
        #'lima': Key('l', static=True),
        #'mike': Key('m', static=True),
        #'novakeen': Key('n', static=True),
        #'oscar': Key('o', static=True),
        #'prime': Key('p', static=True),
        #'quebec': Key('q', static=True),
        #'romeo': Key('r', static=True),
        #'sierra': Key('s', static=True),
        #'tango': Key('t', static=True),
        #'uniform': Key('u', static=True),
        #'victor': Key('v', static=True),
        #'whiskey': Key('w', static=True),
        #'x-ray': Key('x', static=True),
        #'yankee': Key('y', static=True),
        #'zulu': Key('z', static=True),

        #'shift arch': Key('A', static=True),
        #'shift brav': Key('B', static=True),
        #'shift char': Key('C', static=True),
        #'shift delta': Key('D', static=True),
        #'shift echo': Key('E', static=True),
        #'shift foxy': Key('F', static=True),
        #'shift goof': Key('G', static=True),
        #'shift hotel': Key('H', static=True),
        #'shift india': Key('I', static=True),
        #'shift julia': Key('J', static=True),
        #'shift kilo': Key('K', static=True),
        #'shift lima': Key('L', static=True),
        #'shift mike': Key('M', static=True),
        #'shift novakeen': Key('N', static=True),
        #'shift oscar': Key('O', static=True),
        #'shift prime': Key('P', static=True),
        #'shift quebec': Key('Q', static=True),
        #'shift romeo': Key('R', static=True),
        #'shift sierra': Key('S', static=True),
        #'shift tango': Key('T', static=True),
        #'shift uniform': Key('U', static=True),
        #'shift victor': Key('V', static=True),
        #'shift whiskey': Key('W', static=True),
        #'shift x-ray': Key('X', static=True),
        #'shift yankee': Key('Y', static=True),
        #'shift zulu': Key('Z', static=True),

        #'zero': Key('0'),
        #'one': Key('1'),
        #'two': Key('2'),
        #'three': Key('3'),
        #'four': Key('4'),
        #'five': Key('5'),
        #'six': Key('6'),
        #'seven': Key('7'),
        #'eight': Key('8'),
        #'nine': Key('9'),

        #'ace': Key('space'),
        #'tabby': Key('tab'),

        #'ampersand': Key('ampersand'),
        #'apostrophe': Key('apostrophe'),
        #'starling': Key('asterisk'),
        #'at sign': Key('at'),
        #'backslash': Key('backslash'),
        #'backtick': Key('backtick'),
        #'pipe sim': Key('bar'),
        #'caret': Key('caret'),
        #'deckle': Key('colon'),
        #'boom': Key('comma'),
        #'dolly': Key('dollar'),
        #'(dot|period)': Key('dot'),
        #'quote': Key('dquote'),
        #'equals': Key('equal'),
        #'clamor': Key('exclamation'),
        #'hashtag': Key('hash'),
        #'minus': Key('minus'),
        #'modulo': Key('percent'),
        #'plus': Key('plus'),
        #'question': Key('question'),
        #'semper': Key('semicolon'),
        #'slash': Key('slash'),
        #'thin quote': Key('squote'),
        #'underscore': Key('underscore'),

        #'langle': Key('langle'),
        #'lace': Key('lbrace'),
        #'lack': Key('lbracket'),
        #'laip': Key('lparen'),
        #'rangle': Key('rangle'),
        #'race': Key('rbrace'),
        #'rack': Key('rbracket'),
        #'raip': Key('rparen'),

        #'zero': Key('0'),
        #'ane': Key('1'),
        #'twain': Key('2'),
        #'traio': Key('3'),
        #'fairn': Key('4'),
        #'faif': Key('5'),
        #'six': Key('6'),
        #'seven': Key('7'),
        #'eigen': Key('8'),
        #'nine': Key('9'),


    }

letter = RuleRef(rule=LetterRule(), name='letter')
letter_sequence = Repetition(letter, min=1, max=32, name='letter_sequence')

def executeLetter(letter):
    letter.execute()

def executeLetterSequence(letter_sequence):
    for letter in letter_sequence:
        letter.execute()

#---------------------------------------------------------------------------
# Set up this module's configuration.

# This defines a configuration object with the name "gvim".
config            = Config("gvim")
config.cmd        = Section("Language section")


# This searches for a file with the same name as this file (gvim.py), but with
# the extension ".py" replaced by ".txt". In other words, it loads the
# configuration specified in the file gvim.txt
namespace = config.load()

#---------------------------------------------------------------------------
# Here we prepare the list of formatting functions from the config file.

# Retrieve text-formatting functions from this module's config file.
#  Each of these functions must have a name that starts with "format_".
format_functions = {}
if namespace:
    for name, function in namespace.items():
     if name.startswith("format_") and callable(function):
        spoken_form = function.__doc__.strip()

        # We wrap generation of the Function action in a function so
        #  that its *function* variable will be local.  Otherwise it
        #  would change during the next iteration of the namespace loop.
        def wrap_function(function):
            def _function(dictation):
                formatted_text = function(dictation)
                Text(formatted_text).execute()
            return Function(_function)

        action = wrap_function(function)
        format_functions[spoken_form] = action


# Here we define the text formatting rule.
# The contents of this rule were built up from the "format_*"
#  functions in this module's config file.
if format_functions:
    class FormatRule(MappingRule):

        mapping  = format_functions
        extras   = [Dictation("dictation")]

else:
    FormatRule = None


#---------------------------------------------------------------------------
# Here we define the keystroke rule.

# This rule maps spoken-forms to actions.  Some of these
#  include special elements like the number with name "n"
#  or the dictation with name "text".  This rule is not
#  exported, but is referenced by other elements later on.
#  It is derived from MappingRule, so that its "value" when
#  processing a recognition will be the right side of the
#  mapping: an action.
# Note that this rule does not execute these actions, it
#  simply returns them when it's value() method is called.
#  For example "up 4" will give the value Key("up:4").
# More information about Key() actions can be found here:
#  http://dragonfly.googlecode.com/svn/trunk/dragonfly/documentation/actionkey.html
class NormalModeKeystrokeRule(MappingRule):

    exported = False

    mapping = {
        # Directions
        "hotel [<n>]": Key("h"),
        "julia [<n>]": Key("j"),
        "kilo [<n>]": Key("k"),
        "lima [<n>]": Key("l"),

        "dolly": Key("dollar"),
        "modulo": Key("percent"),

        "lower case": Key("g,u"),
        "upper case": Key("g,U"),
        "swap case": Key("tilde"),

        "visual": Key("v"),
        "visual line": Key("s-v"),
        "visual block": Key("c-v"),

        "next": Key("n"),
        "previous": Key("N"),
        "brav [<n>]": Key("b:%(n)d"),
        "whiskey [<n>]": Key("w:%(n)d"),
        "echo [<n>]": Key("e:%(n)d"),

        "page center": Key("z,dot"),
        "text format": Key("g,q"),

        "next paragraph": Key("rbrace"),
        "previous paragraph": Key("lbrace"),
        "a paragraph": Key("a,p"),
        "inner paragraph": Key("i,p"),

        "single [<n>]": Key("x:%(n)d"),
        #"backspace [<n>]": Key("backspace:%(n)d"),


        "Pete macro [<n>]": Key("at,at:%(n)d"),

        "join [<n>]": Key("J:%(n)d"),

        "rip": Key("d"),
        "rip [<n>] (whiskey|word)": Text("%(n)ddw"),
        "rip a (whiskey | word)": Key("d,a,w"),
        "rip inner (whiskey | word)": Key("d,i,w"),
        "rip a paragraph": Key("d,a,p"),
        "rip inner paragraph": Key("d,i,p"),
        "rip a (paren|parenthesis|raip|laip)": Key("d,a,rparen"),
        "rip inner (raip|laip)": Key("d,i,rparen"),
        "rip a (bracket|rack|lack)": Key("d,a,rbracket"),
        "rip inner (bracket|rack|lack)": Key("d,i,rbracket"),
        "rip a (bracket|race|lace)": Key("d,a,rbrace"),
        "rip inner (bracket|race|lace)": Key("d,i,rbrace"),

        #"[<n>] (increment|increase)": Key("c-a:%(n)d"),
        #"[<n>] (decrement|decrease)": Key("c-x:%(n)d"),

        "shift rip": Key("s-d"),
        "rip line [<n>]": Key("%(n)d,d,d"),

        "rice [<n>]": Key("u:%(n)d"),
        "role [<n>]": Key("c-r:%(n)d"),

        #'[<n>] find <letter>': Text('%(n)df') + Function(executeLetter),
        #'[<n>] shift find <letter>': Text('%(n)dF') + Function(executeLetter),
        'find [<n>] <letter>': Text('%(n)df') + Function(executeLetter),
        'shift find [<n>] <letter>': Text('%(n)dF') + Function(executeLetter),

        #'[<n>] again': Text('%(n)d;'),
        #'[<n>] shift again': Text('%(n)d,'),

        #'[<n>] until <letter>': Text('%(n)dt') + Function(executeLetter),
        #'[<n>] shift until <letter>': Text('%(n)dT') + Function(executeLetter),
        'until [<n>] <letter>': Text('%(n)dt') + Function(executeLetter),
        'shift until [<n>] <letter>': Text('%(n)dT') + Function(executeLetter),

        "yank": Key("y"),
        "yank a paragraph": Key("y,a,p"),
        "yank inner paragraph": Key("y,i,p"),
        "yank a raip": Key("y,a,rparen"),
        "yank inner raip": Key("y,i,rparen"),
        "yank a rack": Key("y,a,rparen"),
        "yank inner rack": Key("y,i,rbracket"),
        "yank a race": Key("y,a,rparen"),
        "yank inner race": Key("y,i,rbrace"),
        "yank a rangle": Key("y,a,rparen"),
        "yank inner rangle": Key("y,i,rangle"),
        "yank line": Key("y,y"),
        "yank inner word": Key("y,i,w"),
        "yank word": Key("y,w"),

        "squirt": Key("p"),
        "sprout": Key("P"),

        "replace": Key("r"),
        "shift replace": Key("R"),

        "shift left": Key("langle,langle"),
        "shift right": Key("rangle,rangle"),

        #"fuzzy find": Key("backslash,t"),

	# Python specific macros that work together with certain plug-ins
	
	# used in Jedi vim
	"go to definition": Key("backslash,d"),

        # Pete is shorthand for repeat
        "[<n>] Pete": Key("dot:%(n)d"),

        #"mimic <text>": release + Mimic(extra="text"),

        "kapa sink": Key("A,escape,o"),
        "kapa dock": Key("A,semicolon,escape,o"),
        
        "quick save": Key("colon,w,enter"),
        "ZZ": Key("colon,Z,Z"),

    }
    extras   = [
        letter,
        letter_sequence,
        IntegerRef("n", 1, 100),
        Dictation("text"),
        Dictation("text2"),
    ]
    defaults = {
        "n": 1,
    }
    # Note: when processing a recognition, the *value* of
    #  this rule will be an action object from the right side
    #  of the mapping given above.  This is default behavior
    #  of the MappingRule class' value() method.  It also
    #  substitutes any "%(...)." within the action spec
    #  with the appropriate spoken values.


#---------------------------------------------------------------------------
# Here we create an element which is the sequence of keystrokes.

# First we create an element that references the keystroke rule.
#  Note: when processing a recognition, the *value* of this element
#  will be the value of the referenced rule: an action.
normal_mode_alternatives = []
normal_mode_alternatives.append(RuleRef(rule=NormalModeKeystrokeRule()))
if FormatRule:
    normal_mode_alternatives.append(RuleRef(rule=FormatRule()))
normal_mode_single_action = Alternative(normal_mode_alternatives)

# Second we create a repetition of keystroke elements.
#  This element will match anywhere between 1 and 16 repetitions
#  of the keystroke elements.  Note that we give this element
#  the name "sequence" so that it can be used as an extra in
#  the rule definition below.
# Note: when processing a recognition, the *value* of this element
#  will be a sequence of the contained elements: a sequence of
#  actions.
normal_mode_sequence = Repetition(normal_mode_single_action,
    min=1, max=16, name="normal_mode_sequence")


#---------------------------------------------------------------------------
# Here we define the top-level rule which the user can say.

# This is the rule that actually handles recognitions.
#  When a recognition occurs, it's _process_recognition()
#  method will be called.  It receives information about the
#  recognition in the "extras" argument: the sequence of
#  actions and the number of times to repeat them.
class NormalModeRepeatRule(CompoundRule):

    # Here we define this rule's spoken-form and special elements.
    spec     = "<normal_mode_sequence> [[[and] repeat [that]] <n> times]"
    extras   = [
            # Sequence of actions defined above.
            normal_mode_sequence,
            # Times to repeat the sequence.
            IntegerRef("n", 1, 100),
        ]
    defaults = {
            # Default repeat count.
            "n": 1,
        }

    # This method gets called when this rule is recognized.
    # Arguments:
    #  - node -- root node of the recognition parse tree.
    #  - extras -- dict of the "extras" special elements:
    #     . extras["sequence"] gives the sequence of actions.
    #     . extras["n"] gives the repeat count.
    def _process_recognition(self, node, extras):
        # A sequence of actions.
        normal_mode_sequence = extras["normal_mode_sequence"]
        # An integer repeat count.
        count = extras["n"]
        for i in range(count):
            for action in normal_mode_sequence:
                action.execute()
        release.execute()


#---------------------------------------------------------------------------

gvim_window_rule = MappingRule(
    name = "gvim_window",
    mapping = {
        # window navigation commands
        "glass left": Key("c-w,h"),
        "glass right": Key("c-w,l"),
        "glass up": Key("c-w,k"),
        "glass down": Key("c-w,j"),

        # window creation commands
        "glass split": Key("c-w,s"),
        "glass vertical split": Key("c-w,v"),
        },
    extras = [
        ]
)

#---------------------------------------------------------------------------

gvim_tabulator_rule = MappingRule(
    name = "gvim_tabulators",
    mapping = {
        # tabulator navigation commands
        "glass next tab": Key("g,t"),
        "glass previous tab": Key("g,T"),
        },
    extras = [
        ]
)

#---------------------------------------------------------------------------

gvim_general_rule = MappingRule(
    name = "gvim_general",
    mapping = {
        "walk back": Key("escape,u"),
        },
    extras = [
        ]
)

#---------------------------------------------------------------------------

gvim_navigation_rule = MappingRule(
    name = "gvim_navigation",
    mapping = {
        "up we go": Key("g,g"),
        "base camp": Key("G"),
        "go old": Key("c-o"),

        "cursor top": Key("s-h"),
        "cursor middle": Key("s-m"),
        "cursor (low | bottom)": Key("s-l"),

        # line navigation
        "jump to line <line>": Key("colon") + Text("%(line)s\n"),

        # searching
        #"search <text>": Key("slash") + Text("%(text)s\n"),
        "search": Key("slash"),
        "search this": Key("asterisk"),
        "search this up": Key("hash"),
        "back search": Key("question") + Text("%(text)s\n"),

        },
    extras = [
        Dictation("text"),
        IntegerRef("n", 1, 50),
        IntegerRef("line", 1, 10000)
        ]
)

#---------------------------------------------------------------------------


class ExModeEnabler(CompoundRule):
    # Spoken command to enable the ExMode grammar.
    spec = "enter command mode"

    # Callback when command is spoken.
    def _process_recognition(self, node, extras):
        exModeBootstrap.disable()
        normalModeGrammar.disable()
        ExModeGrammar.enable()
        Key("colon").execute()
        print "ExMode grammar enabled"
        print "Available commands:"
        print '  \n'.join(ExModeCommands.mapping.keys())
        print "\n(EX MODE)"


class ExModeDisabler(CompoundRule):
    # spoken command to exit ex mode
    spec = "<command>"
    extras = [Choice("command", {
        "cancel": "cancel",
    })]

    def _process_recognition(self, node, extras):
        ExModeGrammar.disable()
        exModeBootstrap.enable()
        normalModeGrammar.enable()
        if extras["command"] == "cancel":
            print "ex mode command canceled"
            Key("escape").execute()
        else:
            print "ex mode command accepted"
            Key("enter").execute()
        print "\n(NORMAL)"

# handles ExMode control structures
class ExModeCommands(MappingRule):
    mapping  = {
        "tab edit": Text("tabe "),

        "set number": Text("set number "),
        "set relative number": Text("set relativenumber "),
        "set ignore case": Text("set ignorecase "),
        "set no ignore case": Text("set noignorecase "),
        "set file format UNIX": Text("set fileformat=unix "),
        "set file format DOS": Text("set fileformat=dos "),
        "set file type Python": Text("set filetype=python"),
        "set file type tex": Text("set filetype=tex"),

        "show me the working directory": Text("pwd \n"),

        "help": Text("help"),
        "substitute": Text("s/"),
        "list all": Text("!ls -al "),
        "list in file": Text("r!ls "),

        # Eddit specific important files
        "eddit configuration file": Text("tabe ~/.vimrc"),

        # Git stuff with "fugitive"
        "fugitive status": Text("Gstatus"),
        "fugitive commit": Text("Gcommit"),

        # Specific places
        "enter directory speach coding home": Text("/cygdrive/c/Users/omyers/Documents/NatLink"),
        "enter directory computer home": Text("/cygdrive/c/Users/omyers/"),
        "enter directory repositories home": Text("/cygdrive/c/Users/omyers/PortableHardDriveSynced/repositories")
    }
    extras = [
        Dictation("text"),
        IntegerRef("n", 1, 50),
    ]
    defaults = {
        "n": 1,
    }


#---------------------------------------------------------------------------

class InsertModeEnabler(CompoundRule):
    spec = "<command>"
    extras = [Choice("command", {
        "insert": "i",
        "shift insert": "I",

        "change": Key("c"),
        "change (word|whiskey)": Key("c,w"),
        "change (echo|end)": Key("c,e"),
        "change a paragraph": Key("c,a,p"),
        "change inner paragraph": Key("c,i,p"),
        "change a (paren|parenthesis|raip|laip)": Key("c,a,rparen"),
        "change inner (paren|parenthesis|raip|laip)": Key("c,i,rparen"),
        "change a (bracket|rack|lack)": Key("d,a,rbracket"),
        "change inner (bracket|rack|lack)": Key("d,i,rbracket"),
        "change a (bracket|race|lace)": Key("d,a,rbrace"),
        "change inner (bracket|race|lace)": Key("d,i,rbrace"),
        "shift change": "C",

        "change line" : "S",
        "change chair" : "s",

        "(after | append)": "a",
        "shift (after | append)": "A",

        "oh": "o",
        "shift oh": "O",

	# Jedi vim rename command
	#"rename": "backslash,r",
    })]

    def _process_recognition(self, node, extras):
        InsertModeBootstrap.disable()
        normalModeGrammar.disable()
        InsertModeGrammar.enable()
        for string in extras["command"].split(','):
            key = Key(string)
            key.execute()
        print "Available commands:"
        print '  \n'.join(InsertModeCommands.mapping.keys())
        print "\n(INSERT)"



class InsertModeDisabler(CompoundRule):
    # spoken command to exit InsertMode
    spec = "<command>"
    extras = [Choice("command", {
        "cancel": "cancel",
        "leave insert": "escape",
        "escape": "escape"
    })]

    def _process_recognition(self, node, extras):
        InsertModeGrammar.disable()
        InsertModeBootstrap.enable()
        normalModeGrammar.enable()
        Key("escape").execute()
        if extras["command"] == "cancel":
            Key("u").execute()
            print "Insert command canceled"
        else:
            print "Insert command accepted"
        print "\n(NORMAL)"


# handles InsertMode control structures
class InsertModeCommands(MappingRule):
    mapping  = {
        #"<text>": Text("%(text)s"),
        "(scratch|delete) [<n>]": Key("c-w:%(n)d"),
        "slap [<n>]": Key("enter:%(n)d"),
        #"tab [<n>]": Key("tab:%(n)d"),
        #"backspace [<n>]": Key("backspace:%(n)d"),
        "(scratch|delete) line": Key("c-u"),

        #Ultisnip stuff
        "complete": Key("c-j"),
        "snip next": Key("c-l"),
        "snip previous": Key("c-h"),

	#"assign": Key("space,equal,space"),
	#"plus": Key("space,plus,space"),
	#"minus": Key("space,minus,space"),
	#"times": Key("space,asterisk,space"),
	#"equals": Key("space,equal,equal,space"),
	#"not equals": Key("space,exclamation,equal,space"),
	#"triple quote": Key("dquote,dquote,dquote"),

	# snippets for snipmate
	#"new fixture": Key("f,i,x,tab"),
	#"new method": Key("d,e,f,s,tab"),
	#"new class": Key("c,l,tab"),
	#"new function": Key("d,e,f,tab"),
	#"new while loop": Key("w,h,tab"),
	#"new for loop": Key("f,o,r,tab"),

        #'zero': Key('0'),
        #'ane': Key('1'),
        #'twain': Key('2'),
        #'traio': Key('3'),
        #'fairn': Key('4'),
        #'faif': Key('5'),
        #'six': Key('6'),
        #'seven': Key('7'),
        #'eigen': Key('8'),
        #'nine': Key('9'),

        'shift arch': Key('A', static=True),
        'shift brav': Key('B', static=True),
        'shift char': Key('C', static=True),
        'shift delta': Key('D', static=True),
        'shift echo': Key('E', static=True),
        'shift foxy': Key('F', static=True),
        'shift goof': Key('G', static=True),
        'shift hotel': Key('H', static=True),
        'shift india': Key('I', static=True),
        'shift julia': Key('J', static=True),
        'shift kilo': Key('K', static=True),
        'shift lima': Key('L', static=True),
        'shift mike': Key('M', static=True),
        'shift novakeen': Key('N', static=True),
        'shift oscar': Key('O', static=True),
        'shift prime': Key('P', static=True),
        'shift quebec': Key('Q', static=True),
        'shift romeo': Key('R', static=True),
        'shift sierra': Key('S', static=True),
        'shift tango': Key('T', static=True),
        'shift uniform': Key('U', static=True),
        'shift victor': Key('V', static=True),
        'shift whiskey': Key('W', static=True),
        'shift x-ray': Key('X', static=True),
        'shift yankee': Key('Y', static=True),
        'shift zulu': Key('Z', static=True),




    }
    extras = [
        Dictation("text"),
        IntegerRef("n", 1, 50),
    ]
    defaults = {
        "n": 1,
    }


#---------------------------------------------------------------------------

gvim_exec_context = AppContext(executable="gvim")
# set the window title to vim in the putty session for the following context to
# work.
vim_putty_context = AppContext(title="vim")
putty_context = AppContext(title="192.168.56.1 - PuTTY")
#putty_context = AppContext(title="2. bash")
debian_putty_context = AppContext(title="Debian")
pycharm_context = AppContext(title="PyCharm")
gvim_context = (gvim_exec_context | vim_putty_context | putty_context | debian_putty_context | pycharm_context)

# set up the grammar for vim's ex mode
exModeBootstrap = Grammar("ExMode bootstrap", context=gvim_context)
exModeBootstrap.add_rule(ExModeEnabler())
exModeBootstrap.load()
ExModeGrammar = Grammar("ExMode grammar", context=gvim_context)
ExModeGrammar.add_rule(ExModeCommands())
ExModeGrammar.add_rule(ExModeDisabler())
ExModeGrammar.load()
ExModeGrammar.disable()



# set up the grammar for vim's insert mode
InsertModeBootstrap = Grammar("InsertMode bootstrap", context=gvim_context)
InsertModeBootstrap.add_rule(InsertModeEnabler())
InsertModeBootstrap.load()
InsertModeGrammar = Grammar("InsertMode grammar", context=gvim_context)
InsertModeGrammar.add_rule(InsertModeCommands())
InsertModeGrammar.add_rule(InsertModeDisabler())
InsertModeGrammar.load()
InsertModeGrammar.disable()




# set up the grammar for vim's normal mode and start normal mode
normalModeGrammar = Grammar("gvim", context=gvim_context)
normalModeGrammar.add_rule(NormalModeRepeatRule())
normalModeGrammar.add_rule(gvim_window_rule)
normalModeGrammar.add_rule(gvim_tabulator_rule)
normalModeGrammar.add_rule(gvim_general_rule)
normalModeGrammar.add_rule(gvim_navigation_rule)
normalModeGrammar.load()



# Unload function which will be called at unload time.
def unload():
    global normalModeGrammar
    if normalModeGrammar: normalModeGrammar.unload()
    normalModeGrammar = None

    global ExModeGrammar
    if ExModeGrammar: ExModeGrammar.unload()
    ExModeGrammar = None

    global InsertModeGrammar
    if InsertModeGrammar: InsertModeGrammar.unload()
    InsertModeGrammar = None
