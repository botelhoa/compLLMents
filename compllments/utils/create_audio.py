 
import os
import zipfile
from urllib import request
from pydub import AudioSegment


def download_mozilla_data(config: dict):

    file1_save_name = os.path.join("data", config["first_url"].split("/")[-1].split("?")[0])
    file2_save_name = os.path.join("data", config["second_url"].split("/")[-1].split("?")[0])

    if os.path.isfile(file1_save_name):
        print("Found", file1_save_name, ", skipping download.")
    else:
        print("Downloading", file1_save_name, "...")
        request.urlretrieve(config["first_url"], file1_save_name)

    if os.path.isfile(file2_save_name):
        print("Found", file2_save_name, ", skipping download.")
    else:
        print("Downloading", file2_save_name, "...")
        request.urlretrieve(config["second_url"], file2_save_name)


    audio_directory = file1_save_name.split(".zip")[0]
    if not os.path.isdir(audio_directory):
        with zipfile.ZipFile(file1_save_name, 'r') as zip_ref:
            zip_ref.extractall("data")


    silence = AudioSegment.silent(duration=500)
    combined_audio = None

    for file in os.listdir(audio_directory):

        file_path = os.path.join(audio_directory, file)
        sound = AudioSegment.from_mp3(file_path) + silence

        if combined_audio:
            combined_audio += sound
        else:
            combined_audio = sound


    save_path = os.path.join("data", "combined_personal_audio.wav")
    combined_audio.export(save_path, format="wav")