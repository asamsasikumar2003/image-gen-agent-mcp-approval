import requests

class ImageAgent:
    def __init__(self, mcp_url):
        self.mcp_url = mcp_url

    def generate_image(self, prompt):
        response = requests.post(self.mcp_url, json={"prompt": prompt})
        return response.json()

    def generate_bulk_images(self, prompt, count):
        responses = []
        for _ in range(count):
            responses.append(self.generate_image(prompt))
        return responses