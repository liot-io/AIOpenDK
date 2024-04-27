import os
import youtube_dl

def validate_youtube_url(url):
    """Validate if the given URL is a potential YouTube URL."""
    if "youtube.com/watch?v=" in url or "youtu.be/" in url and "http" or "https":
        return True
    return False

def save_subtitles(video_url, output_dir):
    """Download subtitles as .srt and convert them to .md, then save."""
    ydl_opts = {
        'format': 'best',
        'quiet': True,
        'subtitleslangs': ['en'],
        'writeautomaticsub': True,
        'skip_download': True,
        'outtmpl': os.path.join(output_dir, '%(id)s.%(ext)s'),
        'postprocessors': [{
            'key': 'FFmpegSubtitlesConvertor',
            'format': 'srt',
        }]
    }
    
    try:
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([video_url])
            info_dict = ydl.extract_info(video_url, download=False)
            subtitle_file_path = os.path.join(output_dir, f"{info_dict['id']}.en.srt")
            if os.path.exists(subtitle_file_path):
                return subtitle_file_path
    except Exception as e:
        print(f"Error: {e}")

    return None

def convert_srt_to_md(srt_path):
    """Convert subtitles from SRT format to Markdown format."""
    try:
        with open(srt_path, 'r') as file:
            content = file.readlines()

        markdown_content = []
        for line in content:
            if line.strip().isdigit() or '-->' in line:
                continue
            markdown_content.append(line.strip() + '  \n')  # Markdown newline
        
        md_path = srt_path.replace('.srt', '.md')
        with open(md_path, 'w') as md_file:
            md_file.writelines(markdown_content)
        return md_path
    except Exception as e:
        print(f"Error: {e}")
        return None

def main():
    output_dir = 'processed_yt_videos'
    os.makedirs(output_dir, exist_ok=True)
    
    video_url = input("Enter a YouTube video URL: ")
    if validate_youtube_url(video_url):
        print("Success")
        srt_path = save_subtitles(video_url, output_dir)
        if srt_path and convert_srt_to_md(srt_path):
            print(f"Markdown file is created successfully at {srt_path.replace('.srt', '.md')}")
        else:
            print("Failed to convert and save YouTube video.")
    else:
        print("Failed to process input URL. Try another link.")

if __name__ == "__main__":
    main()
