# simple_http_server
-----------------------
Steps to setup your own:
1. open CLI (Command Line Interface) of your machine and type cd into cloned git repository "simple_http_server"
2. type "sudo chmod +x server.py", you may have to enter your machine's login password, enter it then press enter
3. now you are ready, type "./server.py" in the CLI whenever you want to start your server
4. to stop the server, go to the running CLI and press "ctrl-c" or "^C" and the message will appear that the server has stopped
---------------------------

Note: if you are a windows user, you have to find your external ip address and then type:

http://your-external-ip-address:8080/home.html

to run the website on other machine (other than the deployed TCP server), you ca simply access the website from your machine on
which server is deployed, you can simply type:

localhost:8080/home.html

or

127.0.0.1:8080/home.html

or

192.168.2.1:8080/home.html

Note: you can modify the home.html file and add more files in the same directory
