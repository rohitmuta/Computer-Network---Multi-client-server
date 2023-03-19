#...Code by Rohit

# Python TCP Client 1
import socket
import time

host = socket.gethostname()
port = 8000
BUFFER_SIZE = 2000
print("Client Awake!")
print("Enter 'exit' to shutdown!!")
MESSAGE = input("Client: Enter message: ")   #get commands from client

tcpClient1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #initiate socket
tcpClient1.connect((host, port))                        #connect socket
c_hostname = socket.gethostname() + '#'                 #get client hostname
tcpClient1.send(c_hostname.encode())                    #send client hostname to server

try:
    while MESSAGE != 'exit':
        try:
            tcpClient1.settimeout(300)      # Client will run for 5 minutes
            initial_time = time.time()      # Store the time when request is sent
            tcpClient1.send(MESSAGE.encode())

            data = tcpClient1.recv(BUFFER_SIZE)
            new_data = data.decode()
            # Retrieve the socket info of the server
            delimiter = new_data.find('#')
            new_info = new_data[delimiter+1:]
            serv_family = new_data[:delimiter-1]
            serv_type = new_info[:new_info.find('#')]
            new_info = new_info[new_info.find('#')+1:]
            serv_proto = new_info[:new_info.find('#')]
            new_info = new_info[new_info.find('#') + 1:]
            serv_timeout = new_info
            if '#' in new_data:
                # Print socket info of the server
                print('Server Socket Family: '+serv_family+', Server Socket Type: '+serv_type+', Server Socket Protocol: '+serv_proto)
                print('Server Socket Timeout: '+serv_timeout)
            ending_time = time.time()  # Time when acknowledged the request
            elapsed_time = None
            # Calculate RTT
            elapsed_time = str(ending_time - initial_time)
            if '#' not in new_data:
                # Print RTT
                print('The Round Trip Time for the response is ' + elapsed_time[:7] + ' secs')
                print("Server Response: ", data.decode())
            data = None    # Clearing variable
            MESSAGE = input("Client: Enter message to continue: ")
        except :
            print('Timeout!')
            break
except KeyboardInterrupt:
    pass
    tcpClient1.close()

tcpClient1.close()
