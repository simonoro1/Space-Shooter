import py2exe
setup( name= "juego",
scripts = ["main.py",
console = [ "main.py",
options = {"py2exe": {"bundle_files": 1 }},
zipfile = None, 

)