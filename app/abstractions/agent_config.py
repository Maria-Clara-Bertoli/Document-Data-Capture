from enums.agent_enum import AgentEnum
from langchain.agents import create_agent
from langgraph.graph.state import CompiledStateGraph
from langchain.agents.structured_output import ToolStrategy
from abstractions.agent_utilities import ResponseFormat, define_model, define_checkpointer, monitor_tool, delete_old_messages, create_table_in_the_database, inserts_information_into_the_table, query_data_in_table

class AgentConfig:

    """This class is used to configure the agent."""

    def config_agent(self) -> CompiledStateGraph:
        """
        Configure the agent.

        Returns: 
            CompiledStateGraph: The configured agent.
        """
        try:
            agent = create_agent(
                model=define_model(),
                checkpointer=define_checkpointer(),
                system_prompt=AgentEnum.SYSTEM_PROMPT.value,
                response_format = ToolStrategy(ResponseFormat),
                middleware=[monitor_tool, delete_old_messages],
                tools = [create_table_in_the_database, inserts_information_into_the_table, query_data_in_table]
            )
            return agent
        except Exception as error:
            raise(f"The agent could not be configured: {error}")