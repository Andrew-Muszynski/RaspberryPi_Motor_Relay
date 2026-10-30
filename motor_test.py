import time
import automationhat

# STUDENT EDIT: Change ONLY the number below, first to 3, then to 6.
RUN_SECONDS = 2  # How long the RELAY stays energized, in seconds.

# Pseudocode: wait for TEST -> relay ON -> wait RUN_SECONDS -> relay OFF.
# NO wiring: motor runs during the wait. NC wiring: motor pauses instead.
# On NC, relay OFF powers the motor; unplug 12 V to stop it.
relay = automationhat.relay.one

try:
    relay.off()
    answer = input(f"Type TEST for a {RUN_SECONDS}-second relay pulse: ")
    if answer.strip() == "TEST":
        print("Relay 1 ON")
        relay.on()
        time.sleep(RUN_SECONDS)
    else:
        print("Cancelled.")
except (KeyboardInterrupt, EOFError):
    print("\nInterrupted.")
finally:
    relay.off()
    print("Relay 1 OFF")
