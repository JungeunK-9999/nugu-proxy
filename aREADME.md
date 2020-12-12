# STMT 음성지원 서비스


## 대표 발화문 (음성 명령어)
- 태스크 리스트
- 디테일 확인
- 태스크 확인
- 태스크 완료
- 그만

## 주요 기능
- 태스크 목록 확인
- 진행중인 태스크의 세부 사항 확인
- 진행중인 태스크 확인
- 태스크 상태를 완료로 변경 (미완 -> 완료)

 [시나리오]

![nugu 시나리오](https://6-things-must-to-do.github.io/docs/static/4b24f650d43b9c34d380a78863e96c30/9d76a/utterance.png)

## NUGU play 동작
1. wake-up

2. paly 진입

3. 명령어 입력

      3-1) 인식 성공

      3-2) 인식 실패

      3-3) proxy server 연결 실패

4. NUGU.ACTION.fallback

## backend proxy server && project server
