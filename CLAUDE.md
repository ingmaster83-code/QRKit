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

## 작업 규칙
- 새 도구 추가 시 index.html 카드, sitemap.xml 업데이트 필수
- 다운로드 버튼은 id="downloadBtn" 사용
- SEO 키워드: QR코드 생성, QR코드 만들기, 바코드 생성, QR코드 읽기
