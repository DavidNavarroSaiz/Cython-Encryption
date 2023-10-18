import shutil
import subprocess
import os
import zipfile
import time
import glob

## Cythonize: Add folders where files need to be cythonized in the 'rutas' list.
## Each folder should contain a setup.py file to configure the desired files for cythonization.
shutil.copytree('./', 'MontajeVidrio')

rutas = ["./MontajeVidrio/yolov5", "./MontajeVidrio/yolov5/security_classes",
         "./MontajeVidrio/yolov5/security_classes/Alarmas", "./MontajeVidrio/yolov5/security_classes/Utils",
         "./MontajeVidrio/yolov5/security_classes/parametros"]

for i in rutas:
    # Create a setup.py file in each folder and execute it to cythonize the files in that folder.
    file = open(i + "/create_setup.py", "w")
    file.write("import subprocess" + os.linesep)
    file.write("subprocess.Popen(['python', '{}/setup.py', 'build_ext', '--inplace'])".format(i))
    file.close()
    exec(open(i + "/create_setup.py").read())

time.sleep(60)

### Move the generated files after cythonization to their respective folders.
print("Moving files")

files = glob.glob('./*.pyd')
for i in files:
    # Move files to the required folders based on their names.
    # Replace 'helloworld.cp38-win_amd64.pyd' with the actual names in your case.
    # Adjust the paths accordingly for your specific use case.
    if (i.endswith('detect.cp38-win_amd64.pyd') or i.endswith('detectClass.cp38-win_amd64.pyd')):
        os.replace(i, "./MontajeVidrio/yolov5" + i)
    # Other elif conditions for different filenames and corresponding folders...

