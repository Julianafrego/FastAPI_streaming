import os   # biblioteca para permitir interações com o sistema operacional
import requests
from pathlib import Path #para manipular os caminhos no sistema operacional


def download_video(url: str, output_file: str):
    
        # Obtém o diretório padrão de downloads do sistema
        downloads_directory = str(Path.home() / "Downloads")
        #definição do caminho para o arquivo de saida
        output_path = os.path.join(downloads_directory, output_file)    
        
        with requests.get(url, stream=True) as response:
            response.raise_for_status()
            with open(output_path, 'wb') as file:
                for chunk in response.iter_content(chunk_size=8192):
                    if chunk:
                        file.write(chunk)
                
        
                    
if __name__ == "__main__":
        
        # URL do endpoint do vídeo no servidor FastAPI
        video_url = "http://127.0.0.1:8000/video"  
        
        # Nome do arquivo de saída
        output_file = "downloaded_video.mp4"  
        
        #chama a função que baixa o video 
        download_video(video_url, output_file)      
