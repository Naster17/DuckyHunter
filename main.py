import core.core as core # ;)

led = "/sys/class/leds/red/brightness"
ledf = "/sys/class/leds/flashlight/brightness"
hid = "/dev/hidg0"
hid_type = "keyboard"

hid = core.Converter(led, ledf, hid, hid_type)
hid.Analyzer("script.txt")
