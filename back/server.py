from fastapi import FastAPI, Response
from fastapi.responses import StreamingResponse
import uvicorn
import os

app = FastAPI()

async def stream_video(file_path: str):
    video_path = os.path.join(os.path.dirname(__file__), "../video/praia.mp4")
    
    with open(video_path, 'rb') as file: # abre o arquivo em modo de leitura binaria
        chunk_size = 1024 * 1024  # 1 MB chunks
        while chunk := file.read(chunk_size): # lê um chunk é atribue a  variavel até chunk ser vazio
            yield chunk

@app.get("/video")
async def get_video():
        video_path = os.path.join(os.path.dirname(__file__), "../video/praia.mp4")
        return StreamingResponse(stream_video(video_path), media_type="video/mp4")

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)