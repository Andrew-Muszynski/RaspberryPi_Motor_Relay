# Raspberry Pi Motor Relay Lab

Control relay 1 on a Pimoroni Automation HAT using a Raspberry Pi 4. Start with normally open (NO), change the duration, then compare the same program using normally closed (NC).

**Complete Lab 2 first.** Bring your own bootable Raspberry Pi OS SD card. The Pi, HAT, motor, and prepared power supply stay at the workstation. Demonstrate both configurations to a TA, then respond in the Brightspace discussion thread.

## 1. Prepare the station

With Pi power disconnected, insert your SD card. Start with the prepared supply lead on relay 1 **COM** and the motor lead on **NO**. Leave NC empty. The two black wires stay joined outside the HAT.

Leave the 12 V motor supply unplugged for software setup and the first relay test. Power the Pi using its own USB-C supply. Do not connect 12 V to Pi GPIO or HAT power pins. Use only the motor assembly checked by a TA; the motor, contacts, wiring, fuse, and suppression must suit the load.

One station has an inline switch. OFF interrupts motor power; ON allows the relay to control it. Still unplug the 12 V supply before moving wires.

## 2. Install the Automation HAT library

Run these commands in the Pi terminal, one line at a time. This installs Git as well as downloading the HAT installer.

```bash
sudo apt update
sudo apt install -y git
cd ~
git clone https://github.com/pimoroni/automation-hat
cd ~/automation-hat
./install.sh
sudo reboot
```

Follow the installer prompts to enable interfaces and create the `pimoroni` Python environment. If the `automation-hat` folder already exists, skip cloning and run `./install.sh` inside that folder. If already installed on this SD card, skip this section.

**Git missing?** A GitHub account does not install Git on your Pi. Check with `git --version`. If the command is not found, run `sudo apt update`, then `sudo apt install -y git`, and check again. Downloading a public repository does not require Git username/email configuration or a GitHub login.

## 3. Download this lab

Download the lab from [Andrew-Muszynski/RaspberryPi_Motor_Relay](https://github.com/Andrew-Muszynski/RaspberryPi_Motor_Relay).

```bash
git clone https://github.com/Andrew-Muszynski/RaspberryPi_Motor_Relay.git \
  ~/motor-relay-lab
cd ~/motor-relay-lab
```

Clone once per SD card. For an existing copy, run `git pull --ff-only` from that folder before making edits. If Git cannot update because of local changes, keep your work and ask a TA; do not discard it.

## 4. Run the first relay test

After reboot, open Terminal and run:

```bash
source ~/.virtualenvs/pimoroni/bin/activate
cd ~/motor-relay-lab
python motor_test.py
```

Keep the 12 V supply unplugged. Type uppercase `TEST` and press Enter. Relay 1 should click on, then off about two seconds later. Any other input cancels. Activate the Python environment again in every new terminal.

Ask a TA to check the setup before connecting motor power. Secure the motor and keep its shaft clear. On NO, the motor runs during the relay pulse and stops afterward.

## 5. Change one value

Open the script:

```bash
nano motor_test.py
```

**Change only this number near the top:**

```python
RUN_SECONDS = 2
```

1. Change `2` to `3`, save, and run the script again.
2. Change `3` to `6`, save, and run it again.
3. Measure the approximate motor run times and show the six-second NO test to a TA.

Save in nano with **Ctrl+O**, then **Enter**. Exit with **Ctrl+X**. Run again with `python motor_test.py`. The prompt uses `RUN_SECONDS` automatically, so no other line needs editing. Keep this value positive. Leave `relay.one`, `try`, `except`, and `finally` unchanged.

### Pseudocode

```text
Set RUN_SECONDS to the required relay pulse duration.
Set relay 1 OFF.
Wait for the user to type TEST.
If TEST was entered:
    Turn relay 1 ON.
    Wait RUN_SECONDS seconds.
Otherwise:
    Cancel the pulse.
On completion or a normal Python interruption:
    Turn relay 1 OFF.
```

`RUN_SECONDS` controls duration, not motor speed. Do not use rapid switching or PWM with this relay.

## 6. Compare normally closed

1. Unplug the 12 V supply. Run `sudo poweroff`, wait for shutdown, and disconnect Pi power.
2. Move only the motor lead from relay 1 **NO** to **NC**. Keep COM unchanged and leave NO empty. Ask a TA to check it.
3. Reconnect Pi power, log in, activate the environment, and start the same script. Leave `RUN_SECONDS = 6`.
4. With a TA present, connect motor power and enable the inline switch if fitted. **On NC, the motor can start immediately, including while the program waits for TEST.**
5. Type `TEST`. Observe the six-second interruption in motor power, followed by power returning. Show this behavior to a TA, then switch OFF if fitted and unplug the 12 V supply.

| Relay state | COM connection | Motor on NO | Motor on NC |
| --- | --- | --- | --- |
| OFF, coil not energized | NC | Unpowered | Powered |
| ON, coil energized | NO | Powered | Unpowered |

This table assumes the 12 V supply is connected and the inline switch, if fitted, is ON. The motor may coast briefly after power is interrupted.

**Relay OFF does not always mean motor OFF.** With NC wiring, `relay.off()` reconnects motor power. Ctrl+C, cancelling the prompt, and program exit are not motor-stop controls on NC. Use the inline switch or unplug the 12 V supply. The `finally` block handles normal completion and Python interruptions; it cannot guarantee a safe state during a Pi freeze, forced process kill, or contact failure.

## 7. Finish

After showing both configurations to a TA, follow the discussion prompts on Brightspace. Keep your measured durations and observations.

Unplug the 12 V supply, shut down the Pi, and disconnect Pi power. Return the motor lead to **NO**, leaving COM unchanged and NC empty. Remove your SD card after shutdown. Leave both supplies disconnected for the next student.

## Quick help

- **No module named automationhat:** activate the `pimoroni` environment in this terminal, then use `python`, not `sudo python`.
- **Environment path missing:** complete the HAT installer and create its Python environment.
- **Relay clicks but motor does not run:** unplug motor power and ask a TA to check the leads, supply, and inline switch.
- **Motor runs after the script exits:** check whether it is wired to NC. Disconnect motor power before changing anything.

Library installation reference: https://github.com/pimoroni/automation-hat
