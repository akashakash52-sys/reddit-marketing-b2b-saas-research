from youtube_transcript_api import YouTubeTranscriptApi

video_id = input("Enter YouTube Video ID: ")

try:
    ytt_api = YouTubeTranscriptApi()

    transcript = ytt_api.fetch(video_id)

    with open("transcript.txt", "w", encoding="utf-8") as f:
        for line in transcript:
            f.write(line.text + "\n")

    print("Transcript saved successfully.")

except Exception as e:
    print("Error:", e)