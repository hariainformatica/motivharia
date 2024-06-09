import subprocess

#limpiar los archivos del directorio data
subprocess.run(['rm', '-rf', './data/*'])
#esperar hasta que se eliminen los archivos
subprocess.run(['sleep', '2'])

# Ejecutar converttxtcsv.py
subprocess.run(['python', './converttxtcsv.py'])

# Ejecutar getauth.py
subprocess.run(['python', './getauth.py'])

# Ejecutar getfrase.py
subprocess.run(['python', './getfrase.py'])

# Ejecutar lastbuildsqlite.py
subprocess.run(['python', './lastbuildsqlite.py'])