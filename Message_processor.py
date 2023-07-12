from abc import ABC, abstractmethod
import re
class Message_app(ABC):
    @abstractmethod
    def SendMessage(self):
        pass
class Sms_services(Message_app):
    def SendMessage(self,message,number):
        print(f"Message was sent to {number} successfully")
class Email_services(Message_app):
    def SendMessage(self, message, email):
        print(f"Message was sent to {email} successfully")
class Whatsapp_services(Message_app):
    def SendMessage(self, message, number):
        print(f"Message was sent to {number} successfully")

class Validate:
    def IsvalidNumber(self,num):
        Pattern=re.compile("^[6-9]\d{9}$")
        return Pattern.match(num)
    def IsvalidEMmail(self,email):
        Pattern = r'[^@]+@[^@]+\.[a-z]+'
        return re.match(Pattern, email)


service1 = Sms_services()
service2 = Email_services()
service3 = Whatsapp_services()
validate = Validate()

flag = "yes"
while (flag == "yes"):
    print("Enter 1 to Send SMS \nEnter 2 to Send Email \nEnter 3 to Send WhatsApp \nEnter 4 to quit")
    x=int(input("ENTER:"))

    if x==1:
        number=input("Enter number:")
        if validate.IsvalidNumber(number):
            message=input("Enter Message to send :")
            service1.SendMessage(message, number)
        else:
            print("Invalid Number")
    if x==2:
        email=input("Enter Email ID:")
        if validate.IsvalidEMmail(email):
            message=input("Enter the Message (Not more than 300 words) :")
            service2.SendMessage(message, email)
        else:
            print("Incorrect mail Id")
    if x==3:
        number = input("Enter number:")
        if validate.IsvalidNumber(number):
            message = input("Enter Message to send :")
            service3.SendMessage(message, number)
        else:
            print("Invalid Number")

    if x == 4:
        print("Thank You!")


    flag = input("do you want to continue? yes / no: ")