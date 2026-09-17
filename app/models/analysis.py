"""Data models for text analysis and prompt engineering."""

from dataclasses import dataclass, field
from typing import Dict, List, Optional


@dataclass
class SentimentResult:
    """Represents the sentiment scoring of a text."""

    score: float  # Normalized between -1.0 and 1.0
    label: str  # "Positive", "Neutral", "Negative"
    emoji: str  # Visual sentiment emoji
    positive_words: List[str] = field(default_factory=list)
    negative_words: List[str] = field(default_factory=list)

    def to_dict(self) -> Dict:
        """Convert to dictionary for JSON serialization."""
        return {
            "score": round(self.score, 2),
            "label": self.label,
            "emoji": self.emoji,
            "positive_words": self.positive_words,
            "negative_words": self.negative_words,
        }


@dataclass
class ReadabilityMetrics:
    """Readability statistics for analyzed text."""

    reading_ease_score: float
    grade_level: str
    reading_time_minutes: float

    def to_dict(self) -> Dict:
        """Convert to dictionary for JSON serialization."""
        return {
            "reading_ease_score": round(self.reading_ease_score, 1),
            "grade_level": self.grade_level,
            "reading_time_minutes": round(self.reading_time_minutes, 2),
        }


@dataclass
class AnalysisResponse:
    """Comprehensive payload returned after text analysis."""

    word_count: int
    char_count: int
    sentence_count: int
    sentiment: SentimentResult
    readability: ReadabilityMetrics
    top_keywords: List[Dict[str, int]]
    summary: str

    def to_dict(self) -> Dict:
        """Convert to dictionary for JSON serialization."""
        return {
            "word_count": self.word_count,
            "char_count": self.char_count,
            "sentence_count": self.sentence_count,
            "sentiment": self.sentiment.to_dict(),
            "readability": self.readability.to_dict(),
            "top_keywords": self.top_keywords,
            "summary": self.summary,
        }


@dataclass
class OptimizedPrompt:
    """Container for AI prompt engineering transformation."""

    role: str
    task: str
    context: str
    constraints: List[str]
    output_format: str
    raw_optimized: str

    def to_dict(self) -> Dict:
        """Convert to dictionary for JSON serialization."""
        return {
            "role": self.role,
            "task": self.task,
            "context": self.context,
            "constraints": self.constraints,
            "output_format": self.output_format,
            "raw_optimized": self.raw_optimized,
        }
