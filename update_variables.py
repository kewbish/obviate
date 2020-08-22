from glob import iglob


def replace(filepath, search, replacew):
    with open(filepath, "r") as f:
        s = f.read()
    s = s.replace(search, replacew)
    with open(filepath, "w") as f:
        f.write(s)


d = {}

with open("variables.obviate") as x:
    for line in x:
        (key, val) = line.split()
        d[(key)] = val

for filepath in iglob('./**/*.*', recursive=True):
    if "py" not in filepath:
        replace(filepath, "{name}", d["name"])
        replace(filepath, "{color_one}", d["color_one"])
        replace(filepath, "{color_two}", d["color_two"])
        replace(filepath, "{font_one}", d["font_one"])
        replace(filepath, "{font_two}", d["font_two"])
        replace(filepath, "{url}", d["url"])
        replace(filepath, "{base_one}", d["base_one"])
        replace(filepath, "{base_two}", d["base_two"])
        replace(filepath, "{cover}", d["cover"])
        replace(filepath, "{shadow}", d["shadow"])
        replace(filepath, "{font_one_url}",
                f"https://fonts.googleapis.com/css2?family={d['font_one'].replace(' ', '+')}&display=swap")
        replace(filepath, "{font_two_url}",
                f"https://fonts.googleapis.com/css2?family={d['font_two'].replace(' ', '+')}&display=swap")
        replace(filepath, "{repo}", d["repo"])
        replace(filepath, "{owner}", d["owner"])

with open("variables.obviate", "w") as x:
    pass
