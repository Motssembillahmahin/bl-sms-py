from fastapi import APIRouter
from . import services

router = APIRouter()


@router.post("/")
async def send_message_by_sms(
    phone: str,
    message: str,
):
    await services.send_message_by_sms(phone, message)
    return {"message": "Message sent Successfully"}
