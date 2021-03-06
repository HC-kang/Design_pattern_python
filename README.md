## 파이썬 디자인 패턴

> "복잡합을 줄이는 일이 컴퓨터 프로그래밍의 핵심이다."  
> -브라이언 커니핸(Brian Kernighan)

> "모든 컴퓨터 과학 문제는 여러 단계의 추상화로 해결할 수 있다."  
> -데이비드 휠러(David Wheeler)

이 두 인용구는, 안정적이고 재사용성 높은 유연한 소프트웨어의 설계가 우리에게 얼마나 중요한지를 다시 한 번 되뇌이게 해 줍니다.

이러한 문제를 다루는데에 있어서, 저는 **추상화**와 **재사용성**에 가장 높은 가치를 두고 있습니다.  
왜냐하면, 소프트웨어 개발뿐 아닌 인류의 역사를 보더라도, 가장 유용한 개념이 바로 이 두가지였다고 생각하기 때문입니다.

사람의 인지능력은 한계가 있습니다.  
따라서 무언가를 습득하는 능력은, 대상의 본질을 최대한 받아들이기 쉬운 형태로 압축하는 능력에 달려있습니다.  
이렇게 대상의 본질을 요약해내는 것이 바로 **추상화**입니다.

또한 한번 사용한 무언가를 비슷한 다른 용도로 사용하거나, 한번 익힌 무언가를 비슷한 다른 상황에 활용하는 것이 바로 **재사용성**입니다.  
그런데 여기서 조금만 더 나아가서, 사용한 것을 전혀 다른 새로운 방법으로 사용하거나, 익힌것을 완전히 다른 순간에 활용하는 것을 **창의성** 이라고 할 수 있겠습니다.

이 외에도 저는 철저히 *아는만큼 보인다*는 말을 믿기 때문에, 앞으로의 기초체력이 될, 패턴을 읽는 능력을 기르고자 디자인 패턴을 별도로 공부하기 시작했습니다.

### 목차

---

1. 디자인 패턴 개요
2. [싱글톤 디자인 패턴](https://github.com/HC-kang/Design_pattern_python/tree/master/02_singleton_pattern)
3. [팩토리 패턴](https://github.com/HC-kang/Design_pattern_python/tree/master/03_factory_pattern)
4. [퍼사드 패턴](https://github.com/HC-kang/Design_pattern_python/tree/master/04_facade_pattern)
5. [프록시 패턴](https://github.com/HC-kang/Design_pattern_python/tree/master/05_proxy_pattern)
6. [옵서버 패턴](https://github.com/HC-kang/Design_pattern_python/tree/master/06_observer_pattern)
7. [커맨드 패턴](https://github.com/HC-kang/Design_pattern_python/tree/master/07_command_pattern)
8. [템플릿 메소드 패턴](https://github.com/HC-kang/Design_pattern_python/tree/master/08_template_pattern)
9. [MVC 패턴](https://github.com/HC-kang/Design_pattern_python/tree/master/09_MVC_pattern)
10. [상태 디자인 패턴](https://github.com/HC-kang/Design_pattern_python/tree/master/10_state_pattern)
11. 안티 패턴

---

### 1장. 디자인 패턴 개요

1. 디자인 패턴의 종류

   - **생성(Creation)**

   1. 객체가 생성되는 방식 중시
   2. 생성 관런 상세로직을 숨김
   3. 코드는 생성하려는 객체형과 독립적

   - **구조(Structural)**

   1. 클래스와 객체를 더 큰 결과물로 합칠수 있도록 설계
   2. 구조를 간결화하고 클래스와 객체간의 상호관계를 파악하기 용이
   3. 클래스 상속과 컴포지션을 중시

   - **행위(Behavioral)**

   1. 객체간의 상호작용과 책임 중시
   2. 객체간 상호작용을 하되 **느슨한 결합** 중시

2. 객체지향 프로그래밍

   - 객체
   - 클래스
   - 메소드
   - 캡슐화
   - 다형성
   - 상속
   - 추상화
   - 컴포지션

3. 객체지향 디자인의 기본 원칙

   - 개방-폐쇄 원칙
   - 제어 반전 원칙
   - 인터페이스 분리 원칙
   - 단일 책임 원칙
   - 치환 원칙

4. 디자인 패턴의 개념

   - GoF가 무엇인가?

     'GOF의 디자인 패턴'을 집필한 네 명의 저자  
      Erich Gamma, Richard Helm, Ralph Johnson, John Vissides

   - 디자인 패턴의 주요 기능

   1. 언어에 독립적
   2. 새로운 패턴이 지속적으로 등장
   3. 목적에따라 변경 가능

---

### Remark

#### 참고

1. ['파이썬 디자인 패턴(체탄 기리다, 에이콘출판)'](http://www.kyobobook.co.kr/product/detailViewKor.laf?ejkGb=KOR&mallGb=KOR&barcode=9791161752440&orderClick=LAG&Kc=)
2. https://gmlwjd9405.github.io/2018/07/04/class-diagram.html

---
