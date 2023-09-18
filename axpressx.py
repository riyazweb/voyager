from bs4 import BeautifulSoup
import xml.etree.ElementTree as ET
import requests
from moviepy.video.VideoClip import TextClip
from moviepy.video.tools.subtitles import SubtitlesClip

from bing_image_downloader import downloader
from moviepy.editor import *
from moviepy.video.io.VideoFileClip import VideoFileClip
from moviepy.audio.fx.all import volumex

from moviepy.audio.io.AudioFileClip import AudioFileClip
from moviepy.video.VideoClip import ColorClip
from moviepy.video.compositing.CompositeVideoClip import CompositeVideoClip
from moviepy.video.fx.all import resize
import moviepy.editor as mp

import os
from whisper.utils import write_srt
import whisper
import openai
import re

import os
openai.api_key = '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'

# Define the URL of the XML file
url = "https://pib.gov.in/RssMain.aspx?ModId=6&Lang=1&Regid=3"

# Send an HTTP GET request to the URL and get the response
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the XML content
    root = ET.fromstring(response.content)

    # Find all 'link' elements under 'item'
    link_elements = root.findall(".//item/link")

    # Check if there are at least two 'link' elements
    if len(link_elements) >= 1:
        # Extract the URL from the second 'link' element
        second_link_element = link_elements[6]  # Index 1 for the second element
        second_link = second_link_element.text
        print(second_link)
        # Send an HTTP GET request to the second link and get the content
        link_response = requests.get(second_link)

        # Check if the request to the second link was successful
        if link_response.status_code == 200:
            # Parse the HTML content using BeautifulSoup
            soup = BeautifulSoup(link_response.text, 'html.parser')

            # Extract the text from the HTML
            text_content = soup.get_text()

            # Remove extra spaces and gaps
            content = ' '.join(text_content.split())

            # Save the cleaned text content to a text file
            with open("content.txt", "w", encoding="utf-8") as file:
                file.write(content)
            print(f"Cleaned content from the second link saved as 'content.txt'")
        else:
            print("Failed to fetch the content from the second link.")
    else:
        print("There are not enough 'link' elements in the XML.")
else:
    print("Failed to fetch the XML from the URL.")

# from claude_api import Client
"""
Reverse engineering of Google Bard
"""
# Import either speak or speak2 from the custom_voice modules based on the user input


