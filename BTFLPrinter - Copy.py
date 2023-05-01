import pymsteams
import subprocess 

#Printer Magic 
BTFL_Printer = "<ip address>" #IP address of the printer

param = "-n" 
command = ["ping", param, "1", BTFL_Printer]

if subprocess.call(command) == 0: 
    printer_status = "Up!"
    message = "The printer is too BUILT TO LAST to break! Have a great day."
else: 
    printer_status = "Down!"
    message = "If the printer is down, please contact the S6! Either the IP address changed or the printer is actually down. Have an amazing BUILT TO LAST DAY!"


#Teams connector magic 
myTeamsMessage = pymsteams.connectorcard("<webhook url>")


myTeamsMessage.color("#0000FF")
myTeamsMessage.title("Printer Status: {0}".format(printer_status))
myTeamsMessage.text(message)

myTeamsMessage.send() #Inform the company on printer status! 
