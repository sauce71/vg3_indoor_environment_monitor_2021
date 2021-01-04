import network, time
sta_if = network.WLAN(network.STA_IF)
sta_if.active(True)
sta_if.scan() # Scan for available access points
sta_if.connect("sidespeilet_2G", "Tinnea010306") # Connect to an AP
retries = 0
while (not sta_if.isconnected()) and (retries < 300):
    time.sleep(0.1)
    retries +=1
print(sta_if.ifconfig())