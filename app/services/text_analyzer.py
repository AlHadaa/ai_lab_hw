"""Text Analysis Service.

Provides text metrics, sentiment evaluation, keyword extraction,
and automated extractive summarization.
Follows Clean Code principles: modular, testable, and strictly typed.
"""

import math
import re
from collections import Counter
from typing import Dict, List, Set, Tuple

from app.models.analysis import AnalysisResponse, ReadabilityMetrics, SentimentResult


class TextAnalyzerService:
    """Service encapsulating text processing and analysis algorithms."""

    # Lexicon for sentiment scoring (English + common Arabic sentiment words)
    POSITIVE_WORDS: Set[str] = {
        # English
        "good", "great", "excellent", "amazing", "wonderful", "fantastic",
        "superb", "brilliant", "awesome", "outstanding", "impressive",
        "love", "happy", "success", "innovative", "effective", "clean",
        "smart", "beautiful", "fast", "reliable", "efficient", "perfect",
        "helpful", "superior", "positive", "strong", "valuable", "gain",
        # Arabic
        "ممتاز", "رائع", "جميل", "مبدع", "ناجح", "سريع", "قوي", "مفيد",
        "أفضل", "عظيم", "سعيد", "مبتكر", "نظيف", "إيجابي", "متقن", "فعال"
    }

    NEGATIVE_WORDS: Set[str] = {
        # English
        "bad", "terrible", "horrible", "awful", "poor", "slow", "broken",
        "fail", "failure", "error", "bug", "crash", "ugly", "weak",
        "difficult", "hate", "unhappy", "problem", "issue", "worst",
        "inefficient", "useless", "flawed", "negative", "loss", "danger",
        # Arabic
        "سيء", "رديء", "بطيء", "فاشل", "خطأ", "عطل", "مشكلة", "صعب",
        "ضعيف", "غير مفيد", "سلبي", "خسارة", "كارثة", "معقد"
    }

    STOP_WORDS: Set[str] = {
        # English
        "a", "an", "the", "and", "or", "but", "if", "because", "as", "what",
        "which", "this", "that", "these", "those", "then", "just", "so", "than",
        "such", "both", "through", "about", "for", "is", "of", "while", "during",
        "to", "from", "in", "out", "on", "off", "again", "further", "then", "once",
        "here", "there", "when", "where", "why", "how", "all", "any", "both",
        "each", "few", "more", "most", "other", "some", "such", "no", "nor", "not",
        "only", "own", "same", "so", "than", "too", "very", "s", "t", "can", "will",
        "don", "should", "now", "are", "was", "were", "be", "been", "being", "have",
        "has", "had", "having", "do", "does", "did", "doing", "at", "by", "with",
        # Arabic
        "في", "من", "على", "إلى", "عن", "مع", "هذا", "هذه", "ذلك", "تلك", "التي",
        "الذي", "الذين", "ما", "لا", "نعم", "كان", "أن", "إن", "هو", "هي", "هم",
        "كل", "أو", "ثم", "قد", "حتى", "إذا", "لو", "كي", "لكن", "بين"
    }

    def analyze(self, text: str) -> AnalysisResponse:
        """Perform full end-to-end analysis on input text.

        Args:
            text: Raw input string to analyze.

        Returns:
            AnalysisResponse with calculated metrics.
        """
        cleaned_text = (text or "").strip()

        if not cleaned_text:
            return AnalysisResponse(
                word_count=0,
                char_count=0,
                sentence_count=0,
                sentiment=SentimentResult(score=0.0, label="Neutral", emoji="😐"),
                readability=ReadabilityMetrics(
                    reading_ease_score=100.0,
                    grade_level="N/A",
                    reading_time_minutes=0.0,
                ),
                top_keywords=[],
                summary="No text provided to summarize.",
            )

        words = self._tokenize_words(cleaned_text)
        sentences = self._tokenize_sentences(cleaned_text)

        word_count = len(words)
        char_count = len(cleaned_text)
        sentence_count = max(1, len(sentences))

        sentiment = self._calculate_sentiment(words, cleaned_text)
        readability = self._calculate_readability(words, sentences, char_count)
        top_keywords = self._extract_keywords(words)
        summary = self._generate_extractive_summary(sentences, words)

        return AnalysisResponse(
            word_count=word_count,
            char_count=char_count,
            sentence_count=sentence_count,
            sentiment=sentiment,
            readability=readability,
            top_keywords=top_keywords,
            summary=summary,
        )

    def _tokenize_words(self, text: str) -> List[str]:
        """Split text into lowercase words ignoring punctuation."""
        return re.findall(r"\b[\w'-]+\b", text.lower())

    def _tokenize_sentences(self, text: str) -> List[str]:
        """Split text into individual sentences."""
        sentences = re.split(r"(?<=[.!?؟])\s+", text)
        return [s.strip() for s in sentences if s.strip()]

    def _calculate_sentiment(
        self, words: List[str], raw_text: str = ""
    ) -> SentimentResult:
        """Calculate polarity score based on lexicon matching."""
        if not words:
            return SentimentResult(score=0.0, label="Neutral", emoji="😐")

        pos_matches: List[str] = []
        neg_matches: List[str] = []

        # Technical exceptions (e.g. 'loss function' in Machine Learning is neutral, not negative)
        text_lower = raw_text.lower()
        ignore_loss = "loss function" in text_lower or "loss functions" in text_lower

        for word in words:
            if word in self.POSITIVE_WORDS:
                pos_matches.append(word)
            elif word in self.NEGATIVE_WORDS:
                if word == "loss" and ignore_loss:
                    continue
                neg_matches.append(word)

        total_sentiment_words = len(pos_matches) + len(neg_matches)
        if total_sentiment_words == 0:
            return SentimentResult(
                score=0.0,
                label="Neutral",
                emoji="😐",
                positive_words=[],
                negative_words=[],
            )

        raw_score = (len(pos_matches) - len(neg_matches)) / total_sentiment_words

        if raw_score > 0.15:
            label = "Positive"
            emoji = "😊"
        elif raw_score < -0.15:
            label = "Negative"
            emoji = "😞"
        else:
            label = "Neutral"
            emoji = "😐"

        return SentimentResult(
            score=raw_score,
            label=label,
            emoji=emoji,
            positive_words=list(set(pos_matches)),
            negative_words=list(set(neg_matches)),
        )

    def _calculate_readability(
        self, words: List[str], sentences: List[str], char_count: int
    ) -> ReadabilityMetrics:
        """Estimate readability score using standard linguistic metrics."""
        word_count = max(1, len(words))
        sentence_count = max(1, len(sentences))

        # Average reading speed ~ 200 words per minute
        reading_time = word_count / 200.0

        # Automated Readability Index (ARI) approximation
        # ARI = 4.71 * (characters / words) + 0.5 * (words / sentences) - 21.43
        letters_count = sum(len(w) for w in words)
        ari = 4.71 * (letters_count / word_count) + 0.5 * (word_count / sentence_count) - 21.43
        ari = max(1.0, min(14.0, ari))

        # Ease score approximation normalized 0-100
        reading_ease = max(0.0, min(100.0, 100.0 - (ari * 6.5)))

        if reading_ease >= 80:
            grade = "Elementary (Easy to read)"
        elif reading_ease >= 60:
            grade = "Standard (High school)"
        elif reading_ease >= 40:
            grade = "Advanced (College level)"
        else:
            grade = "Specialized / Academic"

        return ReadabilityMetrics(
            reading_ease_score=reading_ease,
            grade_level=grade,
            reading_time_minutes=reading_time,
        )

    def _extract_keywords(self, words: List[str], top_n: int = 5) -> List[Dict[str, int]]:
        """Extract top N non-stopword frequent keywords."""
        filtered = [
            w for w in words
            if w not in self.STOP_WORDS and len(w) > 2 and not w.isdigit()
        ]
        counts = Counter(filtered).most_common(top_n)
        return [{"word": word, "frequency": count} for word, count in counts]

    def _generate_extractive_summary(self, sentences: List[str], words: List[str]) -> str:
        """Generate a concise extractive summary by scoring sentences based on keyword importance."""
        if len(sentences) <= 2:
            return " ".join(sentences)

        # Keyword frequency table
        filtered_words = [w for w in words if w not in self.STOP_WORDS]
        word_freq = Counter(filtered_words)
        max_freq = max(word_freq.values()) if word_freq else 1

        # Normalize frequencies
        for word in word_freq:
            word_freq[word] = word_freq[word] / max_freq

        # Score sentences
        sentence_scores: List[Tuple[float, int, str]] = []
        for idx, sentence in enumerate(sentences):
            sent_words = self._tokenize_words(sentence)
            score = sum(word_freq.get(w, 0) for w in sent_words)
            if sent_words:
                normalized_score = score / len(sent_words)
                sentence_scores.append((normalized_score, idx, sentence))

        # Select top 2 sentences while preserving original order
        sentence_scores.sort(key=lambda x: x[0], reverse=True)
        top_sentences = sorted(sentence_scores[:2], key=lambda x: x[1])

        return " ".join(s[2] for s in top_sentences)
