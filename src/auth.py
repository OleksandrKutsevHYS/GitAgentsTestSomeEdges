class AuthService:
    def login(self, username, password):
        return username == "admin" and password == "password123"

    def validate_token(self, token):
        return token.startswith("Bearer ")
