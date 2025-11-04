# Anime Style Transfer Telegram Bot

A Telegram bot that transforms photos into different anime art styles using GAN models. The bot can convert your images into the style of famous anime directors: Hosoda Mamoru, Kon Satoshi, Miyazaki Hayao, and Shinkai Makoto.

## Features

- Image style transfer using pre-trained GAN models
- Support for multiple anime director styles
- Automatic image resizing while preserving aspect ratio
- In-memory image processing (no temporary files needed)
- User-friendly Telegram interface

## Project Structure

```
neural_network_imagechangestyle_tgbot/
├── bot/
│   ├── handlers.py      # Telegram bot command & message handlers
│   └── keyboard.py      # Telegram bot keyboard layouts
├── models/
│   ├── Transformer.py   # Neural network architecture
│   └── test.py          # Image processing and model handling
├── .env                # Environment variables (bot token)
├── requirements.txt    # Project dependencies
└── tg_bot_start.py     # Bot initialization and startup
```



1. Clone:
```
 git clone https://github.com/MrXanter/neural_network_imagechangestyle_tgbot
```

2. Install dependencies:

Intiate virtual environment:
```bash
python -m venv .venv
```

Activate virtual environment for Linux:
```
source .venv/bin/activate
```

Activate virtual environment for Windows:
```
.venv/bin/activate
```

Install required packages:
```bash
pip install -r requirements.txt
```

3. Create a `.env` file with your Telegram bot token:
```
BOT_TOKEN=your_bot_token_here
```

4. Run the bot:
```bash
python tg_bot_start.py
```

## Docker (Linux/amd64)
```
docker pull mrxanter/telegram_bot:latest
```
When creating a container, mention a BOT_TOKEN environment variable with your telegram API token.


Or Run with the BOT_TOKEN environment variable:
```
docker run -e BOT_TOKEN=your_bot_token_here mrxanter/telegram_bot:latest
```

## Docker(Windows Users)
```
git clone https://github.com/MrXanter/neural_network_imagechangestyle_tgbot
```
Create .env file, write:
```
BOT_TOKEN=your_telegram_API_token_here
```
Then, create docker image:
```
docker build . -t telegram_bot
```
When creating a container, mention a BOT_TOKEN environment variable with your telegram API token.


## How It Works

### Neural Network (`Transformer.py`)
- Implements a GAN architecture for style transfer
- Uses residual blocks and instance normalization
- Processes images through multiple convolutional layers

### Image Processing (`test.py`)
- Handles image loading and preprocessing
- Manages multiple style models
- Converts images between RGB and BGR color spaces
- Applies neural style transfer

### Bot Interface (`handlers.py`)
- `/start` - Initiates bot interaction
- `send the image` - Prompts for style selection
- Style selection using inline keyboard
- Image processing and result delivery
- `/back` - Returns to main menu

### Keyboard Layout (`keyboard.py`)
- Main menu with "send the image" button
- Style selection inline keyboard
- Back button for navigation

## Usage

1. Start the bot with `/start`
2. Click "send the image" button
3. Select desired anime style
4. Send your photo
5. Wait for the processed image
6. Use `/back` to return to main menu

## Notes

- Best results are achieved with nature photos
- Processing time depends on image size and server load
- GPU acceleration is supported if available
- original directory of test.py - https://github.com/Yijunmaverick/CartoonGAN-Test-Pytorch-Torch
- HuggingFace with neural models - https://huggingface.co/akiyamasho/AnimeBackgroundGAN-Shinkai