# freeCodeCamp - Information Security - Courses - II - Python for Penetration Testing


## 1. Code - TCP Server & Client

### Requirements

python3 properly installed in your computer, preferably also netstat

### Instructions

  *  Open two terminal windows in the folder where the files are located
  *  In the first window, run "python3 TCP_server.py" first, if you used a host =< 1024, then it will request you root auth, for this use "sudo python3 TCP_server.py"
  *  Then in the second window, run "python3 TCP_client.py", if it requests root auth, use "sudo python3 TCP_client.py"
  *  You might be able to see the server message and client address in the terminals at this point
  *  For displaying all the active network connections on your machine, along netstat installed ('sudo apt-get install net-tools', in Ubuntu) you can use "netstat -tuln | grep ''" in the terminal.
  *  In case you would like to see the network stat of the TCP server, you could look for it using "netstat -tuln | grep '192.168.0.9'" in the terminal. This will show you the TCP server port as well.

