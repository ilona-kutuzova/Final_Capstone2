import random

#parts status inputs
input_code_firmware = random.randint(0,2)
input_code_software = random.randint(0,2)
input_code_antennas = random.randint(0,2)
input_code_camera = random.randint(0,2)
input_code_arms = random.randint(0,2)
input_code_torso = random.randint(0,2)
input_code_connection = random.randint(0,2)

#Tuple for Results
global boot_results
boot_results = ("FAIL] SCOUT cannot operate.","OK]","WARN] SCOUT service degraded. Repair or replace soon.")

#creating ScoutRobot class
class ScoutRobot():
  
  #creating __init__() method
  def __init__(self, firmware_result, software_result, antennas_result, camera_result, arms_result, torso_result, connection_result):
    self.firmware_result = firmware_result
    self.software_result = software_result
    self.antennas_result = antennas_result
    self.camera_result = camera_result
    self.arms_result = arms_result
    self.torso_result = torso_result
    self.connection_result = connection_result
    

  #method to check firmware status
  def check_firmware(self, input_code):
    if (input_code_firmware == 0):
      self.firmware_result = boot_results[0]
    elif (input_code_firmware == 1):
      self.firmware_result = boot_results[1]
    else:
      self.firmware_result = boot_results[2]
      
  #method to check software status
  def check_software(self, input_code):
    if (input_code_software == 0):
      self.software_result = boot_results[0]
    elif (input_code_software == 1):
      self.software_result = boot_results[1]
    else:
      self.software_result = boot_results[2]

  #method to check antennas
  def check_antennas(self, input_code):
    if (input_code_antennas == 0):
      self.antennas_result = boot_results[0]
    elif (input_code_antennas == 1):
      self.antennas_result = boot_results[1]
    else:
      self.antennas_result = boot_results[2]

  #method to check camera apparatus
  def check_camera(self, input_code):
    if (input_code_camera == 0):
      self.camera_result = boot_results[0]
    elif (input_code_camera == 1):
      self.camera_result = boot_results[1]
    else:
      self.camera_result = boot_results[2]

  #method to check arms
  def check_arms(self, input_code):
    if (input_code_arms == 0):
      self.arms_result = boot_results[0]
    elif (input_code_arms == 1):
      self.arms_result = boot_results[1]
    else:
      self.arms_result = boot_results[2]

  #method to check torso
  def check_torso(self, input_code):
    if (input_code_torso == 0):
      self.torso_result = boot_results[0]
    elif (input_code_torso == 1):
      self.torso_result = boot_results[1]
    else:
      self.torso_result = boot_results[2]

  #method to check connection
  def check_connection(self, input_code):
    if (input_code_connection == 0):
      self.connection_result = boot_results[0]
    elif (input_code_connection == 1):
      self.connection_result = boot_results[1]
    else:
      self.connection_result = boot_results[2]

#initiating ScoutRobot class object 
robot = ScoutRobot(input_code_firmware, input_code_software, input_code_antennas, input_code_camera, input_code_arms, input_code_torso, input_code_connection)

#checking all parts for robot
robot.check_firmware(input_code_firmware)
robot.check_software(input_code_software)
robot.check_antennas(input_code_antennas)
robot.check_camera(input_code_camera)
robot.check_arms(input_code_arms)
robot.check_torso(input_code_torso)
robot.check_connection(input_code_connection)

#declaring the counter for FAIL status
fail_counter = 0

if robot.antennas_result == boot_results[0]:
  fail_counter = fail_counter + 1 
if robot.camera_result == boot_results[0]:
  fail_counter = fail_counter + 1 
if robot.arms_result == boot_results[0]:
  fail_counter = fail_counter + 1 
if robot.torso_result == boot_results[0]:
 fail_counter = fail_counter + 1 
if robot.connection_result == boot_results[0]:
  fail_counter = fail_counter + 1 
#declaring the counter for OK status
ok_counter = 0

if robot.antennas_result == boot_results[1]:
  ok_counter = ok_counter + 1
if robot.camera_result == boot_results[1]:
  ok_counter = ok_counter + 1
if robot.arms_result == boot_results[1]:
  ok_counter = ok_counter + 1
if robot.torso_result == boot_results[1]:
  ok_counter = ok_counter + 1
if robot.connection_result == boot_results[1]:
  ok_counter = ok_counter + 1

ok_counter = str(ok_counter)

#declaring the counter for WARN status
warn_counter = 0

if robot.antennas_result == boot_results[2]:
  warn_counter = warn_counter + 1 
if robot.camera_result == boot_results[2]:
  warn_counter = warn_counter + 1 
if robot.arms_result == boot_results[2]:
  warn_counter = warn_counter + 1 
if robot.torso_result == boot_results[2]:
  warn_counter = warn_counter + 1 
if robot.connection_result == boot_results[2]:
  warn_counter = warn_counter + 1 

warn_counter = str(warn_counter)

#checking the critical statuses for final conclusion
#whether the robot is operational
if fail_counter >= 1 or input_code_connection == 0:
  final_message = "\nSCOUNT CANNOT OPERATE: SHUTTING DOWN"
else:
  final_message = "\nSCOUT IS OPERATIONAL"

fail_counter = str(fail_counter)

#printing the final result
print("Starting up....", "\nFIRMWARE LOADED [" + robot.firmware_result,
     "\nSOFTWARE LOADED [" + robot.software_result,
     "\n",
     "\nBEGIN BOOT SEQUENCE CHECKS",
     "\n--------------------------",
     "\nChecking antennas (L/R):          [" + robot.antennas_result,
     "\nChecking camera apparatus:        [" + robot.camera_result,
     "\nChecking arms (L/R):              [" + robot.arms_result,
     "\nChecking torso:                   [" + robot.torso_result,
     "\nChecking connection:              [" + robot.connection_result,
     "\n",
     "\nChecks completed with: " 
      + ok_counter + " [OK]  " + warn_counter + " [WARN]  " 
      + fail_counter + " [FAIL]" + final_message)
