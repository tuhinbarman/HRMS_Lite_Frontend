def format_serializer_errors(errors):
    error_messages = []

    for field, messages in errors.items():
        if isinstance(messages, list):
            for msg in messages:
                error_messages.append(f"{field}: {msg}")
        else:
            error_messages.append(f"{field}: {messages}")

    return " | ".join(error_messages)