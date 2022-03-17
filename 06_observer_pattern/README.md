## 6장. 옵서버 패턴

### 0. 행위 디자인 패턴 개요

- 행위 패턴은 객체의 역할(행동)에 중점을 두는 패턴임. 기능이 확장되기 위해서는 필연적으로 다수의 객체들이 상호작용해야 하는데, 이 때 상호작용, 즉 역할 또는 행위에 초점을 두는 패턴임.
- 행위 패턴에서 객체들은 상호작용을 하되 느슨하게 결합되어있어야 함.

### 1. 옵서버 패턴 개요

옵서버 패턴에서 Subject(객체)는 Observer(자식)들의 목록을 유지하고, 필요시(옵서버의 메소드를 호출 할 시) 옵서버에 이것을 요청을 알림. 이러한 특성으로 인해 분산 시스템에서 주로 활용.

#### 옵서버 패턴의 목적

- 객체 간 1:N 관계를 형성, 관리하고 객체의 상태를 자동으로 종속된 객체들에게 알릴 수 있음.
- 서브젝트의 핵심 부분을 캡슐화 할 수 있음.

#### 옵서버 패턴의 장단점

##### 장점

- 객체 간 '느슨한 결합' 원칙을 따른다.
- Subject, Observer는 완전히 독립적이어서, 기능수정이나 추가개발시에도 별도의 클래스 수정의 필요성이 없다.
- 필요시 새로운 Observer를 언제든 추가/삭제 할 수 있다.

##### 단점

- ConcreteObserver는 상속을 통해서만 Observer의 인터페이스를 구현할 수 있으며, 컴포지션\*을 선택 할 수 없다.
- 제대로 구현되지 않은 Observer는 복잡도를 높이고 성능 저하의 원인이 됨.
- Notification은 신뢰성이 높지 않음. 이로인한 Race Condition(경쟁 상태), 또는 (동시 접근으로 인한)비일관성이 발생할 수 있음.

**참고: \* 상속 vs 컴포지션**

| 상속                            | 컴포지션                          |
| ------------------------------- | --------------------------------- |
| IS-A                            | HAS-A                             |
| 탈것과 자동차(car IS-A vehicle) | 탈것과 엔진(vehicle HAS-A engine) |
| 소속                            | 구성                              |
| **캡슐화를 깨뜨릴 수 있음**     | 계층적 관계 구현이 어려움         |

-

#### <옵서버 패턴 UML 다이어그램>

![observer_pattern](https://user-images.githubusercontent.com/81678439/158602070-a75c179d-e1ea-40cd-ba75-a70df8214edc.png)

- Subject: Observers를 관리하는 객체. register(), deregister() 등의 메소드로 observers를 관리하지만, 해당 메소드는 Observer에서 사용함.
- Observer: Abstract Class
  - 서브젝트를 감시하는 객체를 위한 인터페이스
  - 이를 위해 ConcreteObserver가 갖춰야 할 메소드를 추상 메소드로 갖는다.
- ConcreteObserver: Subject의 상태를 저장.

### 2. 옵서버 패턴 예제(코드참조)

#### 01_observer.py

- 생략(코드참조)

#### 02_news_publisher.py

- NewsPublisher: Subject
  - attach(), detach(): Subscriber가 등록, 해제할수 있게 하는 메소드
  - subscribers(): 현재 등록된 Subscriber 반환
  - notifySubscribers(): 현재 뉴스를 공유하기
  - addNews(), getNews()
- Subscriber: Observer(abstract class)
  - update(): abstract method
- SNS, Email, AnyOtherSubscriber: ConcreteObservers
  - \_\_init\_\_(): news_publisher를 인자로 받아 news_publisher.attach를 통해 자신을 NewsPublisher객체에 등록함.
  - update()
  - 추상 클래스의 인터페이스를 구체적으로 구현하는 옵서버

### 3. 옵서버 패턴의 종류

#### 풀 모델

- **Observer**가 주체임.
- Subject 는 변경사항이 있다는 사실만 Observers에게 브로드캐스트
- noti를 전달받은 Observer는 필요한 변경사항을 Pull 해와야 함.
- 위처럼 두 단계로 구성된 관계로 비효율적 -> 잘 쓰이지 않음.

#### 푸시 모델

- **Subject**가 주체임.
- Subject는 필요성을 체크하지 않고, 변경된 데이터를 직접 Observer에게 발송함(Push)
- 이로인해 필요없는 데이터가 전송될 수 있어, 응답시간이 늦어질 수 있음.
- 따라서 꼭 필요한 데이터만 선별하는 별도의 시스템 설계가 필요함.

### 4. 기타

#### 느슨한 결합?

낮은 결합도와 높은 응집도는 소프트웨어 설계에서 매우 중요한 원칙임.  
이 중 낮은 결합도, 즉 느슨한 결합(Loose Coupling)은 객체들이 서로에 대해 알고있는 정도가 낮다는 것을 의미한다. 다르게 설명하자면 하나의 객체가 다른 객체에 의존성이 낮아야 한다는 뜻이다.
이것을 통해 우리는

- 일부분의 수정이, 예상치않게 주변의 다른 객체나 다른 요소에 영향을 끼치는 위험성을 줄일 수 있음.
- 테스트와 차후 유지보수, 추가개발이 원활해짐
- 시스템을 쉽게 여러 부분으로 분할 할 수 있고, 이를 통해 비슷한 다른 프로젝트나 제품에 해당 코드를 재사용 할 수 있음.

이를 옵저버 패턴에 대해 적용해 보자면,

- Subject는 Observer가 어떤 인터페이스를 구현하는지 모른다. 즉 Subject는 데이터만 제공 해 줄 뿐, 이를 Observer가 어떻게 활용하는지는 모른다. 심지어 ConcreteObserver의 존재 여부도 알지 못한다.(== 없어져도 상관이 없다. == 언제든 추가되어도 상관 없다.)
- 당연하게도 Observer가 어디서, 어떻게 사용되는지는 Subject와 전혀 상관이 없다. 즉 완전히 독립되어있다.
