#!/bin/python3
##################################################
# rsync-linux-home.py                            #
# @frab1t                                        #
# https://github.com/frab1t/rsync-linux-home.py  #
##################################################
import subprocess
import getpass

DRIVE_UUID="df577c96-3d53-473b-b216-07ced6685eaa" # set your drive UUID

USER=getpass.getuser()
SRC_DIR="/home/{}/".format(USER)
DEST_DIR="/run/media/{user}/{drive_uuid}/rsync-linux-home/".format(user=USER,drive_uuid=DRIVE_UUID)
LOG_FILENAME = 'rsync.log'

# rsync options
OPTIONS = [
    "-avruhz",
    "--delete",
    "--stats",
    "--log-file={LOG_FILENAME}".format(LOG_FILENAME=LOG_FILENAME)
] 

# directories includes (pattern rsync include/exclude)
INCLUDES = [
    "Progetti/***",
    "Scrivania/***",
    "Documenti/***",
    "Immagini/***",
    "Musica/***",
    "Video/***"
]

# directories excludes (pattern rsync include/exclude)
EXCLUDES = [
    "*"
]


def generate_includes(inc):
    includes=[]
    for i in inc:
        includes.append("--include={}".format(i))
    
    return includes


def generate_excludes(ex):
    excludes=[]
    for e in ex:
        excludes.append("--exclude={}".format(e))
    
    return excludes


def generate_statement(options, includes, excludes, source, destination):
    includes_generated = generate_includes(includes)
    excludes_generated = generate_excludes(excludes)

    cmd=['rsync'] #,'--dry-run']

    for o in options:
        cmd.append(o)
    
    for i in includes_generated:
        cmd.append(i)

    for e in excludes_generated:
        cmd.append(e)
    
    cmd.append(source)
    cmd.append(destination)

    return cmd


def execute_backup(cmd):   
    summary_backup() 
    try:
        print("> Backup Started")
        process = subprocess.run(cmd, check=True, capture_output=True)
        
        print(process.stdout.decode('UTF-8'))
        
        print("> Backup Terminated")
    except subprocess.SubprocessError as sperror:
        print("> Backup Aborted")
        print('Error rsync')
        print("Exit code: {}".format(sperror.args[0]))
    except Exception as exception:
        print("> Backup Aborted")
        print('Error')
        print(exception)



def summary_backup():
    print("""rsync-linux-home
from: {source}
to: {destination}

log file: {log_file}

rsync options: {opt}""".format(source=SRC_DIR, destination=DEST_DIR, opt=OPTIONS, log_file=LOG_FILENAME))


cmd = generate_statement(OPTIONS, INCLUDES, EXCLUDES, SRC_DIR, DEST_DIR)
execute_backup(cmd)
