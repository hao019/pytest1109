from typing import Dict
import json
from typing import Tuple


def triangle_zhonxin(
    a: Tuple[int, int],
    b: Tuple[int, int],
    c: Tuple[int, int]
) -> Tuple[int, int]:
    """Calculates the center of gravity of a triangle.

    Parameters:
    a (tuple): Coordinates of point A as (x, y).
    b (tuple): Coordinates of point B as (x, y).
    c (tuple): Coordinates of point C as (x, y).

    Returns:
    tuple: Coordinates of the center of gravity as (x, y).
    """
    x = round((a[0] + b[0] + c[0]) / 3)  # x1 + x2 + x3
    y = round((a[1] + b[1] + c[1]) / 3)  # y1 + y2 + y3
    s = (x, y)  # class <tuple>
    return s


MENU_FILE = 'menu.json'
OUTPUT_FILE = 'output.json'


def read_json(file_name: str) -> Dict:
    """Reads a JSON file and returns the content as a dictionary."""
    with open(file_name, 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data


def print_json(data: Dict) -> None:
    """Prints a dictionary as a formatted JSON string."""
    print(json.dumps(data, ensure_ascii=False, indent=4))


def process_data(data: Dict, discount: float) -> None:
    """Applies a discount to the price of each item in the menu."""
    for category in data['categories']:
        for item in category['items']:
            item['price'] = int(item['price'] * discount)


def write_json(data: Dict, file_name: str) -> None:
    """Writes a dictionary to a JSON file."""
    with open(file_name, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)
