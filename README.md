# Knockbell
Ever wished your door would ring a bell when knocked? Ever want to really confuse visitors and tradespeople? Then this is the project for you.


# Components
Written to run under FreeRTOS on an ESP32.

Also requires a power supply of some kind, and a cheap piezo transducer of the sort that can be picked up for 99p here in the UK.


# Hardware setup

* Bodge the piezo pickup onto the back of the door somehow. Contact adhesive is a good option. Hook up between D34 and GND on the ESP32.
* Maybe solder things up if you really care. 2.54mm jumpers and some blue-tac also work if you're a lazy brute.
* Profit?

# Software setup

## On ESP32

The ESP32 SW is hacked together using a bunch of the examples that ship with the devkit. Everything is in one file. The WiFi network settings need configuring in `menuconfig` on the host. The SW has a hard-coded IP address and port number to send the packets to.

## On host PC

Assuming Linux. If you want to use something else, I have neither the intention nor capacity to provide support.

Knock packets are sent to a single IP address and port over UDP. The python script is a real simple UDP server which should be run on this machine. It contains a list of IP addresses to ssh into and run an `espeak` command to trigger a spoken warning. It assumes that ssh keys have been preshared.

Possible to configure the UDP server to run as something like a `systemd` service; dead simple `systemd` unit file hooked up to runlevel 5 would do it.

# Calibrarion

The knock detection is dead simple, but may need some calibration for specific doors. My piezo registers a voltage of ~400mV normally, and >1100mV when knocked. These thresholds may be different for you.

We can't just trigger every time we see a peak, as things like opening or closing the door would also be liable to register as knocks. So instead, we need to see at least three peaks, no more than 30 samples apart and no less than 5 samples apart. This seems to work well for me. People in other parts of the world may knock differently. The logic for this is right at the bottom of the file, and is dead simple.

# Known issues

After sending too many knocks in a short period of time, I start seeing network issues. It seems to be related to the size of the state table in my router - the WiFi network the ESP32 is on is firewalled off from the network  my personal devices are on, so there is a NAT in the way. Maybe I'm being too simplistic about how I'm handling network traffic. If you care than knocking tens of times per minute causes failures and can be bothered to fix it, please submit a PR.
