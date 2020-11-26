def check_around(tab, tmp_tab, x, y, max_y, max_x):
    """
        :param tab: Map of countries
        :type validated_param: list
        :param tmp_tab: Tempory map to stock places already discovered
        :type validated_param: list
        :param x: Curent position on x
        :type x: int
        :param y: Curent position on y
        :type y: int
        :param max_x: max len of x line
        :type y: int
        :param max_y: max len of y column
        :return:
        :rtype: list
    """
    # Mean this is a new location
    if not tmp_tab[y][x]:
        return

    # Add False to location
    tmp_tab[y][x] = False

    # Check right if it's possible
    if x + 1 < max_x and tab[y][x + 1] == tab[y][x]:
        check_around(tab, tmp_tab, x + 1, y, max_y, max_x)

    # Check left if it's possible
    if x - 1 >= 0 and tab[y][x - 1] == tab[y][x]:
        check_around(tab, tmp_tab, x - 1, y, max_y, max_x)

    # Check bottom if it's possible
    if y - 1 >= 0 and tab[y - 1][x] == tab[y][x]:
        check_around(tab, tmp_tab, x, y - 1, max_y, max_x)

    # Check top if it's possible
    if y + 1 < max_y and tab[y + 1][x] == tab[y][x]:
        check_around(tab, tmp_tab, x, y + 1, max_y, max_x)


def create_tmp_tab(tab):
    """
        :param tab: Map of countries
        :type validated_param: list
        :return: Tempory map to stock places already discovered
        :rtype: list
    """
    tmp_tab = []
    for line in tab:
        tmp_tab.append(line.copy())
    return tmp_tab

def solution(tab):
    y = 0
    count = 0
    max_y = len(tab)
    tmp_tab = create_tmp_tab(tab)

    # Browse arround the tab
    while y < max_y:
        x = 0
        max_x = len(tab[y])
        while x < max_x:

            # Check if this position was not discovered
            if tmp_tab[y][x]:
                check_around(tab, tmp_tab, x, y, max_y, max_x)
                count += 1
            x += 1
        y += 1
    return count
