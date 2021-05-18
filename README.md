#### Quick instructions: just give executable permissions to it and type ./server.py in your CLI --have-fun
---------------------
# simple_http_server
-----------------------

## Note: this program uses 8080 as default port for listening on HTTP
## You can change this by using `python server.py <your-specified-port-number>`
### Example: `python server.py 7000` (you've to pass it as a CLI argument)

Steps to setup your own:
1. open CLI (Command Line Interface) of your machine and type cd into cloned git repository "simple_http_server"
2. type "sudo chmod +x server.py", you may have to enter your machine's login password, enter it then press enter
3. now you are ready, type "./server.py" in the CLI whenever you want to start your server
4. to stop the server, go to the running CLI and press "ctrl-c" or "^C" and the message will appear that the server has stopped
---------------------------

to run the website on other machine (other than the deployed TCP server), you ca simply access the website from your machine on
which server is deployed, you can simply type:
the port 8080 will only work if you didn't changed it, if it was changed, you have to enter that port instead of 8080

localhost:8080/

or

127.0.0.1:8080/

Note: you can modify the index.html file and add more files in the same directory
