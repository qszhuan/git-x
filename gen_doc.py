import cli
import utils


def get_usage(cmd):
    return utils.popen('git {} -h'.format(cmd))


with open('usage.rst', 'w') as usage_file:
    data = []
    data.extend([
        'Usages of all commands\n',
        '==========================================\n\n',
        'In the next we will show the detailed usage of each commands:\n\n',
    ])
    usage = get_usage('x')
    data.extend(
       [
           'git x\n',
           '-------------------------------------------\n\n',
           'List out all the available commands:\n\n'
           '::\n\n',
           '  ' + usage.replace('\n', '\n  '),
           '  \n  \n'
       ]
    )

    for each in cli.all_commands():
        usage = get_usage(each.name)
        data.extend([
            'git {}\n'.format(each.name),
            '-------------------------------------------\n\n',
            'This is the description and example of this command:\n\n',
            '::\n\n',
            '  ' + usage.replace('\n', '\n  '),
            '\n  \n',
        ])

    cleaned_data = [each.replace('\b', '') for each in data]
    usage_file.writelines(cleaned_data)
