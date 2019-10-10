import logging
logger=logging.getLogger('monitoring_system.'+__name__)


class Subsystem():
        def __init__(self, monitor, idx, temp=0.0):
            self.monitor = monitor
            self.temp = temp
            self.id = idx
            self.monitor.add_subsystem(self)
            logger.info("subsystem %d  is created", self.id)

        def set_temp(self, temp):
            self.temp = temp
            logger.info("subsystem %d temperature is changed to %f", self.id, self.temp)
            self.monitor.changed()

        def get_temp(self):
            return self.temp

        def serialize(self):
            return {
                'index': self.id,
                'temperature': self.temp
            }

