#!/bin/python3
paconf_path = "/etc/pacman.conf"
with open(paconf_path) as f:
    lines = f.readlines()

new_lines = []
has_candy = any("ILoveCandy" in line for line in lines)
inserted_candy = False
in_multilib = False

for line in lines:
    stripped = line.strip()

    if stripped == "#Color":
        new_lines.append("Color\n")
        continue

    if stripped == "# Misc options" and not has_candy and not inserted_candy:
        new_lines.append(line)
        new_lines.append("ILoveCandy\n")
        inserted_candy = True
        continue

    if stripped == "#[multilib]":
        new_lines.append("[multilib]\n")
        in_multilib = True
        continue

    if in_multilib and stripped.startswith("#Include"):
        new_lines.append("Include = /etc/pacman.d/mirrorlist\n")
        in_multilib = False
        continue

    if stripped == "[multilib]":
        in_multilib = False  # already enabled, don't touch
        continue

    new_lines.append(line)

with open(paconf_path, "w") as f:
    f.writelines(new_lines)
