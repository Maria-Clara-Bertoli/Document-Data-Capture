from typing import List
from pymongo.synchronous.collection import Collection
from abstractions.database_utilities import search_for_specific_file

class ChatConfig:

    """This class is used to configure the existing conversation between the agent and the user."""

    def __init__(self, text: str, file_id: str, dialogue_id: int, mongo_collection: Collection):
        self.text = text
        self.file_id = file_id
        self.dialogue_id = dialogue_id
        self.mongo_collection = mongo_collection

    def config_dialogue(self) -> dict:
        """
        Sets the ID of the existing conversation between the agent and the user.
        
        Returns:
            dict: The dialogue ID in the form of a dictionary.
        """
        if self.dialogue_id is None:
            raise Exception("You need to specify a valid dialogue ID")
        else:
            config = {"configurable": {"thread_id": str(self.dialogue_id)}}
            return config

    def config_messages(self) -> List[dict]:
        """
        Sets the messages format send to the agent. 

        Returns:
            List[dict]: Messages format that should be sent to the agent. 
        """
        if self.text is None:
            raise Exception("You need to send a valid message to the agent")
        else:
            if self.file_id is not None:
                file_data = search_for_specific_file(self.mongo_collection, self.file_id)

                messages = [
                    {
                        "role": "user",
                        "content": [
                            {"type": "text", "text": self.text},
                            {"type": "file", "base64": file_data["file"], "mime_type": "application/pdf"}
                        ]
                    }
                ]
            else:
                messages = [
                    {
                        "role": "user",
                        "content": [
                            {"type": "text", "text": self.text},
                        ]
                    }
                ]
            
            return messages
