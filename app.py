import os
import speech_recognition as sr


def convert_audio_to_text(audio_file_path):
    recognizer = sr.Recognizer()

    if not os.path.exists(audio_file_path):
        print(f"Error: The file '{audio_file_path}' was not found.")
        return None

    print(f"Processing audio file: {audio_file_path}...")

    with sr.AudioFile(audio_file_path) as source:
        recognizer.adjust_for_ambient_noise(source, duration=0.5)
        audio_data = recognizer.record(source)

    try:
        # Converts audio using Google's free speech recognition web API
        text = recognizer.recognize_google(audio_data)
        print("\n--- Transcription Successful ---")
        return text

    except sr.UnknownValueError:
        print("\nError: Could not understand the audio clearly.")
        return None
    except sr.RequestError as e:
        print(f"\nError: Could not connect to internet service; {e}")
        return None


if __name__ == "__main__":
    # Ensure you have a 'sample.wav' file in this same folder to test it!
    audio_file = "sample.wav"

    if not os.path.exists(audio_file):
        print(
            f"Please place a valid audio file named '{audio_file}' in this folder."
        )
    else:
        transcription = convert_audio_to_text(audio_file)
        if transcription:
            print("\nResult:")
            print(transcription)

            # Saves the text automatically to a file
            with open("transcription_result.txt", "w") as f:
                f.write(transcription)
            print("\nSaved to 'transcription_result.txt'")