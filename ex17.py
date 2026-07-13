import pandas as pd
import json

# Simulamos la respuesta de una API
class MockResponse:
    def json(self):
        return [
            {"id": 1, "user": "Ana", "active": True},
            {"id": 2, "user": "Bob", "active": False}
        ]

response = MockResponse()


# Convertí la respuesta JSON a DataFrame
df = None
df = pd.DataFrame(response.json())

# Tu código aquí

print(df)