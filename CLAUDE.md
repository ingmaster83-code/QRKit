# QRKit 프로젝트 지침

## 프로젝트 개요
- **사이트명:** QR킷 (QRKit)
- **URL:** https://qrkit.wooahouse.com
- **GitHub:** https://github.com/ingmaster83-code/QRKit
- **배포:** GitHub Pages (main 브랜치 → root)

## 기술 스택
- 순수 HTML / CSS / JS (프레임워크 없음)
- QR 생성: qrcodejs (CDN)
- QR 읽기: jsQR (CDN)
- 바코드: JsBarcode (CDN)
- PWA: manifest.json + sw.js + js/pwa-install.js

## 서비스 목적
QR코드 생성·읽기·바코드 생성을 브라우저에서 무료로 제공.

## 도구 목록 (11개)
URL QR, 텍스트 QR, WiFi QR, 명함 QR(vCard), 이메일 QR, 전화번호 QR,
QR읽기(파일), 카메라 QR읽기, 바코드생성기, QR배치생성(CSV),
**QR커스터마이징**(색상+로고 오버레이, qrcode.js+Canvas)
*굵은 글씨 = 최근 추가*

## 작업 규칙
- 새 도구 추가 시 index.html 카드, sitemap.xml 업데이트 필수
- 다운로드 버튼은 id="downloadBtn" 사용
- SEO 키워드: QR코드 생성, QR코드 만들기, 바코드 생성, QR코드 읽기
