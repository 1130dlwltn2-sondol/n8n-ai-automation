# 92. 확인 문제와 해설

이 책의 핵심 내용을 점검하는 문제 20문항입니다. 먼저 풀어 보고 해설을 확인하세요.

1. 워크플로우를 시작시키는 노드는?
가. Set 노드
나. 트리거 노드
다. Code 노드
라. Merge 노드

2. 정해진 시간에 워크플로우를 실행하는 트리거는?
가. Webhook Trigger
나. Manual Trigger
다. Schedule Trigger
라. Error Trigger

3. 노드 사이를 흐르는 데이터의 단위는?
가. 패킷
나. 아이템
다. 세션
라. 토큰

4. 표현식의 올바른 표기는?
가. { $json.name }
나. {{ $json.name }}
다. [[ $json.name ]]
라. (( $json.name ))

5. API 키 같은 비밀값을 안전하게 보관하는 기능은?
가. 환경 변수 직접 입력
나. Credentials
다. Set 노드
라. 메모장

6. 조건에 따라 참/거짓 두 갈래로 나누는 노드는?
가. Switch
나. IF
다. Filter
라. Merge

7. 세 가지 이상의 경우를 나누기에 적합한 노드는?
가. IF
나. Switch
다. Loop Over Items
라. Aggregate

8. 아이템을 하나씩 꺼내 반복 처리하는 노드는?
가. Merge
나. Loop Over Items
다. Filter
라. Webhook

9. 여러 아이템을 하나의 아이템으로 뭉치는 노드는?
가. Aggregate
나. Split
다. Switch
라. Set

10. 실패한 노드를 지정 횟수만큼 다시 시도하는 설정은?
가. Continue
나. Retry On Fail
다. Always Output Data
라. Execute Once

11. 워크플로우 전체의 에러를 받아 처리하는 트리거는?
가. Schedule Trigger
나. Manual Trigger
다. Error Trigger
라. Webhook Trigger

12. 외부 HTTP 호출로 워크플로우를 시작하는 트리거는?
가. Webhook Trigger
나. Schedule Trigger
다. Manual Trigger
라. Error Trigger

13. 프롬프트를 언어 모델에 보내 답을 받는 노드는?
가. AI 에이전트 노드
나. LLM 노드
다. Memory 노드
라. Vector Store 노드

14. AI 에이전트 노드를 구성하는 세 요소가 아닌 것은?
가. Chat Model
나. Tools
다. Memory
라. Webhook

15. 문서 검색 결과를 프롬프트에 넣어 답하게 하는 방식은?
가. 파인튜닝
나. RAG
다. 임베딩 고정
라. 프롬프트 캐싱

16. 문서를 적당한 길이로 나누는 과정은?
가. 임베딩
나. 청킹(텍스트 분할)
다. 리랭킹
라. 인덱싱 삭제

17. n8n을 AI 도구의 도구로 공개할 때 쓰는 표준은?
가. REST
나. MCP
다. SOAP
라. gRPC

18. 워크플로우를 자동 실행되게 하려면?
가. Active 스위치를 켠다
나. Save만 하면 된다
다. 노드를 삭제한다
라. 브라우저를 닫는다

19. 셀프호스팅 n8n에서 워크플로우가 사라지지 않게 하려면?
가. 매일 수동으로 복사한다
나. 데이터 볼륨을 연결한다
다. 클라우드에만 저장한다
라. 노드를 잠근다

20. 에이전트에게 위험한 작업을 맡길 때 함께 써야 하는 것은?
가. 더 큰 모델
나. 휴먼인더루프 승인 흐름
다. 더 많은 도구
라. 더 긴 프롬프트

정답과 해설
1. 나 - 워크플로우는 항상 트리거 노드에서 시작된다.
2. 다 - Schedule Trigger는 cron 등으로 정해진 시간에 실행된다.
3. 나 - 데이터는 JSON 아이템의 배열 형태로 흐른다.
4. 나 - 표현식은 중괄호 두 개 {{ }} 안에 쓴다.
5. 나 - Credentials에 저장하면 마스킹되고 공유 시에도 노출되지 않는다.
6. 나 - IF 노드는 조건의 참/거짓에 따라 두 갈래로 나눈다.
7. 나 - Switch 노드는 여러 조건에 따라 여러 갈래로 나눈다.
8. 나 - Loop Over Items는 아이템을 하나씩 꺼내 반복한다.
9. 가 - Aggregate는 여러 아이템을 하나로 합친다.
10. 나 - Retry On Fail은 실패 시 지정 횟수만큼 재시도한다.
11. 다 - Error Trigger로 시작하는 워크플로우를 Error Workflow로 지정한다.
12. 가 - Webhook Trigger는 외부 HTTP 호출로 시작된다.
13. 나 - LLM 노드는 프롬프트를 모델에 보내 답을 받는다.
14. 라 - 에이전트는 Chat Model, Tools, Memory로 구성된다.
15. 나 - RAG는 검색 결과를 프롬프트에 넣어 답하게 한다.
16. 나 - 청킹은 문서를 검색하기 좋은 길이로 나누는 과정이다.
17. 나 - MCP는 AI 모델이 외부 도구를 쓰는 공개 표준이다.
18. 가 - 스케줄이나 웹훅으로 자동 실행되려면 Active를 켜야 한다.
19. 나 - 데이터 볼륨을 연결하면 컨테이너를 지워도 데이터가 유지된다.
20. 나 - 중요한 작업은 사람의 승인을 거치는 흐름과 함께 쓴다.
