import math


def do_turkey_math(temp_1, time_1, temp_2, time_2, oven_temp):
  valid_input = validate_inputs(temp_1, time_1, temp_2, time_2, oven_temp)
  if not valid_input:
    return False

  time_1 = int(time_1)
  temp_1 = int(temp_1)
  time_2 = int(time_2)
  temp_2 = int(temp_2)
  oven_temp = int(oven_temp)

  # Newton's law of cooling
  # dT/dt = -k(T-T0)
  #   where dT is the change in Temp
  #   where dt is the change in time
  #   where T is the current temperature
  #   where T0 is the ambient temperature
  #   where k is a constant
  # Solving the diffEq:
  # T = Ce^(-kt) + T0
  # T0 is the oven temp
  # T is the desired temperature
  # Get 2 (temperature, time) points and use that to solve for
  # C and k
  # Then determine at which time the body will reach the desired temp.

  ##
  C = temp_1 - oven_temp  # Assumes time_1 is 0
  time_delta = time_2 - time_1
  k = math.log((temp_2 - oven_temp)/C) / time_delta

  DESIRED_TEMP = 161
  time_remaining = math.log((DESIRED_TEMP - oven_temp)/C)/k
  # Make it clear to the user that this is the time from t1.
  # Use clocks to make this consistent.
  # Assumes that t2 was taken right now.
  time_remaining -= time_2

  return {
      'time_remaining': time_remaining,
      'temp_1': temp_1,
      'time_1': time_1,
      'temp_2': temp_2,
      'time_2': time_2,
      'oven_temp': oven_temp
  }


def validate_inputs(temp_1, time_1, temp_2, time_2, oven_temp):
  # All values are defined
  if not temp_1 or not temp_2 or not time_1 or not time_2:
    return False

  # Temps are numbers
  # Time is number
  # Time is real time
  # Time 2 is greater than Time 1
  # Temp 2 is greater than Temp 1
  # Oven temp is in a reasonable oven temp range

  return True
