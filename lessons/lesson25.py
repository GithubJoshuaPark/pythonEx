# lessons/lesson25.py
import os
import sys
import utils

utils.show_base_name(__file__, True)

def main():
    """
    이 수업은 간단한 파이썬 패키지를 만들고 사용하는 방법을 시연합니다.
    """
    print("--- Lesson 25: 간단한 패키지 구축 및 사용 ---")

    # 1. 파이썬 패키지란?
    # 파이썬 패키지는 관련된 모듈을 단일 디렉토리 계층 구조로 구성하는 방법입니다.
    # 이는 더 구조적이고 관리하기 쉬운 코드베이스를 가능하게 합니다.
    # 디렉토리에 __init__.py 파일이 포함되어 있으면 파이썬 패키지로 간주됩니다.

    print("\n--- 1. 파이썬 패키지 이해하기 ---")
    print("패키지는 이름 충돌을 방지하고 코드 재사용성을 향상시킵니다.")
    print("이 수업을 위해 다음과 같은 가상 패키지 구조를 만들었습니다:")
    print("  lessons/")
    print("    my_simple_package/")
    print("      __init__.py    # 'my_simple_package'를 패키지로 만듭니다")
    print("      my_module.py   # 패키지 내의 모듈")
    print("-" * 20)

    # 2. 간단한 패키지의 구조
    # - 최상위 패키지 디렉토리 (예: 'my_simple_package')
    # - __init__.py: 디렉토리를 파이썬 패키지로 표시합니다. 비어있을 수도 있고,
    #   패키지가 임포트될 때 무엇이 임포트될지 정의할 수도 있습니다.
    # - 모듈 (.py 파일)에는 함수, 클래스 등이 포함됩니다.

    print("\n--- 2. 패키지 구조 설명 ---")
    # 'my_simple_package'의 __init__.py 파일을 읽어와 내용을 출력합니다.
    init_file_path = os.path.join(os.path.dirname(__file__), "my_simple_package", "__init__.py")
    try:
        with open(init_file_path, 'r', encoding='utf-8') as f:
            init_content = f.read()
        print("  my_simple_package/__init__.py 내용:")
        print("  " + init_content.replace('\n', '\n  '))
    except FileNotFoundError:
        print(f"  오류: {init_file_path} 파일을 찾을 수 없습니다.")

    # 'my_simple_package'의 my_module.py 파일을 읽어와 내용을 출력합니다.
    module_file_path = os.path.join(os.path.dirname(__file__), "my_simple_package", "my_module.py")
    try:
        with open(module_file_path, 'r', encoding='utf-8') as f:
            module_content = f.read()
        print("  my_simple_package/my_module.py 내용:")
        print("  " + module_content.replace('\n', '\n  '))
    except FileNotFoundError:
        print(f"  오류: {module_file_path} 파일을 찾을 수 없습니다.")

    print("-" * 20)

    # 3. 패키지 사용하기 (설치 후 또는 sys.path 수정 후)
    # 실제 시나리오에서는 패키지를 pip로 설치하여 사용하지만,
    # 이 수업에서는 'lessons' 디렉토리가 sys.path에 추가되어 있으므로,
    # 'my_simple_package'를 직접 임포트할 수 있습니다.
    print("\n--- 3. 패키지 사용하기 ---")

    # 'lessons' 디렉토리는 이미 `main.py`에 의해 `sys.path`에 추가됩니다.
    # 따라서, `my_simple_package`를 마치 'lessons' 내의 하위 패키지처럼 임포트할 수 있습니다.
    try:
        # 'lessons' 디렉토리를 기준으로 'my_simple_package'를 임포트합니다.
        # 실제 환경에서는 `pip install` 후에 `import my_package.my_module` 형태로 사용합니다.
        # 이 데모에서는 lessons 패키지 내부에 my_simple_package가 있다고 가정합니다.
        from lessons import my_simple_package
        from lessons.my_simple_package import my_module

        print(f"  my_simple_package.__version__: {my_simple_package.__version__}")
        print(f"  my_simple_package.__author__: {my_simple_package.__author__}")

        print(f"  {my_module.greet('Learner')}")
        print(f"  5와 7의 합: {my_module.add(5, 7)}")
        print(f"  {my_module.farewell('Python')}")

    except ImportError as e:
        print(f"  my_simple_package 모듈을 임포트할 수 없습니다. 오류: {e}")
        print("  `lessons/my_simple_package/` 디렉토리가 존재하며,")
        print("  `__init__.py` 및 `my_module.py` 파일을 포함하고 있는지 확인하십시오.")
    except Exception as e:
        print(f"  예상치 못한 오류가 발생했습니다: {e}")

    print("-" * 20)

    # 4. 패키징 및 배포 (개념적 개요)
    # pip를 통해 패키지를 설치 가능하게 하고 공유하려면 일반적으로
    # 'setuptools'와 'setup.py' 또는 'pyproject.toml' 파일을 사용합니다.

    print("\n--- 4. 개념: 패키징 및 배포 ---")
    print("'setup.py' 파일은 패키지, 메타데이터 및 종속성을 설명합니다.")
    print("예시 'setup.py' 내용 (프로젝트 루트에 있어야 하며 여기에 있는 것이 아님):")
    print("""
# setup.py (예시)
from setuptools import setup, find_packages

setup(
    name='my-awesome-package',
    version='0.1.0',
    author='당신의 이름',
    author_email='your.email@example.com',
    description='내 패키지에 대한 간략한 설명',
    long_description=open('README.md', encoding='utf-8').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/yourusername/my-awesome-package',
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
    install_requires=[
        'requests>=2.25.1',
        'numpy>=1.20.0',
    ],
)
""")
    print("\n개발을 위해 패키지를 로컬에 설치하는 방법:")
    print("  pip install -e .  # 편집 가능한 설치")
    print("일반 패키지로 설치하는 방법:")
    print("  pip install .")
    print("배포 패키지 (소스 및 휠)를 빌드하는 방법:")
    print("  python setup.py sdist bdist_wheel")
    print("그런 다음 'twine'을 사용하여 PyPI에 업로드할 수 있습니다.")
    print("\n최신 파이썬 프로젝트는 패키징을 위해 'poetry' 또는 'flit'과 함께 'pyproject.toml'을 사용하는 경우가 많습니다.")
    print("개념은 유사합니다: 메타데이터와 종속성을 정의합니다.")
    print("-" * 20)

    utils.show_base_name(__file__, False)

if __name__ == "__main__":
    main()
else:
    utils.show_base_name(__file__, False)