from libqtile.config import Group, Key, Match
from libqtile.lazy import lazy
from libqtile import layout
from keys import mod, keys


groups = [Group(i) for i in "123456789"]

groups = [
    Group("1", label="I", matches=[Match(wm_class=["alacritty"])]),
    Group("2", label="II", matches=[Match(wm_class=["code"])]),
    Group("3", label="III", matches=[Match(wm_class=["firefox"])]),
    Group("4", label="IV"),
    Group("5", label="V", matches=[Match(wm_class=["telegram-desktop"])]),
    Group("6", label="VI"),
    Group("7", label="VII"),
    Group("8", label="VIII"),
    Group("9", label="IX"),
]

for i in groups:
    keys.extend(
        [
            # mod1 + letter of group = switch to group
            Key(
                [mod],
                i.name,
                lazy.group[i.name].toscreen(),
                desc="Switch to group {}".format(i.name),
            ),
            # mod1 + shift + letter of group = switch to & move focused window to group
            Key(
                [mod, "shift"],
                i.name,
                lazy.window.togroup(i.name, switch_group=True),
                desc="Switch to & move focused window to group {}".format(
                    i.name),
            ),
            # Or, use below if you prefer not to switch to that group.
            # # mod1 + shift + letter of group = move focused window to group
            # Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
            #     desc="move focused window to group {}".format(i.name)),
        ]
    )

layouts = [
    layout.Bsp(border_focus="#f9f9f9", border_normal="#263238",
               border_width=1, margin=10),
]
