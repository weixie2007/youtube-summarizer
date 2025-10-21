# YouTube Video Summarizer Project

This project is a Python application that searches for YouTube videos based on a query, retrieves their content, and generates both text and audio summaries.

## Features

* **YouTube Search**: Uses the YouTube Data API v3 to find a list of relevant videos.
* **Multimodal Summarization**: Uses the Google Gemini API to "watch" and "listen" to videos directly to create a summary.
* **Transcript Fallback**: If a video is too long for the multimodal API, it attempts to summarize its text transcript instead.
* **Text Summary**: Provides a concise text summary of each video.
* **Audio Summary**: (Planned) Provides a podcast-style audio version of the summary using a Text-to-Speech API.

## Setup

1.  **Clone this repository** (or download the files).
2.  **Install dependencies**:
    ```bash
    pip install google-api-python-client google-generativeai python-dotenv
    ```
3.  **Get API Keys**:
    * **YouTube Data API**: Follow the [Google Cloud setup guide](https://console.cloud.google.com/apis/dashboard) to create a project and get an API key. Enable the "YouTube Data API v3".
    * **Google Gemini API**: Get your API key from [Google AI Studio](https://aistudio.google.com/app/apikey).
4.  **Create `.env` file**:
    * Create a file named `.env` in the root folder.
    * Add your API keys:
        ```
        YOUTUBE_API_KEY="YOUR_YOUTUBE_API_KEY_HERE"
        GEMINI_API_KEY="YOUR_GEMINI_API_KEY_HERE"
        ```

## Usage

Run the main application from your terminal:

```bash
python main.py