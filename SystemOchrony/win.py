
from weakref import finalize
import PySimpleGUI as sg

title="System sprawdzania ochrony obuwia (2S2O)"
fsize=10
font_text=("Fixedsys", 20)
font_title=("Fixedsys", 30)
font_btn=("Fixedsys", 17)


#sg.theme("DarkAmber")
base=[
    #[sg.Text("pred1 :: 000.0",key="keyprediction",font = font_text,pad=(40,5))],
    #[sg.Text("pred2 :: 000.0",key="keyprediction1",font = font_text,pad=(40,5))],
    [sg.Column( [[sg.Button("EXIT",font = font_btn,pad=(5,5))]],justification="center")]
]

film1=[
    [sg.Text("Status:",font = font_text,pad=(15,15))],
    [sg.Image(key="img2",size=(300,220))]
]

film=[
    [sg.Text("Camera Video:",font = font_text,pad=(15,15))],
    [sg.Image(key="img",size=(320,240))]
]


layout = [ 
    [sg.Column([[sg.Text("Shoe/cover prediction",font = font_title,pad=(20,20))]],justification="center")],
    [ 
        #sg.Column(base,justification="center"),
        sg.Column(film1,justification="center"),
        sg.VSeperator(),
        sg.Column(film,justification="center"),
        sg.VSeperator(),
        sg.Column(base,justification="center"),
    ] 
]

#layout2=[ [sg.Column([[sg.Image(key="go-stop")]], justification="center")]]
wnd=sg.Window(title, layout)
#stop=sg.Window(title="Pass", layout=layout2,margins=(0,0))



