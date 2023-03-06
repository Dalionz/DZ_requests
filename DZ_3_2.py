import requests

class YaUploader():

    def __init__(self, token: str):
        self.token = token
        self.ya_url = "https://cloud-api.yandex.net/"

    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': f'OAuth {self.token}'
        }

    def upload_file_to_disk(self, disk_file_path, filename):
        href_response = self._get_upload_link(disk_file_path=disk_file_path)
        href = href_response.get("href", "")
        response = requests.put(url=href, data=open(filename, 'rb'))
        if response.status_code == 201:
            print("Success")

    def _get_upload_link(self, disk_file_path):
        upload_url = f"{self.ya_url}v1/disk/resources/upload"
        headers = self.get_headers()
        params = {"path": disk_file_path, "overwrite": "true"}
        response = requests.get(upload_url, headers=headers, params=params)
        return response.json()

if __name__ == '__main__':
    # Получить путь к загружаемому файлу и токен от пользователя
    token = ''
    uploader = YaUploader(token=token)
    result = uploader.upload_file_to_disk('Netology/test.txt', 'text.txt')

