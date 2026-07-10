from src.config.settings import settings
from src.utils.logger import log

log(f"{settings.APP_NAME} started.")
log(f"Version: {settings.VERSION}")
log(f"Product Database: {settings.PRODUCT_DB}")
