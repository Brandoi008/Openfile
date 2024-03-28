def write_to_file():
 
  try:
    with open("my_file.txt", "w") as file: 
      file.write("This is the first line of text.\n")
      file.write("Here's another line with a number: 42\n")
      file.write("And a final line with a mix: String and 3.14\n")
      print("Successfully wrote content to my_file.txt")
  except FileNotFoundError:
    print("Error: File 'my_file.txt' not found.")
  except PermissionError:
    print("Error: Insufficient permissions to write to the file.")
  except Exception as e:  # Catch other unexpected errors
    print(f"Unexpected error: {e}")

def read_file():
  """
  Reads the contents of "my_file.txt" and displays them.
  """
  try:
    with open("my_file.txt", "r") as file:  # Open in read mode
      content = file.read()
      print("Contents of my_file.txt:")
      print(content)
  except FileNotFoundError:
    print("Error: File 'my_file.txt' not found.")
  except PermissionError:
    print("Error: Insufficient permissions to read the file.")
  except Exception as e:
    print(f"Unexpected error: {e}")

def append_to_file():
  """
  Opens "my_file.txt" in append mode and adds more content.
  """
  try:
    with open("my_file.txt", "a") as file:  # Open in append mode
      file.write("\nHere are some additional lines:\n")
      file.write("Line 4 with another number: 100\n")
      file.write("Line 5 with a floating-point value: 2.718\n")
      print("Successfully appended content to my_file.txt")
  except PermissionError:
    print("Error: Insufficient permissions to append to the file.")
  except Exception as e:
    print(f"Unexpected error: {e}")

if __name__ == "__main__":
  write_to_file()
  read_file()
  append_to_file()
  read_file()  # Read again to show appended content
