# lessons/lesson31.py
import json
import os
import time
import utils

utils.show_base_name(__file__, True)

# JSON 파일 경로 정의
TODO_FILE = "todo_list.json"

# --- 데이터 처리 함수 ---

def load_tasks():
    """
    JSON 파일에서 할 일 목록을 로드합니다. 파일이 없으면 빈 리스트를 반환합니다.
    """
    if not os.path.exists(TODO_FILE):
        return []
    try:
        with open(TODO_FILE, 'r', encoding='utf-8') as f:
            tasks = json.load(f)
            return tasks
    except (json.JSONDecodeError, FileNotFoundError):
        return []

def save_tasks(tasks):
    """
    할 일 목록을 JSON 파일에 저장합니다.
    """
    with open(TODO_FILE, 'w', encoding='utf-8') as f:
        json.dump(tasks, f, indent=4, ensure_ascii=False)

def get_next_id(tasks):
    """
    새로운 할 일에 대한 다음 ID를 계산합니다.
    """
    if not tasks:
        return 1
    return max(task['id'] for task in tasks) + 1

# --- CRUD 및 UI 함수 ---

def add_task(tasks):
    """
    새로운 할 일을 추가합니다.
    """
    description = input("추가할 할 일 내용을 입력하세요: ").strip()
    if description:
        new_task = {
            "id": get_next_id(tasks),
            "description": description,
            "done": False,
            "created_at": time.strftime("%Y-%m-%d %H:%M:%S")
        }
        tasks.append(new_task)
        save_tasks(tasks)
        print(f"'{description}' 할 일이 추가되었습니다.")
    else:
        print("할 일 내용이 비어있습니다. 추가하지 않았습니다.")

def list_tasks(tasks):
    """
    모든 할 일 목록을 출력합니다.
    """
    print("\n--- TODO 목록 ---")
    if not tasks:
        print("할 일이 없습니다.")
    else:
        for task in sorted(tasks, key=lambda x: x['id']):
            status = "✅" if task['done'] else "❌"
            print(f"{status} [{task['id']}] {task['description']}")
    print("-----------------")

def mark_task_done(tasks):
    """
    특정 할 일을 완료 상태로 변경합니다.
    """
    try:
        task_id = int(input("완료로 표시할 할 일의 ID를 입력하세요: "))
        task_found = False
        for task in tasks:
            if task['id'] == task_id:
                task['done'] = True
                task_found = True
                save_tasks(tasks)
                print(f"[{task_id}] 할 일을 완료로 표시했습니다.")
                break
        if not task_found:
            print(f"ID {task_id}에 해당하는 할 일을 찾을 수 없습니다.")
    except ValueError:
        print("잘못된 ID입니다. 숫자를 입력하세요.")

def delete_task(tasks):
    """
    특정 할 일을 삭제합니다.
    """
    try:
        task_id = int(input("삭제할 할 일의 ID를 입력하세요: "))
        original_count = len(tasks)
        tasks_to_keep = [task for task in tasks if task['id'] != task_id]

        if len(tasks_to_keep) < original_count:
            save_tasks(tasks_to_keep)
            print(f"[{task_id}] 할 일이 삭제되었습니다.")
        else:
            print(f"ID {task_id}에 해당하는 할 일을 찾을 수 없습니다.")
    except ValueError:
        print("잘못된 ID입니다. 숫자를 입력하세요.")

def print_menu():
    """
    사용자 메뉴를 출력합니다.
    """
    print("\n--- 메뉴 ---")
    print("1. 할 일 목록 보기")
    print("2. 할 일 추가하기")
    print("3. 할 일 완료하기")
    print("4. 할 일 삭제하기")
    print("5. 종료")
    print("------------")

def main():
    """
    TODO 애플리케이션의 메인 루프를 실행합니다.
    """
    print("--- Lesson 31: JSON 파일을 사용한 TODO 앱 (CRUD) ---")

    tasks = load_tasks()

    while True:
        print_menu()
        choice = input("선택: ").strip()

        if choice == '1':
            list_tasks(tasks)
        elif choice == '2':
            add_task(tasks)
            tasks = load_tasks() # Re-load tasks after modification
        elif choice == '3':
            mark_task_done(tasks)
            tasks = load_tasks()
        elif choice == '4':
            delete_task(tasks)
            tasks = load_tasks() # Re-load tasks to get the updated list
        elif choice == '5':
            print("TODO 앱을 종료합니다.")
            break
        else:
            print("잘못된 선택입니다. 메뉴에서 1-5 사이의 숫자를 입력하세요.")

        # 작은 딜레이를 주어 사용자 경험을 개선
        time.sleep(1)

    # 애플리케이션 종료 시 생성된 파일 정리
    if os.path.exists(TODO_FILE):
        os.remove(TODO_FILE)
        print(f"\n정리: '{TODO_FILE}' 파일이 삭제되었습니다.")

    utils.show_base_name(__file__, False)

if __name__ == "__main__":
    main()
else:
    utils.show_base_name(__file__, False)