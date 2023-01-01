from socket import *
import time
from tqdm import tqdm
started_time = time.time()
if __name__ == '__main__':
    host_name = input('Enter IP address : ')
    t_IP = gethostbyname(host_name)
    range1 = input("Enter first range : ")
    range2 = input("Enter Second Range : ")
    print('Scanning on host : ' , t_IP)
    for i in tqdm(range(int(range1) , int(range2))):
        server = socket(AF_INET , SOCK_STREAM)
        connection = server.connect_ex((t_IP , i))
        if(connection == 0):
            print('port %d: OPEN' % (i ,))
            server.close()
    print('time token : ' , time.time() - started_time)