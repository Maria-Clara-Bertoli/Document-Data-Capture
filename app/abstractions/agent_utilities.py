import os
import sqlite3
from logger import logger
from typing import Callable
from langchain.tools import tool
from dataclasses import dataclass
from langgraph.types import Command
from langgraph.runtime import Runtime
from langchain.agents import AgentState
from langchain.tools.tool_node import ToolCallRequest
from langgraph.checkpoint.memory import InMemorySaver
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.messages import RemoveMessage, ToolMessage
from langchain.agents.middleware import wrap_tool_call, after_model

@tool(name_or_callable="create_table_in_the_database", description="This tool creates a table in the database. Use it after extracting structured data from documents.")
def create_table_in_the_database(sql: str) -> bool:
    """
    Creates the extracted table from a document in the database.
    
    Args: 
        sql (str): SQL command to create a table in the database.

    Returns:
        True: Indicates whether the table was successfully created in the database.
    """
    connection = sqlite3.connect(os.getenv("DATABASE_PATH"))
    cursor = connection.cursor()
    cursor.execute(sql)
    connection.close()

    return True

@tool(name_or_callable="inserts_information_into_the_table", description="This tool inserts information into a previously created table in the database. Use it to add data to a pre-existing table in the database.")
def inserts_information_into_the_table(sql: str) -> bool:
    """
    Inserts information into a previously created table in the database.
    
    Args: 
        sql (str): SQL command to insert information into a previously created table in the database.

    Returns:
        True: Indicates whether all the information was inserted into the table presents in the database.
    """
    connection = sqlite3.connect(os.getenv("DATABASE_PATH"))
    cursor = connection.cursor()
    cursor.execute(sql)
    connection.commit()
    connection.close()
    
    return True

@tool(name_or_callable="query_data_in_table", description="This tool queries data in pre-existing tables in the database. Use it to extract specific data from tables present in the database.")
def query_data_in_table(sql: str) -> str:
    """
    Querying information in tables in the database.
    
    Args:
        sql (str): SQL command to extract specific information from tables in the database, according to user requests.

    Returns:
        True: Indicates whether the database query was successful.
    """
    connection = sqlite3.connect(os.getenv("DATABASE_PATH"))

    cursor = connection.cursor()
    raw_response = cursor.execute(sql)
    refined_response = raw_response.fetchall()

    connection.close()
    return refined_response

@wrap_tool_call
def monitor_tool(
    request: ToolCallRequest,
    handler: Callable[[ToolCallRequest], ToolMessage | Command],
) -> ToolMessage | Command:
    """
    Monitore the tools used by the agent.
    
    Args:
        request (ToolCallRequest): Tool request.
        handler (Callable[[ToolCallRequest], ToolMessage | Command]): Request object call.
    
    Returns:
        ToolMessage | Command: The message or call from the tool that is being made.
    """
    logger.info(f"Running a tool '{request.tool_call['name']}' with the following arguments: {request.tool_call['args']}")
    
    try:
        result = handler(request)
        return result
    except Exception as error:
        raise Exception(f"The tool could not be executed: {error}")
    
@after_model
def delete_old_messages(state: AgentState, runtime: Runtime) -> dict | None:
    """
    Delete old messages from the conversation with the agent.
    
    Args:
        runtime (Runtime): Runtime.
        state (AgentState): Agent state.
    
    Returns:
        dict | None: A notice informing that old messages have been deleted.
    """
    messages = state["messages"]
    if len(messages) > 10:
        return {"messages": [RemoveMessage(id=message.id) for message in messages[:3]]}
    return None

@dataclass
class ResponseFormat:

    """This class is responsible for defining a response model."""

    punny_response: str
    default_response: str = "Your message is outside the expected standard."

def define_model() -> ChatGoogleGenerativeAI:
    """
    Defines the model used by the agent.
    
    Returns:
        ChatGoogleGenerativeAI: Model used by the agent.
    """
    model = ChatGoogleGenerativeAI(
        timeout=60,
        temperature=0.5,
        max_tokens=125000,
        model="gemini-2.5-flash"
    )
    return model

def define_checkpointer() -> InMemorySaver:
    """
    Defines the checkpointer.

    Returns:
        InMemorySaver: Agent's memory state.
    """
    checkpointer = InMemorySaver()
    return checkpointer