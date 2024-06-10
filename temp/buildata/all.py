import subprocess
import platform
import os
import shutil

#limpiar los archivos del directorio data
# Comprobar si existe el directorio
if os.path.exists('../../data'):
    if platform.system() == 'Windows':
        shutil.rmtree('../../data',)
    else:
        subprocess.run(['rm', '-rf', '../../data'])

#esperar hasta que se eliminen los archivos
if platform.system() == 'Windows':
    subprocess.run(['timeout', '/t', '2'])
else:
    subprocess.run(['sleep', '2'])

#crear directorio ../data
if platform.system() == 'Windows':
    os.mkdir('../../data')
else:
    subprocess.run(['mkdir', '../../data'])

# Ejecutar converttxtcsv.py
subprocess.run(['python', './converttxtcsv.py'])

# Ejecutar getauth.py
subprocess.run(['python', './getauth.py'])

# Ejecutar getfrase.py
subprocess.run(['python', './getfrase.py'])

# Ejecutar lastbuildsqlite.py
subprocess.run(['python', './lastbuildsqlite.py'])