
# java -jar ./app/build/libs/app-standalone.jar /home/vbatista/estudo/ontologias/datamodel/owl/datamodel-functional.ofn /home/vbatista/estudo/ontologias/datamodel/owl/datamodel-owl.owl

import subprocess

converter = "libs/app-standalone.jar"
origin = "/home/vbatista/estudo/ontologias/datamodel/owl/datamodel-functional.ofn"
dest = "/home/vbatista/estudo/ontologias/datamodel/owl/datamodel-owl.owl"

command = "java -jar {converter} {origin} {dest}".format(converter=converter, origin=origin, dest=dest)

def run_command(command):
    p = subprocess.Popen(command, shell=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT)
    return p.communicate()

run_command(command)


