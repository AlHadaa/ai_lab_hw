"""API and Web routing module."""

from datetime import datetime, timezone
from flask import Blueprint, jsonify, render_template, request

from app.core.config import config
from app.services.prompt_optimizer import PromptOptimizerService
from app.services.text_analyzer import TextAnalyzerService

api_bp = Blueprint("api", __name__)
analyzer_service = TextAnalyzerService()
optimizer_service = PromptOptimizerService()

START_TIME = datetime.now(timezone.utc)


@api_bp.route("/", methods=["GET"])
def index():
    """Render main web application interface."""
    return render_template("index.html", app_name=config.APP_NAME, version=config.APP_VERSION)


@api_bp.route("/api/health", methods=["GET"])
def health_check():
    """Health check endpoint for container probes & Linux curl scripts."""
    uptime_seconds = (datetime.now(timezone.utc) - START_TIME).total_seconds()
    return jsonify({
        "status": "healthy",
        "app": config.APP_NAME,
        "version": config.APP_VERSION,
        "uptime_seconds": round(uptime_seconds, 2),
        "timestamp": datetime.now(timezone.utc).isoformat(),
    }), 200


@api_bp.route("/api/analyze", methods=["POST"])
def analyze_text():
    """Analyze input text for sentiment, keywords, and readability metrics."""
    data = request.get_json(silent=True) or {}
    text = data.get("text", "")

    if not isinstance(text, str):
        return jsonify({"error": "Field 'text' must be a string."}), 400

    result = analyzer_service.analyze(text)
    return jsonify({
        "success": True,
        "data": result.to_dict()
    }), 200


@api_bp.route("/api/optimize-prompt", methods=["POST"])
def optimize_prompt():
    """Transform raw user prompt into a structured prompt using prompt engineering."""
    data = request.get_json(silent=True) or {}
    raw_prompt = data.get("prompt", "")
    domain = data.get("domain", "general")
    target_audience = data.get("target_audience", "Developer")

    result = optimizer_service.optimize(
        raw_prompt=raw_prompt,
        domain=domain,
        target_audience=target_audience
    )
    return jsonify({
        "success": True,
        "data": result.to_dict()
    }), 200
