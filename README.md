# 🤖 Discord Ticket Bot

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)  
[![Python](https://img.shields.io/badge/Python-3.11+-blue?logo=python&logoColor=white)](https://www.python.org/)  
[![Made by Reverse](https://img.shields.io/badge/Made%20by-Reverse-%23ff69b4)](https://github.com/reversepy)  
[![Discord](https://img.shields.io/discord/1376577777524015105?label=Join%20Discord&logo=discord&color=5865F2)](https://discord.gg/nitrogang)  

A simple and clean ticket bot for your server. Made by Reverse.

## 💡 Features
- `/ticket` command opens a private support channel
- Only the user and support role can see the ticket
- `!close` to delete the ticket
- Status shows: `made by reverse | v.1.0`

## ⚙️ Setup
1. Clone the repo
2. Install the requirements:
   ```bash
   pip install -r requirements.txt
   ```
3. Edit `config.json` with your token, server ID, role ID, etc.
4. Run the bot:
   ```bash
   python bot.py
   ```

## 🧪 Example
- User runs `/ticket`
- Bot creates a channel like `#ticket-reverse`
- Support team joins and chats with user
- User types `!close`
- Channel gets deleted

## 📄 License
MIT License © 2025 Reverse
