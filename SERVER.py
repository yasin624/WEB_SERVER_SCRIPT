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
        self.pakcket_size=2*1024


    def starts_server(self,max_client=1):
        self.server.bind((self.Ip, self.PORT))
        self.server.listen(max_client)
        print("My IP Adrr : ",self.Ip)

    def listen(self, max_client):
        self.server.listen(max_client)
    def REKLAM(self,img):
        #################################### fps
        cv2.putText(img, "Tum haklari saklidir © 2020 | yalcinyazilimciik", (img.shape[1]-700,                                                            img.shape[0]-13), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (100, 255, 0),1)
        return img
    def client_accept(self):
        client, addr = self.server.accept()
        client.send(bytes(" HOSŞGELDİN SERVERE ", "utf8"))
        print(" \n connect to : ", addr)
        return client

    def decode_arr(self,image_bytes):
        # Verinin uzunluğunu kontrol et
        a = image_bytes.find(b"\xff\xd8")
        b = image_bytes.find(b"\xff\xd9")
        if a != -1 and b != -1:
            jpg = image_bytes[a:b+2]
            image_bytes = image_bytes[b+2:]

            # Görüntüyü decode et
            image = cv2.imdecode(np.frombuffer(jpg, dtype=np.uint8), cv2.IMREAD_COLOR)
        else:
            return False,image_bytes
        return image,image_bytes

    def take_msg (self,client):
        basla=True
        while basla:
            # Görüntüyü al
            image_bytes = b""
            while True:
                # Biraz veri al
                chunk = client.recv(self.pakcket_size)
                if not chunk:
                    break
                image_bytes += chunk

                img,image_bytes=self.decode_arr(image_bytes)
                if type(img)!=type(False):
                    new_time=time.time()
                    img=self.FPS(new_time,img)
                    # Görüntüyü göster
                    cv2.imshow("Frame", img)
                    if cv2.waitKey(1) & 0xFF == ord("q"):
                        basla=False
                        break
            cv2.destroyAllWindows()
            return False
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

    def send_arr(self,client,reklam=True):
        camera = cv2.VideoCapture(0)

        fps = camera.get(cv2.CAP_PROP_FPS)
        width = camera.get(cv2.CAP_PROP_FRAME_WIDTH)
        height = camera.get(cv2.CAP_PROP_FRAME_HEIGHT)
        print(f"\n webcam max  fps :  {int(fps)}  ( {int(width)} X {int(height)} ) ")
        star=True
        while star:
            # Görüntüyü al
            ret, frame = camera.read()
            #frame=cv2.resize(frame,(1280,720))
            if reklam:
                frame=self.REKLAM(frame)
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


def send_video():
    while True:
        print(server_logo)
        server=SERVER()
        server.starts_server()
        client=server.client_accept()
        inside=server.send_arr(client)
        if not inside:
            client.close()


def take_video():
    while True:
        print(server_logo)
        server=SERVER()
        server.starts_server()
        client=server.client_accept()
        inside=server.take_msg(client)
        if not inside:
            client.close()

if __name__=="__main__":
    take_video()
