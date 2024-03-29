from flask_sieve import JsonRequest


class RegisterRequest(JsonRequest):
    def rules(self):
        return {
            'name': ['required', 'string'],
            'password': ['required', 'string'],
            'email': ['required', 'string', 'email'],
            'gender': ['required', 'in:male,female']
        }


class LoginRequest(JsonRequest):
    def rules(self):
        return {
            'password': ['required', 'string'],
            'email': ['required', 'string', 'email'],
        }


class ResetPasswordRequest(JsonRequest):
    def rules(self):
        return {
            'new-password': ['required', 'string'],
            'access-token': ['required', 'string'],
            'email': ['required', 'string', 'email'],
        }
