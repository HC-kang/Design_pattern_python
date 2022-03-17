## 7장. 커맨드 패턴

### 1. 커맨드 패턴 개요

커맨드 패턴은 특정 객체의 행동(기능)을 수행할 때 필요한, 아래와 같은 정보를 **캡슐화**하는 패턴임.

- 메소드 명
- 메소드를 소유하는 객체
- 메소드 인자

코드예제를 보기 이전에 실생활의 예시를 들자면, 각종 설치 마법사를 들 수 있음.  
사용자는 인터페이스를 통해 원하는 설정사항을 선택하고, 이를 저장해두고 있다가 마지막에 '설치' 버튼을 누르는 순간 이때까지 저장된 정보를 바탕으로 진짜 설치를 시작함.  
즉, Command 객체를 통해 사용자의 요구사항, 환경설정을 계속해서 저장해 두고, 마지막에 excute()메소드를 호출하는 방식으로 캡슐화하는 구조임.

#### 커맨드 패턴의 목적

- 클라이언트의 요청을 객체 속에 캡슐화한다.
- 이때 요청사항을 각각의 parameter로 지정한다.
- 요청사항을 단계별로 큐에 저장한다
- 객체지향 콜백을 지원한다 (?)
- 작은 단위 연산을 조합하여 상위 연산을 만들 수 있다.

#### 커맨드 패턴의 사용

- ReDo, RollBack: 요청을 순서대로 저장하고, 필요시 하나씩 순차적으로 실행
- 비동기 작업 수행: Invoker가 요청을 큐에 저장하고 순차적으로 Receiver로 보내면서, 메인 스레드와 비동기적으로 프로세스를 수행

#### 커맨드 패턴의 장단점

1. 장점
   - 작업을 요청하는 클래스와 수행하는 클래스를 분리할 수 있다.
   - 큐에 커맨드를 순서대로 저장해 사용할 수 있다.
   - 기존 코드의 수정 없이 커맨드를 수정 할 수 있다.
   - 롤백이나 리두를 쉽게 구현할 수 있다.
2. 단점
   - 클래스와 객체가 많아 복잡해진다.
   - 모든 작업이 독립적이므로, 구현 및 유지보수시에 신경 써야하는 클래스가 많다.

#### <커맨드 패턴 UML 다이어그램>

![command_pattern](https://user-images.githubusercontent.com/81678439/158711807-10c8d288-17a0-4f9b-9cd5-07bbbab4e103.png)

- Command: 연산을 수행할 인터페이스를 정의
- ConcreteCommand: Receiver 객체와 연산 간 바인딩을 정의
- Client: ConcreteCommand 객체를 생성하고 Receiver를 설정
- Invoker: ConcreteCommand에 수행 요청
- Receiver: 요청에 관련된 연산을 관리

#### 전반적인 플로우

1. 클라이언트가 특정 연산 요청
2. Invoker는 요청을 캡슐화하여 큐에 저장
3. ConcreteCommand는 이 요청을 Receiver에 수행요청

### 2. 커맨드 패턴 예제(코드참조)

#### 01_install_wizard.py

- 생략(코드참조)

#### 02_command.py

- 생략(코드참조)

#### 03_stock_order.py

증권거래소 예제. 주말간 고객이 중개사에게 주식 매수 및 매도요청을 할 때, 중개사는 이를 바로 실행하지 못하고 요청을 큐에 담아두었다가, 월요일 아침에 요청을 거래소에 전달함.

- Order: Command(Abstract Class)
  - execute(): Abstract Method
- Buy, SellStockOrder: ConcreteCommand
- StockTrade: Receiver(거래소)
- Agent: Invoker(중개사)
  - \_\_orderQueue = [] 를 보유중

**세부 프로세스 구현**

1. 클라이언트는 StockTrade()로 stock 인스턴스 생성(Receiver 지정)
2. Buy, SellStockOrder(ConcreteCommand)로 StockTrade에 주문을 생성
3. Agent 클래스인 agent 인스턴스 객체 생성
4. agent.placeOrder()메소드를 통해 클라이언트의 요청을 주문
