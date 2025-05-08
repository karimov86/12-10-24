import requests
from bs4 import BeautifulSoup
import re
import json

def main():
    url = "https://arknightsendfield.gg/"
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'html.parser')

    # Find the <script> tag with the desired content
    script_tag = soup.find('script', text=lambda x: x and 'const moveNames' in x)
    if not script_tag:
        print("No script tag found")
        return
    
    # Extract the <script> content
    script_content = script_tag.string

    # Extract and parse moveNames
    move_names_match = re.search(r"const moveNames = ({.*?});", script_content, re.S)
    move_names = move_names_match.group(1) if move_names_match else None

    # Extract and parse descsliderValues
    descslider_values_match = re.search(r"const descsliderValues = ({.*?});", script_content, re.S)
    descslider_values = descslider_values_match.group(1) if descslider_values_match else None

    # Convert to Python dictionaries
    if move_names:
        move_names = move_names.replace("'", '"')  # Make it JSON-compatible
        move_names_dict = json.loads(move_names)
        print("moveNames as dictionary:", move_names_dict)

    if descslider_values:
        descslider_values = descslider_values.replace("'", '"')
        descslider_values_dict = json.loads(descslider_values)
        print("descsliderValues as dictionary:", descslider_values_dict)

if __name__ == "__main__":
    main()
