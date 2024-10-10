import socket
import time

def get_sequence_from_server(host, port):
    try:
        # Create a socket connection
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((host, port))
            time.sleep(0.5)  # Allow time for the server to respond
            data = s.recv(1024).decode()  # Adjust buffer size as needed
            print(f"Received data: {data}")
            
            # Extract the sequence from the data
            startpos = data.find("[")
            endpos = data.find("]")
            if startpos == -1 or endpos == -1:
                print("Invalid data format.")
                return []
            
            seq = data[startpos + 1:endpos]
            print(f"Extracted sequence: {seq}")
            
            # Sanitize and convert the sequence to integers
            numbers = []
            for item in seq.split(','):
                try:
                    # Strip whitespace and quotes, then convert to int
                    number = int(item.strip().strip('"').strip("'"))
                    numbers.append(number)
                except ValueError:
                    print(f"Skipping invalid number: {item}")
            
            return numbers
    except Exception as e:
        print(f"An error occurred: {e}")
        return []

def find_odd_one_out(numbers):
    print(numbers)
    count = {}
    diff = numbers[1] - numbers[0]
    print(diff)
    for number in numbers:
        count[number] = count.get(number, 0) + 1
    
    for number, cnt in count.items():
        if cnt == 1:
            return number

if __name__ == "__main__":
    host = '167.71.136.12'
    port = 5099
    sequence = get_sequence_from_server(host, port)
    
    if sequence:
        odd_one_out = find_odd_one_out(sequence)
        print(f"The odd number out is: {odd_one_out}")

