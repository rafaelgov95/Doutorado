from google_drive_downloader import GoogleDriveDownloader as gdd


def download_file(file_id, output_file):
    gdd.download_file_from_google_drive(file_id=file_id, dest_path=output_file, unzip=False)


# Exemplo de uso
file_id = '1WwPXYjgFuEag8aBNyQm4OI9MCBpvOZXW'  # Substitua pelo ID do arquivo do Google Drive
output_file = './nome_do_arquivo.mp4'  # Substitua pelo nome desejado para o arquivo local

download_file(file_id, output_file)
