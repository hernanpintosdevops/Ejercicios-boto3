import boto3

s3 = boto3.client('s3')

# Parámetros por defecto
bucket_name = 'mi-bucket-ejemplo-boto-hernan331'
object_key = 'coco.txt'
download_path = f'/home/hernan/mi_proyecto/descargas/{object_key}'

try:
    s3.download_file(bucket_name, object_key, download_path)
    print(f'Archivo {object_key} descargado a {download_path}')
except Exception as e:
    print(f'Error descargando archivo: {e}')