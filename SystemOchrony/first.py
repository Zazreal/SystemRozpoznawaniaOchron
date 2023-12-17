
from imageai.Classification.Custom import CustomImageClassification
import os
from PIL import Image,ImageFilter  
import cv2
from PIL import ImageEnhance
import win
import PySimpleGUI as sg
import time
#import sound

#wczytanie obrazka 



print("cv2 version: " + cv2.__version__ )

execution_path = os.getcwd() #ustawienie sciezki uruchamiania
prediction = CustomImageClassification()  #wybranie funkcjonalno�ci (w�asna klasyfikacja obrazu)
prediction.setModelTypeAsDenseNet121()    #wybranie typu sieci neuronowej (DenseNet121)
prediction.setModelPath(os.path.join(execution_path, "SHOES\models\model-best-0.99.h5")) #nauczony model sieci 
prediction.setJsonPath(os.path.join(execution_path, "SHOES\json\model_class.json"))      #json z obiektami do rozpoznania
prediction.loadModel(num_objects=2)       #ilosc obiektow do rozpoznania
  
# define a video capture object
vid = cv2.VideoCapture(0)
i = 0
n=1
cover=0
j=0

while(True):
      
    # Capture the video frame
    # by frame
    event, values = win.wnd.read(timeout=5)
    #win.stop.read(timeout=5)
    check, frame = vid.read()
    # save frame as jpg
    #cv2.imshow("frame", frame)
    cv2.imwrite("frame.jpg", frame)
    im = Image.open("frame.jpg")


    #zwiekszenie jasnosci
    #enh = ImageEnhance.Brightness(im)  
    #im2=enh.enhance(1.1)
    ##zwiekszenie kontrastu
    #enh2=ImageEnhance.Contrast(im2)
    #enhaced=enh2.enhance(1.05)
    #enhaced = im
    #enhaced.save("new.jpg")
    #enhaced = enhaced.resize((int(enhaced.size[0]/(enhaced.size[0]/320)),int(enhaced.size[1]/(enhaced.size[1]/240))), resample=Image.BICUBIC)
    #enhaced.save("new.png")
    im = im.resize((int(im.size[0]/(im.size[0]/320)),int(im.size[1]/(im.size[1]/240))), resample=Image.BICUBIC)
    .save("new.png")

    if cover>99:
        j=j+1
        if j>9:
            #win.stop["go-stop"].update(filename=os.path.join(execution_path, "go.png"))
            win.wnd["img2"].update(filename=os.path.join(execution_path, "go.png"))
    else:
        j=0
        #win.stop["go-stop"].update(filename=os.path.join(execution_path, "stop.png"))
        win.wnd["img2"].update(filename=os.path.join(execution_path, "stop.png"))

    if j>10:
        #sound.comunicate(0)
        #sound.comunicate(1)
        j=0
        time.sleep(10)
    

    predictions, probabilities = prediction.classifyImage(os.path.join(execution_path, "new.jpg"), result_count=2 )
    key="keyprediction";
    for eachPrediction, eachProbability in zip(predictions, probabilities):
        #win.wnd[key].update(eachPrediction+" :: "+str("{:0>6}".format("{:.2f}".format(round(eachProbability,2)))))
        if eachPrediction=="cover":
            cover= eachProbability      
        key="keyprediction1"
    win.wnd["img"].update(filename=os.path.join(execution_path, "new.png"))


    if event == sg.WINDOW_CLOSED or event=="EXIT":
        break
 

win.wnd.close()

# After the loop release the cap object
vid.release()
# Destroy all the windows
cv2.destroyAllWindows()

