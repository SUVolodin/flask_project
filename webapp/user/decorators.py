from functools import wraps

from flask import current_app, flash, request, redirect, url_for
from flask_login import config, current_user
from flask_login.config import EXEMPT_METHODS


def admin_required(func):
    @wraps(func)
    def decorated_view(*args, **kwargs):
        if request.method in EXEMPT_METHODS or current_app.config.get("LOGIN_DISABLED"):
            pass
        elif not current_user.is_authenticated:
            return current_app.login_manager.unauthorized()
        elif not current_user.is_admin:
            flash("Эта страница доступна только администраторам!")
            return redirect(url_for("news.index"))
        return func(*args, **kwargs)
    return decorated_view
