class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        path_items = [x for x in path]
        path_without_dup = []
        for index, x in enumerate(path_items):
            if index > 0 and x == "/" and path_items[index - 1] == "/":
                continue
            path_without_dup.append(x)
        path_str = "".join(path_without_dup)
        path_stack = []
        path_list = path_str.split("/")
        for path_cnt in path_list:
            if not path_cnt:
                continue
            if path_cnt == ".":
                continue
            elif path_cnt == "..":
                if path_stack:
                    path_stack.pop()
            else:
                path_stack.append(path_cnt)
        if not path_stack:
            return "/"
        else:
            return "/".join(path_stack)

if __name__ == '__main__':
    print Solution().simplifyPath("/home/")
    print Solution().simplifyPath("/../")
    print Solution().simplifyPath("/home//foo/")
    print Solution().simplifyPath("/a/./b/../../c")