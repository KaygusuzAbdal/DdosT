# DdosT

Written for the SYN-Flood attack which is type of denial of service. It sends SYN request packets to host and condenses the server's traffic


## Usage:

1. First of all, you must install the requirements with using the command below.
```
pip3 install -r requirements.txt
```

2. Then you can start the program with calling the `DdosT.py` file.
```
python3 DdosT.py
```

3. After the program is opened, you need to enter which Denial of Service attack type you want to choose. You can also use `types` command when you change attack type. (If you want to get more information about commands, use `help` command.)

4. Then, you can check the attack parameters with using `options` command. If you want to change one of them just use `set {option} {new_value}` command.

5. Finally, use the `execute` command to start attack!


### Parameters:
- **RHOST :** Target IP Address
- **RPORT :** Target Port Number
- **COUNT :** Number of Packets
- **SIZE :** Size of Packets (OPTIONAL)(sizes of SYN packets are approximately 62 bytes)


It's written for educational purposes only. If you interested with Cyber Security, you can check and use the codes to learn how to do DDoS attack with python.

## Video:

[![tool usage video](https://img.youtube.com/vi/qJ4Cem45P4M/0.jpg)](https://www.youtube.com/watch?v=qJ4Cem45P4M)
