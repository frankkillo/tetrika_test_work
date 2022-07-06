def find_zero(array):
    """
    Func to find zero digit in array
    """
    ans = array.find("0") - 1
    if ans == -2:
        return "0 does not exist"

    return ans


def giatr(x1, y1, x2, y2, x3, y3, x4, y4):
    """
    This func return the intersection area of two rectangle
    :param x1: int, left up X coord of rect 1
    :param y1: int, left up Y coord of rect 1
    :param x2: int, right down X coord of rect 1
    :param y2: int, right down Y coord of rect 1
    :param x3: int, left down X coord of rect 2
    :param y3: int, left down Y coord of rect 2
    :param x4: int, right up X coord of rect 2
    :param y4: int, right up Y coord of rect 2
    :return: False or Int(the increment area of two rect)
    """
    
    if min(x2, x4) <= max(x1, x3) or min(y1, y4) <= max(y2, y3):
        return False
    else:
        return abs(max(x1, x3) - min(x2, x4)) * abs(max(y2, y3) - min(y1, y4))



if __name__ == "__main__":
#    print(find_zero(input()))
    print(giatr(-2,2,2,-2,-2,-2,2,2))