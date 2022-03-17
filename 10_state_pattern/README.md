## 10장. 상태 디자인 패턴

### 1. 상태 디자인 패턴 개요

행위 디자인 패턴의 한 종류로, 상태를 나타내는 객체 패턴이라고도 부른다.  
객체는 내부 상태에 따라 여러가지 행위를 캡슐화하는데, 이 상태에서 상태 패턴은 런타임 중에 객체의 행위를 변경한다.

라디오를 예로 들면, 전원을 켠 후, FM인 상태에서 스캔 버튼을 누르면 라디오는 FM 채널을 스캔한다. 그런다음 AM채널로 변경한 후 스캔 버튼을 누르면 이번에는 AM 채널을 스캔한다. 즉 현재 채널의 상태에 따라 스캔이라는 버튼으로 작동하는 행위가 전원이 켜진채로(런타임에서) 동적으로 변한다.

#### 상태 디자인 패턴의 목적

#### 상태 디자인 패턴의 장단점

1. 장점

   - 상태 패턴에서 객체의 행위는 해당 state에서의 실행함수 결과값을 반환한다. 다시말해 행위는 상태에 따라 런타임에서 변경된다. 이를통해 if/else문의 조건을 줄일 수 있다.
   - 다형성 구현이 쉽다.
   - 상태 관련 행위가 모두 ConcreteState에 모여있으므로, 응집도를 높일 수 있다.
   - 새로운 ConcreteClass를 추가해서 쉽게 신규 상태가 기능을 추가하거나 구현 할 수 있다. 이로인해 코드의 유연성이 높아지고 유지보수가 쉬워진다.
   - 허용되는 상태를 통제하기 쉽다.

2. 단점
   - 클래스의 남발이 심하다. 모든 상태를 각각의 ConcreteClass로 구현한다면, 관리해야 할 클래스가 지나치게 많아진다. 결과적으로 전체 상태를 확인하기 어렵다.
   - 새로운 행위는 ConcreteClass로 쉽게 추가할 수 있지만, Context 클래스도 이에 맞게 수정해주어야 한다. 따라서 기능을 추가함에따라 Context 클래스는 점점 복잡해진다.

#### <상태 디자인 패턴 UML 다이어그램>

![state_pattern](https://user-images.githubusercontent.com/81678439/158714222-d8c9bfc5-85ec-4b0a-9b57-4859f5f259a0.png)

- State: 객체의 행위를 캡슐화하는 인터페이스. 행위는 객체의 상태에 따라 동적으로 변화한다.
- ConcreteState: State인터페이스를 구현하는 서브클래스. 특정 상태에서 객체의 행위를 구현한다.
- Context: 사용자가 선택, 요청을 넘겨받는 클래스. 특정 상태의 객체를 구현한 ConcreteState의 인스턴스를 가지고있고, 사용자의 요청에 맞는 적절한 메소드를 호출한다.

### 2. 상태 디자인 패턴 예제(코드참조)

#### 01_state.py

- State: Abstract Class.
  - Handle(): Abstract Method
- ConcreteStateA/B: State의 구현체.
- Context: 구체화된 ConcreteState의 인스턴스를 state 변수로 보유하며, 이에따라 Handle()메소드의 행위가 달라진다.

#### 02_remote.py

- State: Abstract Class
  - doThis(): Abstract Method
- Start / StopState: Subclasses
- TVContext:
  - set, getState(): 상태를 변경하거나 가져오는 메서드
  - doThis(): self.state에 따라 각각의 상태에 맞는 행위를 실행하는 메서드
  - volumeUpDown / channelupDown(): 상태와 관련없는, 정적인 별개의 메서드

#### 03_computer_state.py

- ComputerState: Abstract Class
  - switch: Abstract Method
- Off, On, Suspend, Hibernate: 추상 클래스에 대한 구현체
  - name: 현재 상태
  - allowed: 현재 상태에서 이동 가능한 다음상태의 리스트
- Computer: Context Class
