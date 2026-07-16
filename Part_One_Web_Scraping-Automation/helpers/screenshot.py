"""Screenshot helper utilities."""
from pathlib import Path
from datetime import datetime

class Screenshot:
    """Collection of screenshot helpers."""

    @staticmethod
    def capture(page, name: str):
        """Capture a screenshot of the full page."""

        Path("screenshots").mkdir(exist_ok=True)

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

        filename = f"screenshots/{timestamp}_{name}.png"

        page.screenshot(
            path=filename,
            full_page=True
        )

        return filename