import subprocess
import pytest
import sys

# Task: T018
def run_cli(*args):
    result = subprocess.run(
        [sys.executable, "-m", "src.cli.main", *args],
        capture_output=True,
        text=True
    )
    return result

def test_cli_update_task_not_found():
    result = run_cli("update", "999", "New Title", "New Desc")
    assert result.returncode == 1
    assert "Error: Task with ID 999 not found" in result.stdout

def test_cli_delete_task_not_found():
    result = run_cli("delete", "999")
    assert result.returncode == 1
    assert "Error: Task with ID 999 not found" in result.stdout
