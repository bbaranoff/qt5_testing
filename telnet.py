import telnetlib
HOST= "0"
tn = telnetlib.Telnet(HOST, "30000")
tn.read_until("commands")
tn.write(b"help\n")
tn.write(b"write rx_gain 30\n")
tn.write(b"write use_cnfg_file 1\n")

