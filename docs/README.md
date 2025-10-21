# YouTube Video Summarizer Project

This project is a Python application that searches for YouTube videos based on a query, retrieves their content, and generates text summaries.

## Features

* **YouTube Search**: Uses the YouTube Data API v3 to find a list of relevant videos.
* **Multimodal Summarization**: Uses the Google Gemini API (`gemini-2.5-flash`) to "watch" and "listen" to videos directly to create a summary.
* **Text Summary**: Provides a concise text summary of each video.
* **Interactive Prompts**: Asks the user for the search topic and the number of videos to summarize.

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