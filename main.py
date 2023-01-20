'''
    Description: This is a FOSS project aimed to help programmers to alter module's code in run-time.
                 Currently, only from python code and on python modules.
    Author: CodeDoushair
    Python-version: 3.10
'''

from importlib import reload
import inspect
import re
import io
import builtins

'''
I should further explore:
from types import ModuleType
from importlib.machinery import ModuleSpec
        "     .util.module_from_spec
'''
'''
1. get source code
    1. get source file by __file__
    2. save it on a backup variable
'''

'''
regex
2. find
    1. declarations
        1. func
            1. name
            2. args
                1. type             
            3. return type
            4. decors
            5. source code (by line, offseted from the first line of source code)
        2. class
        3. vars
        4. NOTA (not of the above = normal instructions)
    2. doc

* need to be identified by indentions
'''

'''
3. change what's to be changed
    1. get the origin from step 2
    2. get the desired change from the user
    3. replace it!
'''

'''
4. load the changes on the file
4.1. reload the module
'''

'''
5. safely close changes
    1. reload the origin to the file
    2. reload the module

* add support to with statment like:
with open(...) as f:
    ...

# ( f.close() )

'''

# example:
'''
from importlib import reload
import antigravity

# for convenience
loc = antigravity.__file__

# 1st run - before altering
antigravity.geohash(37.421542, -122.085589, b'2005-05-26-10458.68')
# -> 37.857713 -122.544543

# open and make the desired changes
with open(loc) as f:
    origin = f.read()

new = origin.replace("print(\'", "print(\'Hello: ")

with open(loc, "w") as f:
    f.write(new)

# reloading the module using importlib
reload(antigravity)

# 2nd run - after altering
antigravity.geohash(37.421542, -122.085589, b'2005-05-26-10458.68')
# -> Hello: 37.857713 -122.544543

# return everything back to previous state
with open(loc, "w") as f:
    f.write(origin)
'''