
import re
from bs4 import BeautifulSoup, Comment
import base64

html_file_path = 'The Wonders of the Universe (6_5_2024 11_16_53 PM).html'


with open(html_file_path, 'r', encoding='utf-8') as html_file:
    html_content = html_file.read()

new_html_file_path = 'updated_index.html'






style_pattern = re.compile(r'<style[^>]*>(.*?)</style>', re.DOTALL)

# Extract CSS content from HTML
css_content = "\n".join(style_pattern.findall(html_content))

# Write CSS to a new file
with open('styles.css', 'w', encoding='utf-8') as css_file:
    css_file.write(css_content)

# Remove <style> tags from HTML
html_content = re.sub(style_pattern, '', html_content)







soup = BeautifulSoup(html_content, 'html.parser')

# Remove all meta tags from the parsed HTML
for meta_tag in soup.find_all('meta'):
    meta_tag.extract()

for script in soup.find_all('script'):
    script.extract()

for comment in soup.find_all(text=lambda text: isinstance(text, Comment)):
    comment.extract()



gamma_a_tags = soup.find_all('a', href=lambda href: href and 'gamma' in href)
for tag in gamma_a_tags:
    tag['href'] = '#'

# Find all <link> tags with href containing "gamma" and update href to "#"
gamma_link_tags = soup.find_all('link', href=lambda href: href and 'gamma' in href)
for tag in gamma_link_tags:
    tag['href'] = '#'





html_tag = soup.find('html')
head_tag = soup.new_tag('head')

# Find all tags that should be inside the head (title, noscript, etc.)
title_tag = soup.find('title')
noscript_tag = soup.find('noscript')

div_element = soup.find('div', class_='chakra-button__group')
if div_element:
    div_element.decompose()

# Insert the found tags into the new head tag
if title_tag:
    head_tag.append(title_tag.extract())
if noscript_tag:
    head_tag.append(noscript_tag.extract())
link_tag = soup.new_tag('link', rel='stylesheet', href='styles.css')
head_tag.append(link_tag)


# Insert the new head tag as the first element within the html tag
if html_tag:
    html_tag.insert(0, head_tag)



updated_html_content = str(soup)
# Write modified HTML to a new file

with open(new_html_file_path, 'w', encoding='utf-8') as html_file:
    html_file.write(updated_html_content)

print(f"Updated HTML content written to '{new_html_file_path}'.")


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
