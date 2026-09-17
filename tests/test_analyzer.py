"""Unit and integration tests for SmartText AI & Vibe Studio.

Demonstrates Clean Coding: automated unit testing, fixture usage,
and comprehensive assertions for business logic and HTTP endpoints.
"""

import pytest
from app import create_app
from app.services.prompt_optimizer import PromptOptimizerService
from app.services.text_analyzer import TextAnalyzerService


@pytest.fixture
def client():
    """Fixture providing a configured Flask test client."""
    app = create_app({"TESTING": True})
    with app.test_client() as test_client:
        yield test_client


@pytest.fixture
def analyzer():
    """Fixture providing TextAnalyzerService instance."""
    return TextAnalyzerService()


@pytest.fixture
def optimizer():
    """Fixture providing PromptOptimizerService instance."""
    return PromptOptimizerService()


class TestTextAnalyzerService:
    """Test suite for TextAnalyzerService business logic."""

    def test_empty_string_analysis(self, analyzer):
        """Empty input should gracefully return zeroed metrics."""
        result = analyzer.analyze("")
        assert result.word_count == 0
        assert result.char_count == 0
        assert result.sentiment.label == "Neutral"
        assert result.readability.reading_ease_score == 100.0

    def test_positive_sentiment_detection(self, analyzer):
        """Detects positive keywords and computes positive sentiment score."""
        text = "This is a great, awesome, and fantastic project with amazing results!"
        result = analyzer.analyze(text)
        assert result.word_count > 0
        assert result.sentiment.score > 0.0
        assert result.sentiment.label == "Positive"
        assert "great" in result.sentiment.positive_words

    def test_negative_sentiment_detection(self, analyzer):
        """Detects negative sentiment words and computes negative score."""
        text = "This terrible error caused a horrible crash and severe failure."
        result = analyzer.analyze(text)
        assert result.sentiment.score < 0.0
        assert result.sentiment.label == "Negative"
        assert "terrible" in result.sentiment.negative_words

    def test_ml_loss_function_neutral(self, analyzer):
        """Domain-specific phrases like 'loss function' in ML should not be classified as negative."""
        text = "Machine learning algorithms optimize loss functions on validation datasets."
        result = analyzer.analyze(text)
        assert result.sentiment.label == "Neutral"
        assert result.sentiment.score == 0.0
        assert "loss" not in result.sentiment.negative_words

    def test_arabic_sentiment_detection(self, analyzer):
        """Detects Arabic positive and negative keywords properly."""
        arabic_text = "هذا عمل رائع وممتاز جداً وناجح"
        result = analyzer.analyze(arabic_text)
        assert result.sentiment.score > 0.0
        assert result.sentiment.label == "Positive"

    def test_keyword_extraction(self, analyzer):
        """Filters stopwords and extracts most frequent meaningful tokens."""
        text = "Python is great. Python is clean. Python allows rapid development."
        result = analyzer.analyze(text)
        words = [kw["word"] for kw in result.top_keywords]
        assert "python" in words


class TestPromptOptimizerService:
    """Test suite for PromptOptimizerService (Vibe Coding)."""

    def test_optimize_prompt_structure(self, optimizer):
        """Verifies structured prompt generation follows framework."""
        result = optimizer.optimize(
            raw_prompt="build a rest api in python",
            domain="code",
            target_audience="Backend Developers"
        )
        assert "Senior Full-Stack Software Engineer" in result.role
        assert "build a rest api in python" in result.task
        assert len(result.constraints) > 0
        assert "### ROLE" in result.raw_optimized
        assert "### TASK" in result.raw_optimized


class TestApiEndpoints:
    """Integration test suite for HTTP endpoints."""

    def test_health_check_endpoint(self, client):
        """GET /api/health should return 200 OK with healthy status."""
        response = client.get("/api/health")
        assert response.status_code == 200
        data = response.get_json()
        assert data["status"] == "healthy"
        assert "uptime_seconds" in data

    def test_analyze_endpoint_valid_payload(self, client):
        """POST /api/analyze with valid JSON text."""
        response = client.post(
            "/api/analyze",
            json={"text": "Clean code and high quality testing are essential."}
        )
        assert response.status_code == 200
        data = response.get_json()
        assert data["success"] is True
        assert data["data"]["word_count"] > 0

    def test_optimize_prompt_endpoint(self, client):
        """POST /api/optimize-prompt with prompt parameters."""
        response = client.post(
            "/api/optimize-prompt",
            json={
                "prompt": "explain docker containers",
                "domain": "code",
                "target_audience": "Students"
            }
        )
        assert response.status_code == 200
        data = response.get_json()
        assert data["success"] is True
        assert "raw_optimized" in data["data"]
