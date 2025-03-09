"""
This module defines the environment in which the agent operates.
"""

import subprocess

class Environment:
    def __init__(self):
        """
        Initializes the Environment.
        """
        pass

    def execute_code(self, code: str) -> str:
        """
        Executes the given code in the environment.

        Args:
            code: A string containing the code to be executed.

        Returns:
            A string containing the result of the code execution.
        """
        try:
            process = subprocess.Popen(
                ["python", "-c", code],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
            )
            stdout, stderr = process.communicate()
            if stderr:
                return f"Error: {stderr}"
            return stdout
        except subprocess.CalledProcessError as e:
            return f"Error: {str(e)}"
        except Exception as e:
            return f"Error: {str(e)}"
