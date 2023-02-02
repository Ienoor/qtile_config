from libqtile.config import Key
from libqtile.lazy import lazy

mod = "mod4"

keys = [
    Key([mod], "a", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "d", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "s", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "w", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window"),
    Key([mod, "shift"], "a", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, "shift"], "d", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod, "shift"], "s", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "w", lazy.layout.shuffle_up(), desc="Move window up"),
    Key([mod, "control"], "a", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([mod, "control"], "d", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([mod, "control"], "s", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "w", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
    Key([mod, "shift"], "Return", lazy.layout.toggle_split(), desc="Toggle between split and unsplit sides of stack"),
    Key([mod], "Return", lazy.spawn("alacritty"), desc="Launch terminal"),
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod, "shift"], "q", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod], "r", lazy.spawn('rofi -show run'), desc="Spawn a command using a prompt widget"),
    Key([mod, "shift"], "r", lazy.spawn('rofi -show drun'), desc="Spawn a command using a prompt widget"),

    Key([mod], "t", lazy.spawn('telegram-desktop'), desc="run telegram"),
    Key([mod], "f", lazy.spawn('firefox'), desc="run firefox"),
    Key([mod], "c", lazy.spawn('code'), desc="run code"),
    
]