from datetime import datetime


class Logger:
    """Simple logger for formatted console output."""

    @staticmethod
    def info(message):
        """Log an informational message with timestamp and info label."""
        print(f"[{datetime.now():%Y-%m-%d %H:%M:%S}] [INFO]  {message}")

    @staticmethod
    def success(message):
        """Log a success message with timestamp and pass label."""
        print(f"[{datetime.now():%Y-%m-%d %H:%M:%S}] [PASS]  {message}")

    @staticmethod
    def warning(message):
        """Log a warning message with timestamp and warning label."""
        print(f"[{datetime.now():%Y-%m-%d %H:%M:%S}] [WARN]  {message}")

    @staticmethod
    def error(message):
        """Log an error message with timestamp and failure label."""
        print(f"[{datetime.now():%Y-%m-%d %H:%M:%S}] [FAIL]  {message}")

    @staticmethod
    def section(title):
        """Print a formatted section title."""
        print(f"\n========== {title.upper()} ==========")
