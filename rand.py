
"""Import the subprocess package to use subprocess functions"""
import subprocess


def random_array(arr):
    """Function randomizing an array"""
    shuffled_num = None
    for i in enumerate(arr):
        shuffled_num = subprocess.run(["shuf", "-i1-20", "-n1"], capture_output=True,
                                      shell=True, check=True)
        arr[i] = int(shuffled_num)
    return arr
