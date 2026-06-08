"""
WooaQR KO 페이지 메타 디스크립션 CTR 최적화
- 기준: 네이버 서치어드바이저 노출 대비 CTR 개선
- 최우선: "qr 코드와 텍스트" 376 노출 0% CTR → qr-text.html 타이틀+설명 교체
- 핵심: "전화번호 qrcode/qr 생성" 130 노출 합계, CTR 2~6%
"""
import re, os

BASE = 'C:/개인/wooahouse/QRKit'

# { 파일: (설명매칭용_prefix, 새_description, 새_title 또는 None) }
PAGES = {
    'index.html': (
        'URL·텍스트·WiFi·명함·이메일 QR코드 생성',
        'URL·텍스트·WiFi·명함·이메일·전화번호 QR코드 생성, QR코드·바코드 읽기까지 무료! 회원가입·설치 없이 브라우저에서 바로 사용. 파일은 서버에 저장되지 않아 100% 안전 — 우아QR(WooaQR)',
        None
    ),
    # ── 376 노출 0% CTR: 타이틀도 함께 교체 ─────────────────────────────
    'qr-text.html': (
        '텍스트·메모를 QR코드로 무료 변환',
        '텍스트·글자를 QR코드로 무료 변환 — 어떤 내용이든 QR코드로 즉시 제작해 PNG로 다운로드. 회원가입·설치 없이 브라우저에서 바로 사용.',
        '텍스트·글자를 QR코드로 무료 변환 — QR코드와 텍스트 생성기 무설치 | WooaQR'
    ),
    # ── 전화번호 관련 키워드 66+39+25 노출 ────────────────────────────────
    'qr-phone.html': (
        '전화번호를 QR코드로 무료 변환',
        '전화번호 QR코드 생성 무료 — 전화번호를 QR코드로 변환하면 스캔 즉시 전화 연결. 크기·색상 커스텀 가능, 회원가입·설치 없이 바로 사용.',
        None
    ),
    # ── 바코드·카메라 관련 키워드 ─────────────────────────────────────────
    'qr-barcode-reader.html': (
        '이미지 파일에서 QR코드와 바코드',
        '바코드·QR코드 읽기 무료 — 이미지 파일에서 QR코드·바코드(EAN-13·CODE128 등)를 자동 인식. 회원가입·설치 없이 브라우저에서 바로 사용.',
        None
    ),
    'qr-camera.html': (
        '웹캠 카메라로 QR코드를 실시간 스캔',
        '카메라 QR코드 읽기 무료 — 웹캠으로 QR코드를 실시간 스캔. 앱 없이 브라우저에서 바로 사용, PC·스마트폰 모두 지원. 서버 전송 없이 100% 안전.',
        None
    ),
    # ── qr코드 색상변경 키워드 ─────────────────────────────────────────────
    'qr-custom.html': (
        'QR코드 색상을 자유롭게 변경하고 로고',
        'QR코드 색상 변경·로고 삽입 무료 — 색상을 자유롭게 바꾸고 로고를 삽입해 브랜드 QR코드 제작. 회원가입·설치 없이 브라우저에서 바로 사용.',
        None
    ),
    # ── 나머지 전체 ────────────────────────────────────────────────────────
    'barcode-generator.html': (
        'CODE128, EAN-13, UPC-A',
        '바코드 생성기 무료 — CODE128·EAN-13·UPC-A·CODE39 바코드를 온라인으로 즉시 생성. 크기·높이 조절, PNG 다운로드, 회원가입·설치 없이 바로 사용.',
        None
    ),
    'qr-batch.html': (
        '여러 URL을 한 번에 QR코드로 생성',
        'QR코드 일괄 생성 무료 — 여러 URL을 한 번에 QR코드로 생성. 최대 20개를 입력하면 ZIP 파일로 다운로드. 회원가입·설치 없이 바로 사용.',
        None
    ),
    'qr-calendar.html': (
        '이벤트 제목·시작일시',
        'QR 일정 생성기 무료 — 이벤트 제목·날짜·장소를 QR코드로 변환. 스캔하면 스마트폰 캘린더에 즉시 추가. 회원가입·설치 없이 바로 사용.',
        None
    ),
    'qr-email.html': (
        '이메일 주소·제목·내용을 QR코드로 변환',
        '이메일 QR코드 생성 무료 — 이메일 주소·제목·내용을 QR코드로 변환. 스캔하면 이메일 앱이 자동으로 열립니다. 회원가입·설치 없이 바로 사용.',
        None
    ),
    'qr-location.html': (
        '위도·경도 또는 주소를 QR코드로 변환',
        '위치 QR코드 생성 무료 — 위도·경도 또는 주소를 QR코드로 변환. 스캔하면 지도 앱이 바로 열립니다. 내 위치 자동 감지, 회원가입·설치 없이 바로 사용.',
        None
    ),
    'qr-reader.html': (
        'QR코드 이미지 파일을 업로드해 내용을',
        'QR코드 읽기 무료 — QR코드 이미지를 업로드하면 내용을 즉시 확인. 드래그&드롭 지원, 브라우저에서 처리해 서버 전송 없이 100% 안전. 회원가입·설치 없이 바로 사용.',
        None
    ),
    'qr-sms.html': (
        '전화번호와 문자 내용을 QR코드로 변환',
        'SMS 문자 QR코드 생성 무료 — 전화번호와 문자 내용을 QR코드로 변환. 스캔하면 문자 앱이 자동으로 열립니다. 회원가입·설치 없이 바로 사용.',
        None
    ),
    'qr-social.html': (
        '인스타그램·유튜브·틱톡·X·페이스북',
        '소셜미디어 QR코드 생성 무료 — 인스타그램·유튜브·틱톡·X·카카오톡 프로필을 QR코드로 변환. 명함·인쇄물에 바로 활용, 회원가입·설치 없이 바로 사용.',
        None
    ),
    'qr-url.html': (
        'URL을 QR코드로 무료 변환',
        'URL QR코드 생성 무료 — 링크·사이트 주소를 QR코드로 즉시 변환해 PNG로 다운로드. 크기·색상 커스텀 가능, 회원가입·설치 없이 브라우저에서 바로 사용.',
        None
    ),
    'qr-vcard.html': (
        '이름·전화·이메일·회사 정보를 vCard QR코드로',
        '명함 QR코드 생성 무료 (vCard) — 이름·전화·이메일·회사 정보를 QR코드로 변환. 스캔하면 연락처에 바로 저장. 회원가입·설치 없이 바로 사용.',
        None
    ),
    'qr-wifi.html': (
        'WiFi 이름(SSID)과 비밀번호를 QR코드로',
        'WiFi QR코드 생성 무료 — WiFi 이름·비밀번호를 QR코드로 변환. 스캔하면 비밀번호 입력 없이 바로 WiFi 연결. 회원가입·설치 없이 바로 사용.',
        None
    ),
}

