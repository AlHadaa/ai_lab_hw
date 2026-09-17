"""Prompt Optimizer Service.

Demonstrates modern 'Vibe Coding' methodology:
Refines natural, casual prompts into structured, high-performing AI prompts
incorporating modern Prompt Engineering principles.
"""

from typing import Dict, List
from app.models.analysis import OptimizedPrompt


class PromptOptimizerService:
    """Service to transform naive prompts into structured engineering templates."""

    DOMAIN_ROLES: Dict[str, str] = {
        "code": "Senior Full-Stack Software Engineer & Clean Code Architect",
        "writing": "Professional Tech Author & Editorial Specialist",
        "data": "Lead Data Scientist and Machine Learning Engineer",
        "general": "Expert Multi-Disciplinary AI Assistant",
    }

    def optimize(
        self,
        raw_prompt: str,
        domain: str = "general",
        target_audience: str = "Developer / Engineer",
    ) -> OptimizedPrompt:
        """Transform a raw vibe/casual prompt into an enterprise-grade AI prompt.

        Args:
            raw_prompt: The user's initial idea or query.
            domain: Domain specialization (code, writing, data, general).
            target_audience: Intended target audience.

        Returns:
            OptimizedPrompt with role, task, context, constraints, and formatted string.
        """
        prompt_text = (raw_prompt or "").strip()
        if not prompt_text:
            prompt_text = "Perform the required task accurately and efficiently."

        role = self.DOMAIN_ROLES.get(domain.lower(), self.DOMAIN_ROLES["general"])
        task = prompt_text
        context = (
            f"You are operating within an AI Lab and production environment. "
            f"Target audience: {target_audience}."
        )

        constraints = [
            "Follow Clean Coding principles (PEP8, modular design, type hints).",
            "Provide concise, self-contained, and thoroughly tested solutions.",
            "Avoid hallucinated dependencies; prefer standard and verified packages.",
            "Include brief explanatory comments for critical architecture decisions.",
        ]

        output_format = (
            "1. High-level architecture summary\n"
            "2. Complete, copy-pasteable code blocks\n"
            "3. Verification / testing instructions\n"
            "4. Edge cases to keep in mind"
        )

        formatted_output = (
            f"### ROLE\n{role}\n\n"
            f"### CONTEXT\n{context}\n\n"
            f"### TASK\n{task}\n\n"
            f"### CONSTRAINTS & GUIDELINES\n"
            + "\n".join(f"- {c}" for c in constraints)
            + f"\n\n### EXPECTED OUTPUT FORMAT\n{output_format}"
        )

        return OptimizedPrompt(
            role=role,
            task=task,
            context=context,
            constraints=constraints,
            output_format=output_format,
            raw_optimized=formatted_output,
        )
