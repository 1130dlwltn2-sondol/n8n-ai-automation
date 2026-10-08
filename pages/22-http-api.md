# 22. HTTP Request와 API 연동

n8n에 전용 노드가 없는 서비스와 연결할 때는 HTTP Request 노드를 씁니다. REST API라면 대부분 이 노드 하나로 연동됩니다.

설정은 여섯 가지를 채웁니다. Method는 GET, POST, PUT, DELETE 중 선택합니다. URL은 호출할 주소입니다. Authentication은 인증 방식을 고릅니다. API 키를 헤더에 넣는 방식이 가장 흔합니다. Send Query는 URL 파라미터, Send Body는 POST 본문을 켜는 옵션입니다. 본문은 JSON으로 보내는 경우가 많습니다.

예를 들어 환율 API를 호출한다고 해 봅시다. Method를 GET으로, URL에 API 주소를 넣습니다. 실행하면 응답 JSON이 아이템으로 들어옵니다. 그 다음 Set 노드에서 {{ $json.rates.KRW }} 처럼 원하는 값만 뽑아 씁니다.

인증이 필요한 API는 Credentials를 먼저 만듭니다. 노드 설정의 Credential 항목에서 Create new을 누르고, API 키나 토큰을 입력합니다. 한 번 만들어 두면 다른 워크플로우에서도 재사용됩니다. 중요한 점은 API 키를 노드 설정에 직접 적지 않는 것입니다. Credentials에 넣어 두면 화면에 마스킹되어 표시되고, 워크플로우를 공유해도 키가 노출되지 않습니다.

외부 API를 쓸 때는 응답 구조를 먼저 확인하는 습관이 좋습니다. HTTP Request 노드를 단독으로 실행해 보고, 어떤 필드가 오는지 본 뒤에 표현식을 작성합니다. API 문서의 예제 응답을 복사해 두고 대조하면 실수가 줄어듭니다.

실습: 공개 API 호출
1. HTTP Request 노드로 공개 환율 API 호출하기
2. Set 노드로 원화 환율만 추출하기
3. 결과를 확인하기

핵심 정리
- 전용 노드가 없는 서비스는 HTTP Request 노드로 연동한다.
- Method, URL, 인증, 쿼리, 본문을 채우면 대부분 해결된다.
- API 키는 Credentials에 저장하고 노드에 직접 적지 않는다.
- 실행 결과를 먼저 보고 표현식을 작성한다.
