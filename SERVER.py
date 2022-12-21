import time

import cv2
import socket
import numpy as np

server_logo = """

                                                                                                    
                                                                                                    
                                                                                                    
             ||||||                    |||||||||||||||||||||                                        
            |||||||                   ||||||||||||||||||||||||                                      
            ||||||||                 |||||||||||||||||||||||||                                      
            |||  |||                 |||                   ||||                                     
            |||  |||                 |||                    |||                                     
            ||||||||                 |||                    |||                                     
            |||||||                  |||                    |||                                     
             |||||                   ||                     |||                                     
              ||||                   |||  |||||||||||||||   |||                                     
              ||||     |||||||||||||||||  |||||||||||||||   ||||||||||||||||                        
              |||||   |||||||||||||||||    |||||||||||||    |||||||||||||||||                       
              |||||   ||||||||||||||||||                    ||||||||||||||||||                      
              |||||  ||||            ||                     |||            |||                      
           || |||||  |||             ||                     |||            |||                      
          |||||||||  |||             ||                     |||            |||                      
          |  ||||||  |||             ||   |||||||||||||||   |||            |||                      
          || ||||||| |||  |||||||||  ||   |||||||||||||||   ||| |||||||||  |||                      
          |||| ||||| |||  |||||||||  |||   |||||||||||||    ||| |||||||||  |||                      
            ||  |||| |||             |||                    |||            |||                      
            ||  ||||||||             |||                    |||            |||                      
            ||  ||||| ||             |||                    |||            |||                      
             ||  |||| ||  |||||||||  |||   |||||||||||||    ||| |||||||||  |||                      
             ||  ||||| |  |||||||||  |||  |||||||||||||||   ||| |||||||||  |||                      
             ||  ||||| |             |||  |||||||||||||||   |||            |||                      
              ||  |||||              |||   |||||||||||||    |||            |||                      
              ||  |||||              |||                    |||            |||||                    
               ||  |||||  |||||||||  |||                    ||| |||||||||  |||||                    
               ||  |||||  |||||||||  |||                    ||| |||||||||  ||||||                   
                ||  |||||            |||    |||||||||||     |||            ||||||                   
                ||  ||||||           |||  |||||||||||||||   |||            |||||||                  
                 ||  |||||           |||  |||||||||||||||   |||            |||||||                  
                 |||  |||||          |||   |||||||||||||    ||| |||||||||  ||||||||                 
                  ||  ||||||         |||                    ||| |||||||||  ||||||||                 
                  |||  |||||         |||                    |||            ||| ||||                 
                   |||  |||||        |||                    |||            ||| ||||                 
                    ||  ||||||       |||                    |||            ||| |||||                
                    |||  ||||||      |||  |||||||||||||||   ||| |||||||||  ||| |||||                
                     |||  ||||||     |||  |||||||||||||||   ||| |||||||||  ||| |||||                
                      |||  ||||||    |||   |||||||||||||    |||            ||| |||||                
                       |||  ||||||   ||                     |||            ||| |||||                
                       ||||  ||||||  ||                     |||            ||| |||||                
                        ||||  |||||| |||                    |||            ||| ||||                 
                         ||||  |||||||                      |||            ||| ||||                 
                          ||||  |||||||                     |||            ||||||||                 
                           ||||  |||||||                    |||            || |||||                 
                            ||||  ||||||||                  |||            | |||||                  
                              |||   ||||||||                |||              |||||                  
                               ||||  |||||||||              |||             |||||                   
                                ||||  |||||||||             |||            |||||                    
                                 |||||  ||||||||||          |||          |||||||                    
                                   ||||   |||||||||||       |||         |||||||                     
                                    |||||   ||||||||||||     |       ||||||||| |                    
                                      |||||  |||||||||||||||||||||||||||||||| |                     
                                        ||||||  ||||||||||||||||||||||||||||||                      
                                          ||||||   ||||||||||||||||||||||| ||                       
                                            |||||||  |||||||||||||||||||||||                        
                                              |||||||||    ||||||||  ||||||                         
                                                 ||||||||||||||||||||||||                           
                                                    |||||||||||||||||||                             
                                                         |||||||||                                  
                                                                                                    
                                                                                                    
                                                                                                    
                                                                                                    
                                                                                                    
                                               ||                                                   
                                            ||####|                                                 
                                           |#######                                                 
                                           |##|||||                                                 
                                           |##|        |||||   |||||||||   ||||  |||||   ||||||     
      |###||######  |#    |####| ######|   |###|      |#####|  ##|##||##|  |##| |#####|  ##|##|     
     |##||#|||##||  |#|   |#||##|||##||    |#####||  |##||###  #####||##|  ##| |##||##|  #####|     
     |#       #|    ###   |#  |#|  ##       ||#####| ##|  |##| ###|  |##| |##| ##|  |##| ###|       
     |##||    #|   |# #|  |#|||#|  ##         ||###||########| ###    |##||##| ########| ###        
      |####|  #|   ## ##  |####|   ##           |##||########| ###    |##||#|  ########| ###        
          #|  #|  |#####| |# ##    ##           |##||##|       ###     |#|##|  ##|       ###        
     |#| |#|  #|  |#####| |# |#|   ##      |#|||###| |##|||||  ###     |####   |##|||||  ###        
     |#####   #|  ##   ## |#  |#|  ##      |######|  |######|  ###     |###|   |######|  ###        
                                           ||###||    ||###||  |#|      |#||    ||###||  |#|        
                                                                                                    
                                                                                                    
                                                                                              

"""






