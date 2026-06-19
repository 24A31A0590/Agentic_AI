import sys
import io
from contextlib import redirect_stdout
import traceback

def execute_code(code: str) -> dict:
    """
    Executes Python code and captures the standard output and any errors.
    """
    if not code.strip():
        return {"output": "", "error": "No code provided."}
    
    f = io.StringIO()
    error_msg = ""
    
    try:
        with redirect_stdout(f):
            # Execute with restricted globals/locals
            exec(code, {"__builtins__": __builtins__}, {})
    except Exception as e:
        error_msg = traceback.format_exc()
        
    return {
        "output": f.getvalue(),
        "error": error_msg
    }
