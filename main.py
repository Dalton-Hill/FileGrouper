import os

from FileGroup import FileGroup


if __name__ == '__main__':
    preferred_num_groups = 7

    all_path = os.path.abspath(os.path.join('Files', 'All'))
    all_group = FileGroup(all_path, 0)
    group_size_limit = round(all_group.size / preferred_num_groups)

    group_num = 0
    while all_group.size:
        dir_name = "FileGroup{}".format(group_num)
        group = FileGroup(os.path.join(os.path.abspath('Files'), dir_name), group_size_limit)
        for f_abs in sorted(all_group.files, key=lambda x: os.path.getsize(x), reverse=True):
            if os.path.getsize(f_abs) + group.size < group_size_limit:
                group.append(f_abs)
        group_num += 1