class SERVER():
    def __init__(self):
        self.HOST = socket.gethostname() # Standard loopback interface address (localhost)
        self.Ip = socket.gethostbyname(self.HOST)
        self.PORT = 9999     # Port to listen on (non-privileged ports are > 1023)
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        self.deneme_img = r"D:\program files\GITHUB\GIF_EDITOR\img_and_gift\DRAGON.jpg"

        self.prev_frame_time=0


    def starts_server(self,max_client=1):
        self.server.bind((self.Ip, self.PORT))
        self.server.listen(max_client)
        print("My IP Adrr : ",self.Ip)

    def listen(self, max_client):
        self.server.listen(max_client)

    def client_accept(self):
        client, addr = self.server.accept()
        client.send(bytes(" HOSŞGELDİN SERVERE ", "utf8"))
        print(" connect to : ", addr)
        return client
    def msg_decode_arr(self,client): # print(" connect to : ",addr)
        pass
    def shows(self,frame):
        try:
            cv2.imshow("RECEIVING VIDEO",frame)
        except:
            pass
    def FPS(self,time,img):
        #################################### fps
        fps = 1/(time-self.prev_frame_time)
        self.prev_frame_time=time
        cv2.putText(img, "FPS : "+str(int(fps)), (20,20), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (100, 255, 0),1)
        return img

    def send_arr(self,client):
        camera = cv2.VideoCapture(0)
        fps = camera.get(cv2.CAP_PROP_FPS)
        width = camera.get(cv2.CAP_PROP_FRAME_WIDTH)
        height = camera.get(cv2.CAP_PROP_FRAME_HEIGHT)
        print(f" {int(fps)} :  {int(width)} X {int(height)}")
        star=True
        while star:
            # Görüntüyü al
            ret, frame = camera.read()
            #frame=cv2.resize(frame,(1280,720))

            # Görüntüyü JPEG formatta sıkıştır
            ret, jpeg = cv2.imencode(".jpg", frame)

            # Görüntüyü sockete gönder
            try:
                client.sendall(jpeg.tobytes())
                time.sleep(0.01)
            except:
                star=False

        # Kamerayı ve socketi kapat
        camera.release()
        return False


if __name__=="__main__":
    while True:
        print(server_logo)
        server=SERVER()
        server.starts_server()
        client=server.client_accept()
        inside=server.send_arr(client)
        if not inside:
            client.close()
