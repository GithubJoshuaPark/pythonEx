# lessons/lesson19.py
import utils

utils.show_base_name(__file__, True)

def main():
    """
    이 수업은 파이썬의 상속, 다형성, 매직 메서드에 대해 다룹니다.
    """
    print("--- Lesson 19: 상속, 다형성, 매직 메서드 ---")

    # --- 1부: 상속 ---
    # 상속은 다른 클래스(부모/기반 클래스)의 모든 메서드와
    # 속성을 상속받는 클래스를 정의할 수 있게 해줍니다.

    print("\n--- 1부: 상속 ---")

    class Animal:
        """모든 동물을 위한 기본 클래스입니다."""
        def __init__(self, name):
            self.name = name

        def speak(self):
            raise NotImplementedError("서브클래스에서 추상 메서드를 구현해야 합니다")

        def eat(self):
            print(f"{self.name}이(가) 먹고 있습니다.")

    class Dog(Animal):
        """Animal을 상속받는 Dog 클래스입니다."""
        def __init__(self, name, breed):
            super().__init__(name) # 부모 클래스의 생성자 호출
            self.breed = breed

        def speak(self): # 메서드 오버라이딩
            return f"{self.name}가 멍멍 짖습니다!"

        def fetch(self):
            return f"{self.name}이(가) 공을 가져오고 있습니다."

    class Cat(Animal):
        """Animal을 상속받는 Cat 클래스입니다."""
        def __init__(self, name, color):
            super().__init__(name)
            self.color = color

        def speak(self): # 메서드 오버라이딩
            return f"{self.name}가 야옹합니다!"

        def scratch(self):
            return f"{self.name}이(가) 할퀴고 있습니다."

    my_dog = Dog("버디", "골든 리트리버")
    my_cat = Cat("야옹이", "태비")

    print(f"나의 강아지: {my_dog.name}, {my_dog.breed}")
    print(f"강아지 소리: {my_dog.speak()}")
    my_dog.eat()
    print(f"강아지 행동: {my_dog.fetch()}")

    print(f"\n나의 고양이: {my_cat.name}, {my_cat.color}")
    print(f"고양이 소리: {my_cat.speak()}")
    my_cat.eat()
    print(f"고양이 행동: {my_cat.scratch()}")
    print("-" * 20)

    # --- 2부: 다형성 ---
    # 다형성은 "많은 형태"를 의미합니다. OOP에서는 다른 클래스의 객체들이
    # 공통 슈퍼클래스의 객체로 취급될 수 있음을 의미합니다.
    # 이를 통해 메서드가 호출되는 객체에 따라 다른 작업을 수행할 수 있습니다.

    print("\n--- 2부: 다형성 ---")

    animals = [Dog("맥스", "래브라도"), Cat("장화", "검은색")]

    for animal in animals:
        print(f"{animal.name} ({animal.__class__.__name__} 클래스) 소리: {animal.speak()}")

    # 이것이 다형성을 보여줍니다: 'speak' 메서드는 루프에서 'animal' 객체로
    # 일반적으로 처리되더라도, 객체가 Dog인지 Cat인지에 따라 다르게 동작합니다.
    print("-" * 20)

    # --- 3부: 매직 메서드 (던더 메서드) ---
    # 매직 메서드(던더 메서드)는 앞뒤에 이중 밑줄이 있는 파이썬의 특수 메서드입니다.
    # 직접 호출하는 것이 아니라 특정 상황(예: 객체 생성, len() 호출 시)에 파이썬에 의해 호출됩니다.

    print("\n--- 3부: 매직 메서드 ---")

    class Book:
        def __init__(self, title, author, pages):
            self.title = title
            self.author = author
            self.pages = pages

        def __str__(self):
            """사람이 읽기 좋은 형태의 객체 문자열 표현입니다."""
            return f"'{self.title}', {self.author} 저"

        def __repr__(self):
            """공식적인 객체 문자열 표현 (개발자용), 모호하지 않아야 합니다."""
            return f"Book('{self.title}', '{self.author}', {self.pages})"

        def __len__(self):
            """len() 함수에 의해 호출됩니다."""
            return self.pages

        def __add__(self, other):
            """'+' 연산자에 의해 호출됩니다."""
            if isinstance(other, Book):
                return Book(f"{self.title} & {other.title}", "다수 저자", self.pages + other.pages)
            raise TypeError("Book 객체만 더할 수 있습니다")

        def __eq__(self, other):
            """'==' 연산자에 의해 호출됩니다."""
            if isinstance(other, Book):
                return self.title == other.title and self.author == other.author
            return False

        def __call__(self, reader_name):
            """객체를 함수처럼 호출할 수 있게 만듭니다."""
            return f"{reader_name}이(가) '{self.title}'을(를) 읽고 있습니다."

    book1 = Book("은하수를 여행하는 히치하이커를 위한 안내서", "더글러스 애덤스", 193)
    book2 = Book("우주 끝에 있는 레스토랑", "더글러스 애덤스", 160)
    book3 = Book("은하수를 여행하는 히치하이커를 위한 안내서", "더글러스 애덤스", 193) # book1과 동일

    print(f"책 1: {book1}") # __str__ 호출
    print(f"책 1 repr: {repr(book1)}") # __repr__ 호출

    print(f"책 1의 길이 (페이지 수): {len(book1)}") # __len__ 호출

    # __add__ 사용
    combined_book = book1 + book2
    print(f"합쳐진 책: {combined_book} (총 페이지: {len(combined_book)})")

    # __eq__ 사용
    print(f"책 1 == 책 2: {book1 == book2}")
    print(f"책 1 == 책 3: {book1 == book3}")

    # __call__ 사용
    print(book1("아서 덴트")) # 객체를 함수처럼 호출
    print("-" * 20)

    utils.show_base_name(__file__, False)

if __name__ == "__main__":
    main()
else:
    utils.show_base_name(__file__, False)
