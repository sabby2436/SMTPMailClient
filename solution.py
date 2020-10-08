from socket import *


def smtp_client(port=1025, mailserver='127.0.0.1'):
    msg = "\r\n My message"
    endmsg = "\r\n.\r\n"

    # Choose a mail server (e.g. Google mail server) if you want to verify the script beyond GradeScope

    # Create socket called clientSocket and establish a TCP connection with mailserver and port

    # Fill in start
    clientSocket = socket(AF_INET,SOCK_STREAM)
    clientSocket.connect((mailserver, SMTP_PORT))
    # Fill in end

    recv = clientSocket.recv(1024).decode()
    #print(recv)
    if recv[:3] != '220':
        print('220 reply not received from server.')

    # Send HELO command and print server response.
    heloCommand = 'HELO Alice\r\n'
    clientSocket.send(heloCommand.encode())
    recv1 = clientSocket.recv(1024).decode()
    #print(recv1)
    if recv1[:3] != '250':
        print('250 reply not received from server.')

    # Send MAIL FROM command and print server response.
    # Fill in start
    mailCommand = 'MAIL FROM: chintan.t94@gmail.com\r\n'
    clientSocket.send(mailCommand.encode())
    recv1 = clientSocket.recv(1024).decode()
    #print('MAIL FROM: ', recv1)
    if recv1[:3] != '250':
        #print('250 reply not received')
    # Fill in end

    # Send RCPT TO command and print server response.
    # Fill in start
    receiveCommand = 'RCPT TO: cdt303@nyu.edu\r\n'
    clientSocket.send(receiveCommand.encode())
    recv1 = clientSocket.recv(1024).decode()
    #print('RCPT TO: ', recv1)
    if recv1[:3] != '250':
        #print('250 reply not received')
    # Fill in end

    # Send DATA command and print server response.
    # Fill in start
    dataCommand = 'DATA\r\n'
    clientSocket.send(dataCommand.encode())
    recv1 = clientSocket.recv(1024).decode()
    print('DATA: ',recv1)
    if recv1[:3] != '250':
        print('250 reply not received')
    # Fill in end

    # Send message data.
    # Fill in start
    dataCommand = 'SUBJECT: SMPT Lab Test Email\r\n'+msg+endmsg
    clientSocket.send(dataCommand.encode())
    recv1 = clientSocket.recv(1024).decode()
    #print('Message data: ',recv1)
    if recv1[:3] != '250':
        #print('250 reply not received')
    # Fill in end

    # Message ends with a single period.
    # Fill in start
    dataCommand = 'SUBJECT: SMPT Lab Test Email\r\n'+endmsg
    clientSocket.send(dataCommand.encode())
    recv1 = clientSocket.recv(1024).decode()
    #print('Message data: ',recv1)
    if recv1[:3] != '250':
        #print('250 reply not received')
    # Fill in end

    # Send QUIT command and get server response.
    # Fill in start
    quitCmd = "QUIT\r\n"
    clientSocket.send(quitCmd.encode())
    recv1 = clientSocket.recv(1024).decode()
    #print('QUIT: ',recv1)
    if recv1[:3] != '221':
        #print('221 reply not received')
    # Fill in end


if __name__ == '__main__':
    smtp_client(1025, '127.0.0.1')