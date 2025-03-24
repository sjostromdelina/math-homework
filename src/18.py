def greet(name):
    """
    A function to print a greeting message.
    
    Parameters:
    name (str): The name of the person being greeted.
    
    Returns:
    str: A greeting message in the form "Hello [name]!"
    """
    return f"Hello {name}!"

if __name__ == "__main__":
    # Example usage
    print(greet("Alice"))
