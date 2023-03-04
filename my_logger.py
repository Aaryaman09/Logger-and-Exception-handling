import logging
import traceback
import csv

class CustomLogger:

    def __init__(self, log_file_path, log_level=logging.INFO):
        self.log_file_path = log_file_path
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(log_level)
        formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
        file_handler = logging.FileHandler(self.log_file_path)
        file_handler.setFormatter(formatter)
        self.logger.addHandler(file_handler)

    def log(self, message, level=logging.INFO):
        if level == logging.INFO:
            self.logger.info(message)
        elif level == logging.WARNING:
            self.logger.warning(message)
        elif level == logging.ERROR:
            self.logger.error(message)
        elif level == logging.CRITICAL:
            self.logger.critical(message)

    def export_logs_to_csv(self, csv_file_path):
        with open(self.log_file_path, 'r') as log_file:
            with open(csv_file_path, 'w', newline='') as csv_file:
                csv_writer = csv.writer(csv_file)
                csv_writer.writerow(['Timestamp', 'Level', 'Message'])
                for line in log_file:
                    if line.startswith('20'):
                        log_data = line.split(' ', 2)
                        csv_writer.writerow([log_data[0], log_data[1], log_data[2].strip()])

class CustomExceptionHandler:

    def __init__(self, logger):
        self.logger = logger

    def handle_exception(self, exc_type, exc_value, exc_traceback):
        error_message = f"{exc_type.__name__}: {exc_value}"
        stack_trace = traceback.format_exception(exc_type, exc_value, exc_traceback)
        self.logger.log(error_message, level=logging.ERROR)
        self.logger.log(''.join(stack_trace), level=logging.ERROR)
        sys.__excepthook__(exc_type, exc_value, exc_traceback)
