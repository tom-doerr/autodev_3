"""
This module defines the interface for interacting with the LLM using DSPy.
"""

import dspy

class GeneratePlan(dspy.Signature):
    """Generates a plan for a given task."""
    task_description = dspy.InputField()
    plan = dspy.OutputField()

class GenerateCode(dspy.Signature):
    """Generates code for a given step in the plan."""
    step = dspy.InputField()
    code = dspy.OutputField()

class GenerateFinalResult(dspy.Signature):
    """Generates the final result of the task execution."""
    context = dspy.InputField()
    result = dspy.OutputField()

class DSPyLLM(dspy.Module):
    def __init__(self):
        super().__init__()
        self.generate_plan = dspy.Predict(GeneratePlan)
        self.generate_code = dspy.Predict(GenerateCode)
        self.generate_final_result = dspy.Predict(GenerateFinalResult)

    def generate_plan(self, task_description: str) -> list[str]:
        """
        Generates a plan for executing a given task using the LLM.

        Args:
            task_description: A string describing the task to be executed.

        Returns:
            A list of strings representing the steps in the plan.
        """
        prediction = self.generate_plan(task_description=task_description)
        return prediction.plan.split("\n")

    def generate_code(self, step: str) -> str:
        """
        Generates code for a given step in the plan using the LLM.

        Args:
            step: A string describing the step for which code needs to be generated.

        Returns:
            A string containing the generated code.
        """
        prediction = self.generate_code(step=step)
        return prediction.code

    def update_context(self, step: str, code: str, result: str):
        """
        Updates the LLM with the result of executing a given step.

        Args:
            step: A string describing the step that was executed.
            code: A string containing the code that was executed.
            result: A string containing the result of executing the code.
        """
        # In DSPy, context is managed implicitly through the module's state.
        # You might need to implement a more sophisticated context management strategy
        # depending on the complexity of your task.
        pass

    def generate_final_result(self, context: str) -> str:
        """
        Generates the final result of the task execution using the LLM.

        Returns:
            A string containing the final result.
        """
        prediction = self.generate_final_result(context=context)
        return prediction.result
