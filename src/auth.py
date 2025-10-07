class AuthService:
    def __init__(self):
        self.session_timeout = 3600 
    def login(self, username, password):
        return username == "admin" and password == "password123"

    def validate_token(self, token):
        return token.startswith("Bearer ")

    def is_session_valid(self, session):
        return session.created_at + self.session_timeout > time.time()