def main():

    print("Welcome to  Chat!")

    while True:
        top = input("images:")
        import os
        import requests
        from bs4 import BeautifulSoup
        from urllib.parse import urlparse, urljoin

        # URL of the webpage containing the images
        url = f"{second_link}"

        # Send an HTTP GET request to the URL
        response = requests.get(url)

        # Check if the request was successful
        if response.status_code == 200:
            # Parse the HTML content of the page
            soup = BeautifulSoup(response.content, "html.parser")
            
            # Find all image tags on the page
            img_tags = soup.find_all("img")
            
            # Create a directory to save the images
            os.makedirs(f"{top}", exist_ok=True)
            
            # Download each image whose file name starts with "image"
            for img_tag in img_tags:
                img_url = img_tag.get("src")
                if img_url:
                    img_url = urljoin(url, img_url)  # Make sure the URL is absolute
                    img_name = os.path.basename(urlparse(img_url).path)
                    
                    # Check if the file name starts with "image"
                    if img_name.startswith("image"):
                        img_path = os.path.join(f"{top}", img_name)
                        
                        # Send an HTTP GET request to the image URL
                        img_response = requests.get(img_url)
                        
                        # Check if the request was successful
                        if img_response.status_code == 200:
                            # Save the image to the directory
                            with open(img_path, "wb") as img_file:
                                img_file.write(img_response.content)
                            print(f"Downloaded: {img_path}")
                        else:
                            print(f"Failed to download: {img_url}")
        else:
            print(f"Failed to retrieve the webpage: {url}")

        # cop = input("You: ")

    # Read the content from the text file
        with open('content.txt', 'r', encoding='utf-8') as file:
            content = file.read()
        # Make a request to the GPT-3.5 Turbo model
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            # model="davinci-002",
            messages=[
                {"role": "user", "content": f"summarize this text in 50 words: {content}"}
            ]
        )

        OP = response['choices'][0]['message']['content']
        OP = OP.replace('"', '')

        print(OP)

        from feautures.custom_voice import speak

        # option = 1

        fish = top
        speak(OP)
        # limit = 8

        # n = input("Enter 'n' (y/n): ")
        # y = n.lower() == 'y'

        # cop = f"{OP}"
        # if y:
        #     cop = cop.split('\n', 1)[1]
        # cp = re.sub(r'[^\w\s]', '', cop)

        # from elevenlabs import generate, play, set_api_key, save

        # voice = generate(
        #     text=f"{cop}",
        #     voice="Bella",
        #     model="eleven_multilingual_v2"
        # )
        # save(voice,'data.mp3')
        # # Set the dimensions of the video

        VIDEO_WIDTH = 854
        VIDEO_HEIGHT = 480

        # Set the duration of each image

        # Set the path to the music file
        MUSIC_PATH = "data.mp3"
        # Replace spaces in title with hyphens
        # Download images of cats
        # Download images of cats
        # from pygoogle_image import image as pi

        # # Set the directory path to the folder containing the images
        # import PIL

        # IMAGE_PATHS = []
        # if option == 1:
        #     for element in top.split(','):

        #         pi.download(keywords=f'{element}', limit=limit)

        #         # Replace spaces in title with hyphens
        #         dog = element.replace(" ", "_")
        #         folder_path = f"images/{dog}/"
        #         if not os.path.exists(folder_path):
        #             continue
        #             # Get the file paths to all the images in the folder except the first two
        #         for f in os.listdir(folder_path):
        #             if f.endswith(('.jpg', '.jpeg', '.png', '.gif')):
        #                 image_path = os.path.join(folder_path, f)
        #                 with PIL.Image.open(image_path) as img:
        #                     width, height = img.size
        #                     if width > 80 and height > 36:
        #                         IMAGE_PATHS.append(image_path)

        # elif option == 2:
        #     for element in top.split(','):

        #         downloader.download(f"{element}", limit=limit, output_dir="images",
        #                             adult_filter_off=True, force_replace=False)

        #         folder_path = f"images/{element}/"
        #         if not os.path.exists(folder_path):
        #             continue
        #             # Get the file paths to all the images in the folder
        #         image_paths = [os.path.join(folder_path, f) for f in os.listdir(
        #             folder_path) if f.endswith(('.jpg', '.png', '.jpeg'))]
        #         # Add the image paths to the list
        #         IMAGE_PATHS += image_paths
        # else:
        #     print("Invalid option entered. Please enter either 1 or 2.")

        import os

        # Change this to your actual image directory
        IMAGE_DIR = f'{top}'

        # Get a list of image files in the specified directory
        IMAGE_PATHS = [os.path.join(IMAGE_DIR, filename) for filename in os.listdir(IMAGE_DIR) if filename.startswith('image') and filename.endswith(('.jpg', '.png', '.jpeg'))]

        num_images = len(IMAGE_PATHS)
        audio_clip = AudioFileClip(MUSIC_PATH)
        audio_duration = audio_clip.duration
        IMAGE_DURATION = audio_duration / num_images

        # Create a list of video clips
        # Set the blur amount
        # Create a list of video clips
        video_clips = []
        for image_path in IMAGE_PATHS:
            # Create an image clip for the current image
            image_clip = ImageClip(image_path)
            # Calculate the new height based on the aspect ratio of the original image
            new_height = int(
                VIDEO_WIDTH / image_clip.w * image_clip.h)
            # Resize the image to fit the video dimensions without black bars
            image_clip = image_clip.resize(
                (VIDEO_WIDTH, new_height))
            image_clip = image_clip.set_position(
                ("center", "center"))
            image_clip = image_clip.set_duration(IMAGE_DURATION)

            # Create a black background clip
            bg_clip = ColorClip(
                (VIDEO_WIDTH, VIDEO_HEIGHT), color=(0, 0, 0))
            bg_clip = bg_clip.set_duration(IMAGE_DURATION)

            # Combine the image clip with the background clip
            video_clip = CompositeVideoClip([bg_clip, image_clip])

            # Append the video clip to the list
            video_clips.append(video_clip)

            # Concatenate the video clips in a loop until the audio ends

        # Concatenate the video clips in a loop until the audio ends
         # Concatenate the video clips in a loop until the audio ends
        audio_clip = AudioFileClip(MUSIC_PATH)
        audio_duration = audio_clip.duration
        final_clip = concatenate_videoclips(
            video_clips, method="compose", bg_color=(0, 0, 0))
        final_clip = final_clip.set_duration(
            audio_duration).loop(duration=audio_duration)

        # Set the audio file for the final video clip
        final_clip = final_clip.set_audio(
            audio_clip.set_duration(final_clip.duration))

        # Set the audio file for the final video clip
        # Set the desired output file name
        filename = f"{fish}.mp4"

        # Check if the file already exists
        if os.path.isfile(filename):
            # If it does, add a number to the filename to create a unique name
            basename, extension = os.path.splitext(filename)
            i = 1
            while os.path.isfile(f"{basename}_{i}{extension}"):
                i += 1
            filename = f"{basename}_{i}{extension}"

            # Write the video file with the updated filename
        final_clip.write_videofile(filename, fps=30)

        FONT = "Muroslant.otf"
        input_path = f"{fish}.mp4"
        print("Transcribing audio...")
        model = whisper.load_model("base")
        result = model.transcribe(input_path, verbose=False)

        subtitle_path = os.path.splitext(input_path)[0] + ".srt"
        with open(subtitle_path, "w", encoding="utf-8") as srt_file:
            write_srt(result["segments"], file=srt_file)

        print("Generating subtitles...")
        orig_video = VideoFileClip(input_path)

        def generator(txt): return TextClip(txt,
                                            font=FONT if FONT else "Courier",
                                            fontsize=38,
                                            color='white',
                                            size=orig_video.size,
                                            method='caption',
                                            align='center',)
        subs = SubtitlesClip(subtitle_path, generator)

        print("Compositing final video...")
        final = CompositeVideoClip(
            [orig_video, subs.set_position('center', 'middle')])
        final_path = os.path.splitext(input_path)[0] + "_final.mp4"
        final.write_videofile(final_path, fps=orig_video.fps)
        file_names = [f"{filename}"]
        for file_name in file_names:
            if os.path.exists(file_name):
                os.remove(file_name)
                print(f"File '{file_name}' deleted successfully.")
            else:
                print(f"File '{file_name}' does not exist.")


if __name__ == "__main__":
    main()
