from Observer import Observer
import logging
logger = logging.getLogger('monitoring_system.'+__name__)


class Fan(Observer):
    def __init__(self,monitor,idx,max_rpm=100):
        self.index = idx
        self.max_rpm = max_rpm
        self.monitor = monitor
        monitor.subscribe(self)
        self.curr_rpm = None
        self.update(monitor.curr_max)
        logger.info("Fan %d  is created", self.index)

    def update(self, temp=None):
        if temp <= 25.0:
            self.set_rpm(0.2*self.max_rpm)
        elif temp >= 75.0:
            self.set_rpm(self.max_rpm)
        else:
            self.set_rpm(self.max_rpm*(0.2+(((temp-25)*80)/50)/100)) # This can be simplified but keeping it as it is for simplifying explaination of the equation

    def set_rpm(self, rpm):
        self.curr_rpm = int(rpm)
        logger.info("Running Speed of Fan %d is updated to %d RPM", self.index, self.curr_rpm)

    def set_max_rpm(self, rpm):
        self.max_rpm = rpm
        self.update(self.monitor.curr_max)
        logger.info("Max speed of Fan %d is updated to %d RPM", self.index, self.max_rpm)

    def serialize(self):
        return {
            'index' : self.index,
            'max_speed': self.max_rpm,
            'curr_speed': self.curr_rpm
        }
