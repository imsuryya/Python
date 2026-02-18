import logging
import os
from datetime import datetime

print("=== Basic Logging ===")

logging.basicConfig(level=logging.INFO)
logging.info("Application started")
logging.warning("This is a warning message")
logging.error("This is an error message")

print("\n=== Logging Levels ===")

logging.debug("Debug message - detailed information")
logging.info("Info message - general information")
logging.warning("Warning message - something unexpected")
logging.error("Error message - serious problem")
logging.critical("Critical message - program may crash")

print("\n=== Logging to File ===")

log_dir = "logs"
if not os.path.exists(log_dir):
    os.makedirs(log_dir)

log_file = os.path.join(log_dir, "app.log")

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    filename=log_file,
    filemode='w'
)

logger = logging.getLogger(__name__)

logger.info("Student Surya logged in")
logger.info("Marks updated for Priya")
logger.warning("Low disk space detected")
logger.error("Failed to connect to database")

print(f"Logs written to {log_file}")

print("\n=== Structured Logging ===")

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s | %(levelname)-8s | %(name)s | %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    handlers=[
        logging.FileHandler(os.path.join(log_dir, "detailed.log")),
        logging.StreamHandler()
    ],
    force=True
)

logger = logging.getLogger("StudentManagement")

def process_student_marks(student_name, marks):
    logger.info(f"Processing marks for {student_name}")
    try:
        if marks < 0 or marks > 100:
            logger.error(f"Invalid marks: {marks} for {student_name}")
            raise ValueError("Marks must be between 0 and 100")
        logger.info(f"Marks {marks} validated for {student_name}")
        return True
    except Exception as e:
        logger.exception(f"Exception occurred while processing {student_name}")
        return False

process_student_marks("Surya", 95)
process_student_marks("Priya", 150)

print("\n=== Custom Logger with Multiple Handlers ===")

student_logger = logging.getLogger("StudentLogger")
student_logger.setLevel(logging.DEBUG)

file_handler = logging.FileHandler(os.path.join(log_dir, "students.log"))
file_handler.setLevel(logging.INFO)

console_handler = logging.StreamHandler()
console_handler.setLevel(logging.WARNING)

formatter = logging.Formatter('%(asctime)s - %(name)s - [%(levelname)s] - %(message)s')
file_handler.setFormatter(formatter)
console_handler.setFormatter(formatter)

student_logger.addHandler(file_handler)
student_logger.addHandler(console_handler)

student_logger.debug("Debug: Student data loaded")
student_logger.info("Info: Student Arjun registered")
student_logger.warning("Warning: Student database backup pending")
student_logger.error("Error: Failed to send email notification")

print("\n=== Logging in Production ===")

production_logger = logging.getLogger("Production")

class StudentManager:
    def __init__(self):
        self.logger = logging.getLogger(self.__class__.__name__)
        self.students = {}
    
    def add_student(self, name, marks):
        self.logger.info(f"Adding student: {name}")
        try:
            if not name:
                raise ValueError("Student name cannot be empty")
            self.students[name] = marks
            self.logger.info(f"Successfully added {name} with marks {marks}")
        except Exception as e:
            self.logger.error(f"Failed to add student: {e}")
    
    def get_student(self, name):
        self.logger.debug(f"Retrieving student: {name}")
        if name in self.students:
            self.logger.info(f"Found student: {name}")
            return self.students[name]
        else:
            self.logger.warning(f"Student not found: {name}")
            return None

manager = StudentManager()
manager.add_student("Surya", 95)
manager.add_student("Priya", 88)
manager.get_student("Surya")
manager.get_student("Unknown")

print(f"\nLogging examples completed! Check logs in '{log_dir}/' directory")
