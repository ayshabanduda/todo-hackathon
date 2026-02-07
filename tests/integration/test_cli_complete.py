import subprocess
import pytest
import sys

# Task: T013
def run_cli(*args):
    result = subprocess.run(
        [sys.executable, "-m", "src.cli.main", *args],
        capture_output=True,
        text=True
    )
    return result

def test_cli_complete_task_not_found():
    result = run_cli("complete", "999")
    assert result.returncode == 1
    assert "Error: Task with ID 999 not found" in result.stdout

# Integration test for success would require persistence or a combined script
# Since we are in-memory per process, we can't easily test add + complete in separate subprocesses
# unless we implement a test command that does both or use a file-based mock.
# For now, we'll focus on the error handling which is verifiable.
