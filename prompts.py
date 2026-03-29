"""Midjourney AI画像生成マスター - プロンプト定義

Midjourney特化ブログ用のプロンプトを一元管理する。
JSON-LD構造化データ（BlogPosting / FAQPage / BreadcrumbList）対応。
"""

# ペルソナ設定
PERSONA = (
    "あなたはMidjourneyとAI画像生成の日本語エキスパートです。"
    "プロンプトエンジニアリング・スタイル制御・パラメータ調整に精通し、"
    "初心者からプロクリエイターまで幅広い読者に実践的な情報を届けるプロのテックライターです。"
    "Midjourneyの最新バージョン（v7）や競合ツール（Flux、DALL-E、Stable Diffusion）"
    "との比較も客観的に行えます。"
    "商用利用・著作権・ライセンスの知識も豊富です。"
)

# 記事フォーマット指示
ARTICLE_FORMAT = """
【記事構成（必ずこの順序で書くこと）】

## この記事でわかること
- ポイント1（具体的なベネフィット）
- ポイント2
- ポイント3

## 結論（先に結論を述べる）
（読者が最も知りたい答えを最初に提示）

## 本題（H2で3〜5セクション）
（具体的な手順・プロンプト例。実際のプロンプトテンプレートを含める）

## プロンプト実例集
（コピペで使えるプロンプトテンプレートを3〜5個紹介）

## 他のAI画像生成ツールとの比較
（Flux / DALL-E / Stable Diffusion / Adobe Firefly との違いを表形式で整理）

## よくある質問（FAQ）
### Q1: （よくある質問1）
A1: （回答1）

### Q2: （よくある質問2）
A2: （回答2）

### Q3: （よくある質問3）
A3: （回答3）

## まとめ
（要点整理と次のアクション提案）
"""

# カテゴリ別SEOキーワードヒント
CATEGORY_PROMPTS = {
    "Midjourney 使い方": "Midjourney 使い方、Midjourney 始め方、Midjourney Discord、Midjourney Web版、Midjourney 初心者",
    "Midjourney 料金・プラン": "Midjourney 料金、Midjourney 無料、Midjourney プラン比較、Midjourney Basic Pro、Midjourney 月額",
    "Midjourney v7": "Midjourney v7、Midjourney v7 新機能、Midjourney v7 使い方、Midjourney 最新バージョン、v7 プロンプト",
    "Midjourney プロンプト術": "Midjourney プロンプト、Midjourney プロンプト コツ、Midjourney プロンプト テンプレート、呪文、プロンプトエンジニアリング",
    "Midjourney vs Flux": "Midjourney Flux 比較、Midjourney vs Flux、AI画像生成 比較 2026、どっちがいい、Flux.1",
    "AI画像生成テクニック": "AI画像生成 テクニック、アスペクト比、スタイル指定、ネガティブプロンプト、--ar --stylize --chaos",
    "AI画像生成比較": "AI画像生成 比較、Midjourney DALL-E 比較、Stable Diffusion 比較、Adobe Firefly 比較、最強 AI画像生成",
    "Midjourney 活用事例": "Midjourney ビジネス活用、Midjourney 商用利用、Midjourney デザイン、Midjourney イラスト、副業",
}

# ニュースソース
NEWS_SOURCES = [
    "Midjourney公式 (https://www.midjourney.com/)",
    "Midjourney Discord (https://discord.gg/midjourney)",
    "The Verge (https://www.theverge.com/ai-artificial-intelligence)",
    "Ars Technica (https://arstechnica.com/ai/)",
    "AI画像生成まとめ (https://www.reddit.com/r/midjourney/)",
]

# FAQ構造化データの有効化
FAQ_SCHEMA_ENABLED = True

# キーワード選定用の追加プロンプト
KEYWORD_PROMPT_EXTRA = (
    "MidjourneyとAI画像生成に関するキーワードを選んでください。\n"
    "日本のユーザーが検索しそうな実用的なキーワードを意識してください。\n"
    "「Midjourney 使い方」「Midjourney プロンプト」「AI画像生成 比較」のような、\n"
    "検索ボリュームが見込めるキーワードを優先してください。"
)


