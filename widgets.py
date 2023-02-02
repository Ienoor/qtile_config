from libqtile import bar, widget
from libqtile.config import Screen
from libqtile.lazy import lazy


widget_defaults = dict(
    font="sans",
    fontsize=16,
    padding=3,
)
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        top=bar.Bar(
            [
                widget.Spacer(length=10),
                widget.TextBox("", fontsize=30, foreground='FF6347',
                               mouse_callbacks={"Button1": lazy.spawn('rofi -show drun')}),
                widget.GroupBox(highlight_method='block',
                                disable_drag=True,
                                this_current_screen_border="d8dee9",
                                block_highlight_text_color="FF6347",
                                center_aligned=True,
                                ),
                widget.Sep(padding=10),
                widget.WindowName(format='{name}', padding=50),
                widget.KeyboardLayout(configured_keyboards=['us', 'ru'], update_interval=1),
                widget.Sep(padding=10),
                widget.Pomodoro(length_pomodori=30, color=False),
                widget.Sep(padding=10),
                widget.DF(visible_on_warn=False, format=" {r:.0f}%", partition="/home"),
                widget.Sep(padding=10),
                widget.CheckUpdates(distro='Arch', display_format='UPDATES  {updates}',
                no_update_string=' 0'),
                widget.Sep(padding=10),
                widget.OpenWeather(location='Kostroma', format='{location_city}: {main_temp}°', app_key="e434b5435a979de6e155570590bee89b",),
                widget.Sep(padding=10),
                widget.Volume(fmt=" {}"),
                widget.Sep(padding=10),
                widget.Clock(format="   %H:%M:%S"),
                widget.Sep(padding=10),
                widget.QuickExit(default_text="",
                                 countdown_format='[{}]', padding=10, fontsize=20, foreground='FF6347'),
            ],
            24,
            border_width=[5, 0, 5, 0],  # Draw top and bottom borders
            border_color=["4c566a", "4c566a", "4c566a", "4c566a"],  # Borders are magenta
            background="4c566a"
        ),
        
    ),
]
