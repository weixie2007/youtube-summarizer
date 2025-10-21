import os
import load_dotenv
import google.generativeai as genai
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# --- 1. SETUP & CONFIGURATION ---

load_dotenv.load_dotenv()

# Get the API keys from the environment
YOUTUBE_API_KEY = os.getenv("YOUTUBE_API_KEY")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# Configure the Gemini API
if GEMINI_API_KEY:
    genai.configure(api_key=GEMINI_API_KEY)
else:
    print("Error: GEMINI_API_KEY not found. Please set it in your .env file.")

# --- 2. STEP 1: YOUTUBE SEARCH FUNCTION ---

def search_youtube_videos(query, max_results=5):
    """
    Searches YouTube for videos matching a query.
    """
    if not YOUTUBE_API_KEY:
        print("Error: YOUTUBE_API_KEY not found.")
        return []

    try:
        youtube = build("youtube", "v3", developerKey=YOUTUBE_API_KEY)
        
        print(f"\nSearching YouTube for: '{query}'...")
        search_request = youtube.search().list(
            q=query,
            part="snippet",
            type="video",
            maxResults=max_results
        )
        
        response = search_request.execute()
        
        videos = []
        for item in response.get("items", []):
            video_title = item["snippet"]["title"]
            video_url = f"https://www.youtube.com/watch?v={item['id']['videoId']}"
            
            videos.append({
                "title": video_title,
                "url": video_url 
            })
            
        print(f"Found {len(videos)} videos.")
        return videos

    except HttpError as e:
        print(f"An HTTP error {e.code} occurred:\n{e.content}")
        return []
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return []

# --- 3. STEP 2: MULTIMODAL SUMMARIZATION FUNCTION ---

def summarize_video(video_url, title):
    """
    Summarizes the video by sending its URL directly 
    to the Gemini (multimodal) API.
    """
    print(f"\n--- Starting summary for: {title} ---")
    
    prompt = """
    You are an expert video summarizer. 
    Please provide a concise, one-paragraph summary of this video.
    Focus on the main topics and key takeaways.
    """
    
    try:
        model_name = "models/gemini-2.5-flash"
        
        if not genai.get_model(model_name):
            print(f"Error: Gemini model '{model_name}' not available.")
            return "Error: Model not available."
            
        model = genai.GenerativeModel(model_name)
        
        video_part = {"file_data": {"file_uri": video_url}}

        print("Generating summary...")
        response = model.generate_content([prompt, video_part])
        
        print("Summary successful.")
        return response.text
    
    except Exception as e:
        print(f"Multimodal summarization failed: {e}")
        return f"Error: Could not summarize video. Reason: {e}"


# --- 4. MAIN EXECUTION (UPDATED WITH USER PROMPTS) ---

if __name__ == "__main__":
    
    # Check for the required API keys
    if not (YOUTUBE_API_KEY and GEMINI_API_KEY):
        print("--- Missing API Keys ---")
        if not YOUTUBE_API_KEY: print("- YOUTUBE_API_KEY not in .env")
        if not GEMINI_API_KEY: print("- GEMINI_API_KEY not in .env")
    
    else:
        # **--- 1. GET USER INPUT ---**
        print("Welcome to the YouTube Summarizer!")
        
        # **Get search query from user**
        search_query = input("Please enter the topic you want to search for: ")
        
        # **Get number of videos from user and validate it**
        max_count = 0
        while max_count <= 0:
            try:
                max_count_str = input("How many videos would you like to summarize? (e.g., 3): ")
                max_count = int(max_count_str)
                if max_count <= 0:
                    print("Please enter a number greater than 0.")
            except ValueError:
                print("Invalid input. Please enter a whole number.")
        
        # **--- 2. CALL OUR SEARCH FUNCTION ---**
        video_list = search_youtube_videos(search_query, max_results=max_count)
        
        # **--- 3. LOOP AND SUMMARIZE ---**
        if video_list:
            print("\n--- Starting Summarization Process ---")
            
            results = []
            for video in video_list:
                summary = summarize_video(
                    video_url=video["url"],
                    title=video["title"]
                )
                
                results.append({
                    "title": video["title"],
                    "url": video["url"],
                    "summary": summary
                })

            # **--- 4. PRINT THE FINAL RESULTS ---**
            print("\n\n--- All Summaries Complete ---")
            for i, result in enumerate(results, 1):
                print(f"\n{i}. {result['title']}")
                print(f"   URL: {result['url']}")
                print(f"   Summary: {result['summary']}")