!!READ ME!!

!!By Rohit!!

Requirements: Python 3.6 or above
TCP Multithreaded Server and client with HTTP using sockets in Python


Instructions to run the Server:
(If Running in Pycharm, Run in Terminal)
1. Open Terminal(CMD)(from the path where thefiles reside) and enter command:
	~python server.py
	This will start the Server and will be running for 5 minutes until timeout.
	Server will be listening to multiple requests from multiple clients limited to 5 threads.
	Server can send message to clients if the clients initiate a conversation.

Instructions to run the Client-01:
Client and Server can also communicate with each other like a chatting app.
(Ex: Client: Enter message: hello
	Server Response:  hey)
(If Running in Pycharm, Run in Terminal)
1. Open Terminal(CMD)(from the path where the files reside) and enter command:
	~python client.py
2. Enter following commands to request from the server:
	Type 'help' to get the commands   (Ex: Client: Enter message: help)
		~This will list out the commands to the client fromthe server

	Type 'info' to get Server info    (Ex: Client: Enter message: info)
		~This will list the Server Socket information (Like Socket Family, Type, Protocal,etc.)

	Type 'google' to access Google    (Ex: Client: Enter message: google)
		~This will open www.google.com in the default browser

	Type 'send filename' with filename to request a file  (Ex: Client: Enter message: send file1.txt)
		~This will send the file from server and display over the client window

	Type 'send index.html' to access local webpage  (Ex: Client: Enter message: send index.html)
		~This will provide access to the index.html webpage to the client from server

	Type 'exit' to shutdown
		~This will close the Client

Instructions to run Client-02:
	Similar to the instructions for client-01.
	You can run mutiple instance of client.py program as multiple clients

