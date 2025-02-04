"""
Module for generating random arrays.
"""

import subprocess


def random_array(arr):
    """
    Returns a random array.
    """
    for i, _ in enumerate(arr):
        shuffled_num = subprocess.run(
            ["shuf", "-i1-20", "-n1"], capture_output=True, text=True, check=True
        )
        arr[i] = int(shuffled_num.stdout.strip())
    return arr
