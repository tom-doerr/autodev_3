"""
This module contains the core logic for the LLM coding agent using DSPy.
"""
from llm_interface import DSPyLLM
from environment import Environment

class Agent:
    """
    The Agent class is responsible for executing tasks by interacting with the LLM (DSPy) and the environment.
    """
    def __init__(self, llm: DSPyLLM, environment: Environment):
        """
        Initializes the Agent with a DSPy LLM and an environment.

        Args:
            llm: An instance of the DSPyLLM class.
            environment: An instance of the Environment class.
        """
        self.llm = llm
        self.environment = environment

    def execute_task(self, task_description: str) -> str:
        """
        Executes a given task by interacting with the LLM (DSPy) and the environment.

        Args:
            task_description: A string describing the task to be executed.

        Returns:
            A string containing the result of the task execution.
        """
        # 1. Generate a plan using the LLM
        plan: list[str] = self.llm.generate_plan(task_description)

        # 2. Execute the plan step-by-step
        context = ""
        for step in plan:
            # 3. Generate code for the current step
            code: str = self.llm.generate_code(step)

            # 4. Execute the code in the environment
            result: str = self.environment.execute_code(code)

            # 5. Update the LLM with the result (context)
            self.llm.update_context(step, code, result)
            context += f"Step: {step}\nCode: {code}\nResult: {result}\n"

        # 6. Return the final result
        return self.llm.generate_final_result(context)
