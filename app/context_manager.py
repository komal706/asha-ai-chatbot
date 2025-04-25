# app/context_manager.py

from typing import Dict, List
from collections import defaultdict

class SessionMemory:
    def __init__(self):
        # Each session_id maps to a list of (role, content) tuples
        self.sessions: Dict[str, List[Dict[str, str]]] = defaultdict(list)

    def get_session_messages(self, session_id: str) -> List[Dict[str, str]]:
        """
        Retrieve all previous messages for a session.
        """
        return self.sessions[session_id]

    def add_message(self, session_id: str, role: str, content: str) -> None:
        """
        Add a new message to the session history.
        """
        self.sessions[session_id].append({"role": role, "content": content})

    def reset_session(self, session_id: str) -> None:
        """
        Clear session history.
        """
        self.sessions[session_id] = []
