import json
import sys
import subprocess
import os,os.path




LOGS_DIRECTORY_PATH:str = "./logs"
SERVER_PATH:str = "./src/server.py"
CLIENT_1_PATH:str = "./Clients/main.py"
CLIENT_2_PATH:str = "./Clients/main.py"

SERVER_MAX_RUN_COUNT:int = 10

checked_logs:list = []


def panic(error_message:str) -> None:
    print("Panic!: ",error_message);
    sys.exit(1)


def get_options_input(input_message:str,options:list) -> str:
    if len(options)==0:
        panic("The length of the options list cannot be empty!")

    text:str = ""
    while True:
        text = input(input_message + " " + str(options)+" : ")
        if text in options:
            return text


def clean() -> int:

    if not os.path.exists(LOGS_DIRECTORY_PATH):
        return 0

    if get_options_input("Am I allowed to delete the log folder at \""+LOGS_DIRECTORY_PATH+"\"",
                         ["y","n"])=="n":
        panic("User did not give me the permission to delete a folder")

    return subprocess.call("rm -rf "+LOGS_DIRECTORY_PATH , shell=True)


def run_server():
    return subprocess.call("python3 "+SERVER_PATH+" -p1 "+CLIENT_1_PATH+" -p2 "+
                           CLIENT_2_PATH , shell=True)
def run_server_loop():
    0

def report():
    target = "./logs/1662572839165/game.json"



def main() -> None:
    # clean()
    # run_server()
    report()


if __name__=="__main__":
    main()
