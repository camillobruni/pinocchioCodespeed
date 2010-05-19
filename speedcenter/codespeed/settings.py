# -*- coding: utf-8 -*-
## Define some default options here ##
defaultexecutable = 6 # Executable that should be chosen as default in the overview
                         # Given as the id of the executable.
                         # Example: defaultexecutable = 1

defaultbaseline = None #{'executable' : 2, 'revision' : 'baseline'}, # ruby 1.87
# Which executable + revision should be default as a baseline
# Given as the id of the executable + commitid of the revision
# Example: defaultbaseline = {'executable': 4, 'revision': 262}
                       
baselinelist = None #[{'executable' : 8, 'revision' : 'baseline'}] #Phaor
#[
#    {'executable' : 1, 'revision' : 'baseline'}, # ruby 1.87
#    {'executable' : 3, 'revision' : 'baseline'}, # GNU Smalltalk v3.0.3
#    {'executable' : 2, 'revision' : 'baseline'}, # ruby 1.9.0 
#    {'executable' : 5, 'revision' : 'baseline'}, # Python 3.1.1+
#    {'executable' : 4, 'revision' : 'baseline'}, # Python 2.6.4
#    {'executable' : 8, 'revision' : 'baseline'}, # Pharo
#] 

# Which executables + revisions should be listed as comparison options
# Example:defaultbaseline = [
#             {'executable': 4, 'revision': 262},
#             {'executable': 2, 'revision': 56565},
#]
