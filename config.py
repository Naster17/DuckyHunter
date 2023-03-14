###############################
#           Config            #
###############################

# Use an tools/led_tester.py or use this manual:
# Find /sys/class/leds/
# In the folders that appear, find the brightness file and change the data from 0 to 255
# Do not forget to save the data that was there before
# Ex: echo 255 > /sys/class/leds/flashlight/brightness
led = "/sys/class/leds/red/brightness"
ledf = "/sys/class/leds/flashlight/brightness"


usb = "/sys/class/power_supply/usb/online"
check_sleep_time = 1

hid = "/dev/hidg0"
hid_type = "keyboard"

path_to_hid = "core/hid-keyboard"

default_delay = 0.01
default_write_delay = 0.02