def build_keyword_prompt(config):
    """キーワード選定プロンプトを構築する"""
    categories_text = "\n".join(f"- {cat}" for cat in config.TARGET_CATEGORIES)
    category_hints = "\n".join(
        f"- {cat}: {hints}" for cat, hints in CATEGORY_PROMPTS.items()
    )
    return (
        f"{PERSONA}\n\n"
        "Midjourney AI画像生成マスターブログ用のキーワードを選定してください。\n\n"
        f"{KEYWORD_PROMPT_EXTRA}\n\n"
        f"カテゴリ一覧:\n{categories_text}\n\n"
        f"カテゴリ別キーワードヒント:\n{category_hints}\n\n"
        "以下の形式でJSON形式のみで回答してください（説明不要）:\n"
        '{"category": "カテゴリ名", "keyword": "キーワード"}'
    )


def build_article_prompt(keyword, category, config):
    """Midjourney特化記事生成プロンプトを構築する"""
    category_hints = CATEGORY_PROMPTS.get(category, "")
    news_sources_text = "\n".join(f"- {src}" for src in NEWS_SOURCES)

    return f"""{PERSONA}

以下のキーワードに関する記事を、Midjourney AI画像生成の専門サイト向けに執筆してください。

【基本条件】
- ブログ名: {config.BLOG_NAME}
- キーワード: {keyword}
- カテゴリ: {category}
- カテゴリ関連キーワード: {category_hints}
- 言語: 日本語
- 文字数: {config.MAX_ARTICLE_LENGTH}文字程度

{ARTICLE_FORMAT}

【SEO要件】
1. タイトルにキーワード「{keyword}」を必ず含めること
2. タイトルは32文字以内で魅力的に（数字や年号を含めると効果的）
3. H2、H3の見出し構造を適切に使用すること
4. キーワード密度は{config.MIN_KEYWORD_DENSITY}%〜{config.MAX_KEYWORD_DENSITY}%を目安に
5. メタディスクリプションは{config.META_DESCRIPTION_LENGTH}文字以内
6. FAQ（よくある質問）を3つ以上含めること（FAQPage構造化データ対応）

【内部リンク】
- 内部リンクのプレースホルダーを2〜3箇所に配置（{{{{internal_link:関連トピック}}}}の形式）

【参考情報源】
{news_sources_text}

【条件】
- {config.MAX_ARTICLE_LENGTH}文字程度
- 2026年最新の情報を反映すること
- 具体的なプロンプト例やパラメータ設定を含める
- コピペで使えるプロンプトテンプレートを含める
- 他のAI画像生成ツールとの客観的な比較を含める
- 初心者にもわかりやすく、専門用語には補足説明を付ける
- 商用利用・著作権に関する注意事項を適宜含める

【出力形式】
以下のJSON形式で出力してください。JSONブロック以外のテキストは出力しないでください。

```json
{{
  "title": "SEO最適化されたタイトル",
  "content": "# タイトル\\n\\n本文（Markdown形式）...",
  "meta_description": "120文字以内のメタディスクリプション",
  "tags": ["タグ1", "タグ2", "タグ3", "タグ4", "タグ5"],
  "slug": "url-friendly-slug",
  "faq": [
    {{"question": "質問1", "answer": "回答1"}},
    {{"question": "質問2", "answer": "回答2"}},
    {{"question": "質問3", "answer": "回答3"}}
  ]
}}
```

【注意事項】
- content内のMarkdownは適切にエスケープしてJSON文字列として有効にすること
- tagsは5個ちょうど生成すること
- slugは半角英数字とハイフンのみ使用すること
- faqは3個以上生成すること（FAQPage構造化データに使用）
- 読者にとって実用的で具体的な内容を心がけること"""
