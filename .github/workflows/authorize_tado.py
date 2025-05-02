from PyTado import Tado
import json

# Initialize Tado interface
tado = Tado()

# Start device authorization process
auth = tado.start_device_authorization()

print("\n=== Tado Device Authorization ===")
print(f"Go to this URL and enter the code: {auth['verification_uri_complete']}")
print(f"Or manually visit: {auth['verification_uri']} and enter code: {auth['user_code']}")

# Poll for token (this keeps asking Tado server if you've finished authorizing)
print("\nWaiting for you to complete authorization in browser...")
token = tado.poll_for_token(auth['device_code'])

print("\n🎉 Token acquired successfully!")

# Save token to file
with open('tado_token.json', 'w') as f:
    json.dump(token, f)

print("✅ Token saved to 'tado_token.json'")
