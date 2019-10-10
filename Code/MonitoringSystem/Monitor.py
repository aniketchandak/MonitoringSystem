from Subsystem import Subsystem
from Fan import Fan
from Observable import Observable
import logging
logger = logging.getLogger('monitoring_system.'+__name__)


class Monitor(Observable):
    def __init__(self):
        self.subsystems = list()
        self.curr_max = 0.0
        super(Monitor,self).__init__()

    def add_subsystem(self,subsystem):
        self.subsystems.append(subsystem)

    def max_temp(self):
        max_temp = -50.0
        for each in self.subsystems:
            if each.get_temp() > max_temp:
                max_temp = each.get_temp()
        return max_temp

    def changed(self):
        max_temp = self.max_temp()
        if max_temp != self.curr_max:
            logger.info("Change in maximum temperature. Current max temp is: %f ",max_temp)
            self.notify(max_temp)
            self.curr_max = max_temp





