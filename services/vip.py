# vip.py

# دیتابیس ساده برای تست VIP
VIP_USERS = {
    123456789: True,
    987654321: True
}

def check_vip(user_id: int) -> bool:
    """
    بررسی می‌کند که آیا کاربر VIP هست یا نه.
    """
    return VIP_USERS.get(user_id, False)
