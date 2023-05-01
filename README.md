# Intro to my various scripts 

Within this repo I plan on posting random scripts that I have created to complete various tasks. This is mainly for fun and to learn cool stuff! 

## BTFL Printer 

This script connects the power of `ping` with the power of an `Incoming Webhook' connector for Microsoft Teams.

The script is pretty straight forward and short! First, you will need to ensure that you have pymsteams with `pip install pymsteams` and subprocess. Then, all the script needs is two peices of information: 1) Your printers IP address and 2) your webhook URL that you can get from teams after configuring the webhook. 

The first half of the script just sends a single ping request to the designated IP using the ping -n parameter. Then, if the printer is up then the return value of this command should be 0. If that is the case, then the message variable is changed to reflect the printer status (either up or down). 

The magic is in the `Incoming Webhook` connector that you set up through teams! Using `pymsteams` you are able to customize the message, title, color, etc. Puting everything together, we get a `Microsoft Teams Printer Status Connector`. 

To make it even better I tried to use `Windows Task Scheduler` to run this script on a defined schedule, but was unable to get this to work. I will be looking into alternate methods in the future. 

pymsteams documentation: https://pypi.org/project/pymsteams/

## Future project Name 

Future project stuff here.....
