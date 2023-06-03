
import pywhatkit
import pyautogui
import time
from twilio.rest import Client
from pynput.keyboard import Key, Controller

from compllments.config import TWILIO_CONFIG


class Texter:
    def __init__(self, message_type: str) -> None:
        self.message_type = message_type

        if self.message_type == "sms":
            self.TwilioTexter = Client(TWILIO_CONFIG["account_sid"], TWILIO_CONFIG["auth_token"])

        elif self.message_type == "whatsapp":
            self.keyboard = Controller()

        
    def send(self, number, message,):

        if self.message_type == "whatsapp":

            pywhatkit.sendwhatmsg_instantly(
                phone_no=number, 
                message=message,
            )

            time.sleep(2)
            pyautogui.click()
            time.sleep(2)
            self.keyboard.press(Key.enter)
            self.keyboard.release(Key.enter)
            
        elif self.message_type == "sms":

            assert TWILIO_CONFIG["from_"] != number, "Please change the recipient. Twilio does not let you tet yourself."

            message = self.TwilioTexter.messages.create(
                        body= message,
                        from_ = TWILIO_CONFIG["from_"],
                        to= number,
                    )





