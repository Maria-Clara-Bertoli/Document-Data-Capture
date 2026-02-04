from models.messages import MessageResponse
from abstractions.chat_config import ChatConfig
from langgraph.graph.state import CompiledStateGraph
from pymongo.synchronous.collection import Collection

class AgentUsecase:

    """This class is used to configure the agent's dialog and messages, and to invoke the agent."""

    def __init__(self, text: str, file_id: str, dialogue_id: int, agent: CompiledStateGraph, mongo_collection: Collection):
        self.agent = agent
        self.chat_config = ChatConfig(text=text, 
                                      file_id=file_id, 
                                      dialogue_id=dialogue_id, 
                                      mongo_collection=mongo_collection)

    def calls_agent_resources(self) -> MessageResponse:
        """
        Calls the resources related to the agent.
        
        Returns:
            MessageResponse: Response returned by the agent.
        """
        config = self.chat_config.config_dialogue()
        messages = self.chat_config.config_messages()

        response = self.agent.invoke(
            config=config,
            input={"messages": messages}
        )
        return {"text": getattr(response["structured_response"], "punny_response")}