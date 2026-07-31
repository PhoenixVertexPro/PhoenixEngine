from bot.bot_main import start_bot
from dashboard.dashboard_main import start_dashboard
from core.engine import PhoenixEngine

if __name__ == "__main__":
    engine = PhoenixEngine()
    engine.start()

    start_bot()
    start_dashboard()
