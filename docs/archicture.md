# Application Architecture

This document details the technical architecture for the YouTube Summarizer. The application operates as a multi-step pipeline.

## Core Components

1.  **Search (YouTube Data API)**: A module that takes a text query and returns a list of YouTube video URLs.
2.  **Summarizer (Google Gemini API)**: A module that takes a video URL and returns a text summary.
3.  **Main Application**: The main script (`main.py`) that orchestrates these components.

## Summarization Flow (Multimodal-Only)

We use a direct multimodal-only strategy for summarization.

1.  **Input**: A public YouTube video URL (e.g., `https://www.youtube.com/watch?v=...`)
2.  **API Call**: The URL is sent directly to the **Google Gemini API** (e.g., `gemini-2.5-flash`) with a prompt like, "Summarize this video."
3.  **Process**: The multimodal model analyzes the video frames, audio, and speech directly.
4.  **Output**: A high-quality text summary.

### Limitations

* This approach will fail for videos that are private or unlisted.
* This approach will also fail if a video's duration exceeds the API's processing limit (e.g., ~45 minutes for `gemini-2.5-flash`).