ok_count = 0
fail_count = 0

for fname, (match_prefix, new_desc, new_title) in PAGES.items():
    fpath = os.path.join(BASE, fname)
    if not os.path.exists(fpath):
        print(f'  SKIP (없음): {fname}')
        continue

    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1) meta description 교체
    pattern_desc = r'(<meta name="description" content=")[^"]*(")'
    def desc_replacer(m):
        if match_prefix in m.group(0):
            return m.group(1) + new_desc + m.group(2)
        return m.group(0)
    new_content = re.sub(pattern_desc, desc_replacer, content)

    if new_content == content:
        print(f'  MISS: {fname} — "{match_prefix[:30]}"')
        fail_count += 1
        continue

    # 2) og:description / twitter:description 동기화
    new_content = re.sub(
        r'(<meta property="og:description" content=")[^"]*(")',
        lambda x: x.group(1) + new_desc + x.group(2),
        new_content
    )
    new_content = re.sub(
        r'(<meta name="twitter:description" content=")[^"]*(")',
        lambda x: x.group(1) + new_desc + x.group(2),
        new_content
    )

    # 3) 타이틀 교체 (지정된 페이지만)
    if new_title:
        new_content = re.sub(
            r'(<title>)[^<]*(</title>)',
            lambda x: x.group(1) + new_title + x.group(2),
            new_content
        )
        # og:title / twitter:title 도 동기화
        new_content = re.sub(
            r'(<meta property="og:title" content=")[^"]*(")',
            lambda x: x.group(1) + new_title.split(' | ')[0] + x.group(2),
            new_content
        )
        new_content = re.sub(
            r'(<meta name="twitter:title" content=")[^"]*(")',
            lambda x: x.group(1) + new_title.split(' | ')[0] + x.group(2),
            new_content
        )

    with open(fpath, 'w', encoding='utf-8') as f:
        f.write(new_content)
    title_note = ' [타이틀도 교체]' if new_title else ''
    print(f'  OK{title_note}: {fname}')
    ok_count += 1

print(f'\n완료: {ok_count}개 교체, {fail_count}개 실패')
