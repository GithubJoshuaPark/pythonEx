import os
import sys
import subprocess
from typing import List

import utils

# Friendly descriptions for lessons (shown in the menu). Keys are filenames.
DESCRIPTIONS = {
    "lesson01.py": "hello_world",
    "lesson02.py": "variables_and_data_types",
    "lesson03.py": "basic_input_output",
    "lesson04.py": "numbers_and_math_operations",
    "lesson05.py": "strings_and_string_methods",
    "lesson06.py": "if_statements_and_comparisons",
    "lesson07.py": "while_loops_and_for_loops",
    "lesson08.py": "lists_and_list_operations",
    "lesson09.py": "tuples_sets_and_frozensets",
    "lesson10.py": "dictionaries_and_dict_methods",
    "lesson11.py": "defining_and_calling_functions",
    "lesson12.py": "function_parameters_and_return_values",
    "lesson13.py": "lambda_functions_and_builtin_functions",
    "lesson14.py": "modules_imports_and_standard_library",
    "lesson15.py": "working_with_files_read_write",
    "lesson16.py": "exceptions_try_except_finally",
    "lesson17.py": "custom_exceptions_and_error_design",
    "lesson18.py": "classes_and_objects_basics",
    "lesson19.py": "inheritance_polymorphism_and_magic_methods",
    "lesson20.py": "list_comprehensions_generators_and_iterators",
    "lesson21.py": "command_line_args_with_sys_argv",
    "lesson22.py": "logging_and_debugging_basics",
    "lesson23.py": "unit_tests_with_unittest_pytest_intro",
    "lesson24.py": "virtualenv_and_requirements_txt_demo",
    "lesson25.py": "building_and_using_a_simple_package",
    "lesson26.py": "working_with_json_csv_and_apis",
    "lesson27.py": "sqlite_database_access_with_sqlite3",
    "lesson28.py": "asyncio_coroutines_and_tasks_basic",
    "lesson29.py": "simple_web_app_with_fastapi_or_flask",
    "lesson30.py": "numpy_and_pandas_intro_for_data_processing",
    "lesson31.py": "todo_app_using_json_file_crud",
}


def discover_lessons(dir_path: str = "lessons") -> List[str]:
    """Return sorted list of lesson file paths under `dir_path`."""
    if not os.path.isdir(dir_path):
        return []
    files = [f for f in os.listdir(dir_path) if f.endswith(".py") and not f.startswith("__")]
    files.sort()
    return [os.path.join(dir_path, f) for f in files]


def show_menu(lessons: List[str]) -> None:
    """Print a numbered menu of available lessons."""
    print()
    print("======================================================")
    print("Select (1 ~ 31) to run (or 'q' | 'Q' [Enter] to quit):")
    print("======================================================")
    for idx, path in enumerate(lessons, start=1):
        name = os.path.basename(path)
        desc = DESCRIPTIONS.get(name, "")
        emojis = utils.get_random_emojis(1)
        emoji_str = emojis[0] if emojis else ""
        if desc:
            print(f"  {idx:2d}. {emoji_str} {name}  # {desc}")
        else:
            print(f"  {idx:2d}. {emoji_str} {name}")
    print("======================================================")
    print("  q | Q [Enter] to Quit")
    print("======================================================")

def run_lesson(path: str) -> None:
    """Execute the given lesson file in a subprocess using the current Python interpreter."""
    print()
    try:
        module_name = os.path.splitext(os.path.basename(path))[0]
        # run as package module so top-level imports (e.g. `import utils`) resolve
        res = subprocess.run([sys.executable, "-m", f"lessons.{module_name}"])
        if res.returncode != 0:
            print(f"Lesson exited with code {res.returncode}")
    except FileNotFoundError:
        print(f"Could not find lesson file: {path}")
    except Exception as e:
        print(f"Error running lesson: {e}")
    finally:
        pass

def main() -> None:
    lessons = discover_lessons()
    if not lessons:
        print("No lessons found in the 'lessons/' directory.")
        return

    while True:
        show_menu(lessons)
        choice = input("Enter choice: ").strip()
        if choice.lower() in {"q", "Q", "quit", "exit"}:
            print("Bye.")
            break
        if not choice.isdigit():
            print("Please enter a number from the menu or 'q' | 'Q' to quit.")
            continue
        idx = int(choice) - 1
        if idx < 0 or idx >= len(lessons):
            print("Invalid selection; try again.")
            continue
        lesson_path = lessons[idx]
        run_lesson(lesson_path)
        # pause before showing menu again
        utils.p_pause()


if __name__ == "__main__":
    utils.show_base_name(__file__, True)
    main()
    utils.show_base_name(__file__, False)