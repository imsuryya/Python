import pytest
import logging
import os
import tempfile

def test_logging_basic_levels():
    logger = logging.getLogger("test_basic")
    logger.setLevel(logging.DEBUG)
    
    assert logger.level == logging.DEBUG

def test_logger_with_handler():
    logger = logging.getLogger("test_handler")
    handler = logging.StreamHandler()
    logger.addHandler(handler)
    
    assert len(logger.handlers) > 0

def test_logging_to_file(tmp_path):
    log_file = tmp_path / "test.log"
    
    logger = logging.getLogger("test_file")
    logger.setLevel(logging.INFO)
    
    handler = logging.FileHandler(log_file)
    logger.addHandler(handler)
    
    logger.info("Test message")
    
    assert log_file.exists()
    content = log_file.read_text()
    assert "Test message" in content

def test_logging_formatter():
    logger = logging.getLogger("test_formatter")
    handler = logging.StreamHandler()
    
    formatter = logging.Formatter('%(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    
    assert handler.formatter is not None

def test_logging_levels_hierarchy():
    logger = logging.getLogger("test_hierarchy")
    logger.setLevel(logging.WARNING)
    
    assert logger.isEnabledFor(logging.ERROR)
    assert logger.isEnabledFor(logging.WARNING)
    assert not logger.isEnabledFor(logging.INFO)

def test_custom_logger_class():
    class StudentLogger:
        def __init__(self, name):
            self.logger = logging.getLogger(name)
            self.logger.setLevel(logging.INFO)
        
        def log_student_added(self, student_name):
            self.logger.info(f"Student {student_name} added")
            return True
    
    student_logger = StudentLogger("students")
    result = student_logger.log_student_added("Surya")
    assert result == True

def test_logging_exception(tmp_path):
    log_file = tmp_path / "exceptions.log"
    
    logger = logging.getLogger("test_exception")
    logger.setLevel(logging.ERROR)
    
    handler = logging.FileHandler(log_file)
    logger.addHandler(handler)
    
    try:
        raise ValueError("Test error")
    except ValueError:
        logger.exception("An error occurred")
    
    content = log_file.read_text()
    assert "An error occurred" in content
    assert "ValueError" in content

def test_multiple_handlers(tmp_path):
    log_file = tmp_path / "multi.log"
    
    logger = logging.getLogger("test_multi")
    logger.setLevel(logging.DEBUG)
    
    file_handler = logging.FileHandler(log_file)
    stream_handler = logging.StreamHandler()
    
    logger.addHandler(file_handler)
    logger.addHandler(stream_handler)
    
    assert len(logger.handlers) == 2
