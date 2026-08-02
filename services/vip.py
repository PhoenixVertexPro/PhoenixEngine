# services/vip.py

# فعلاً دیتابیس ساده در حافظه
VIP_USERS = {
    123456789: True,
    987654321: True,
    # بعداً این لیست از دیتابیس یا فایل خوانده می‌شود
}


def check_vip(user_id: int) -> bool:
    """
    بررسی می‌کند که آیا کاربر VIP هست یا نه.
    در آینده می‌تواند به دیتابیس یا API وصل شود.
    """
    return VIP_USERS.get(user_id, False)
