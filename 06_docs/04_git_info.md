# Git 저장소 정보

## 저장소 정보
- **원격 저장소 URL**: https://github.com/25492551/HR_WEB.git
- **로컬 저장소 경로**: c:\Project\HR_WEB-main
- **기본 브랜치**: main
- **초기화 일시**: 2026-01-23T210812

## Git 사용자 정보
- **이름**: 25492551
- **이메일**: dltmdrlf77@gmail.com

## 원격 저장소 설정
- **원격 이름**: origin
- **Fetch URL**: https://github.com/25492551/HR_WEB.git
- **Push URL**: https://github.com/25492551/HR_WEB.git

## 브랜치 정보
- **로컬 브랜치**: main
- **원격 브랜치**: origin/main
- **추적 설정**: main 브랜치는 origin/main을 추적

## Git 설정 (로컬)
```
core.repositoryformatversion=0
core.filemode=false
core.bare=false
core.logallrefupdates=true
core.symlinks=false
core.ignorecase=true
user.email=dltmdrlf77@gmail.com
user.name=25492551
remote.origin.url=https://github.com/25492551/HR_WEB.git
remote.origin.fetch=+refs/heads/*:refs/remotes/origin/*
branch.main.remote=origin
branch.main.merge=refs/heads/main
```

## 인증 정보
- **토큰 타입**: Fine-grained Personal Access Token
- **토큰 이름**: HR_WEB
- **만료일**: 2026-02-22
- **필요 권한**:
  - Contents (Read and write) - 필수
  - Administration (Read and write)
  - Metadata (Read-only)

## 보안 참고사항
⚠️ **중요**: Personal Access Token은 민감한 정보입니다.
- 토큰은 Git 설정 파일에 저장되어 있지 않습니다
- 원격 저장소 URL에 토큰이 포함되어 있을 수 있습니다
- 토큰이 노출된 경우 즉시 재생성하세요
- 토큰은 GitHub Settings → Developer settings → Personal access tokens에서 관리할 수 있습니다

## 주요 작업 내역
- 2026-01-23T210812: Git 저장소 초기화 및 첫 커밋
- 2026-01-23T210812: 원격 저장소 연결 및 푸시 완료
- 총 58개 파일, 56,595줄 추가

## 유용한 Git 명령어
```bash
# 상태 확인
git status

# 변경사항 추가
git add .

# 커밋
git commit -m "커밋 메시지"

# 푸시
git push -u origin main

# 풀 (원격 변경사항 가져오기)
git pull origin main

# 원격 저장소 확인
git remote -v

# 브랜치 확인
git branch -a
```

## 문제 해결
### 푸시 권한 오류 (403)
- Fine-grained token에 Contents 권한이 필요합니다
- GitHub에서 토큰 편집 → Repository permissions → Contents → Read and write 설정

### 원격 저장소와 충돌
- `git pull origin main --allow-unrelated-histories`로 병합
- 충돌 해결 후 `git push -u origin main`
