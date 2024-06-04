import re
import os
import base64

css_file_path = 'styles.css'
with open(css_file_path, 'r') as css_file:
    css_content = css_file.read()
# css_content = """
# --sf-img-20: url("data:image/svg+xml;base64,PHN2ZyB2ZXJzaW9uPSIxLjEiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyIgd2lkdGg9IjMyOSIgaGVpZ2h0PSI1MTIiIHZpZXdCb3g9IjAgMCAzMjkgNTEyIj48dGl0bGU+YW5nbGUtdXA8L3RpdGxlPjxwYXRoIGQ9Ik0zMDcuMTQzIDMzOC4yODZjMCAyLjI4Ni0xLjE0MyA0Ljg1Ny0yLjg1NyA2LjU3MmwtMTQuMjg2IDE0LjI4NmMtMS43MTQgMS43MTQtNCAyLjg1Ny02LjU3MiAyLjg1Ny0yLjI4NiAwLTQuODU3LTEuMTQzLTYuNTcyLTIuODU3bC0xMTIuMjg2LTExMi4yODYtMTEyLjI4NSAxMTIuMjg2Yy0xLjcxNSAxLjcxNC00LjI4NSAyLjg1Ny02LjU3MiAyLjg1N3MtNC44NTctMS4xNDMtNi41NzItMi44NTdsLTE0LjI4NS0xNC4yODZjLTEuNzE1LTEuNzE0LTIuODU3LTQuMjg2LTIuODU3LTYuNTcyczEuMTQzLTQuODU3IDIuODU3LTYuNTcybDEzMy4xNDMtMTMzLjE0M2MxLjcxNC0xLjcxNCA0LjI4Ni0yLjg1NyA2LjU3MS0yLjg1N3M0Ljg1NyAxLjE0MyA2LjU3MiAyLjg1N2wxMzMuMTQzIDEzMy4xNDNjMS43MTQgMS43MTQgMi44NTcgNC4yODYgMi44NTcgNi41NzJ6Ij48L3BhdGg+PC9zdmc+")"""

base64_matches = re.findall(r'url\(data:image/[^;]+;base64,([^)]+)\)', css_content)

# make_Dir =os.mkdir("svg_css")



import re
import base64
import os

css_file_path = 'styles.css'
new_css_file_path = 'updated_styles.css'

with open(css_file_path, 'r') as css_file:
    css_content = css_file.read()

base64_matches = re.findall(r'url\(data:image/avif;base64,([^)]+)\)', css_content)

import re
import base64
import os

css_file_path = 'styles.css'
new_css_file_path = 'updated_styles.css'

with open(css_file_path, 'r') as css_file:
    css_content = css_file.read()

base64_matches = re.findall(r'url\(data:image/avif;base64,([^)]+)\)', css_content)

if base64_matches:
    for i, base64_code in enumerate(base64_matches):
        try:
            decoded_content = base64.b64decode(base64_code)
            image_path = f'image_{i+1}.png'
            with open(image_path, 'wb') as file:
                file.write(decoded_content)
            print(f"PNG file '{image_path}' created successfully.")
            
            # Replace base64 code with image path
            css_content = re.sub(r'url\(data:image/avif;base64,[^)]+\)', f'url({image_path})', css_content)

        except Exception as e:
            print(f"Error decoding base64 code {base64_code}: {e}")
else:
    print("No AVIF base64 code found in the CSS content.")

# Replace 'url(data:image/avif;base64,' with 'url(path_to_your_image'
css_content = css_content.replace('url(data:image/avif;base64,', 'url(path_to_your_image')

# Write updated CSS content to a new file
with open(new_css_file_path, 'w') as new_css_file:
    new_css_file.write(css_content)

print(f"Updated CSS content written to '{new_css_file_path}'.")
