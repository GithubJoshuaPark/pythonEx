# utils.py
import random

# 계속하려면 [Enter] 키를 누르세요...
EMOJIS = [
    "💡", "✅️", "⛔", "🚫", "🧩", "✨", "💻", "🐶",
    "🐱", "🐹", "🐰", "🦊", "🐻", "🐼", "🐯", "🦁", "🐮", "🐸",
    "😺", "😸", "😹", "😻", "😼", "😽", "🙀", "🐣", "🐳", "🌏",
    "🍎", "🍳", "⚾️", "🏄", "🚴", "🎧", "🎮", "⚽", "🥊",
    "😊", "🚀", "🐍",
]

def p_pause() -> None:
    """Pause the program until the user presses Enter."""
    input("계속하려면 [Enter] 키를 누르세요...")

def greet(name: str) -> str:
    """Return a greeting for the given name."""
    return f"Hello, {name}!"

def get_random_emojis(count: int = 5) -> list[str]:
    """Return a list of `count` random emojis (duplicates allowed)."""
    if count <= 0:
        return []
    return [random.choice(EMOJIS) for _ in range(count)]

def show_random_emojis(count: int = 5, sep: str = " ") -> None:
    """Print `count` random emojis joined by `sep`."""
    print(sep.join(get_random_emojis(count)))

def show_base_name(file_path: str, isStart: bool=True) -> None:
    """Print the base name of the given file path."""
    import os
    # Print a separator line which has the suitble length with input str before and after the base name for clarity
    # `show_random_emojis` prints to stdout and returns None, so use `get_random_emojis`
    emojis = get_random_emojis(1)
    emoji_str = emojis[0] if emojis else ""
    base_name = " [" + emoji_str + "] " + os.path.basename(file_path) + (" Start" if isStart else " End")
    sep_line = "=" * (len(base_name) + 10)
    print(sep_line)
    print(base_name)
    print(sep_line)

def main() -> None:
    user_name = "World"
    print(greet(user_name))
    # Demonstrate emoji utility
    print("Random emojis:", end=" ")
    show_random_emojis(5)

if __name__ == "__main__":
    main()

# End of file utils.py