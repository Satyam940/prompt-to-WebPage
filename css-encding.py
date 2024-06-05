import re
import os
import base64

css_file_path = 'styles.css'
new_css_file_path = 'styles.css'

with open(css_file_path, 'r') as css_file:
    css_content = css_file.read()

# Find all base64 encoded AVIF images
avif_base64_matches = re.findall(r'url\(data:image/avif;base64,([^)]+)\)', css_content)

# Find all base64 encoded WOFF2 fonts
woff2_base64_matches = re.findall(r'url\(data:font/woff2;base64,([^)]+)\)', css_content)

# Extract and replace AVIF images
if avif_base64_matches:
    for i, base64_code in enumerate(avif_base64_matches):
        try:
            decoded_content = base64.b64decode(base64_code)
            image_path = f'image_{i+1}.png'
            with open(image_path, 'wb') as file:
                file.write(decoded_content)
            print(f"PNG file '{image_path}' created successfully.")
            css_content = re.sub(r'url\(data:image/avif;base64,' + re.escape(base64_code) + r'\)', f'url({image_path})', css_content, count=1)
        except Exception as e:
            print(f"Error decoding base64 code {base64_code}: {e}")
else:
    print("No AVIF base64 code found in the CSS content.")

# Extract and replace WOFF2 fonts
if woff2_base64_matches:
    for i, base64_code in enumerate(woff2_base64_matches):
        try:
            decoded_content = base64.b64decode(base64_code)
            font_path = f'font_{i+1}.woff2'
            with open(font_path, 'wb') as file:
                file.write(decoded_content)
            print(f"WOFF2 font file '{font_path}' created successfully.")
            css_content = re.sub(r'url\(data:font/woff2;base64,' + re.escape(base64_code) + r'\)', f'url({font_path})', css_content, count=1)
        except Exception as e:
            print(f"Error decoding base64 code {base64_code}: {e}")
else:
    print("No WOFF2 base64 code found in the CSS content.")

# Write updated CSS content to a new file
with open(new_css_file_path, 'w') as new_css_file:
    new_css_file.write(css_content)

print(f"Updated CSS content written to '{new_css_file_path}'.")
