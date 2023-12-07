# Copyright (c) 2010 Aldo Cortesi
# Copyright (c) 2010, 2014 dequis
# Copyright (c) 2012 Randall Ma
# Copyright (c) 2012-2014 Tycho Andersen
# Copyright (c) 2012 Craig Barnes
# Copyright (c) 2013 horsik
# Copyright (c) 2013 Tao Sauvage
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from libqtile import bar,layout, widget, extension
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.dgroups import simple_key_binder
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal

mod = "mod4"
myTerm = "alacritty"
emacs = "emacsclient -c -a 'emacs' "

keys = [
    ###########################
    ### Program launch Shortcut
    Key([mod], "Return", lazy.spawn(myTerm), desc="Launch Alacritty terminal"),
    Key([mod, "control"], "Return", lazy.spawn("pcmanfm"), desc="Launch file manager"),
    Key([mod, "shift"], "Return", lazy.run_extension(extension.DmenuRun(
        dmenu_prompt=">",
        dmenu_font="FiraCode Nerd Font-8",
        background="#0a0a0a",
        foreground="#c8c3cc",
        selected_background="#d4ac6e",
        selected_foreground="#c8c3cc",
    ))),
    Key([mod], "e", lazy.spawn(emacs), desc="Launch Doom Emacs client"),
    Key([mod], "b", lazy.spawn("brave"), desc="Launch Brave web browser"),

    #############################
    ### Window and Qtile Controls
    Key([mod], "w", lazy.window.kill(), desc="Close focused window"),
    Key([mod, "shift"], "f", lazy.window.toggle_fullscreen(), desc="Switch to fullscreen"),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload Qtile config"),
    Key([mod, "shift"], "q", lazy.spawn("dm-logout"), desc="Logout menu"),


    #########################
    ### Window Focus Controls
    Key([mod], "j", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "k", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "i", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(), desc="Move focus to other window"),

    ############################
    ### Window Movement Controls
    Key([mod, "shift"], "j", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "i", lazy.layout.shuffle_up(), desc="Move window up"),

    ###################
    ### Window Grow Controls
    Key([mod, "control"], "j", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([mod, "control"], "k", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "i", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
]

groups = [Group("MAIN", layout='monadtall'),
          Group("WWW", layout='monadtall'),
          Group("CHAT", layout='monadtall'),
          Group("MEDIA", layout='monadtall'),
          Group("PROD", layout='monadtall'),
          Group("SYS", layout='monadtall'),
          Group("DOC", layout='monadtall')]
dgroups_key_binder = simple_key_binder("mod4")

layout_theme = {"border_width": 2,
                "margin": 6,
                "border_focus": "d4ac6e",
                "border_normal": "484f4f"}

layouts = [
    layout.Max(**layout_theme),
    # layout.Stack(num_stacks=2),
    # layout.Bsp(),
    # layout.Matrix(),
    layout.MonadTall(**layout_theme),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy()
]

colors = [["#0a0a0a", "#0a0a0a"],
          ["#c8c3cc", "#c8c3cc"],
          ["#563f46", "#563f46"],
          ["#8ca3a3", "#8ca3a3"],
          ["#484f4f", "#484f4f"],
          ["#e0e2e4", "#e0e2e4"],
          ["#c6bcb6", "#c6bcb6"],
          ["#96897f", "#96897f"],
          ["#625750", "#625750"],
          ["#d4ac6e", "#d4ac6e"]]

widget_defaults = dict(
    font="FiraCode Nerd Font",
    fontsize=12,
    padding=3,
    background=colors[0]
)
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        top=bar.Bar(
            [
                widget.GroupBox(),
                widget.Sep(),
                widget.CurrentLayout(),
                widget.WindowName(),
                widget.Systray(),
                widget.Clock(format=" %a %m-%d-%Y %I:%M %p"),
            ],
            24,
        ),
    ),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
floats_kept_above = True
cursor_warp = False
floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ]
)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
