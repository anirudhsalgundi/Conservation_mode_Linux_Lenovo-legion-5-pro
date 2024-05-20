import os
print("Toggle conservation mode for your Lenovo Legion 5 pro in Linux.")
print('Enter your option: \na. Turn OFF (Battery will charge till 100%)')
print('b. Turn ON (Battery will charge till 60%')

prompt = str(input('Enter your option (a/b): '))
if prompt == "b":
    os.system('echo 1  | sudo tee /sys/bus/platform/drivers/ideapad_acpi/VPC2004\:00/conservation_mode')
    print('Conservation mode is "ON", battery will charge till 60%')
elif prompt == "a":
    os.system('echo 0  | sudo tee /sys/bus/platform/drivers/ideapad_acpi/VPC2004\:00/conservation_mode')
    print('Conservation mode is "OFF", battery will charge till 100%')
else:
    print(f'\nError: INVALID INPUT "{prompt}". \nValid inputs: "a" or "b". Try again')
    exit()

print("\n\nThank you for using this tool. This script is written by Anirudh Salgundi, if any issues, please contact salgundi.anirudh@gmail.com")