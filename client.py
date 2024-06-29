import requests

def download_video(url: str, output_file: str):
    with requests.get(url, stream=True) as response:
        response.raise_for_status() # verifica se a solicitação foi bem sucedida
        with open(output_file, 'wb') as file:  # abre o arquivo em modo de escrita binária, o arquivo é escrito e depois fechado
            for chunk in response.iter_content(chunk_size=8192):   # itera sobre o conteúdo da resposta em pedaços, o arquivo será baixado em partes
              if chunk: 
                 file.write(chunk)
                 
if __name__ == "__main__":
    video_url = "http://127.0.0.1:8000/video"  # URL do endpoint do vídeo no servidor FastAPI
    output_file = "downloaded_video.mp4"  # Nome do arquivo de saída
    download_video(video_url, output_file)      
