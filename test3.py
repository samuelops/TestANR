from nornir import InitNornir
from nornir_utils.plugins.functions import print_result, print_title
from nornir_netmiko import netmiko_send_config, netmiko_send_command

def baseconfig(anr):
    anr.run(task=netmiko_send_config, config_file = "config_text")
    anr.run(task=netmiko_send_command, command_string = "show run | sec user")

nr = InitNornir(
    config_file="config.yaml", dry_run=True
    )

devices = nr.filter(rdss=123)
results = devices.run(task=baseconfig)

print_title("DEPLOYING AUTOMATED BASELINE CONFIGURATION")
print_result(results)