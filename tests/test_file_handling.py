import pytest
import os
import tempfile

@pytest.fixture
def temp_file():
    fd, path = tempfile.mkstemp(suffix=".txt")
    os.close(fd)
    yield path
    if os.path.exists(path):
        os.remove(path)

@pytest.fixture
def temp_dir():
    import tempfile
    import shutil
    dir_path = tempfile.mkdtemp()
    yield dir_path
    shutil.rmtree(dir_path)

def test_write_file(temp_file):
    with open(temp_file, "w") as file:
        file.write("Hello, World!")
    
    assert os.path.exists(temp_file)
    with open(temp_file, "r") as file:
        content = file.read()
    assert content == "Hello, World!"

def test_read_file(temp_file):
    with open(temp_file, "w") as file:
        file.write("Test content")
    
    with open(temp_file, "r") as file:
        content = file.read()
    
    assert content == "Test content"

def test_append_file(temp_file):
    with open(temp_file, "w") as file:
        file.write("Line 1\n")
    
    with open(temp_file, "a") as file:
        file.write("Line 2\n")
    
    with open(temp_file, "r") as file:
        content = file.read()
    
    assert content == "Line 1\nLine 2\n"

def test_readline(temp_file):
    with open(temp_file, "w") as file:
        file.write("First line\nSecond line\nThird line")
    
    with open(temp_file, "r") as file:
        first_line = file.readline()
    
    assert first_line == "First line\n"

def test_readlines(temp_file):
    with open(temp_file, "w") as file:
        file.write("Line 1\nLine 2\nLine 3")
    
    with open(temp_file, "r") as file:
        lines = file.readlines()
    
    assert len(lines) == 3
    assert lines[0] == "Line 1\n"
    assert lines[2] == "Line 3"

def test_writelines(temp_file):
    lines = ["First\n", "Second\n", "Third\n"]
    
    with open(temp_file, "w") as file:
        file.writelines(lines)
    
    with open(temp_file, "r") as file:
        content = file.read()
    
    assert content == "First\nSecond\nThird\n"

def test_file_not_found():
    with pytest.raises(FileNotFoundError):
        with open("nonexistent_file_12345.txt", "r") as file:
            file.read()

def test_file_exists(temp_file):
    assert os.path.exists(temp_file)

def test_file_size(temp_file):
    content = "Hello, World!"
    with open(temp_file, "w") as file:
        file.write(content)
    
    size = os.path.getsize(temp_file)
    assert size == len(content)

def test_binary_write_read(temp_file):
    data = bytes([65, 66, 67, 68, 69])
    
    with open(temp_file, "wb") as file:
        file.write(data)
    
    with open(temp_file, "rb") as file:
        read_data = file.read()
    
    assert read_data == data

def test_file_iteration(temp_file):
    with open(temp_file, "w") as file:
        file.write("Line 1\nLine 2\nLine 3")
    
    lines = []
    with open(temp_file, "r") as file:
        for line in file:
            lines.append(line.strip())
    
    assert lines == ["Line 1", "Line 2", "Line 3"]

def test_context_manager(temp_file):
    with open(temp_file, "w") as file:
        file.write("Test")
        assert not file.closed
    
    assert file.closed

def test_file_tell_seek(temp_file):
    with open(temp_file, "w") as file:
        file.write("0123456789")
    
    with open(temp_file, "r") as file:
        assert file.tell() == 0
        file.read(5)
        assert file.tell() == 5
        file.seek(0)
        assert file.tell() == 0

def test_file_with_encoding(temp_file):
    text = "Hello, 世界"
    
    with open(temp_file, "w", encoding="utf-8") as file:
        file.write(text)
    
    with open(temp_file, "r", encoding="utf-8") as file:
        content = file.read()
    
    assert content == text

def test_file_remove(temp_dir):
    file_path = os.path.join(temp_dir, "test.txt")
    
    with open(file_path, "w") as file:
        file.write("Test")
    
    assert os.path.exists(file_path)
    os.remove(file_path)
    assert not os.path.exists(file_path)
