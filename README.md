# Auto GitHub Jandi (자동 깃허브 잔디)

GitHub 잔디밭을 자동으로 채워주는 Python 스크립트입니다. 24시간마다 자동으로 커밋을 생성합니다

## 🌱 주요 기능

- **자동 커밋**: 24시간(86400초)마다 자동으로 커밋을 생성합니다
- **연속 실행**: 스크립트가 실행되는 동안 지속적으로 작동합니다
- **커밋 카운트**: `count.txt` 파일을 통해 커밋 횟수를 추적합니다
- **자동 푸시**: 커밋 후 자동으로 `main` 브랜치에 푸시합니다

## 📁 파일 구조

```
auto-github-jandi/
├── README.md          # 프로젝트 설명서 (이 파일)
├── auto_commit.py     # 메인 스크립트
└── count.txt          # 커밋 카운트를 저장하는 파일
```

## 🚀 사용 방법

1. **저장소 클론**
   ```bash
   git clone https://github.com/kwondongwoo0424/auto-github-jandi.git
   cd auto-github-jandi
   ```

2. **Git 설정 (본인의 이름과 이메일로 변경)**
   ```bash
   git config --global user.name "본인의 이름"
   git config --global user.email "본인의 이메일@example.com"
   ```

3. **스크립트 실행**
   ```bash
   python auto_commit.py
   ```

## ⚙️ 동작 원리

1. `count.txt` 파일에서 현재 커밋 번호를 읽어옵니다
2. `README.md` 파일에 공백 문자를 추가합니다
3. Git에 변경사항을 추가하고 커밋합니다
4. `main` 브랜치에 자동으로 푸시합니다
5. 커밋 카운트를 증가시키고 `count.txt`에 저장합니다
6. 24시간 후에 다시 실행됩니다

## 📝 참고사항

- 스크립트는 백그라운드에서 지속적으로 실행됩니다
- 첫 실행 시 즉시 커밋을 생성하고, 이후 24시간 간격으로 실행됩니다
- `count.txt` 파일이 없거나 읽을 수 없는 경우 카운트는 1부터 시작됩니다

## ⚠️ 주의사항

- GitHub의 기여도 정책을 확인하고 사용하세요
- 장기간 실행 시 시스템 리소스를 고려하세요
- 스크립트 중단 시 `Ctrl+C`를 사용하세요  