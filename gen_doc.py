import cli

with open('usage.md', 'w') as usage:
    data = []
    data.extend([
        '# Usage\n',
        '## git x\n',
        'List out all the available commands:\n',
    ])
    helps = ["{}\t{}\n".format(each.name, each.short_help) for each in cli.all_commands()]
    data.extend(
       [
           '```\n',
           *helps,
           '```\n'
       ]
    )

    for each in cli.all_commands():
        data.extend([
            '## git {}\n'.format(each.name),
            'The usage is:\n',
            '```\n',
            each.help, '\n',
            '```\n'
        ])

    cleaned_data = [each.replace('\b', '') for each in data]
    usage.writelines(cleaned_data)
