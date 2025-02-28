import os
import warnings
import json
import inspect

import logging
from pprint import pprint
from dotenv import load_dotenv
from tqdm import tqdm
from typing import List, Dict, Union, Optional

from src.execute_to_do_tasks import run_to_do_tasks
from src.file_compression import image_compression, pdf_compression
from src.file_organizer import organize_files, validate_and_scan_folder
from src.llm_engine.gemini_agent import Agent  
from src.llm_engine.llm_utilities import parse_llm_output


logger = logging.getLogger(__name__)

def accumulate_tools():
    total_tools = []
    for script in [organize_files, image_compression, pdf_compression, run_to_do_tasks]:
        functions = inspect.getmembers(script, inspect.isfunction)
        # Extract function names
        function_names = [(name,fn) for name, fn in functions if fn.__module__  == str(script.__name__)]
        total_tools.extend(function_names)
    
    available_tools = {k:fn for (k, fn) in total_tools}
    tool_descriptions = [f"{name}:\n{func.__doc__}\n\n" for name, func in available_tools.items()]
    return available_tools, tool_descriptions


# let the agent the agent decide on how to proceed with the task
def get_list_of_steps_to_perform_user_query(user_query):

    system_prompt = f"""
        You are an helpful AI-assistant and always respond with a JSON object that has two required keys.
        task: str = The user-query given by the user.
        sub_tasks: List

        Your objective is to break down the task given by the user into multiple sequential sub-tasks. Think about solving the tasks
        from all perspectives if it's open-ended.

        Don't start your answers with "Here is the JSON response", just give the JSON.
        """
    problem_solver_agent = Agent(system_prompt=system_prompt)
    
    llm_output = problem_solver_agent.perform_action(user_query)

    return llm_output

def get_list_of_fn_calls_to_start_job(steps_from_llm, tool_descriptions, fn_order):
    
    system_prompt = f"""You are given a set of steps to solve a problem and a bunch of tools that you can use to perform the steps
                        If you think a particular step cannot be solved using any of the tools, simply skip it.
                        The tools you have access to are:
                        {"".join(tool_descriptions)}
                        The order of functions are:
                        {fn_order}
                        """
    
    agent_job = """Plan the sequence of function calls needed to execute the tasks given the steps.
                Return a JSON array of function calls in order that needs to be executed.
                Don't give any arguments in your sequence of function calls.Ensure the function order is maintained. Just return one json file with function names and steps following the template below. 
                [{'step': 'step_number', 'function': 'function_name'}].
                """
    task_identifier_agent = Agent(system_prompt=system_prompt + agent_job)
    response = task_identifier_agent.perform_action(steps_from_llm)

    return response

def scheduler(user_query, folder_path):

    tools, desc = accumulate_tools()
    fn_order = list(tools.keys())
    llm_response = get_list_of_steps_to_perform_user_query(user_query)
    function_calls = get_list_of_fn_calls_to_start_job(llm_response, desc, fn_order)

    dict_info = parse_llm_output(function_calls)
    print(dict_info)
    if dict_info:
        logger.info("Started scheduling the sub-tasks and tools......")
        print("""
                ░░░░
                ░    ░
            {○_○}   ░ Processing...
            <|   |> ░
            |   |  ░
            ════   ░
                ░░░░
            """)
        
        for step in dict_info:
            func = tools.get(step["function"])
            if func is not None:
                if step["function"] == "move_files_to_categories":
                    dest_map = func(source_dir=folder_path)
                    
                elif step["function"] == "compress_pdf":
                    fname = ""
                    for file in dest_map:
                        if file.endswith(".pdf"):
                            fname = dest_map[file]
                            break
                    if fname != "":
                        func(file_path=fname)   
                
                elif step["function"] == "compress_image":
                    fname = ""
                    for file in dest_map:
                        if file.endswith(".png"):
                            fname = dest_map[file]
                            break
                    if fname != "":
                        func(file_path=fname)  
                
                elif step["function"] == "process_todo_file":
                    func(folder_path=folder_path)
                     








    else:
        return "LLM was unable to fetch the tools required to do your job. Sorry for the inconvenience"
    


if __name__ == "__main__":
    user_quer = ""
    folder_path = ""
    resp =scheduler(user_quer, folder_path)
    print(resp)

