import os

from tqdm import tqdm
from src.llm_engine.gemini_agent import Agent
from src.llm_engine.scheduler import scheduler
from src.file_organizer.validate_and_scan_folder import validate_folder_and_files


def valid_task_identifier(user_query):

    system_prompt = """ You are a helpful AI assistant that works in doing automation of tasks.
                        Given a user-query, try to check if the query aligns with any of the below mentioned tasks.
                          -1: Organize & Manage Folders.
                          -2: Compress PDF Files.
                          -3: Run-to-do Tasks.
                        If the query does not align with the above-mentioned tasks, then state that the action
                        user has mentioned in invalid. Otherwise return valid

                        Return 1 if you feel if that user-query is valid, otherwise return 0.
                                
                    """

    task_identifier_agent = Agent(system_prompt=system_prompt)

    response = task_identifier_agent.perform_action(user_query=user_query)

    return response





if __name__ == "__main__":
    
    print("""
        ╔═══════╗
        ║ ◣_◢ ║
        ║ {○_○} ║
    ╔═══╩═══════╩═══╗
    ║  [│_█_█_█_│]  ║
    ╚═══╦═══════╦═══╝
        ║  ═══  ║
        ║   │   ║
        ╚═══╦═══╝
            ║
         ═══╩═══

    Hi! I am your AI assistant.. I can organize folders, compress files and send invites
    How may I help you today?

        
    """)

    while int(input()):
        #print("Please enter your query/job that you want me to do:\n")
        user_query = input("Please enter your query/job that you want me to do:\n")
        task = valid_task_identifier(user_query)
        if not int(task):
            print("Sorry! I am unable to understand your query!")
            print("Please be specific about your use-case and mention any task that I can align with")
            continue 

        else:
            print("I think I have understood your task and I believe I should be able to resolve it.")
            print("Enter the folder path you want to manage:\n")
            folder_path = input()

            is_valid = validate_folder_and_files(folder_path)
            
            if is_valid: 
                response = scheduler(user_query, folder_path)
            else:
                raise ValueError("The folder path doesn't exist or the folder does not contain any file to manage.")
    
