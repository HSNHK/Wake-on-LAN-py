# A Wake on LAN program that allows you to send magic packets over the Internet
import socket, struct
from datetime import datetime
class Waker():
    def makeMagicPacket(self, macAddress):
        # Take the entered MAC address and format it to be sent via socket
        splitMac = str.split(macAddress,':')
    
        # Pack together the sections of the MAC address as binary hex
        hexMac = struct.pack("BBBBBB", int(splitMac[0], 16),
                             int(splitMac[1], 16),
                             int(splitMac[2], 16),
                             int(splitMac[3], 16),
                             int(splitMac[4], 16),
                             int(splitMac[5], 16))
    
        self.packet = b'\xff' * 6 + hexMac * 16 #create the magic packet from MAC address
    
    def sendPacket(self, packet, destIP, destPort = 9):
        # Create the socket connection and send the packet
        s=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.sendto(packet,(destIP,destPort))
        s.close()
        
    def wake(self, macAddress, destIP, destPort=9):
        self.makeMagicPacket(macAddress)
        self.sendPacket(self.packet, destIP, destPort)
        print ("Packet successfully sent to", macAddress)
        
if __name__ == "__main__":

    print("""                 __                          __"""+"\n"+
          """ _      ______ _/ /_____     ____  ____     / /___ _____"""+"\n"+
          """| | /| / / __ `/ //_/ _ \   / __ \/ __ \   / / __ `/ __ \ """+"\n"+
          """| |/ |/ / /_/ / ,< /  __/  / /_/ / / / /  / / /_/ / / / /"""+"\n"+
          """|__/|__/\__,_/_/|_|\___/   \____/_/ /_/  /_/\__,_/_/ /_/\n\n""")
    print("welcome to wake on lan\n")
    print("[*]github : https://github.com/HSNHK/Wake-on-LAN-py")
    print("[*]simple mac 00:11:22:33:44:55")
    print("[*]simple ip example.com or 192.168.1.3")
    print("[*]simple port 7 or default 9\n\n")
    
    try:
        #This is all the information that needs to be changed to make this work for you
        mac = input("Enter MAC addres : ")
        ip = input("Enter ip addres : ") #The IP address where the packet should be sent
        port = int(input("Enter Port : ")) #The port the packet will be sent on
    except:
        print("You must fill in the entries")
        
    if mac!="" and ip!="" and port>0:
        wol = Waker()
        wol.makeMagicPacket(mac)
        
        print("_________________________________\n\n"+
              "create the magic packet from MAC address : \n"+
              str(wol.packet)+
              "\n_________________________________\n")
        
        wol.sendPacket(wol.packet, ip, port)
        print (f"[%s] Packet successfully sent to [%s]"% (datetime.now(),mac))
    else:
        print("The information was not entered correctly !!!")
