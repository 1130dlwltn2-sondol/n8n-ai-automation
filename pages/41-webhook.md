# 41. 웹훅 트리거

웹훅(Webhook)은 외부에서 URL을 호출하면 워크플로우가 실행되는 방식입니다. "누가 버튼을 누르면", "다른 시스템에서 이벤트가 오면" 같은 실시간 연동에 씁니다.

Webhook 노드를 추가하면 n8n이 고유한 URL을 만들어 줍니다. Test URL과 Production URL이 따로 있습니다. Test URL은 에디터에서 Listen for test event를 누른 상태에서 호출해야 하고, Production URL은 워크플로우가 Active일 때 동작합니다. 개발할 때는 Test URL로, 실제 운영은 Production URL로 씁니다.

HTTP Method는 보통 POST를 씁니다. 호출할 때 보낸 본문(JSON)은 {{ $json.body }} 형태로 들어옵니다. Response 설정을 정할 수 있는데, 마지막 노드의 결과를 그대로 돌려주는 방식과, Respond to Webhook 노드로 중간에 응답을 보내는 방식이 있습니다. 처리가 오래 걸리면 먼저 응답을 보내고 뒤에서 처리하는 것이 좋습니다.

웹훅을 외부에 공개할 때는 보안이 중요합니다. n8n이 셀프호스팅이라면 HTTPS로 공개해야 합니다. 인증이 필요하다면 Header Auth나 Basic Auth를 걸 수 있습니다. 중요한 웹훅에는 호출원에만 알려진 비밀 토큰을 쿼리나 헤더에 넣어 검증하는 방식을 씁니다.

웹훅은 다른 시스템과 n8n을 잇는 다리입니다. 예를 들어 홈페이지의 문의 폼에서 웹훅 URL로 POST를 보내면, n8n이 받아서 AI로 분류하고 담당자에게 알리는 식으로 확장됩니다. Part 8의 실전 프로젝트도 웹훅에서 시작합니다.

실습: 웹훅 수신
1. Webhook 노드를 POST로 추가하고 Test URL 확인하기
2. curl이나 API 테스트 도구로 JSON 보내기
3. 들어온 데이터를 Set 노드로 정리해 출력하기

핵심 정리
- 웹훅은 외부 HTTP 호출로 워크플로우를 시작한다.
- Test URL은 개발용, Production URL은 운영용이다.
- 오래 걸리는 처리는 먼저 응답하고 뒤에서 처리한다.
- 공개 웹훅에는 HTTPS와 인증을 적용한다.
