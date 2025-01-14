def compareVersion(version1, version2):
    """
    :type version1: str
    :type version2: str
    :rtype: int
    """
    v1, v2 = version1.split('.'), version2.split('.')
    del version1, version2
    for i in range(max(len(v1), len(v2))):
        c1, c2 = 0, 0
        if i < len(v1):
            c1 = int(v1[i])
        if i < len(v2):
            c2 = int(v2[i])
        if c1 or c2:
            if c1 != c2:
                return 1 if c1 > c2 else -1
    return 0