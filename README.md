# python-swiprolog-interface

A simple python interface for SWI-Prolog, for terminal use.


## Installation

1. Download the repo files, place the index.py file next to your .pl file(s)
2. Create a virtual environment using virtualenv, and activate it
3. Install pyswip

If you are getting an error, running the script, try moving (and replacing) the tweaked core.py into <your virtual environment>/Lib/site-packages/pyswip folder. If the SWI-Prolog file "libswipl.dll" is not located at "C:/Program Files/swipl/bin/libswipl.dll", make sure to change that path accordingly (Change the LIB_FILE_LOCATION variable, at the top of the `core.py` file)

## Usage

Run `python index.py` to start up the interpreter. By default, this will search and use the first found .pl file, to use.

You can specify a different file by passing in a command line argument, such as `python index.py --i=yourFile.pl`.

The script loads the .pl file, stays at prompt, taking any Prolog queries provided. The .pl file is re-consulted every time a search query is entered, meaning you can change your file without needing to re-start the script.

You can use the up key to scroll back through the query history (even from other times the script was run).


## Limitations

Trace cannot be turned on. This is due to a limitation with the original pyswip library (if it is possible to do it with the library, please let me know/pull request it in, and I'll have a look at adding it in).
