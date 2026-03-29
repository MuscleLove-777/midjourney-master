"""Midjourney AI画像生成マスター - ブログ固有設定"""
import os
from pathlib import Path

BASE_DIR = Path(__file__).parent

BLOG_NAME = "Midjourney AI画像生成マスター"
BLOG_DESCRIPTION = "AI画像生成の最高峰Midjourneyの使い方・プロンプト術・v7最新情報を毎日更新。美しいAIアートを生み出すための完全ガイド。"
BLOG_URL = "https://musclelove-777.github.io/midjourney-master"
BLOG_TAGLINE = "Midjourneyで最高のAIアートを生み出すための日本語情報サイト"
BLOG_LANGUAGE = "ja"

GITHUB_REPO = "MuscleLove-777/midjourney-master"
GITHUB_BRANCH = "gh-pages"
GITHUB_TOKEN = os.environ.get("GITHUB_TOKEN", "")

OUTPUT_DIR = BASE_DIR / "output"
ARTICLES_DIR = OUTPUT_DIR / "articles"
SITE_DIR = OUTPUT_DIR / "site"
TOPICS_DIR = OUTPUT_DIR / "topics"

TARGET_CATEGORIES = [
    "Midjourney 使い方",
    "Midjourney 料金・プラン",
    "Midjourney v7",
    "Midjourney プロンプト術",
    "Midjourney vs Flux",
    "AI画像生成テクニック",
    "AI画像生成比較",
    "Midjourney 活用事例",
]

THEME = {
    "primary": "#ffffff",
    "accent": "#5865F2",
    "gradient_start": "#232338",
    "gradient_end": "#5865F2",
    "dark_bg": "#1a1a2e",
    "dark_surface": "#232338",
    "light_bg": "#f5f5ff",
    "light_surface": "#ffffff",
}

MAX_ARTICLE_LENGTH = 2000
ARTICLES_PER_DAY = 3
SCHEDULE_HOURS = [7, 12, 19]

GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY", "")
GEMINI_MODEL = "gemini-2.5-flash"

ENABLE_SEO_OPTIMIZATION = True
MIN_SEO_SCORE = 75
MIN_KEYWORD_DENSITY = 1.0
MAX_KEYWORD_DENSITY = 3.0
META_DESCRIPTION_LENGTH = 120
ENABLE_INTERNAL_LINKS = True

AFFILIATE_LINKS = {
    "Midjourney": [
        {"service": "Midjourney", "url": "https://www.midjourney.com", "description": "Midjourneyに登録する"},
    ],
    "AI画像生成ツール": [
        {"service": "Stable Diffusion", "url": "https://stability.ai", "description": "Stable Diffusionを試す"},
        {"service": "DALL-E", "url": "https://openai.com/dall-e-3", "description": "DALL-E 3を試す"},
    ],
    "オンライン講座": [
        {"service": "Udemy", "url": "https://www.udemy.com", "description": "UdemyでAI画像生成講座を探す"},
        {"service": "Skillshare", "url": "https://www.skillshare.com", "description": "SkillshareでMidjourneyコースを探す"},
    ],
    "書籍": [
        {"service": "Amazon", "url": "https://www.amazon.co.jp", "description": "AmazonでAI画像生成関連書籍を探す"},
        {"service": "楽天ブックス", "url": "https://www.rakuten.co.jp", "description": "楽天でAI画像生成関連書籍を探す"},
    ],
    "クリエイターツール": [
        {"service": "Adobe Firefly", "url": "https://firefly.adobe.com", "description": "Adobe Fireflyを試す"},
        {"service": "Canva", "url": "https://www.canva.com", "description": "CanvaでAIデザインを始める"},
    ],
}
AFFILIATE_TAG = "musclelove07-22"

ADSENSE_CLIENT_ID = os.environ.get("ADSENSE_CLIENT_ID", "")
ADSENSE_ENABLED = bool(ADSENSE_CLIENT_ID)
DASHBOARD_PORT = 8100
