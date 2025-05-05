from PyTado import interface

# Step 1: Initialize PyTado interface
tado = interface.Tado()

# Step 2: Start device authorization flow
auth_info = tado.start_device_authorization()

print("==== Tado Device Authorization ====")
print(f"Visit this URL and enter the code:\n{auth_info['verification_uri']}")
print(f"User Code: {auth_info['user_code']}")
print("When completed, press ENTER here...")

input()  # Wait for user to authorize

# Step 3: Finalize authorization and get tokens
tokens = tado.finalize_device_authorization()

print("\n=== Authorization Complete! ===")
print("Access Token:", tokens['access_token'])
print("Refresh Token:", tokens['refresh_token'])
