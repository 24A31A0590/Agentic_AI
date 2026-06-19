import math

def generate_complexity_data(complexity_str: str) -> list:
    """Generates data points representing the growth curve of a given Big-O complexity."""
    y_values = []
    comp = complexity_str.lower().replace(" ", "")
    
    for n in range(1, 101):
        if "o(1)" in comp:
            y = 1
        elif "logn" in comp:
            y = math.log2(n)
        elif "nlogn" in comp:
            y = n * math.log2(n)
        elif "n^2" in comp or "n2" in comp:
            y = n ** 2
        elif "n^3" in comp or "n3" in comp:
            y = n ** 3
        elif "2^n" in comp:
            y = 2 ** (n / 10) 
        elif "n!" in comp:
            y = 3 ** (n / 10)
        else: # Default to O(N)
            y = n
            
        y_values.append(y)
        
    return y_values
