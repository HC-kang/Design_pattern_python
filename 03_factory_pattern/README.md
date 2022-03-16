## 3장. 팩토리 디자인 패턴

### 1. 팩토리 디자인 패턴 개요

#### 팩토리 패턴의 종류

- 심플 팩토리 패턴
  - 객체 생성로직을 숨기고 인터페이스로 객체를 생성한다.
- 팩토리 메소드 패턴
  - 인터페이스를 통해 객체를 생성하지만, 서브클래스가 필요한 클래스를 선택한다.
- 추상 팩토리 패턴
  - 인터페이스를 통해 객체 생성에 필요한 클래스를 노출하지 않고 객체를 생성한다.
  - 내부적으로 다른 팩토리 객체를 생성한다.

---

### 2. 심플 팩토리 디자인패턴

#### <심플 팩토리 패턴 UML 다이어그램>

![simple_factory_pattern](https://user-images.githubusercontent.com/81678439/158492016-56fb8bd8-4fe2-4588-9159-1ed693bed938.png)

#### 심플 팩토리 패턴의 특징

- 심플 팩토리 패턴은 사용자가 직접 클래스를 호출하지 않고, 여러 종류의 객체를 생성 할 수 있는 패턴이다.
- 심플 팩토리 패턴은 하나의 패턴으로 인정받지 못하는 경우도 있으나, 이후 본격적인 팩토리 패턴을 이해하기 위해 필수적으로 이해해야한다.

#### 01\_심플 팩토리 디자인패턴 예제(코드참조)

- Animal: 추상 기본 클래스(Abstract)
  - do_say(): 추상 메소드
- Dog: Product1
- Cat: Product2
- Fox: ...  
  ...

---

### 3. 팩토리 메소드 디자인패턴

#### <팩토리 메소드 패턴 UML 다이어그램>

![factory_method_pattern](https://user-images.githubusercontent.com/81678439/158505057-429fe5c0-5be7-4bd1-ab86-1e0224dbb4c2.png)

#### 팩토리 메소드 패턴의 특징

- 인터페이스를 통해 객체를 생성하지만, 서브클래스가 특정 객체를 생성하기 위해 어떤 클래스를 선택할지 결정한다.
- 인스턴스화가 아닌, 상속을 통해서 객체를 생성한다.
- 심플 팩토리와는 다르게, 인스턴스나 서브클래스 등의 객체를 유동적으로 생성할 수 있다.

#### 팩토리 메소드 패턴의 장점

- 유연성과 포괄성을 갖추고 있으며, 특정 클래스에 종속되지 않는다.
- **ConcreteProduct가 아닌, Product(인터페이스)에 의존한다.** .....<- 추가확인
- 객체를 생성하는 코드와 활용하는 코드를 분리 할 수 있다 -> 의존성이 줄어든다.

#### 02\_팩토리 메소드 디자인패턴 예제(코드참조)

- Section: 추상 클래스(Product)
  - describe(): 추상 메소드
- PersonalSection: ConcreteProduct
- AlbumSection: -
- PatentSection: -
- PublicationSection: -
- Profile: 추상 클래스(Creator) -> **Factory**
  - createProfile(): 추상 메소드
  - getSections()
  - addSections()

코드에서 알 수 있다시피, Profile 클래스에는 각각의 프로필들에 대한 정보가 전혀 포함되어있지 않다.

정리하자면, Profile을 상속받은 서브클래스들이, 추상화된 Creator에서 파생된 ConcreteCreator를 가지고, 다른 객체들을 구성한다.

---

### 4. 추상 팩토리 디자인패턴

#### <추상 팩토리 패턴 UML 다이어그램>

![abstract_factory_pattern](https://user-images.githubusercontent.com/81678439/158518614-be8d4b3f-dbce-4abd-8ed6-f456c8abc3c1.png)

- 추상 팩토리 패턴은 클래스를 직접 호출하지 않고, 인터페이스를 통해 관련 객체를 생성하기 위해 활용한다.
- 팩토리 메소드의 경우, 서브클래스가 인스턴스 생성을 하지만 추상 팩토리 메소드의 경우에는 관련된 객체의 집합을 생성한다 ---> 추가확인

#### 03\_추상 팩토리 디자인패턴 예제(코드참조)

- PizzaFactory: Abstract Factory
  - createVegPizza(): 추상 메소드
  - createNonVegPizza(): 추상 메소드
- IndianPizzaFactory: Concrete Factory
- USPizzaFactory: Concrete Factory
- VegPizza: Abstract Product
- NonVegPizza: Abstract Product
- ...Pizzas: Concrete Product
- PizzaStore: **인터페이스** -> 확인필요

---

### 5. 팩토리 메소드 vs 추상 팩토리 메소드

| 팩토리 메소드                                             | 추상 팩토리 메소드                                                    |
| --------------------------------------------------------- | --------------------------------------------------------------------- |
| 객체 생성에 필요한 메소드가 사용자에게 노출됨.            | 관련된 객체 집단을 생성하기 위해 한 개 이상의 팩토리 메소드가 필요함. |
| 어떤 객체를 생성할지 결정하는 상속과 서브클래스가 필요함. | 다른 클래스 객체를 생성하기 위해 컴포지션을 사용.                     |
| 한 개의 객체를 생성하는 팰토리 메소드를 사용.             | 관련된 객체 집단을 생성.                                              |
