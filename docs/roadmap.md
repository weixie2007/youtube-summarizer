# Development Roadmap

This document outlines the development steps taken to build the application.

### ✅ Step 1: YouTube Search (YouTube Data API)

* [X] Set up Google Cloud project and get a YouTube Data API v3 key.
* [X] Write Python function to search for videos by a query.
* [X] Function returns a list of video URLs.

### ✅ Step 2: Multimodal Summarization (Gemini API)

* [X] Set up Google Gemini API key.
* [X] Implement the **Multimodal Flow**: Write a function that sends a YouTube URL directly to the Gemini API (`gemini-2.5-flash`) for summarization.
* [X] Add error handling for common failures (e.g., video is too long).

### ✅ Step 3: Final Application

* [X] Tie all functions together in `main.py`.
* [X] Add user prompts to input the search query and number of videos.
* [X] Loop through search results, summarize each one, and print the final list (Title, URL, and Summary).
* [X] **(Removed)** All audio-related features were removed to simplify the application.