
import pywhatkit
import pyautogui
import time
from twilio.rest import Client
from pynput.keyboard import Key, Controller

from compllments.config import TWILIO_CONFIG


class Texter:
    def __init__(self, message_type: str, content_type: str) -> None:
        self.message_type = message_type
        self.content_type = content_type

        if self.message_type == "sms":
            self.TwilioTexter = Client(TWILIO_CONFIG["account_sid"], TWILIO_CONFIG["auth_token"])

        elif self.message_type == "whatsapp":
            self.keyboard = Controller()

        
    def send(self, number, text_message: str, media_message: str=None, ):

        if self.content_type == "text":
            if self.message_type == "sms":

                assert TWILIO_CONFIG["from_"] != number, "Please change the recipient. Twilio does not let you tet yourself."                
                self.TwilioTexter.messages.create(
                            body= text_message,
                            from_ = TWILIO_CONFIG["from_"],
                            to= number,
                        )
            
            elif self.message_type == "whatsapp":

                pywhatkit.sendwhatmsg_instantly(
                    phone_no=number, 
                    message=text_message,
                )

                time.sleep(2)
                pyautogui.click()
                time.sleep(2)
                self.keyboard.press(Key.enter)
                self.keyboard.release(Key.enter)


        elif self.content_type == "audio":

            pywhatkit.sendwhatmsg_instantly(
                    phone_no=number, 
                    message=text_message,
                )

            pywhatkit.sendwhatdoc_immediately(
                    phone_no=number, 
                    path=media_message,
                )

            breakpoint()
            time.sleep(2)
            pyautogui.click()
            time.sleep(2)
            self.keyboard.press(Key.enter)
            self.keyboard.release(Key.enter)


        elif self.content_type in ["image", "video"]:


            pywhatkit.sendwhatmsg_instantly(
                    phone_no=number, 
                    message=text_message,
                )

            pywhatkit.sendimg_or_video_immediately(
                    phone_no=number, 
                    path=media_message,
                )

            time.sleep(2)
            pyautogui.click()
            time.sleep(2)
            self.keyboard.press(Key.enter)
            self.keyboard.release(Key.enter)



            



            







