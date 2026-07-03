import logging
import os

class LogGenerator:

    @staticmethod
    def logs_gen():
        os.makedirs(".\\Logs", exist_ok=True)
        logging.basicConfig(filename=".\\Logs\\automation.log",
                        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                        datefmt='%d-%b-%y %H:%M:%S %p',
                        level=logging.INFO,
                        force=True)

        log=logging.getLogger()
        return log
