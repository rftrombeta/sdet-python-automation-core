# src/sdet_python_automation_core/core/context/execution_context.py

class ExecutionContext:
    def __init__(self):
        self.http_client = None
        self.last_response = None
