def read_file(filename):
  try:
      with open(filename, 'r') as file:
          return [line.strip().split(',') for line in file if line.strip()]
  except FileNotFoundError:
      return []    

def save_data(filename, data):
  # Open the file for writing
  with open(filename, "w") as file:
      # Write the data to the file
      for item in data:
          file.write(item + "\n")

# this function is to add the data into the file
def append_data(filename, data):
  with open(filename, 'a') as file:
      for item in data:
          file.write(",".join(str(x) for x in item) + "\n")
