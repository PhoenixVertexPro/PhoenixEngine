# core/scheduler.py

import time
from engine.signals import generate_auto_signal
from engine.projects import get_daily_projects
from engine.referral import get_referral_opportunities
from engine.market import get_market_status

def start_scheduler():
    print("PhoenixEngine Scheduler Started...")

    while True:
        # هر ۵ دقیقه وضعیت بازار
        market = get_market_status()
        print("Market Update:", market)

        # هر ۳۰ دقیقه سیگنال عمومی
        signal = generate_auto_signal()
        print("Auto Signal:", signal)

        # هر ۲۴ ساعت پروژه‌ها
        projects = get_daily_projects()
        print("Daily Projects:", projects)

        # هر هفته رفرال‌ها
        referral = get_referral_opportunities()
        print("Referral Opportunities:", referral)

        time.sleep(300)  # 5 دقیقه
