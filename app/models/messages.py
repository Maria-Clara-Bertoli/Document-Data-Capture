from pydantic import BaseModel, Field

class MessageRequest(BaseModel):
    text: str = Field(default=None, title="Text", description="Text message sent to the agent")
    file_id: str = Field(default=None, title="File ID", description="file ID present in the database")
    dialogue_id: int = Field(default=None, title="Dialogue ID", description="ID of the dialogue sent to the agent")

class MessageResponse(BaseModel):
    text: str = Field(default=None, title="Text", description="Text message sent to the user")