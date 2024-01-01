import requests

def download_image(url, file_name):
    response = requests.get(url)
    if response.status_code == 200:
        with open(file_name, 'wb') as file:
            file.write(response.content)
        print("Image downloaded successfully! thanks .a lot")
    else:
        print("Failed to download image. Please check the URL.gi")

# example usage
image_url = "https://example.com/yasaman.jpg"
file_name = "image.jpg"
download_image(image_url, file_name)
