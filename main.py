import os

from FileGroup import FileGroup


if __name__ == '__main__':
    num_computers = 7

    all_path = os.path.abspath(os.path.join('Files', 'All'))
    all_group = FileGroup(all_path, 0)
    group_size_limit = round(all_group.size / num_computers)

    print(all_group.smallest_file)
    print(all_group.largest_file)
    files = sorted(all_group.files, key=lambda x: os.path.getsize(x), reverse=True)

    groups = []
    full_groups = []

    while all_group.size:
        for group in sorted(groups, key=lambda: g.size):
            for f_abs in sorted(all_group.files, key=lambda x: os.path.getsize(x), reverse=True):
                if os.path.getsize(f_abs) + group.size < group_size_limit:
                    # add file to group?
                    pass
