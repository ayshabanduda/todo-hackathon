import subprocess
import pytest
import sys

# Task: T008
def run_cli(*args):
    result = subprocess.run(
        [sys.executable, "-m", "src.cli.main", *args],
        capture_output=True,
        text=True
    )
    return result

def test_cli_add_task():
    result = run_cli("add", "Integration Task", "Desc")
    assert result.returncode == 0
    assert "Task added successfully with ID:" in result.stdout

def test_cli_list_tasks_empty():
    result = run_cli("list")
    assert result.returncode == 0
    # Note: In-memory store is empty for each new process unless we mock or change design
    assert "No tasks found." in result.stdout

def test_cli_add_empty_title():
    result = run_cli("add", "")
    assert result.returncode == 1
    assert "Error: Title cannot be empty" in result.stdout