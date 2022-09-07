import json
import os
import os.path
import subprocess
import sys

LOGS_DIRECTORY_PATH:str = "./logs"
SERVER_PATH:str = "./src/server.py"
CLIENT_1_PATH:str = "./Clients/main.py"
CLIENT_2_PATH:str = "./Clients/main.py"

SERVER_MAX_RUN_COUNT:int = 10

server_run_counter:int = 0;
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


def run_server() -> int:
    return subprocess.call("python3 "+SERVER_PATH+" -p1 "+CLIENT_1_PATH+" -p2 "+
                           CLIENT_2_PATH , shell=True)

def get_latest_log_path() -> tuple[str,str]:
    log_list = os.listdir(LOGS_DIRECTORY_PATH)

    for i in log_list:
        if i not in checked_logs:
            checked_logs.append(i)
            checked_logs.append(str(server_run_counter))
            return i, LOGS_DIRECTORY_PATH + "/" + i + "/game.json"

    panic("Could not find any new logs!")

def rename_log(log_path:str) -> None:
    global server_run_counter

    command:str = "mv "+LOGS_DIRECTORY_PATH+"/"+log_path+" "+LOGS_DIRECTORY_PATH+"/"+str(server_run_counter)
    subprocess.call(command,shell=True)
    server_run_counter+=1


def run_server_loop() -> None:
    for i in range(0,SERVER_MAX_RUN_COUNT):
        run_server()
        log_path = get_latest_log_path()
        print("server run count : "+str(i)+" , ",get_brief_report(log_path[1]))
        rename_log(log_path[0])


def get_brief_report(target:str) -> tuple[str,str]:

    if not os.path.exists(target): panic("Target at \""+target+"\" does not exist!")

    target_dict = json.loads(open(target).read())
    winner:str = "undefined";win_reason:str = "undefined"
    target_dict_igd = target_dict["initial_game_data"]

    for i in target_dict_igd:
        if i == "winner": winner = target_dict_igd[i]
        elif i == "win_reason": win_reason = target_dict_igd[i]

    return winner,win_reason


def main() -> None:
    clean()
    run_server_loop()


if __name__=="__main__":
    main()
