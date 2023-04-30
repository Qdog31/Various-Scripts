import pymsteams
import subprocess 
import asyncio


BTFL_Printer = "<ip address>" #IP address of the printer

#Ping the printer to see if it is up or down
param = "-n" 
command = ["ping", param, "1", BTFL_Printer]

if subprocess.call(command) == 0: 
    printer_status = "Up!"
else: 
    printer_status = "Down!"

#Teams connector magic 
myTeamsMessage = pymsteams.connectorcard("<webhook url>")


myTeamsMessage.color("#0000FF")
myTeamsMessage.title("Printer Status: {0}".format(printer_status))
myTeamsMessage.text("If the printer is down, please contact the S6! Either the IP address changed or the printer is actually down. Have an amazing BUILT TO LAST DAY!")

myTeamsMessage.send() #Inform the company on printer status! 
