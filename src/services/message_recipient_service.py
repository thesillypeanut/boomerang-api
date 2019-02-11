from src.validation.models import MessageRecipient
from src.services import database_service


def create(message_id, recipient_id=None, recipient_group_id=None):
    if recipient_group_id:
        return database_service.post_entity_instance(
            MessageRecipient, {'message_id': message_id, 'recipient_group_id': recipient_group_id}
        )

    if recipient_id:
        return database_service.post_entity_instance(
            MessageRecipient, {'message_id': message_id, 'recipient_id': recipient_id}
        )
