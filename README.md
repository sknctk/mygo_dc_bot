# Discord Bot with Keyword Image Responses

This is a customizable Discord bot built with Python. It supports keyword-based image responses, fuzzy matching, random image selection, response cooldowns, and dynamic activity switching.

---
![Bot Preview](https://media.discordapp.net/attachments/498100518963380236/1322301927987351603/d642a525682c8298.jpg?ex=67706122&is=676f0fa2&hm=eeb55c1117f39661cb871c37e1718f17f40d01303efdc1746691c617b6d55481&=&format=webp&width=1193&height=671)

---
## Features

- **Keyword-Based Image Responses**: Responds with an image if a message contains a matching keyword.
- **Fuzzy Matching**: Matches keywords even if they partially match the message (e.g., threshold set to 50%).
- **Random Image Selection**: For multiple images matching a keyword, the bot randomly selects one to send.
- **Response Cooldown**: Limits how often the bot can respond to the same keyword to avoid spam (default: 10 seconds).
- **Dynamic Image Loading**: Automatically loads keywords and corresponding images from a specified folder.
- **Dynamic Activity Switching**: Periodically changes the bot's activity status between preconfigured options.

---

## Installation

### Prerequisites

- Python 3.8 or higher
- A Discord bot token (available from the [Discord Developer Portal](https://discord.com/developers/applications))

### Setup

1. Clone this repository:
   ```bash
   git clone https://github.com/sknctk/photo_discordbot.git
   cd your-repo-name
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Create a `.env` file in the project root and add the following:
   ```env
   DISCORD_TOKEN=your_discord_bot_token
   IMAGE_FOLDER=images
   LISTEN_CHANNEL_IDS=123456789012345678,987654321098765432
   ```

4. Prepare your `images/` folder with images named after keywords (e.g., `happy1.jpg`, `sad.jpg`, etc.).

---

## Usage

Run the bot using the following command:

```bash
python bot.py
```

### Example

If your `images/` folder contains:
```
images/
├── happy1.jpg
├── happy2.jpg
├── sad.jpg
```

And you send the message `I feel happy today` in the designated channel, the bot will respond with either `happy1.jpg` or `happy2.jpg`.

---

## Configuration

### Threshold

You can configure the keyword matching threshold in `keyword_responder.py`:

```python
keyword_responder = KeywordResponder(KEYWORD_TO_IMAGES, threshold=50)
```

### Cooldown

The cooldown (in seconds) can also be set during `KeywordResponder` initialization:

```python
keyword_responder = KeywordResponder(KEYWORD_TO_IMAGES, cooldown=10)
```

### Dynamic Activity Switching

The bot's activity can be dynamically switched between predefined statuses. Configure activities in `status_manager.py`:

```python
self.activities = [
    discord.Activity(type=discord.ActivityType.listening, name="春日影!"),
    discord.Activity(type=discord.ActivityType.watching, name="MyGO!!!!!")
]
```

The interval for switching can be adjusted in the `start_status_loop` method:

```python
await asyncio.sleep(60)  # Switch every 60 seconds
```

---

## File Structure

```
your-repo-name/
├── bot.py                 # Main bot file
├── config.py              # Configuration and dynamic image loading
├── discord_cog.py         # Bot event handling
├── keyword_responder.py   # Keyword matching logic
├── status_manager.py      # Dynamic activity switching logic
├── images/                # Folder containing images
├── .env                   # Environment variables
└── requirements.txt       # Python dependencies
```

---

## Dependencies

- [discord.py](https://pypi.org/project/discord.py/) - Discord API wrapper
- [fuzzywuzzy](https://pypi.org/project/fuzzywuzzy/) - For fuzzy keyword matching
- [python-dotenv](https://pypi.org/project/python-dotenv/) - For environment variable management
- [aiohttp](https://pypi.org/project/aiohttp/) - For asynchronous HTTP requests

Install them via:
```bash
pip install -r requirements.txt
```

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## Contributing

Contributions are welcome! Feel free to open issues or submit pull requests to improve the bot.

---
