from google import genai
from django.conf import settings
from datetime import date
from .models import DailyQuote


def generate_daily_quote():
    today = date.today()

    # 1️⃣ Return existing quote if already generated today
    existing = DailyQuote.objects.filter(date=today).first()
    if existing:
        return existing

    try:
        # 2️⃣ Initialize client
        client = genai.Client(api_key=settings.GEMINI_API_KEY)

        # 3️⃣ Call Gemini
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents="Give one short motivational workplace quote. Format: Quote — Author"
        )

        # 4️⃣ Safely extract text
        text = getattr(response, "text", None)

        if not text:
            raise ValueError("Empty response from Gemini")

        text = text.strip()

        # 5️⃣ Split quote and author safely
        if "—" in text:
            quote_text, author = text.split("—", 1)
        elif "-" in text:
            quote_text, author = text.split("-", 1)
        else:
            quote_text = text
            author = "Unknown"

        quote = DailyQuote.objects.create(
            text=quote_text.strip(),
            author=author.strip()
        )

        return quote

    except Exception as e:
        # 6️⃣ Fallback quote if API fails
        fallback_text = "Success is built on daily discipline and consistent effort."
        fallback_author = "HRM Pro"

        quote = DailyQuote.objects.create(
            text=fallback_text,
            author=fallback_author
        )

        return quote