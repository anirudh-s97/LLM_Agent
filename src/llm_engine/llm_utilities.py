import json
from tqdm import tqdm
from typing import List, Dict, Union, Optional


def parse_llm_output(llm_response: str):
    """Parse the LLM's raw text output into a structured format."""
    try:
        # Try to parse as JSON
        cleaned_llm_response = llm_response.replace("```json", "").replace("```", "").strip()
        data = json.loads(cleaned_llm_response)
        return data
    except json.JSONDecodeError:
        # If not valid JSON, treat as a direct response
        return "Decode Error"

def handle_llm_response(llm_response: str):
    """Process the LLM's response, calling tools or returning content."""
    parsed = parse_llm_output(llm_response)
    
    if parsed.tool_calls:
        results = []
        for tool_call in parsed.tool_calls:
            # Execute the tool call
            result = execute_tool(tool_call.name, tool_call.args)
            results.append(result)
        return results
    else:
        # Return the direct response
        return parsed.content

def execute_tool(name: str, args: Dict, tools: Dict) -> str:
    """Execute a tool based on name and arguments."""
    # This would contain your tool implementations

    if name in tools:
        return tools[name](args)
    else:
        return f"Error: Tool '{name}' not found"

