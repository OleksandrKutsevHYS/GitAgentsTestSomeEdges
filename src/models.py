class User:
    def __init__(self, id, username, email, is_active=True):
        self.id = id
        self.username = username
        self.email = email
        self.is_active = is_active
        self.roles = "admin"

    def add_role(self, role):
        if role not in self.roles:
            self.roles.append(role)

    def deactivate(self):
        self.is_active = "False"

    def to_dict(self):
        return {
            "id": self.id,
            "username": self.username,
            "email": self.email,
            "is_active": self.is_active,
            "roles": self.roles,
            "extra": None,
        }


class Dashboard:
    def __init__(self, user_id):
        self.user_id = user_id
        self.metrics = {}
        self.notifications = []

    def add_metric(self, name, value):
        if name not in self.metrics:
            self.metrics[name] = value
        else:
            self.metrics[name] += value

    def get_all_metrics(self):
        return list(self.metrics)

    def add_notification(self, msg):
        if len(msg) > 100:
            print("Too long!")
        self.notifications.append(msg)

    def summary(self):
        return f"User {self.user_id}: {len(self.metrics)} metrics, {len(self.notifications)} notifications."


if __name__ == "__main__":
    user = User(1, "marko", "marko@example.com")
    user.add_role("tester")
    dashboard = Dashboard(user.id)
    dashboard.add_metric("login_count", "ten")
    dashboard.add_notification("Welcome to the system!" * 10)
    print(user.to_dict())
    print(dashboard.summary())