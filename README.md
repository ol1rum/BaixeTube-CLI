<div align="center">
  <a href="README.md">🇺🇸 English</a> | <a href="README.pt-br.md">🇧🇷 Português</a>
</div>

<br />

# 🎥 BaixeTube CLI (v2.0)

> A modern, interactive Command Line Interface (CLI) tool for downloading YouTube videos and playlists, built with Python and a robust architecture.

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![yt-dlp](https://img.shields.io/badge/Core-yt--dlp-red)
![License](https://img.shields.io/badge/License-MIT-green)

## 🧠 About the Project

**BaixeTube** is a complete application designed to demonstrate advanced software engineering concepts, focused on media download automation. Unlike simple scripts, it implements:

* **Object-Oriented Architecture (OOP):** Clear separation between Interface (CLI), Business Logic (Downloader), and Persistence (ConfigManager).
* **Interactive Interface (TUI):** Navigable menus using keyboard arrows (powered by `questionary`), eliminating the need for typing numbers or complex commands.
* **Data Persistence:** Saves user preferences (download path, quality, audio format) in a JSON file for seamless usage across sessions.

## ✨ Features

- [x] **Smart Downloads:** Support for Video (MP4) and Audio (MP3/M4A/WAV).
- [x] **Playlists:** Automatically detects playlists and organizes downloads into named subfolders.
- [x] **Metadata:** Automatically embeds thumbnails (cover art) and tags into audio files.
- [x] **Selectable Quality:** From 4K to 480p (data saver).
- [x] **Persistent Settings:** Remembers your download path and preferences.

## 🛠️ Tech Stack

* **Python 3.x**
* **yt-dlp:** The most robust and up-to-date download engine available.
* **Questionary:** For creating professional, interactive CLI menus.
* **Mutagen:** For handling audio metadata.
* **Pathlib:** For cross-platform file path manipulation (Windows/Linux/Mac).

## ⚙️ Installation and Setup

### Prerequisites
For the download engine to work correctly, you need two tools installed on your system and accessible via the terminal (PATH):

1.  **FFmpeg:** Essential for converting and merging video/audio streams.
2.  **Deno (or Node.js):** Runtime required for `yt-dlp` to bypass YouTube's latest protections.

### Step 1: Tool Installation (Windows)
The recommended way is using **Winget** in PowerShell:

    winget install Gyan.FFmpeg
    winget install DenoLand.Deno

*Restart your terminal after installation.*

### Step 2: Project Installation

1.  Clone this repository:

        git clone https://github.com/ol1rum/BaixeTube-CLI.git
        cd baixetube-cli

2.  Create a virtual environment (recommended):

        python -m venv venv
        .\venv\Scripts\activate  # On Windows
        # source venv/bin/activate  # On Linux/Mac

3.  Install dependencies:

        pip install -r requirements.txt

## 🚀 How to Use

Run the main file from the project root:

    python src/main.py

* **Navigation:** Use `↑` and `↓` arrow keys to navigate menus.
* **Selection:** Press `Enter` to confirm.
* **Configuration:** Access the settings menu on the first run to define your preferred download folder.

## ⚠️ Legal Disclaimer

This software was developed strictly for **educational purposes** (studying automation, stream manipulation, and CLI interfaces).
The user is solely responsible for complying with YouTube's Terms of Service and copyright laws. Do not use this tool for piracy or illegal distribution of content.

---
Developed by Murilo