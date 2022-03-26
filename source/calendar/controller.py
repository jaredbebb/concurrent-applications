from numpy import true_divide
from model import Reminder
from view import ViewBase

import logging
import threading
import time


class Controller():

    def __init__(self, reminder, view):
        self.reminder_ = reminder
        self.view_ = view
        
        # Daemon thread that runs in backround. 

        self.threads = list()
        self.poll = True
        self.thread_wait = threading.Thread(target=self.run_every_x_seconds, args=(1, 2), daemon=True)
        self.threads.append(self.thread_wait)
        self.thread_wait.start()

    def run_every_x_seconds(self, name, seconds):
        while(1):
            logging.info("Thread %s: starting", name)
            time.sleep(seconds)
            self.poll = True
            logging.info("Thread %s: finishing", name)

    def requestPoll(self):
        #self.poller
        pass

    def showAll(self):
        #gets list of all Person objects
        people_in_db = self.reminder_.getAll()
        #calls view
        return self.view_.showAllView(people_in_db)


    def input(self):
        if(self.poll):
            self.poll = False
            return True
        return False

    def start(self):
        self.view_.startView()
        poll = self.input()
        if poll:
            return self.showAll()
        else:
            return self.view_.endView()

    def updateView(self) ->bool:
        """
        Intitiate view if model requests it
        """
        if self.reminder_.requestPoll():
            self.showAll()

if __name__ == "__main__":
    from model import CalendarReminder
    from view import GUIView

    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO,
                        datefmt="%H:%M:%S")

    controller = Controller(reminder = CalendarReminder(), view = GUIView())

    #running controller function
    while(1):
        controller.start()