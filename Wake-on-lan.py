# A Wake on LAN program that allows you to send magic packets over the Internet
import socket, struct

class Waker():
    def makeMagicPacket(self, macAddress):
        # Take the entered MAC address and format it to be sent via socket
        splitMac = str.split(macAddress,':')
    
        # Pack together the sections of the MAC address as binary hex
        hexMac = struct.pack('BBBBBB', int(splitMac[0], 16),
                             int(splitMac[1], 16),
                             int(splitMac[2], 16),
                             int(splitMac[3], 16),
                             int(splitMac[4], 16),
                             int(splitMac[5], 16))
    
        self.packet = (b'\xff' * 6) + (hexMac * 16) #create the magic packet from MAC address
    
    def sendPacket(self, packet, destIP, destPort = 7):
        # Create the socket connection and send the packet
        s=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.sendto(packet,(destIP,destPort))
        s.close()
        
    def wake(self, macAddress, destIP, destPort=7):
        self.makeMagicPacket(macAddress)
        self.sendPacket(self.packet, destIP, destPort)
        print ('Packet successfully sent to', macAddress)
        
if __name__ == '__main__':

    print("""                 __                          __"""+"\n"+
          """ _      ______ _/ /_____     ____  ____     / /___ _____"""+"\n"+
          """| | /| / / __ `/ //_/ _ \   / __ \/ __ \   / / __ `/ __ \ """+"\n"+
          """| |/ |/ / /_/ / ,< /  __/  / /_/ / / / /  / / /_/ / / / /"""+"\n"+
          """|__/|__/\__,_/_/|_|\___/   \____/_/ /_/  /_/\__,_/_/ /_/\n""")
    print("welcome to wake on lan")
    print("[*]github : https://github.com/HSNHK/Wake-on-LAN-py")
    print("[*]simpel mac 00:11:22:33:44:55")
    print("[*]simpel ip example.com or 192.168.1.3\n\n")
    
    #This is all the information that needs to be changed to make this work for you
    mac = input("Enter MAC addres : ")
    ip = input("Enter ip addres : ") #The IP address where the packet should be sent
    port = int(input("Enter Port : ")) #The port the packet will be sent on       
    wol = Waker()
    wol.makeMagicPacket(mac)
    wol.sendPacket(wol.packet, ip, port)
    print ('Packet successfully sent to', mac)
