from abc import abstractmethod

class Reminder(object):
    
    @abstractmethod
    def getAll(self):
        pass

class CalendarReminder(object):

    def date(self):
        return "Todays date.."

    def event(self):
        return "Event name.."

    def getAll(self):
        return {
            "event": self.event(),
            "date": self.date(),
        }