def read_file(filename):
  try:
      with open(filename, 'r') as file:
          return [line.strip().split(',') for line in file if line.strip()]
  except FileNotFoundError:
      return []    
  except Exception as e:
      print(f"An error occurred while reading '{filename}': {e}")
      return [] 




def save_data(filename, data):
  try:
      # Open the file for writing
      with open(filename, "w") as file:
          # Write the data to the file
          for item in data:
              file.write(str(item) + "\n")
  except Exception as e:
      print(f"An error occurred while saving data to '{filename}': {e}")


# this function is to add the data into the file
def append_data(filename, data):
  try:
      with open(filename, 'a') as file:
          for item in data:
              file.write(",".join(str(x) for x in item) + "\n")
  except FileNotFoundError:
      print(f"File '{filename}' not found.")
  except Exception as e:
      print(f"An error occurred: {e}")
