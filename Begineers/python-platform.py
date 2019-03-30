# Platform module includes the tools for learning about the interpreter, 
# operating system, and hardware platform where a program is running.

import platform
print("\n *** Check Operating System Platform Details ***\n")
print(f' Python Version : {platform.python_version()}')
print(f' Python Version tuple : {platform.python_version_tuple()}')
print(f' Python Compiler : {platform.python_compiler()}')
print(f' Python Build : {platform.python_build()}')
print(f' Normal : {platform.platform()}')
print(f' Aliased : {platform.platform(aliased=True)}')
print(f' Terse : {platform.platform(terse=True)}')
print(f' Uname : {platform.uname()}')
print(f' System : {platform.system()}')
print(f' Node : {platform.node()}')
print(f' Release : {platform.release()}')
print(f' Version : {platform.version()}')
print(f' Machine : {platform.machine()}')
print(f' Processor : {platform.processor()}')
print(f' Architecture : {platform.architecture()}')