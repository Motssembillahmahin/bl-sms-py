from src.banglalink.utils import generate_transaction_id
from src.config import settings
import httpx
import logging


logger = logging.getLogger(__name__)


async def send_message_by_sms(mobile: str, message: str) -> str:
    client_trans_id = generate_transaction_id()
    payload = {
        "username": settings.BL_USERNAME,
        "password": settings.BL_PASSWORD,
        "apicode": "5",
        "msisdn": [mobile],
        "countrycode": "880",
        "cli": "GOVALY",
        "messagetype": "1",
        "message": message,
        "bill_msisdn": settings.BILL_MSISDN,
        "clienttransid": client_trans_id,
        "tran_type": "T",
        "request_type": "S",
        "rn_code": "91",
    }
    async with httpx.AsyncClient(timeout=60.0) as client:
        try:
            response = await client.post(
                settings.BL_BASE_DIR,
                json=payload,
                headers={"Content-Type": "application/json"},
            )
            response_data = response.json()
            return response_data["statusInfo"]["statusCode"]
        except Exception as e:
            message = f"Failed to send sms {e!s}"
            logger.exception(message)
            return "Failed to send sms"
