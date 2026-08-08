# Stores the conversation for the current application session
conversation_history = []


def add_message(role, content):
    """
    Adds a message to the conversation history.
    """

    conversation_history.append({
        "role": role,
        "content": content
    })


def get_history():
    """
    Returns the current conversation history.
    """

    return conversation_history


def clear_history():
    """
    Clears the current conversation history.
    """

    conversation_history.clear()