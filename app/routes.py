from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from usecases.agent_usecase import AgentUsecase
from abstractions.agent_config import AgentConfig
from usecases.database_usecase import DatabaseUsecase
from fastapi import FastAPI, Request, Response, status
from models.messages import MessageRequest, MessageResponse
from abstractions.database_utilities import calls_database_resources

app = FastAPI()
agent_config = AgentConfig()
agent = agent_config.config_agent()
mongo_collection = calls_database_resources()

@app.exception_handler(exc_class_or_status_code=Exception)
async def exception_handler(request: Request, exception: Exception) -> JSONResponse:
    return JSONResponse(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, content=jsonable_encoder(exception))

@app.post("/talk_to_the_agent", status_code=200, response_model=MessageResponse)
async def talk_to_the_agent(request: MessageRequest) -> MessageResponse:
     agent_usecase = AgentUsecase(agent=agent,
                                  text=request.text, 
                                  file_id=request.file_id,
                                  dialogue_id=request.dialogue_id,
                                  mongo_collection=mongo_collection)
     
     return agent_usecase.calls_agent_resources()

@app.delete("/delete_database_information", status_code=204)
async def delete_database_information() -> JSONResponse:
    database_usecase = DatabaseUsecase()
    database_usecase.calls_database_resources()
    return Response(status_code=status.HTTP_204_NO_CONTENT)

# Precisa ainda de testes unitários, comentários



    
