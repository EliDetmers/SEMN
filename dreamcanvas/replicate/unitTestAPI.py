import unittest
import requests

class TestFlaskAPI(unittest.TestCase):
    def test_upload_and_train(self):
        files = {'zip_file': open('/path/to/your/zip/file.zip', 'rb')}
        response = requests.post('http://127.0.0.1:5000/upload_and_train', files=files)
        self.assertEqual(response.status_code, 200)

    def test_generate_image(self):
        data = {'prompt': 'your_prompt', 'lora_url': 'your_lora_url'}
        response = requests.post('http://127.0.0.1:5000/generate_image', data=data)
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()
