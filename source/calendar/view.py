# from model import Reminder
from PyQt5.QtWidgets import *

# app = QApplication([])
# label = QLabel('Hello World!')
# label.show()
# app.exec_()

from abc import abstractmethod
class ViewBase():
    @abstractmethod
    def showAllView(self):
        pass

    @abstractmethod
    def startView(self):
        pass

    @abstractmethod
    def endView(self):
        pass

class GUIView(ViewBase):

    def showAllView(self, list):
        #    print('In our db we have %i users. Here they are:' % len(list))
        #    for item in list:
        #       print(item.name())
        app = QApplication([])
        for item in list:
            label = QLabel(item)
            label.show()
        app.exec_()


    def startView(self):
        print('MVC - the simplest example')
        print('Do you want to see everyone in my db?[y/n]')
    
    def endView(self):
        print('Goodbye!')
