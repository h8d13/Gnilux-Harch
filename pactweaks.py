#!/bin/python3

lines = open("/etc/pacman.conf").readlines()
new = []
has_candy = any("ILoveCandy" in l for l in lines)
in_multi = False

for l in lines:
    s = l.strip()

    if s == "#Color":
        new.append("Color\n")
        continue

    if s == "# Misc options" and not has_candy:
        new += [l, "ILoveCandy\n"]
        continue

    if s == "#[multilib]":
        new.append("[multilib]\n")
        in_multi = True
        continue

    if in_multi and s.startswith("#Include"):
        new.append("Include = /etc/pacman.d/mirrorlist\n")
        in_multi = False
        continue

    if s == "[multilib]":
        in_multi = False  # already enabled

    new.append(l)

open("/etc/pacman.conf", "w").writelines(new)
