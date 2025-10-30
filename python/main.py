# main.py
def greet(name: str) -> str:
    """A simple greeting function."""
    return f"Hello, {name}!"


if __name__ == "__main__":
    # 当直接运行这个文件时，会执行这里的代码
    message = greet("World")
    print(message)
