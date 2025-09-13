def sort(width:int, height:int, length:int, mass:int) -> str:

    for name, value in zip(["width", "height", "length", "mass"], [width, height, length, mass]):
        if not isinstance(value, (int, float)):
            raise TypeError(f"{name} must be a number, got {type(value).__name__}")
        if value <= 0:
            raise ValueError(f"{name} must be a positive number, got {value}")
        
    bulky = False
    heavy = False

    if any(v >= 150 for v in [width, height, length]) or (width * height * length >= 1000000):
        bulky = True
    if mass >= 20:
        heavy = True
    
    if bulky and heavy:
        return 'REJECTED'
    elif bulky or heavy:
        return 'SPECIAL'
    else:
        return 'STANDARD'
    

def main():
    test_cases = [
        ((100, 100, 10, 10), "STANDARD"),
        ((200, 50, 50, 10), "SPECIAL"),
        ((100, 100, 100, 25), "REJECTED"),
        ((200, 200, 200, 30), "REJECTED"),
    ]

    for i, (inputs, expected) in enumerate(test_cases, 1):
        try:
            result = sort(*inputs)
            print(f"Test {i}: sort{inputs} -> {result} (expected: {expected})")
        except Exception as e:
            print(f"Test {i}: sort{inputs} -> raised {type(e).__name__}: {e}")


if __name__ == "__main__":
    main()