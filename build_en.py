"""
QRKit 영어 버전 자동 생성 스크립트
실행: python build_en.py
결과: en/ 폴더에 영어 버전 HTML 파일 생성
"""

import os, re, shutil, sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

BASE = os.path.dirname(os.path.abspath(__file__))
EN_DIR = os.path.join(BASE, 'en')
os.makedirs(EN_DIR, exist_ok=True)

# ── 1. 페이지별 메타 번역 ─────────────────────────────────────────────────────
PAGE_META = {
    'qr-url.html': {
        'title': 'URL QR Code Generator Free Online – Convert Links to QR | WooaQR',
        'desc':  'Convert any URL or website link to a QR code for free. Customize size and colors. Download as PNG. No signup required — 100% browser-based.',
        'kw':    'URL QR code, link QR code, QR code generator, URL to QR, website QR code, free QR code, QR code maker online',
        'og_title': 'URL QR Code Generator – Free Online | WooaQR',
        'og_desc':  'Turn any URL into a QR code instantly. Customize size and colors. Free, no signup, download as PNG.',
        'app_name': 'URL QR Code Generator',
        'faq': [
            ('What should I do if the QR code is not scanning?',
             'Try increasing the QR code size or the error correction level and regenerate. Also check that the camera lens is clean.'),
            ('How long will the generated QR code work?',
             'The QR code itself never expires. However, the URL encoded inside must remain valid and active.'),
            ('Can I generate a high-resolution QR code for printing?',
             'Yes. Download as PNG in high resolution and use it for printed materials.'),
        ],
        'h1': 'URL QR Code Generator – Free Online',
        'tool_desc': 'Enter any URL to generate a QR code. Customize size and colors, then download as PNG. Everything runs in your browser.',
        'breadcrumb': 'URL QR Code',
        'cross_banner_text': 'Want to edit the QR code image?',
        'cross_banner_link_text': '🖼️ WooaImage – Edit Images →',
        'cross_banner_href': 'https://imagekit.wooahouse.com/',
    },
    'qr-text.html': {
        'title': 'Text QR Code Generator Free Online – Text to QR Code | WooaQR',
        'desc':  'Convert any text or message to a QR code for free. Great for notes, memos, and short messages. Download as PNG. No signup needed.',
        'kw':    'text QR code, text to QR, QR code from text, message QR code, note QR code, free QR code generator',
        'og_title': 'Text QR Code Generator – Free Online | WooaQR',
        'og_desc':  'Convert any text or message to a QR code. Free, no signup. Download as PNG.',
        'app_name': 'Text QR Code Generator',
        'faq': [
            ('How much text can I encode in a QR code?',
             'A QR code can hold up to about 4,000 characters. Longer text results in a denser, more complex code.'),
            ('Can the text be in any language?',
             'Yes. Any language including special characters is supported. Unicode text is encoded correctly.'),
            ('Can I use this to share notes or memos?',
             'Yes. Encode your note as a QR code and anyone can scan it to read the content instantly.'),
        ],
        'h1': 'Text QR Code Generator – Free Online',
        'tool_desc': 'Type or paste any text to generate a QR code. Customize size and colors. Download as PNG. All processing happens in your browser.',
        'breadcrumb': 'Text QR Code',
        'cross_banner_text': 'Need to generate a QR code from a URL instead?',
        'cross_banner_link_text': '🔗 URL QR Code →',
        'cross_banner_href': '../qr-url.html',
    },
    'qr-wifi.html': {
        'title': 'WiFi QR Code Generator Free Online – Share WiFi with QR | WooaQR',
        'desc':  'Generate a WiFi QR code to share your network instantly. Scan with a smartphone to connect automatically — no password typing needed. Free online tool.',
        'kw':    'WiFi QR code, WiFi sharing QR, SSID QR code, WiFi password QR, connect WiFi QR code, free WiFi QR generator',
        'og_title': 'WiFi QR Code Generator – Free Online | WooaQR',
        'og_desc':  'Create a WiFi QR code from SSID and password. Scan to connect instantly. Free, no signup.',
        'app_name': 'WiFi QR Code Generator',
        'faq': [
            ('Does scanning a WiFi QR code connect automatically?',
             'Yes. On modern Android and iOS devices, scanning the QR code will automatically connect to the WiFi network.'),
            ('Is the WiFi password exposed in the QR code image?',
             'The password is not visible in the image itself, but a QR scanner app can read and display the password text.'),
            ('What security types are supported?',
             'WPA/WPA2, WEP, and open (no password) networks are all supported.'),
        ],
        'h1': 'WiFi QR Code Generator – Free Online',
        'tool_desc': 'Enter your WiFi network name (SSID) and password to generate a QR code. Guests can scan to connect instantly without typing. Free and browser-based.',
        'breadcrumb': 'WiFi QR Code',
        'cross_banner_text': 'Need to create a business card QR code?',
        'cross_banner_link_text': '👤 vCard QR Code →',
        'cross_banner_href': '../qr-vcard.html',
    },
    'qr-vcard.html': {
        'title': 'Business Card QR Code Generator Free – vCard QR Code | WooaQR',
        'desc':  'Create a vCard QR code with name, phone, email, and company info. Scan with a smartphone to save contact details instantly. Free digital business card.',
        'kw':    'vCard QR code, business card QR, contact QR code, digital business card, QR code contact, free vCard generator',
        'og_title': 'Business Card QR Code (vCard) – Free Online | WooaQR',
        'og_desc':  'Generate a vCard QR code with your contact info. Scan to save to contacts. Free, no signup.',
        'app_name': 'vCard QR Code Generator',
        'faq': [
            ('What information can I include in a business card QR code?',
             'You can include name, phone number, email, company name, job title, address, and website URL using the vCard standard.'),
            ('Will scanning the QR code automatically add the contact?',
             'Yes. Scanning the QR code will open the contact save screen automatically on most smartphones.'),
            ('Can I create a digital business card with this?',
             'Yes. This is an ideal tool for creating a QR code to use as a modern digital business card.'),
        ],
        'h1': 'Business Card QR Code Generator – Free (vCard)',
        'tool_desc': 'Enter your name, phone, email, and company details to generate a vCard QR code. Share it as a digital business card. All browser-based, free.',
        'breadcrumb': 'vCard QR Code',
        'cross_banner_text': 'Need to generate a QR code for your email?',
        'cross_banner_link_text': '✉️ Email QR Code →',
        'cross_banner_href': '../qr-email.html',
    },
    'qr-email.html': {
        'title': 'Email QR Code Generator Free Online – Pre-fill Email with QR | WooaQR',
        'desc':  'Generate a QR code that pre-fills email address, subject, and body when scanned. Perfect for contact forms and promotions. Free, no signup required.',
        'kw':    'email QR code, mailto QR code, QR code email, pre-fill email QR, contact QR code, free email QR generator',
        'og_title': 'Email QR Code Generator – Free Online | WooaQR',
        'og_desc':  'Create a QR code that opens a pre-filled email when scanned. Free, no signup.',
        'app_name': 'Email QR Code Generator',
        'faq': [
            ('What happens when someone scans the email QR code?',
             'The email app on their device opens with the To address, subject, and body pre-filled, ready to send.'),
            ('Can I include a pre-written message in the email?',
             'Yes. You can pre-fill the recipient, subject, and message body all at once.'),
            ('Is this useful for business contact forms?',
             'Absolutely. Place the QR code on printed materials so customers can send inquiries with a single scan.'),
        ],
        'h1': 'Email QR Code Generator – Free Online',
        'tool_desc': 'Enter an email address, subject, and body to generate a QR code. Scanning it opens a pre-filled email. Perfect for contact pages and flyers.',
        'breadcrumb': 'Email QR Code',
        'cross_banner_text': 'Need to create a phone call QR code?',
        'cross_banner_link_text': '📞 Phone QR Code →',
        'cross_banner_href': '../qr-phone.html',
    },
    'qr-phone.html': {
        'title': 'Phone Number QR Code Generator Free Online | WooaQR',
        'desc':  'Generate a QR code from a phone number. Scanning it will automatically dial the number. Free, no signup. Download as PNG for print or digital use.',
        'kw':    'phone number QR code, QR code phone, call QR code, tel QR code, dial QR code, free phone QR generator',
        'og_title': 'Phone Number QR Code Generator – Free Online | WooaQR',
        'og_desc':  'Create a QR code from a phone number. Scan to call instantly. Free, no signup.',
        'app_name': 'Phone QR Code Generator',
        'faq': [
            ('What happens when someone scans the phone QR code?',
             'The phone app opens with the number pre-dialed, ready to call with one tap.'),
            ('Does it work for international phone numbers?',
             'Yes. Enter the number in international format (e.g. +1-800-555-1234) for best results.'),
            ('Can I use this on printed menus or posters?',
             'Yes. Download the QR code as PNG and add it to any printed or digital material.'),
        ],
        'h1': 'Phone Number QR Code Generator – Free Online',
        'tool_desc': 'Enter a phone number to generate a QR code. Scanning it dials the number instantly. Free, no signup, fully browser-based.',
        'breadcrumb': 'Phone QR Code',
        'cross_banner_text': 'Need to create an SMS QR code?',
        'cross_banner_link_text': '💬 SMS QR Code →',
        'cross_banner_href': '../qr-sms.html',
    },
    'qr-sms.html': {
        'title': 'SMS QR Code Generator Free Online – Pre-fill Text Message QR | WooaQR',
        'desc':  'Generate a QR code that pre-fills a phone number and SMS message when scanned. Perfect for customer service and campaigns. Free, no signup.',
        'kw':    'SMS QR code, text message QR code, sms QR generator, pre-fill SMS QR, message QR code, free SMS QR',
        'og_title': 'SMS QR Code Generator – Free Online | WooaQR',
        'og_desc':  'Create a QR code that opens a pre-filled SMS when scanned. Free, no signup.',
        'app_name': 'SMS QR Code Generator',
        'faq': [
            ('What happens when someone scans the SMS QR code?',
             'The messaging app opens with the recipient number and message body pre-filled, ready to send.'),
            ('Can I pre-write the SMS content?',
             'Yes. Enter the phone number and your message text and both will be pre-filled when scanned.'),
            ('Is this useful for marketing campaigns?',
             'Yes. SMS QR codes on posters or flyers let customers contact you with a single scan.'),
        ],
        'h1': 'SMS QR Code Generator – Free Online',
        'tool_desc': 'Enter a phone number and optional message to generate a QR code. Scanning it opens a pre-filled SMS. Free and fully browser-based.',
        'breadcrumb': 'SMS QR Code',
        'cross_banner_text': 'Need to create a social media QR code?',
        'cross_banner_link_text': '📲 Social Media QR Code →',
        'cross_banner_href': '../qr-social.html',
    },
    'qr-social.html': {
        'title': 'Social Media QR Code Generator Free – Instagram YouTube TikTok | WooaQR',
        'desc':  'Generate QR codes for Instagram, YouTube, TikTok, KakaoTalk, and other social media profiles. Share your profile with a single scan. Free online tool.',
        'kw':    'social media QR code, Instagram QR code, YouTube QR code, TikTok QR code, profile QR code, social QR generator free',
        'og_title': 'Social Media QR Code Generator – Free Online | WooaQR',
        'og_desc':  'Create QR codes for Instagram, YouTube, TikTok and more. Share profiles with a scan. Free, no signup.',
        'app_name': 'Social Media QR Code Generator',
        'faq': [
            ('Which social media platforms are supported?',
             'Instagram, YouTube, TikTok, X (Twitter), Facebook, KakaoTalk, LINE, and more are supported.'),
            ('Can followers reach my profile by scanning?',
             'Yes. Scanning the QR code opens your social media profile page directly.'),
            ('Can I use this on business cards or print materials?',
             'Yes. Download the QR code as PNG and add it to any print or digital material to drive followers to your profile.'),
        ],
        'h1': 'Social Media QR Code Generator – Free Online',
        'tool_desc': 'Select a platform and enter your profile URL to generate a QR code. Scanning it opens your social media profile directly. Free and browser-based.',
        'breadcrumb': 'Social Media QR Code',
        'cross_banner_text': 'Need to create a location QR code?',
        'cross_banner_link_text': '📍 Location QR Code →',
        'cross_banner_href': '../qr-location.html',
    },
    'qr-location.html': {
        'title': 'Location QR Code Generator Free Online – GPS Map QR Code | WooaQR',
        'desc':  'Generate a QR code from GPS coordinates or an address. Scanning opens Google Maps or the native map app automatically. Free, no signup.',
        'kw':    'location QR code, GPS QR code, map QR code, address QR code, Google Maps QR, coordinates QR code, free location QR',
        'og_title': 'Location QR Code Generator – Free Online | WooaQR',
        'og_desc':  'Create a QR code from GPS coordinates or address. Scan to open maps instantly. Free, no signup.',
        'app_name': 'Location QR Code Generator',
        'faq': [
            ('What happens when someone scans the location QR code?',
             'The native map app (Google Maps, Apple Maps, etc.) opens directly to the specified location.'),
            ('Can I use a street address instead of GPS coordinates?',
             'Yes. Enter either GPS coordinates or a full street address — both are supported.'),
            ('Is this useful for shops or event venues?',
             'Absolutely. Place the QR code on flyers or signs so people can navigate to your location with one scan.'),
        ],
        'h1': 'Location QR Code Generator – Free Online',
        'tool_desc': 'Enter GPS coordinates or an address to generate a QR code. Scanning it opens the location in a map app. Great for shops, events, and meetups.',
        'breadcrumb': 'Location QR Code',
        'cross_banner_text': 'Need to create a WiFi QR code?',
        'cross_banner_link_text': '📶 WiFi QR Code →',
        'cross_banner_href': '../qr-wifi.html',
    },
    'qr-custom.html': {
        'title': 'Custom QR Code Generator – Color & Logo QR Code Free | WooaQR',
        'desc':  'Customize QR codes with your brand colors and logo. Change foreground and background colors, insert a logo image in the center. Free online tool.',
        'kw':    'custom QR code, colored QR code, logo QR code, QR code with logo, branded QR code, QR code customizer, color QR generator',
        'og_title': 'Custom QR Code Generator – Color & Logo | WooaQR',
        'og_desc':  'Create branded QR codes with custom colors and a logo image. Free, no signup.',
        'app_name': 'QR Code Customizer',
        'faq': [
            ('Can I insert a logo or image into the QR code?',
             'Yes. Upload a logo image and it will automatically be placed in the center of the QR code.'),
            ('Will the QR code still scan correctly with a logo?',
             'Yes. Thanks to error correction, the QR code remains scannable even with a logo in the center. Avoid making the logo too large.'),
            ('Can I change the colors?',
             'Yes. You can freely set both the foreground (QR pattern) color and the background color.'),
        ],
        'h1': 'Custom QR Code Generator – Color & Logo',
        'tool_desc': 'Customize your QR code with brand colors and a logo. Upload a logo image to embed it in the center. Download as PNG. All runs in your browser.',
        'breadcrumb': 'Custom QR Code',
        'cross_banner_text': 'Need a simple URL QR code?',
        'cross_banner_link_text': '🔗 URL QR Code →',
        'cross_banner_href': '../qr-url.html',
    },
    'qr-reader.html': {
        'title': 'QR Code Reader Free Online – Decode QR from Image | WooaQR',
        'desc':  'Upload a QR code image to read and decode its content instantly. Supports drag & drop. All processing in your browser — no upload to server.',
        'kw':    'QR code reader, QR code decoder, read QR code from image, QR scanner online, decode QR code, free QR reader',
        'og_title': 'QR Code Reader – Free Online | WooaQR',
        'og_desc':  'Upload a QR code image to decode its content. Free, no signup. 100% browser-based.',
        'app_name': 'QR Code Reader',
        'faq': [
            ('What image formats are supported?',
             'PNG, JPG, GIF, and WebP image files are all supported. Drag & drop or click to upload.'),
            ('Is the QR code image sent to a server?',
             'No. All decoding is done locally in your browser. Your image is never uploaded anywhere.'),
            ('What types of QR codes can be read?',
             'URL, text, WiFi, vCard, email, phone, SMS, and all other standard QR code types are supported.'),
        ],
        'h1': 'QR Code Reader – Free Online',
        'tool_desc': 'Upload a QR code image file to instantly read and decode its content. Supports drag & drop. All processing is local — no server upload.',
        'breadcrumb': 'QR Code Reader',
        'cross_banner_text': 'Want to scan a QR code with your camera?',
        'cross_banner_link_text': '📷 Camera QR Scanner →',
        'cross_banner_href': '../qr-camera.html',
    },
    'qr-camera.html': {
        'title': 'Camera QR Code Scanner Free Online – Real-time Webcam QR Reader | WooaQR',
        'desc':  'Scan QR codes in real time using your webcam or mobile camera. No app download needed. Works in browser. Free and instant QR code scanner.',
        'kw':    'camera QR scanner, webcam QR code reader, real-time QR scanner, QR code scan online, live QR reader, free camera QR',
        'og_title': 'Camera QR Code Scanner – Free Online | WooaQR',
        'og_desc':  'Scan QR codes with your webcam or camera in real time. Free, no app download, browser-based.',
        'app_name': 'Camera QR Code Scanner',
        'faq': [
            ('Does this work on a smartphone camera?',
             'Yes. Open in a mobile browser and grant camera permission to scan QR codes in real time.'),
            ('Is camera access required?',
             'Yes. Camera permission is needed to scan in real time. No data is sent to any server.'),
            ('What types of QR codes can be scanned?',
             'All standard QR code types including URL, text, WiFi, vCard, email, and phone are supported.'),
        ],
        'h1': 'Camera QR Code Scanner – Free Online',
        'tool_desc': 'Allow camera access to scan QR codes in real time using your webcam or mobile camera. No app needed — works directly in the browser.',
        'breadcrumb': 'Camera QR Scanner',
        'cross_banner_text': 'Want to decode a QR code from an image file?',
        'cross_banner_link_text': '🔍 QR Code Reader →',
        'cross_banner_href': '../qr-reader.html',
    },
    'qr-barcode-reader.html': {
        'title': 'QR & Barcode Reader Free Online – Decode from Image | WooaQR',
        'desc':  'Upload an image to read QR codes, EAN-13, CODE128, and other barcode formats. Auto-detection. All processing in browser — no server upload.',
        'kw':    'QR barcode reader, barcode image reader, decode barcode, EAN barcode reader, CODE128 reader, QR barcode decoder online',
        'og_title': 'QR & Barcode Reader – Free Online | WooaQR',
        'og_desc':  'Upload an image to decode QR codes and barcodes automatically. Free, no signup, browser-based.',
        'app_name': 'QR & Barcode Image Reader',
        'faq': [
            ('What barcode formats are supported?',
             'QR code, EAN-13, EAN-8, CODE128, CODE39, UPC-A, and other common formats are auto-detected.'),
            ('Is the image uploaded to a server?',
             'No. All decoding runs entirely in your browser. Nothing is sent to any server.'),
            ('Can it read barcodes from product photos?',
             'Yes. Upload a clear photo containing a barcode and the tool will attempt to detect and decode it automatically.'),
        ],
        'h1': 'QR & Barcode Reader – Free Online',
        'tool_desc': 'Upload an image containing a QR code or barcode. The tool auto-detects and decodes it instantly. All processing is local — no server upload.',
        'breadcrumb': 'QR & Barcode Reader',
        'cross_banner_text': 'Need to generate a barcode from scratch?',
        'cross_banner_link_text': '📊 Barcode Generator →',
        'cross_banner_href': '../barcode-generator.html',
    },
    'barcode-generator.html': {
        'title': 'Barcode Generator Free Online – CODE128 EAN-13 UPC-A | WooaQR',
        'desc':  'Generate CODE128, EAN-13, EAN-8, UPC-A, CODE39 barcodes for free. Customize size and height. Download as PNG or SVG. No signup, browser-based.',
        'kw':    'barcode generator, CODE128 barcode, EAN-13 barcode, UPC-A barcode, CODE39 barcode, free barcode maker, online barcode generator',
        'og_title': 'Barcode Generator – CODE128 EAN-13 UPC-A Free Online | WooaQR',
        'og_desc':  'Generate standard barcodes including CODE128, EAN-13, and UPC-A. Download as PNG or SVG. Free, no signup.',
        'app_name': 'Barcode Generator',
        'faq': [
            ('What barcode formats are supported?',
             'CODE128, EAN-13, EAN-8, UPC-A, and CODE39 are all supported.'),
            ('Can I print the generated barcode?',
             'Yes. Download as PNG or SVG for high-quality printing on labels, products, or documents.'),
            ('Is the barcode creation free?',
             'Yes. All barcode types are generated completely free with no signup required.'),
        ],
        'h1': 'Barcode Generator – Free Online',
        'tool_desc': 'Enter your data and select a barcode format to generate a barcode instantly. Download as PNG or SVG. All processing runs in your browser.',
        'breadcrumb': 'Barcode Generator',
        'cross_banner_text': 'Need to read a barcode from an image?',
        'cross_banner_link_text': '🔍 QR & Barcode Reader →',
        'cross_banner_href': '../qr-barcode-reader.html',
    },
    'qr-batch.html': {
        'title': 'Batch QR Code Generator Free – Multiple URLs to QR Codes | WooaQR',
        'desc':  'Generate QR codes for multiple URLs at once. Enter up to 20 URLs and download all QR codes as a ZIP file. Free bulk QR code generator.',
        'kw':    'batch QR code, bulk QR code generator, multiple QR codes, QR code batch, generate many QR codes, mass QR code free',
        'og_title': 'Batch QR Code Generator – Multiple URLs Free | WooaQR',
        'og_desc':  'Generate QR codes for up to 20 URLs at once. Download all as a ZIP file. Free, no signup.',
        'app_name': 'Batch QR Code Generator',
        'faq': [
            ('How many QR codes can I generate at once?',
             'You can enter up to 20 URLs at once and generate all QR codes in one click.'),
            ('How do I download all the QR codes?',
             'All generated QR codes are packaged into a single ZIP file for easy download.'),
            ('Is there a cost for batch generation?',
             'No. Batch QR code generation is completely free with no signup required.'),
        ],
        'h1': 'Batch QR Code Generator – Free Online',
        'tool_desc': 'Enter multiple URLs to generate QR codes in bulk. Download all as a ZIP file. Fast, free, and fully browser-based — no signup required.',
        'breadcrumb': 'Batch QR Code',
        'cross_banner_text': 'Need to generate a single URL QR code?',
        'cross_banner_link_text': '🔗 URL QR Code →',
        'cross_banner_href': '../qr-url.html',
    },
    'qr-calendar.html': {
        'title': 'Calendar Event QR Code Generator Free – QR for Events | WooaQR',
        'desc':  'Generate a QR code for calendar events. Scanning adds the event to your calendar app automatically. Set title, date, time, and location. Free online.',
        'kw':    'calendar QR code, event QR code, iCal QR code, add to calendar QR, event invitation QR, free calendar QR generator',
        'og_title': 'Calendar Event QR Code Generator – Free Online | WooaQR',
        'og_desc':  'Create a QR code for calendar events. Scan to add to calendar instantly. Free, no signup.',
        'app_name': 'Calendar Event QR Code Generator',
        'faq': [
            ('What happens when someone scans the calendar QR code?',
             'The calendar app opens and prompts the user to save the event with all details pre-filled.'),
            ('Which calendar apps are compatible?',
             'Google Calendar, Apple Calendar, Outlook, and other apps that support iCal (.ics) format are compatible.'),
            ('Can I include location and notes in the event?',
             'Yes. You can include the event title, start and end time, location, and notes.'),
        ],
        'h1': 'Calendar Event QR Code Generator – Free Online',
        'tool_desc': 'Enter event details to generate a QR code. Scanning it adds the event to the user\'s calendar app automatically. Free and browser-based.',
        'breadcrumb': 'Calendar QR Code',
        'cross_banner_text': 'Need to create a location QR code for the venue?',
        'cross_banner_link_text': '📍 Location QR Code →',
        'cross_banner_href': '../qr-location.html',
    },
    'index.html': {
        'title': 'Free QR Code Generator & Reader – Barcode Tools Online | WooaQR',
        'desc':  'Free online QR code tools: generate URL, text, WiFi, vCard, email QR codes, read QR from images, and create barcodes. No signup, 100% browser-based.',
        'kw':    'QR code generator, QR code reader, barcode generator, free QR code, WiFi QR, vCard QR, URL QR, online QR tools, WooaQR',
        'og_title': 'Free QR Code Generator & Reader | WooaQR',
        'og_desc':  'All QR code tools in one place — generate, read, and customize QR codes for free. No signup, no upload.',
        'app_name': 'WooaQR',
        'faq': [],
        'h1': 'All QR Code Tools – Free, In One Place',
        'tool_desc': 'Generate, read, and customize QR codes for URLs, WiFi, contacts, and more. 100% free, no signup required, all processing in your browser.',
        'breadcrumb': '',
        'cross_banner_text': '',
        'cross_banner_link_text': '',
        'cross_banner_href': '',
    },
    'about.html': {
        'title': 'About WooaQR – Free Online QR Code Tools',
        'desc':  'WooaQR is a free online toolkit for QR code generation, reading, and barcode creation. All processing happens in your browser — no server upload.',
        'kw':    'WooaQR about, QR code tools, free QR generator, WooaHouse tools',
        'og_title': 'About WooaQR | WooaHouse',
        'og_desc':  'WooaQR is a free browser-based QR code toolkit. No signup, no upload. All tools are completely free.',
        'app_name': 'WooaQR',
        'faq': [],
        'h1': '',
        'tool_desc': '',
        'breadcrumb': '',
        'cross_banner_text': '',
        'cross_banner_link_text': '',
        'cross_banner_href': '',
    },
    'privacy.html': {
        'title': 'Privacy Policy | WooaQR',
        'desc':  'Privacy policy for WooaQR — free QR code tools. Your files and data never leave your browser.',
        'kw':    'WooaQR privacy policy',
        'og_title': 'Privacy Policy | WooaQR',
        'og_desc':  'Privacy policy for WooaQR.',
        'app_name': 'WooaQR',
        'faq': [],
        'h1': '',
        'tool_desc': '',
        'breadcrumb': '',
        'cross_banner_text': '',
        'cross_banner_link_text': '',
        'cross_banner_href': '',
    },
}

# ── 2. 공통 문자열 치환 ──────────────────────────────────────────────────────
COMMON = [
    # lang
    ('<html lang="ko">', '<html lang="en">'),
    # locale
    ('ko_KR', 'en_US'),
    # inLanguage
    ('"inLanguage": "ko"', '"inLanguage": "en"'),
    # priceCurrency
    ('"priceCurrency": "KRW"', '"priceCurrency": "USD"'),
    # paths: CSS, JS, manifest
    ('href="css/style.css"', 'href="../css/style.css"'),
    ('href="/manifest.json"', 'href="../manifest.json"'),
    ('src="js/', 'src="../js/'),
    ('href="js/', 'href="../js/'),
    # header nav
    ('>URL QR<', '>URL QR<'),
    ('>WiFi QR<', '>WiFi QR<'),
    ('>명함 QR<', '>vCard QR<'),
    ('>QR 읽기<', '>QR Reader<'),
    ('>바코드<', '>Barcode<'),
    ('>전체 도구 ›<', '>All Tools ›<'),
    # header-right links
    ('href="about.html" style="color:rgba(255,255,255,0.85); font-size:0.85rem; text-decoration:none;">소개</a>',
     'href="../about.html" style="color:rgba(255,255,255,0.85); font-size:0.85rem; text-decoration:none;">About</a>'),
    ('href="index.html" style="color:rgba(255,255,255,0.85); font-size:0.85rem; text-decoration:none;">전체 도구</a>',
     'href="../index.html" style="color:rgba(255,255,255,0.85); font-size:0.85rem; text-decoration:none;">All Tools</a>'),
    # breadcrumb home
    ('>🏠 홈<', '>🏠 Home<'),
    # free-badge
    ('<span class="free-badge">무료</span>', '<span class="free-badge">FREE</span>'),
    # options panel
    ('<div class="options-title">옵션</div>', '<div class="options-title">Options</div>'),
    ('<div class="options-title">QR 설정</div>', '<div class="options-title">QR Settings</div>'),
    ('<div class="options-title">바코드 설정</div>', '<div class="options-title">Barcode Settings</div>'),
    ('<div class="options-title">WiFi 정보 입력</div>', '<div class="options-title">WiFi Details</div>'),
    ('<div class="options-title">이메일 정보</div>', '<div class="options-title">Email Details</div>'),
    ('<div class="options-title">명함 정보</div>', '<div class="options-title">Contact Details</div>'),
    # option labels
    ('<span class="option-label">QR 크기</span>', '<span class="option-label">QR Size</span>'),
    ('<span class="option-label">전경색 (QR)</span>', '<span class="option-label">Foreground Color</span>'),
    ('<span class="option-label">배경색</span>', '<span class="option-label">Background Color</span>'),
    ('<span class="option-label">바코드 형식</span>', '<span class="option-label">Barcode Format</span>'),
    ('<span class="option-label">바코드 높이</span>', '<span class="option-label">Barcode Height</span>'),
    ('<span class="option-label">바코드 너비</span>', '<span class="option-label">Barcode Width</span>'),
    ('<span class="option-label">보안 유형</span>', '<span class="option-label">Security Type</span>'),
    ('<span class="option-label">네트워크 이름 (SSID)</span>', '<span class="option-label">Network Name (SSID)</span>'),
    ('<span class="option-label">비밀번호</span>', '<span class="option-label">Password</span>'),
    ('<span class="option-label">숨김 네트워크</span>', '<span class="option-label">Hidden Network</span>'),
    ('<span class="option-label">이름</span>', '<span class="option-label">Name</span>'),
    ('<span class="option-label">전화번호</span>', '<span class="option-label">Phone</span>'),
    ('<span class="option-label">이메일</span>', '<span class="option-label">Email</span>'),
    ('<span class="option-label">회사명</span>', '<span class="option-label">Company</span>'),
    ('<span class="option-label">직책</span>', '<span class="option-label">Job Title</span>'),
    ('<span class="option-label">주소</span>', '<span class="option-label">Address</span>'),
    ('<span class="option-label">웹사이트</span>', '<span class="option-label">Website</span>'),
    ('<span class="option-label">수신 이메일</span>', '<span class="option-label">To (Email)</span>'),
    ('<span class="option-label">제목</span>', '<span class="option-label">Subject</span>'),
    ('<span class="option-label">내용</span>', '<span class="option-label">Body</span>'),
    ('<span class="option-label">수신 번호</span>', '<span class="option-label">Phone Number</span>'),
    ('<span class="option-label">문자 내용</span>', '<span class="option-label">Message</span>'),
    ('<span class="option-label">플랫폼</span>', '<span class="option-label">Platform</span>'),
    ('<span class="option-label">프로필 URL</span>', '<span class="option-label">Profile URL</span>'),
    ('<span class="option-label">위도</span>', '<span class="option-label">Latitude</span>'),
    ('<span class="option-label">경도</span>', '<span class="option-label">Longitude</span>'),
    ('<span class="option-label">오류 수정 수준</span>', '<span class="option-label">Error Correction</span>'),
    ('<span class="option-label">로고 이미지</span>', '<span class="option-label">Logo Image</span>'),
    ('<span class="option-label">로고 크기</span>', '<span class="option-label">Logo Size</span>'),
    ('<span class="option-label">이벤트 제목</span>', '<span class="option-label">Event Title</span>'),
    ('<span class="option-label">시작 날짜/시간</span>', '<span class="option-label">Start Date/Time</span>'),
    ('<span class="option-label">종료 날짜/시간</span>', '<span class="option-label">End Date/Time</span>'),
    ('<span class="option-label">장소</span>', '<span class="option-label">Location</span>'),
    ('<span class="option-label">메모</span>', '<span class="option-label">Notes</span>'),
    # input placeholders
    ('placeholder="https://example.com"', 'placeholder="https://example.com"'),
    ('placeholder="텍스트를 입력하세요"', 'placeholder="Enter text here"'),
    ('placeholder="네트워크 이름 (SSID)"', 'placeholder="Network Name (SSID)"'),
    ('placeholder="WiFi 비밀번호"', 'placeholder="WiFi Password"'),
    ('placeholder="이름"', 'placeholder="Name"'),
    ('placeholder="전화번호"', 'placeholder="Phone number"'),
    ('placeholder="이메일 주소"', 'placeholder="Email address"'),
    ('placeholder="회사명"', 'placeholder="Company name"'),
    ('placeholder="직책"', 'placeholder="Job title"'),
    ('placeholder="주소"', 'placeholder="Address"'),
    ('placeholder="https://"', 'placeholder="https://"'),
    ('placeholder="수신 이메일 주소"', 'placeholder="Recipient email"'),
    ('placeholder="이메일 제목"', 'placeholder="Email subject"'),
    ('placeholder="이메일 내용"', 'placeholder="Email body"'),
    ('placeholder="수신 전화번호"', 'placeholder="Phone number"'),
    ('placeholder="문자 내용 (선택)"', 'placeholder="Message (optional)"'),
    ('placeholder="프로필 URL을 입력하세요"', 'placeholder="Enter profile URL"'),
    ('placeholder="위도 (예: 37.5665)"', 'placeholder="Latitude (e.g. 37.5665)"'),
    ('placeholder="경도 (예: 126.9780)"', 'placeholder="Longitude (e.g. 126.9780)"'),
    ('placeholder="이벤트 제목"', 'placeholder="Event title"'),
    ('placeholder="장소 (선택)"', 'placeholder="Location (optional)"'),
    ('placeholder="메모 (선택)"', 'placeholder="Notes (optional)"'),
    ('placeholder="바코드에 넣을 숫자 또는 텍스트"', 'placeholder="Enter number or text for barcode"'),
    ('placeholder="URL을 한 줄에 하나씩 입력하세요 (최대 20개)"',
     'placeholder="Enter one URL per line (up to 20)"'),
    # QR preview
    ('<div class="qr-preview-label">QR코드 미리보기</div>', '<div class="qr-preview-label">QR Code Preview</div>'),
    ('<span>URL을 입력하면 QR코드가 생성됩니다</span>', '<span>Enter a URL to generate a QR code</span>'),
    ('<span>텍스트를 입력하면 QR코드가 생성됩니다</span>', '<span>Enter text to generate a QR code</span>'),
    ('<span>정보를 입력하면 QR코드가 생성됩니다</span>', '<span>Enter details to generate a QR code</span>'),
    ('<span>위 정보를 입력하면 QR코드가 생성됩니다</span>', '<span>Enter the details above to generate a QR code</span>'),
    # buttons
    ('>⬇️ PNG 다운로드<', '>⬇️ Download PNG<'),
    ('>⬇️ 다운로드<', '>⬇️ Download<'),
    ('>⬇️ SVG 다운로드<', '>⬇️ Download SVG<'),
    ('>📦 전체 ZIP 다운로드<', '>📦 Download All (ZIP)<'),
    ('>📦 ZIP 다운로드<', '>📦 Download ZIP<'),
    ('>🔍 QR코드 읽기<', '>🔍 Read QR Code<'),
    ('>📷 카메라 시작<', '>📷 Start Camera<'),
    ('>📷 카메라 중지<', '>📷 Stop Camera<'),
    ('>🎥 카메라 열기<', '>🎥 Open Camera<'),
    ('>📋 복사<', '>📋 Copy<'),
    ('>✅ 복사됨<', '>✅ Copied!<'),
    ('>QR코드 생성<', '>Generate QR Code<'),
    ('>바코드 생성<', '>Generate Barcode<'),
    ('>생성하기<', '>Generate<'),
    # cross link tip
    ('💡 QR코드가 담긴 이미지를 편집하고 싶다면?', '💡 Want to edit the image containing your QR code?'),
    ('<a href="https://imagekit.wooahouse.com/" target="_blank" rel="noopener">WooaImage에서 이미지 편집하기 →</a>',
     '<a href="https://imagekit.wooahouse.com/" target="_blank" rel="noopener">Edit images with WooaImage →</a>'),
    # drop zone
    ('이미지 파일을 여기에 끌어다 놓으세요', 'Drop an image file here'),
    ('또는 클릭하여 파일 선택', 'or click to select a file'),
    ('파일을 여기에 끌어다 놓으세요', 'Drop your file here'),
    ('QR코드 이미지를 여기에 끌어다 놓으세요', 'Drop a QR code image here'),
    ('이미지 파일 선택', 'Select Image File'),
    # file select
    ('파일 선택', 'Select File'),
    # label tags
    ('<label for="urlInput">URL 입력</label>', '<label for="urlInput">Enter URL</label>'),
    ('<label for="textInput">텍스트 입력</label>', '<label for="textInput">Enter Text</label>'),
    ('<label for="urlsInput">URL 목록</label>', '<label for="urlsInput">URL List</label>'),
    # result / decode output
    ('<div class="result-title">디코딩 결과</div>', '<div class="result-title">Decoded Result</div>'),
    ('<div class="result-title">인식 결과</div>', '<div class="result-title">Scan Result</div>'),
    ('디코딩 결과:', 'Decoded Result:'),
    # index hero
    ('<h1>모든 QR코드 작업 무료로, 한 곳에서</h1>',
     '<h1>All QR Code Tools – Free, In One Place</h1>'),
    ('<p>생성·읽기·바코드까지 <strong style="color:#FFD700;">100% 무료</strong><br>회원가입 없이, 파일은 서버에 저장되지 않아요</p>',
     '<p>Generate, read &amp; barcode — <strong style="color:#FFD700;">100% Free</strong><br>No signup. Files never leave your browser.</p>'),
    ('<button id="heroInstallBtn" class="hero-install-btn">📌 홈 화면에 추가</button>',
     '<button id="heroInstallBtn" class="hero-install-btn">📌 Add to Home Screen</button>'),
    # hero-related
    ('<span>이미지 파일도 편집하세요</span>', '<span>Also edit your image files</span>'),
    ('<a href="https://imagekit.wooahouse.com/" target="_blank" rel="noopener">WooaImage에서 이미지 편집하기 →</a>',
     '<a href="https://imagekit.wooahouse.com/" target="_blank" rel="noopener">Edit images with WooaImage →</a>'),
    # category headers
    ('<span class="category-title">QR 생성</span>', '<span class="category-title">QR Code Generator</span>'),
    ('<p class="category-desc">URL·텍스트·WiFi·명함 등 다양한 QR코드를 만드는 도구</p>',
     '<p class="category-desc">Create QR codes for URLs, text, WiFi, contacts, and more</p>'),
    ('<span class="category-title">QR 읽기</span>', '<span class="category-title">QR Code Reader</span>'),
    ('<p class="category-desc">이미지 파일 또는 카메라로 QR코드를 스캔·해독하는 도구</p>',
     '<p class="category-desc">Scan and decode QR codes from image files or camera</p>'),
    ('<span class="category-title">바코드</span>', '<span class="category-title">Barcode</span>'),
    ('<p class="category-desc">다양한 형식의 바코드 생성 및 QR 배치 생성 도구</p>',
     '<p class="category-desc">Barcode generation and bulk QR code creation tools</p>'),
    # tool cards
    ('<div class="tool-name">URL QR코드</div>', '<div class="tool-name">URL QR Code</div>'),
    ('<div class="tool-desc">URL을 QR코드로 변환, 다운로드</div>', '<div class="tool-desc">Convert URL to QR code and download</div>'),
    ('<div class="tool-name">텍스트 QR코드</div>', '<div class="tool-name">Text QR Code</div>'),
    ('<div class="tool-desc">텍스트·메모를 QR코드로 변환</div>', '<div class="tool-desc">Convert text or notes to QR code</div>'),
    ('<div class="tool-name">WiFi QR코드</div>', '<div class="tool-name">WiFi QR Code</div>'),
    ('<div class="tool-desc">WiFi 정보를 QR코드로 간편 연결</div>', '<div class="tool-desc">Share WiFi with a scannable QR code</div>'),
    ('<div class="tool-name">명함 QR코드</div>', '<div class="tool-name">Business Card QR</div>'),
    ('<div class="tool-desc">이름·전화·이메일을 vCard QR로</div>', '<div class="tool-desc">Contact info as vCard QR code</div>'),
    ('<div class="tool-name">이메일 QR코드</div>', '<div class="tool-name">Email QR Code</div>'),
    ('<div class="tool-desc">이메일 주소·제목·내용을 QR로</div>', '<div class="tool-desc">Pre-fill email address, subject, and body</div>'),
    ('<div class="tool-name">전화번호 QR코드</div>', '<div class="tool-name">Phone QR Code</div>'),
    ('<div class="tool-desc">전화번호를 QR코드로 변환</div>', '<div class="tool-desc">Convert phone number to QR code</div>'),
    ('<div class="tool-name">SMS QR코드</div>', '<div class="tool-name">SMS QR Code</div>'),
    ('<div class="tool-desc">수신번호·문자 내용 미리입력 QR 생성</div>', '<div class="tool-desc">Pre-fill phone number and SMS message</div>'),
    ('<div class="tool-name">소셜미디어 QR코드</div>', '<div class="tool-name">Social Media QR</div>'),
    ('<div class="tool-desc">Instagram·YouTube·TikTok·카카오톡 프로필 QR</div>',
     '<div class="tool-desc">Instagram, YouTube, TikTok profile QR</div>'),
    ('<div class="tool-name">위치 QR코드</div>', '<div class="tool-name">Location QR Code</div>'),
    ('<div class="tool-desc">좌표·주소 → 스캔하면 지도 앱 자동 실행</div>',
     '<div class="tool-desc">Coordinates/address → opens map app on scan</div>'),
    ('<div class="tool-name">QR코드 읽기</div>', '<div class="tool-name">QR Code Reader</div>'),
    ('<div class="tool-desc">이미지 파일에서 QR코드 디코딩</div>', '<div class="tool-desc">Decode QR code from image file</div>'),
    ('<div class="tool-name">카메라 QR 읽기</div>', '<div class="tool-name">Camera QR Scanner</div>'),
    ('<div class="tool-desc">웹캠으로 실시간 QR코드 스캔</div>', '<div class="tool-desc">Real-time QR scanning with webcam</div>'),
    ('<div class="tool-name">바코드 생성기</div>', '<div class="tool-name">Barcode Generator</div>'),
    ('<div class="tool-desc">CODE128·EAN-13·UPC-A 바코드 생성</div>', '<div class="tool-desc">Generate CODE128, EAN-13, UPC-A barcodes</div>'),
    ('<div class="tool-name">QR 배치 생성</div>', '<div class="tool-name">Batch QR Code</div>'),
    ('<div class="tool-desc">여러 URL을 한 번에 QR코드로 생성</div>', '<div class="tool-desc">Generate QR codes for multiple URLs at once</div>'),
    ('<div class="tool-name">바코드 이미지 읽기</div>', '<div class="tool-name">Barcode Image Reader</div>'),
    ('<div class="tool-desc">이미지에서 QR·EAN·CODE128 등 자동 인식</div>',
     '<div class="tool-desc">Auto-detect QR, EAN, CODE128 from image</div>'),
    ('<div class="tool-name">QR 커스터마이징</div>', '<div class="tool-name">Custom QR Code</div>'),
    ('<div class="tool-desc">색상·로고 삽입 QR코드 생성</div>', '<div class="tool-desc">Custom colors and logo QR code</div>'),
    ('<div class="tool-name">일정 QR코드</div>', '<div class="tool-name">Calendar Event QR</div>'),
    ('<div class="tool-desc">이벤트 정보를 QR로, 스캔 시 캘린더에 자동 추가</div>',
     '<div class="tool-desc">Event details QR — scan to add to calendar</div>'),
    # features section
    ('개인정보 보호', 'Privacy Protected'),
    ('파일이 서버로 전송되지 않습니다', 'Files never sent to server'),
    ('>빠른 처리<', '>Fast Processing<'),
    ('로컬 처리로 속도 빠름', 'Fast local processing'),
    ('>완전 무료<', '>Completely Free<'),
    ('회원가입 없이 무제한 사용', 'Unlimited, no signup'),
    ('>모든 기기<', '>All Devices<'),
    ('PC·모바일·태블릿 모두 지원', 'Works on PC, mobile, and tablet'),
    # footer
    ('모든 권리 보유.', 'All rights reserved.'),
    ('>개인정보처리방침<', '>Privacy Policy<'),
    ('href="privacy.html"', 'href="../privacy.html"'),
    ('href="about.html"', 'href="../about.html"'),
    ('href="index.html"', 'href="../index.html"'),
    ('>소개<', '>About<'),
    ('>전체 도구<', '>All Tools<'),
    # FAQ heading
    ('>자주 묻는 질문<', '>Frequently Asked Questions<'),
    # pwa install
    ('>📌 홈 화면에 추가<', '>📌 Add to Home Screen<'),
    # our-sites-bar WooaQR active → en/
    ('href="https://qrkit.wooahouse.com/" target="_blank" rel="noopener" class="active"',
     'href="https://qrkit.wooahouse.com/en/" target="_blank" rel="noopener" class="active"'),
    # WooaText icon fix (CLAUDE.md uses ✏️ but site uses 📝)
    ('href="https://textkit.wooahouse.com/" target="_blank" rel="noopener">📝 WooaText</a>',
     'href="https://textkit.wooahouse.com/" target="_blank" rel="noopener">✏️ WooaText</a>'),
    # breadcrumb WooaQR home link
    ('<a href="index.html">WooaQR</a>', '<a href="../index.html">WooaQR</a>'),
    # JS error/status messages
    ("'URL을 입력해주세요.'", "'Please enter a URL.'"),
    ("'텍스트를 입력해주세요.'", "'Please enter text.'"),
    ("'QR코드를 생성할 수 없습니다.'", "'Failed to generate QR code.'"),
    ("'파일을 선택해주세요.'", "'Please select a file.'"),
    ("'지원하지 않는 파일 형식입니다.'", "'Unsupported file format.'"),
    ("'QR코드를 인식하지 못했습니다.'", "'Could not detect a QR code.'"),
    ("'바코드를 인식하지 못했습니다.'", "'Could not detect a barcode.'"),
    # camera messages
    ("'카메라 접근 권한이 필요합니다.'", "'Camera permission is required.'"),
    ("'카메라를 시작할 수 없습니다.'", "'Could not start camera.'"),
    # dynamic content
    ("'QR코드가 생성되었습니다.'", "'QR code generated.'"),
    ("'바코드가 생성되었습니다.'", "'Barcode generated.'"),
    # barcode format options
    ('<option value="CODE128" selected>CODE128 (범용)</option>', '<option value="CODE128" selected>CODE128 (Universal)</option>'),
    ('<option value="EAN13">EAN-13 (상품 바코드)</option>', '<option value="EAN13">EAN-13 (Product barcode)</option>'),
    ('<option value="EAN8">EAN-8 (소형 상품)</option>', '<option value="EAN8">EAN-8 (Small product)</option>'),
    ('<option value="UPCA">UPC-A (미국 상품)</option>', '<option value="UPCA">UPC-A (US product)</option>'),
    ('<option value="CODE39">CODE39 (산업용)</option>', '<option value="CODE39">CODE39 (Industrial)</option>'),
    # WiFi security options
    ('<option value="WPA">WPA/WPA2</option>', '<option value="WPA">WPA/WPA2</option>'),
    ('<option value="WEP">WEP</option>', '<option value="WEP">WEP</option>'),
    ('<option value="nopass">보안 없음 (개방)</option>', '<option value="nopass">None (Open)</option>'),
    # hidden network checkbox
    ('<label>숨김 네트워크</label>', '<label>Hidden Network</label>'),
    # error correction level options
    ('<option value="L">L (7% — 빠름)</option>', '<option value="L">L (7% — Fast)</option>'),
    ('<option value="M" selected>M (15% — 권장)</option>', '<option value="M" selected>M (15% — Recommended)</option>'),
    ('<option value="Q">Q (25% — 높음)</option>', '<option value="Q">Q (25% — High)</option>'),
    ('<option value="H">H (30% — 최고)</option>', '<option value="H">H (30% — Highest)</option>'),
    # about page
    ('<h1 style="font-size:1.8rem;">WooaQR 서비스 소개</h1>', '<h1 style="font-size:1.8rem;">About WooaQR</h1>'),
    ('<p>무료 QR코드 도구 모음 서비스</p>', '<p>Free Online QR Code Toolkit</p>'),
    ('<title>서비스 소개 | WooaQR - 무료 QR코드 도구 모음</title>', '<title>About WooaQR – Free Online QR Code Tools</title>'),
    # privacy page title
    ('<title>개인정보처리방침 | WooaQR</title>', '<title>Privacy Policy | WooaQR</title>'),
    ('<h1>개인정보처리방침</h1>', '<h1>Privacy Policy</h1>'),
    # coupang notice
    ('"이 포스팅은 쿠팡 파트너스 활동의 일환으로, 이에 따른 일정액의 수수료를 제공받습니다."', ''),

    # ── 색상 스팬 (color span labels) ────────────────────────────────────────
    ('<span>QR 코드 색상</span>', '<span>QR Code Color</span>'),
    ('<span>배경 색상</span>', '<span>Background Color</span>'),

    # ── 라벨 태그 (label tags, not option-label) ──────────────────────────────
    ('<label for="toInput">수신자 이메일 *</label>', '<label for="toInput">Recipient Email *</label>'),
    ('<label for="subjectInput">제목</label>', '<label for="subjectInput">Subject</label>'),
    ('<label for="bodyInput">내용</label>', '<label for="bodyInput">Body</label>'),
    ('<label for="phoneInput">전화번호 입력</label>', '<label for="phoneInput">Enter Phone Number</label>'),
    ('<label for="phoneInput">수신자 번호 *</label>', '<label for="phoneInput">Recipient Number *</label>'),
    ('<label for="ssidInput">WiFi 이름 (SSID)</label>', '<label for="ssidInput">WiFi Name (SSID)</label>'),
    ('<label for="passwordInput">비밀번호</label>', '<label for="passwordInput">Password</label>'),
    ('<label for="encryptionSelect">암호화 방식</label>', '<label for="encryptionSelect">Security Type</label>'),
    ('<label for="hiddenCheck">숨겨진 네트워크 (Hidden SSID)</label>', '<label for="hiddenCheck">Hidden Network (Hidden SSID)</label>'),
    ('<label for="nameInput">이름 *</label>', '<label for="nameInput">Name *</label>'),
    ('<label for="orgInput">회사 / 소속</label>', '<label for="orgInput">Company / Organization</label>'),
    ('<label for="titleInput">직책</label>', '<label for="titleInput">Job Title</label>'),
    ('<label for="phoneInput">전화번호</label>', '<label for="phoneInput">Phone</label>'),
    ('<label for="emailInput">이메일</label>', '<label for="emailInput">Email</label>'),
    ('<label for="websiteInput">웹사이트</label>', '<label for="websiteInput">Website</label>'),
    ('<label for="socialInput" id="socialInputLabel">프로필 ID 또는 URL</label>', '<label for="socialInput" id="socialInputLabel">Profile ID or URL</label>'),
    ('<label for="latInput">위도 (Latitude)</label>', '<label for="latInput">Latitude</label>'),
    ('<label for="lngInput" style="margin-top:0.8rem;">경도 (Longitude)</label>', '<label for="lngInput" style="margin-top:0.8rem;">Longitude</label>'),
    ('<label for="addressInput">주소</label>', '<label for="addressInput">Address</label>'),
    ('<label for="barcodeInput">바코드 값 입력</label>', '<label for="barcodeInput">Barcode Value</label>'),
    ('<label>플랫폼 선택</label>', '<label>Select Platform</label>'),
    ('<label>QR코드 크기</label>', '<label>QR Code Size</label>'),

    # ── placeholder 추가 ───────────────────────────────────────────────────────
    ('placeholder="이메일 제목을 입력하세요"', 'placeholder="Enter email subject"'),
    ('placeholder="이메일 내용을 입력하세요 (선택사항)"', 'placeholder="Enter email body (optional)"'),
    ('placeholder="010-1234-5678 또는 +82-10-1234-5678"', 'placeholder="e.g. +1-800-555-1234"'),
    ('placeholder="문자 내용을 입력하세요 (선택사항)"', 'placeholder="Enter message (optional)"'),
    ('placeholder="WiFi 비밀번호 입력 (없으면 비워두세요)"', 'placeholder="WiFi password (leave blank if none)"'),
    ('placeholder="홍길동"', 'placeholder="John Doe"'),
    ('placeholder="(주)회사명"', 'placeholder="Company name"'),
    ('placeholder="부장"', 'placeholder="Manager"'),
    ('placeholder="플랫폼을 먼저 선택하세요"', 'placeholder="Select a platform first"'),
    ('placeholder="예: 37.566535"', 'placeholder="e.g. 37.566535"'),
    ('placeholder="예: 126.977969"', 'placeholder="e.g. 126.977969"'),
    ('placeholder="예: 서울특별시 중구 세종대로 110"', 'placeholder="e.g. 1600 Pennsylvania Ave NW, Washington DC"'),
    ('placeholder="바코드에 인코딩할 텍스트 또는 숫자"', 'placeholder="Enter text or number for barcode"'),
    ('placeholder="QR코드로 변환할 텍스트를 입력하세요..."', 'placeholder="Enter text to convert to QR code..."'),
    ('placeholder="https://example.com 또는 텍스트 입력"', 'placeholder="https://example.com or text"'),
    ('placeholder="예: 팀 미팅, 생일 파티, 의사 예약"', 'placeholder="e.g. Team Meeting, Birthday Party"'),
    ('placeholder="예: 서울시 강남구 테헤란로 123, 회의실 A"', 'placeholder="e.g. 123 Main St, Room A"'),
    ('placeholder="이벤트에 대한 추가 정보를 입력하세요..."', 'placeholder="Add event notes..."'),
    ('@username 또는 프로필 ID', '@username or profile ID'),
    ('채널명 또는 @핸들', 'channel name or @handle'),
    ('프로필 ID 또는 페이지명', 'profile ID or page name'),
    ('오픈채팅 링크를 직접 입력하세요', 'Enter open chat link directly'),

    # ── SMS label ──────────────────────────────────────────────────────────────
    ('문자 내용 <span style="font-weight:400;color:#888;">(선택사항, <span id="charCount">0</span>/80자)</span>',
     'Message <span style="font-weight:400;color:#888;">(optional, <span id="charCount">0</span>/80 chars)</span>'),

    # ── qr-phone info line ─────────────────────────────────────────────────────
    ('숫자와 +, -, 공백만 입력하세요. 국제 형식(+82...)도 지원합니다.',
     'Enter digits and +, -, spaces only. International format (+1...) is supported.'),
    ('생성될 QR 데이터: <strong id="telValue"></strong>',
     'QR data to encode: <strong id="telValue"></strong>'),

    # ── qr-phone cross-link-tip ────────────────────────────────────────────────
    ('💡 명함에 QR코드를 넣고 싶다면? <a href="../qr-sms.html">명함 QR코드 생성하기 →</a>',
     '💡 Want to add a QR code to a business card? <a href="../qr-vcard.html">Business Card QR Code →</a>'),

    # ── qr-wifi usage tip ─────────────────────────────────────────────────────
    ('<strong>📱 사용 방법</strong><br>\n    생성된 QR코드를 인쇄하거나 화면에 표시하면, 스마트폰 카메라로 스캔해서 바로 WiFi에 연결할 수 있습니다. (iOS 11+, Android 10+ 지원)',
     '<strong>📱 How to use</strong><br>\n    Print or display the QR code. Scan with a smartphone camera to connect to WiFi instantly. (iOS 11+, Android 10+)'),

    # ── qr-vcard usage tip ────────────────────────────────────────────────────
    ('<strong>📱 사용 방법</strong><br>\n    생성된 QR코드를 명함에 인쇄하거나 공유하면, 상대방이 스마트폰 카메라로 스캔해서 연락처를 바로 저장할 수 있습니다.',
     '<strong>📱 How to use</strong><br>\n    Print the QR code on your business card or share it. Others can scan with a smartphone camera to save your contact instantly.'),

    # ── WiFi security options (alternate format in source) ────────────────────
    ('<option value="WPA">WPA / WPA2 (일반적)</option>', '<option value="WPA">WPA / WPA2 (Common)</option>'),
    ('<option value="WEP">WEP (구형)</option>', '<option value="WEP">WEP (Legacy)</option>'),
    ('<option value="nopass">없음 (개방형)</option>', '<option value="nopass">None (Open)</option>'),

    # ── camera status badges (JS strings in HTML) ─────────────────────────────
    ('<span class="status-badge stopped" id="statusBadge">⏹ 중지됨</span>',
     '<span class="status-badge stopped" id="statusBadge">⏹ Stopped</span>'),
    ('<span>카메라 시작 버튼을 눌러주세요</span>', '<span>Press Start Camera button</span>'),
    ('<div class="scan-hint">QR코드를 프레임 안에 맞춰주세요</div>',
     '<div class="scan-hint">Align QR code within the frame</div>'),
    ('<button id="startBtn" class="btn-primary">▶ 카메라 시작</button>',
     '<button id="startBtn" class="btn-primary">▶ Start Camera</button>'),
    ('<button id="stopBtn" class="btn-secondary" style="display:none;">⏹ 카메라 중지</button>',
     '<button id="stopBtn" class="btn-secondary" style="display:none;">⏹ Stop Camera</button>'),
    ('<div class="result-label">스캔 결과</div>', '<div class="result-label">Scan Result</div>'),
    ('<button id="copyBtn" class="btn-primary">📋 결과 복사</button>',
     '<button id="copyBtn" class="btn-primary">📋 Copy Result</button>'),
    ('<button id="openBtn" class="btn-secondary" style="display:none;">🔗 URL 열기</button>',
     '<button id="openBtn" class="btn-secondary" style="display:none;">🔗 Open URL</button>'),
    ('<button id="continueBtn" class="btn-secondary">🔄 계속 스캔</button>',
     '<button id="continueBtn" class="btn-secondary">🔄 Continue Scanning</button>'),
    ("if (state === 'scanning') statusBadge.textContent = '🔍 스캔 중...';",
     "if (state === 'scanning') statusBadge.textContent = '🔍 Scanning...';"),
    ("else if (state === 'stopped') statusBadge.textContent = '⏹ 중지됨';",
     "else if (state === 'stopped') statusBadge.textContent = '⏹ Stopped';"),
    ("else if (state === 'found') statusBadge.textContent = '✅ QR코드 발견!';",
     "else if (state === 'found') statusBadge.textContent = '✅ QR Code Found!';"),
    ("let msg = '카메라 접근 실패: ';",
     "let msg = 'Camera access failed: ';"),
    ("if (err.name === 'NotAllowedError') msg += '카메라 권한이 거부되었습니다. 브라우저 설정에서 카메라 권한을 허용해주세요.';",
     "if (err.name === 'NotAllowedError') msg += 'Camera permission was denied. Please allow camera access in your browser settings.';"),
    ("else if (err.name === 'NotFoundError') msg += '카메라를 찾을 수 없습니다.';",
     "else if (err.name === 'NotFoundError') msg += 'No camera found.';"),
    ("else if (err.name === 'NotSupportedError') msg += 'HTTPS 환경에서만 카메라를 사용할 수 있습니다.';",
     "else if (err.name === 'NotSupportedError') msg += 'Camera is only available in HTTPS environments.';"),
    ("copyBtn.textContent = '✅ 복사됨!';",
     "copyBtn.textContent = '✅ Copied!';"),

    # ── camera cross-link-tip ─────────────────────────────────────────────────
    ('💡 이미지 파일로 QR코드를 읽으려면? <a href="../qr-reader.html">QR코드 읽기 (파일 업로드) →</a>',
     '💡 Want to decode a QR code from an image file? <a href="../qr-reader.html">QR Code Reader (file upload) →</a>'),

    # ── qr-reader UI ─────────────────────────────────────────────────────────
    ('<div class="drop-zone-text">이미지를 여기에 드래그하거나 클릭해서 선택</div>',
     '<div class="drop-zone-text">Drag an image here or click to select</div>'),
    ('<div class="drop-zone-sub">PNG, JPG, GIF, WebP, BMP 등 이미지 파일 지원</div>',
     '<div class="drop-zone-sub">Supports PNG, JPG, GIF, WebP, BMP and other image files</div>'),
    ('<div class="result-label">해독 결과</div>', '<div class="result-label">Decoded Result</div>'),
    ('💡 카메라로 실시간 스캔하려면? <a href="../qr-camera.html">카메라 QR 읽기 →</a>',
     '💡 Want to scan in real time? <a href="../qr-camera.html">Camera QR Scanner →</a>'),
    ("resultContent.innerHTML = '<div class=\"result-error\">⚠️ QR코드를 찾을 수 없습니다. 더 선명한 이미지를 사용해보세요.</div>';",
     "resultContent.innerHTML = '<div class=\"result-error\">⚠️ No QR code found. Try a clearer image.</div>';"),

    # ── barcode-generator UI ───────────────────────────────────────────────────
    ('<span class="option-label">형식</span>', '<span class="option-label">Format</span>'),
    ('<option value="EAN13">EAN-13 (12자리 숫자)</option>', '<option value="EAN13">EAN-13 (12-digit number)</option>'),
    ('<option value="UPC">UPC-A (11자리 숫자)</option>', '<option value="UPC">UPC-A (11-digit number)</option>'),
    ('<span class="option-label">라인 폭</span>', '<span class="option-label">Line Width</span>'),
    ('<span class="option-label">값 표시</span>', '<span class="option-label">Show Value</span>'),
    ('<span>바코드 아래 값 표시</span>', '<span>Show value below barcode</span>'),
    ('<span>값을 입력하면 바코드가 생성됩니다</span>', '<span>Enter a value to generate a barcode</span>'),
    ('💡 QR코드도 생성하고 싶다면? <a href="../qr-barcode-reader.html">URL QR코드 생성하기 →</a>',
     '💡 Want to generate a QR code too? <a href="../qr-url.html">URL QR Code Generator →</a>'),
    ("errorMsg.textContent = '⚠️ ' + (e.message || '유효하지 않은 값입니다. 형식에 맞는 값을 입력해주세요.');",
     "errorMsg.textContent = '⚠️ ' + (e.message || 'Invalid value. Please enter a value matching the selected format.');"),

    # ── qr-barcode-reader UI ───────────────────────────────────────────────────
    ('<img id="previewImg" alt="업로드된 이미지">',
     '<img id="previewImg" alt="Uploaded image">'),
    ('<span>🔍 분석 중...</span>', '<span>🔍 Analyzing...</span>'),
    ('<button id="openBtn" class="btn-secondary" style="display:none;">🔗 링크 열기</button>',
     '<button id="openBtn" class="btn-secondary" style="display:none;">🔗 Open Link</button>'),
    ('<h2>지원하는 형식</h2>', '<h2>Supported Formats</h2>'),
    ('<span class="format-tag">QR코드</span>', '<span class="format-tag">QR Code</span>'),
    ('💡 QR코드만 빠르게 읽으려면? <a href="../barcode-generator.html">QR코드 읽기 →</a>',
     '💡 Want to read QR codes quickly? <a href="../qr-reader.html">QR Code Reader →</a>'),
    ("'QR_CODE':     'QR코드',", "'QR_CODE':     'QR Code',"),
    ("'<div class=\"result-label\">인식 결과</div>' +",
     "'<div class=\"result-label\">Detected Result</div>' +"),
    ("'<div class=\"result-error\">⚠️ 인식할 수 없습니다. 이미지가 선명한지 확인해주세요.</div>';",
     "'<div class=\"result-error\">⚠️ Could not detect. Please check the image is clear.</div>';"),
    ("flash(copyBtn, '✅ 복사됨!', '📋 결과 복사');",
     "flash(copyBtn, '✅ Copied!', '📋 Copy Result');"),

    # ── qr-batch UI ───────────────────────────────────────────────────────────
    ('<label for="urlsInput">URL 목록 (한 줄에 하나씩, 최대 20개)</label>',
     '<label for="urlsInput">URL List (one per line, up to 20)</label>'),
    ("urlCount.textContent = lines.length + ' / ' + MAX + '개 입력됨';",
     "urlCount.textContent = lines.length + ' / ' + MAX + ' entered';"),
    ('<div class="url-count" id="urlCount">0 / 20개 입력됨</div>',
     '<div class="url-count" id="urlCount">0 / 20 entered</div>'),
    ('<button id="generateAllBtn" class="btn-primary">⚡ 전체 생성</button>',
     '<button id="generateAllBtn" class="btn-primary">⚡ Generate All</button>'),
    ('<button id="downloadAllBtn" class="btn-primary">⬇️ 전체 ZIP 다운로드</button>',
     '<button id="downloadAllBtn" class="btn-primary">⬇️ Download All (ZIP)</button>'),
    ('💡 단일 URL QR코드를 만들려면? <a href="../qr-url.html">URL QR코드 생성하기 →</a>',
     '💡 Want to create a single URL QR code? <a href="../qr-url.html">URL QR Code Generator →</a>'),
    ("if (urls.length > MAX) { alert('최대 ' + MAX + '개까지 생성할 수 있습니다.'); return; }",
     "if (urls.length > MAX) { alert('You can generate up to ' + MAX + ' QR codes at once.'); return; }"),
    ("generateAllBtn.textContent = '생성 중...';",
     "generateAllBtn.textContent = 'Generating...';"),
    ("item.innerHTML = '<div class=\"batch-item-num\">#' + (i+1) + '</div><div style=\"color:#EF4444;font-size:0.82rem;\">생성 실패</div><div class=\"batch-item-url\">' + escapeHtml(url) + '</div>';",
     "item.innerHTML = '<div class=\"batch-item-num\">#' + (i+1) + '</div><div style=\"color:#EF4444;font-size:0.82rem;\">Generation failed</div><div class=\"batch-item-url\">' + escapeHtml(url) + '</div>';"),
    ("generateAllBtn.textContent = '⚡ 전체 생성';",
     "generateAllBtn.textContent = '⚡ Generate All';"),
    ("downloadAllBtn.textContent = 'ZIP 생성 중...';",
     "downloadAllBtn.textContent = 'Creating ZIP...';"),
    ("downloadAllBtn.textContent = '⬇️ 전체 ZIP 다운로드';",
     "downloadAllBtn.textContent = '⬇️ Download All (ZIP)';"),

    # ── qr-text UI ────────────────────────────────────────────────────────────
    ("document.getElementById('charCount').textContent = text.length + '자';",
     "document.getElementById('charCount').textContent = text.length + ' chars';"),
    ('<div style="text-align:right; font-size:0.8rem; color:var(--text-light); margin-top:-8px;" id="charCount">0자</div>',
     '<div style="text-align:right; font-size:0.8rem; color:var(--text-light); margin-top:-8px;" id="charCount">0 chars</div>'),
    ('💡 텍스트를 더 다양하게 변환하고 싶다면? <a href="../qr-url.html" target="_blank" rel="noopener">WooaText에서 텍스트 도구 보기 →</a>',
     '💡 Want more text conversion tools? <a href="https://textkit.wooahouse.com/" target="_blank" rel="noopener">WooaText – Text Tools →</a>'),
    ("container.innerHTML = '<div class=\"alert alert-error\">텍스트가 너무 깁니다. 내용을 줄여주세요.</div>';",
     "container.innerHTML = '<div class=\"alert alert-error\">Text is too long. Please shorten it.</div>';"),

    # ── qr-url color spans (not matched by options-title variants) ─────────────
    # (already covered by '< span>QR 코드 색상</span>' above)

    # ── qr-email JS strings ───────────────────────────────────────────────────
    ("container.innerHTML = '<div class=\"qr-placeholder\"><span class=\"qr-placeholder-icon\">✉️</span><span>이메일 주소를 입력하면 QR코드가 생성됩니다</span></div>';",
     "container.innerHTML = '<div class=\"qr-placeholder\"><span class=\"qr-placeholder-icon\">✉️</span><span>Enter an email address to generate a QR code</span></div>';"),
    ("<span>이메일 주소를 입력하면 QR코드가 생성됩니다</span>",
     "<span>Enter an email address to generate a QR code</span>"),
    ("container.innerHTML = '<div class=\"alert alert-error\">QR코드 생성에 실패했습니다.</div>';",
     "container.innerHTML = '<div class=\"alert alert-error\">Failed to generate QR code.</div>';"),

    # ── qr-phone JS strings ───────────────────────────────────────────────────
    ("<span>전화번호를 입력하면 QR코드가 생성됩니다</span>",
     "<span>Enter a phone number to generate a QR code</span>"),
    ("container.innerHTML = '<div class=\"qr-placeholder\"><span class=\"qr-placeholder-icon\">📞</span><span>전화번호를 입력하면 QR코드가 생성됩니다</span></div>';",
     "container.innerHTML = '<div class=\"qr-placeholder\"><span class=\"qr-placeholder-icon\">📞</span><span>Enter a phone number to generate a QR code</span></div>';"),

    # ── qr-sms placeholder and JS ──────────────────────────────────────────────
    ("<span>수신자 번호를 입력하면 QR코드가 생성됩니다</span>",
     "<span>Enter recipient number to generate a QR code</span>"),
    ("container.innerHTML = '<div class=\"qr-placeholder\"><span class=\"qr-placeholder-icon\">💬</span><span>수신자 번호를 입력하면 QR코드가 생성됩니다</span></div>';",
     "container.innerHTML = '<div class=\"qr-placeholder\"><span class=\"qr-placeholder-icon\">💬</span><span>Enter recipient number to generate a QR code</span></div>';"),
    ("container.innerHTML = '<div class=\"alert alert-error\">QR코드 생성에 실패했습니다.</div>'+",
     "container.innerHTML = '<div class=\"alert alert-error\">Failed to generate QR code.</div>'+"),

    # ── qr-wifi placeholders and JS ───────────────────────────────────────────
    ("<span>WiFi 이름을 입력하면 QR코드가 생성됩니다</span>",
     "<span>Enter WiFi name to generate a QR code</span>"),
    ("container.innerHTML = '<div class=\"qr-placeholder\"><span class=\"qr-placeholder-icon\">📶</span><span>WiFi 이름을 입력하면 QR코드가 생성됩니다</span></div>';",
     "container.innerHTML = '<div class=\"qr-placeholder\"><span class=\"qr-placeholder-icon\">📶</span><span>Enter WiFi name to generate a QR code</span></div>';"),
    ("container.innerHTML = '<div class=\"alert alert-error\">QR코드 생성에 실패했습니다. 입력값을 확인해주세요.</div>';",
     "container.innerHTML = '<div class=\"alert alert-error\">Failed to generate QR code. Please check your input.</div>';"),

    # ── qr-vcard JS strings ───────────────────────────────────────────────────
    ("<span>이름을 입력하면 QR코드가 생성됩니다</span>",
     "<span>Enter a name to generate a QR code</span>"),
    ("container.innerHTML = '<div class=\"qr-placeholder\"><span class=\"qr-placeholder-icon\">👤</span><span>이름을 입력하면 QR코드가 생성됩니다</span></div>';",
     "container.innerHTML = '<div class=\"qr-placeholder\"><span class=\"qr-placeholder-icon\">👤</span><span>Enter a name to generate a QR code</span></div>';"),
    ("container.innerHTML = '<div class=\"alert alert-error\">QR코드 생성에 실패했습니다. 입력값을 확인해주세요.</div>';",
     "container.innerHTML = '<div class=\"alert alert-error\">Failed to generate QR code. Please check your input.</div>';"),

    # ── qr-social JS strings ──────────────────────────────────────────────────
    ("<span>플랫폼을 선택하고 ID를 입력하면 QR코드가 생성됩니다</span>",
     "<span>Select a platform and enter ID to generate a QR code</span>"),
    ("var PLATFORM_PLACEHOLDER = '플랫폼을 먼저 선택하세요';",
     "var PLATFORM_PLACEHOLDER = 'Select a platform first';"),
    ("preview.textContent = url ? '생성될 URL: ' + url : '';",
     "preview.textContent = url ? 'URL to encode: ' + url : '';"),
    ("<span>카카오톡</span>", "<span>KakaoTalk</span>"),
    ("container.innerHTML = '<div class=\"qr-placeholder\"><span class=\"qr-placeholder-icon\">📱</span><span>플랫폼을 선택하고 ID를 입력하면 QR코드가 생성됩니다</span></div>';",
     "container.innerHTML = '<div class=\"qr-placeholder\"><span class=\"qr-placeholder-icon\">📱</span><span>Select a platform and enter ID to generate a QR code</span></div>';"),
    ("container.innerHTML = '<div class=\"alert alert-error\">QR코드 생성에 실패했습니다.</div>';",
     "container.innerHTML = '<div class=\"alert alert-error\">Failed to generate QR code.</div>';"),

    # ── qr-location UI ────────────────────────────────────────────────────────
    ('<button class="mode-tab active" id="tabCoords" onclick="switchMode(\'coords\')">📐 좌표 입력</button>',
     '<button class="mode-tab active" id="tabCoords" onclick="switchMode(\'coords\')">📐 Enter Coordinates</button>'),
    ('<button class="mode-tab" id="tabAddress" onclick="switchMode(\'address\')">🔍 주소 검색</button>',
     '<button class="mode-tab" id="tabAddress" onclick="switchMode(\'address\')">🔍 Address Search</button>'),
    ('<button class="geo-btn" id="geoBtn">📡 내 위치 가져오기</button>',
     '<button class="geo-btn" id="geoBtn">📡 Get My Location</button>'),
    ('<span class="option-label">링크 형식</span>', '<span class="option-label">Link Format</span>'),
    ('<option value="geo">geo: URI (네이티브 지도 앱)</option>',
     '<option value="geo">geo: URI (Native map app)</option>'),
    ('<option value="maps">Google Maps URL (범용)</option>',
     '<option value="maps">Google Maps URL (Universal)</option>'),
    ("<span>위치 정보를 입력하면 QR코드가 생성됩니다</span>",
     "<span>Enter location details to generate a QR code</span>"),
    ("container.innerHTML = '<div class=\"alert alert-error\">QR코드 생성에 실패했습니다.</div>'+",
     "container.innerHTML = '<div class=\"alert alert-error\">Failed to generate QR code.</div>'+"),
    ("container.innerHTML = '<div class=\"qr-placeholder\"><span class=\"qr-placeholder-icon\">📍</span><span>위치 정보를 입력하면 QR코드가 생성됩니다</span></div>';",
     "container.innerHTML = '<div class=\"qr-placeholder\"><span class=\"qr-placeholder-icon\">📍</span><span>Enter location details to generate a QR code</span></div>';"),
    ("alert('이 브라우저에서는 위치 정보를 지원하지 않습니다.');",
     "alert('Geolocation is not supported by this browser.');"),
    ("alert('위치 정보를 가져오지 못했습니다. 브라우저에서 위치 권한을 허용해 주세요.');",
     "alert('Could not get your location. Please allow location access in your browser.');"),

    # ── qr-custom UI ──────────────────────────────────────────────────────────
    ('<label for="qrInput">URL 또는 텍스트 입력</label>',
     '<label for="qrInput">Enter URL or Text</label>'),
    ('<div class="options-title">커스터마이징 옵션</div>',
     '<div class="options-title">Customization Options</div>'),
    ('<span class="option-label">전경색 (QR 색상)</span>',
     '<span class="option-label">Foreground Color (QR)</span>'),
    ('<span class="option-label">오류 수정 레벨</span>',
     '<span class="option-label">Error Correction Level</span>'),
    ('<option value="L">L (7%) - 기본</option>', '<option value="L">L (7%) - Default</option>'),
    ('<option value="H" selected>H (30%) - 로고 삽입 시 권장</option>',
     '<option value="H" selected>H (30%) - Recommended with logo</option>'),
    ('<span class="option-label">모서리 스타일</span>',
     '<span class="option-label">Corner Style</span>'),
    ('<button class="mask-btn active" data-style="square">기본</button>',
     '<button class="mask-btn active" data-style="square">Default</button>'),
    ('<button class="mask-btn" data-style="round">둥글게</button>',
     '<button class="mask-btn" data-style="round">Rounded</button>'),
    ('<div class="options-title">로고 삽입 (선택)</div>',
     '<div class="options-title">Insert Logo (Optional)</div>'),
    ('<div style="font-size:0.85rem;color:var(--text-light);">로고 이미지 선택 (JPG, PNG, SVG)</div>',
     '<div style="font-size:0.85rem;color:var(--text-light);">Select logo image (JPG, PNG, SVG)</div>'),
    ('<img id="logoPreview" class="logo-preview-small" alt="로고 미리보기">',
     '<img id="logoPreview" class="logo-preview-small" alt="Logo preview">'),
    ('<div style="font-size:0.78rem;color:var(--primary);font-weight:600;">로고가 적용됩니다</div>',
     '<div style="font-size:0.78rem;color:var(--primary);font-weight:600;">Logo will be applied</div>'),
    ('<span class="option-label">로고 모양</span>', '<span class="option-label">Logo Shape</span>'),
    ('<button class="mask-btn active" data-logo-mask="square">정사각형</button>',
     '<button class="mask-btn active" data-logo-mask="square">Square</button>'),
    ('<button class="mask-btn" data-logo-mask="circle">원형</button>',
     '<button class="mask-btn" data-logo-mask="circle">Circle</button>'),
    ('<span class="option-label">로고 패딩</span>', '<span class="option-label">Logo Padding</span>'),
    ('<button class="btn-copy" onclick="removeLogo()" style="margin-top:8px;">로고 제거</button>',
     '<button class="btn-copy" onclick="removeLogo()" style="margin-top:8px;">Remove Logo</button>'),
    ('로고가 클수록 QR 인식률이 낮아집니다. H 오류 수정 레벨을 권장합니다.',
     'Larger logos reduce QR code scan reliability. H error correction level is recommended.'),
    ('<span>URL 또는 텍스트를 입력하면 QR코드가 생성됩니다</span>',
     '<span>Enter URL or text to generate a QR code</span>'),
    ('<button id="downloadBtn" class="btn-primary" disabled>PNG 다운로드</button>',
     '<button id="downloadBtn" class="btn-primary" disabled>Download PNG</button>'),
    ('<button id="downloadSvgBtn" class="btn-secondary" disabled>SVG 다운로드</button>',
     '<button id="downloadSvgBtn" class="btn-secondary" disabled>Download SVG</button>'),
    ('💡 QR코드의 색상을 더 다양하게 탐색하려면 <a href="../qr-url.html" target="_blank" rel="noopener">WooaColor에서 색상 도구 사용하기 →</a>',
     '💡 Want to explore more colors? <a href="https://colorkit.wooahouse.com/" target="_blank" rel="noopener">WooaColor – Color Tools →</a>'),
    # qr-custom comment
    ('  <!-- 구조화 데이터 -->', '  <!-- Structured Data -->'),

    # ── qr-calendar UI ────────────────────────────────────────────────────────
    ('<div class="panel-title">이벤트 정보 입력</div>',
     '<div class="panel-title">Enter Event Details</div>'),
    ('<!-- 제목 -->', '<!-- Title -->'),
    ('<label for="evTitle">이벤트 제목 <span style="color:#EF4444">*</span></label>',
     '<label for="evTitle">Event Title <span style="color:#EF4444">*</span></label>'),
    ('<!-- 시작·종료 일시 -->', '<!-- Start/End Date & Time -->'),
    ('<label for="evStart">시작 일시 <span style="color:#EF4444">*</span></label>',
     '<label for="evStart">Start Date/Time <span style="color:#EF4444">*</span></label>'),
    ('<label for="evEnd">종료 일시</label>', '<label for="evEnd">End Date/Time</label>'),
    ('<!-- 장소 -->', '<!-- Location -->'),
    ('<label for="evLocation">장소</label>', '<label for="evLocation">Location</label>'),
    ('<!-- 설명 -->', '<!-- Description -->'),
    ('<label for="evDesc">설명</label>', '<label for="evDesc">Description</label>'),
    ('<!-- QR 크기 -->', '<!-- QR Size -->'),
    ('<button class="qr-size-btn" data-size="200" onclick="setSize(200, this)">소 (200px)</button>',
     '<button class="qr-size-btn" data-size="200" onclick="setSize(200, this)">S (200px)</button>'),
    ('<button class="qr-size-btn active" data-size="300" onclick="setSize(300, this)">중 (300px)</button>',
     '<button class="qr-size-btn active" data-size="300" onclick="setSize(300, this)">M (300px)</button>'),
    ('<button class="qr-size-btn" data-size="400" onclick="setSize(400, this)">대 (400px)</button>',
     '<button class="qr-size-btn" data-size="400" onclick="setSize(400, this)">L (400px)</button>'),
    ('<button class="btn-generate" onclick="generateQR()">📅 QR 일정 생성</button>',
     '<button class="btn-generate" onclick="generateQR()">📅 Generate Calendar QR</button>'),
    ('<!-- QR 출력 -->', '<!-- QR Output -->'),
    ('<div style="font-size:0.85rem;font-weight:700;color:var(--text);margin-bottom:12px;">생성된 QR코드 — 스캔하면 캘린더에 일정이 추가됩니다</div>',
     '<div style="font-size:0.85rem;font-weight:700;color:var(--text);margin-bottom:12px;">Generated QR Code — Scan to add event to calendar</div>'),
    ('<button class="btn-download" id="downloadBtn" onclick="downloadQR()">⬇ QR코드 다운로드 (PNG)</button>',
     '<button class="btn-download" id="downloadBtn" onclick="downloadQR()">⬇ Download QR Code (PNG)</button>'),
    ('<div style="font-size:0.82rem;font-weight:700;color:var(--text);margin-bottom:6px;">iCalendar 미리보기</div>',
     '<div style="font-size:0.82rem;font-weight:700;color:var(--text);margin-bottom:6px;">iCalendar Preview</div>'),
    ('💡 명함 정보를 QR코드로 만들려면 <a href="qr-vcard.html">명함 QR코드 생성기</a>를 이용하세요.',
     '💡 Want to create a business card QR code? <a href="../qr-vcard.html">Business Card QR Code Generator</a>'),
    ("// 기본 날짜: 오늘 + 1시간 ~ +2시간",
     "// Default date: today + 1h ~ +2h"),
    ("if (!title) { alert('이벤트 제목을 입력하세요.'); document.getElementById('evTitle').focus(); return; }",
     "if (!title) { alert('Please enter an event title.'); document.getElementById('evTitle').focus(); return; }"),
    ("if (!start) { alert('시작 일시를 선택하세요.'); document.getElementById('evStart').focus(); return; }",
     "if (!start) { alert('Please select a start date/time.'); document.getElementById('evStart').focus(); return; }"),
    ("if (end && end < start) { alert('종료 일시는 시작 일시보다 늦어야 합니다.'); document.getElementById('evEnd').focus(); return; }",
     "if (end && end < start) { alert('End date/time must be after start date/time.'); document.getElementById('evEnd').focus(); return; }"),
    ("  // QR 컨테이너 초기화", "  // Reset QR container"),
    ("  // QRCode.js 생성", "  // Generate with QRCode.js"),
    ("  // ICS 미리보기 (표시용, \\r\\n → \\n)", "  // ICS preview (for display, \\r\\n → \\n)"),
    ("  // 출력 표시", "  // Show output"),
    ("    link.download = 'QR_일정_' + (document.getElementById('evTitle').value.trim() || 'calendar') + '.png';",
     "    link.download = 'QR_event_' + (document.getElementById('evTitle').value.trim() || 'calendar') + '.png';"),
    ("    // QRCode.js가 img를 생성한 경우 canvas로 변환",
     "    // Convert img to canvas if QRCode.js generated an img element"),

    # ── index.html ld+json ItemList ───────────────────────────────────────────
    ('"name": "QR 도구 목록"', '"name": "QR Code Tools List"'),
    ('{"@type":"ListItem","position":1,"name":"URL QR코드 생성","url":"https://qrkit.wooahouse.com/qr-url.html"}',
     '{"@type":"ListItem","position":1,"name":"URL QR Code Generator","url":"https://qrkit.wooahouse.com/en/qr-url.html"}'),
    ('{"@type":"ListItem","position":2,"name":"텍스트 QR코드 생성","url":"https://qrkit.wooahouse.com/qr-text.html"}',
     '{"@type":"ListItem","position":2,"name":"Text QR Code Generator","url":"https://qrkit.wooahouse.com/en/qr-text.html"}'),
    ('{"@type":"ListItem","position":3,"name":"WiFi QR코드 생성","url":"https://qrkit.wooahouse.com/qr-wifi.html"}',
     '{"@type":"ListItem","position":3,"name":"WiFi QR Code Generator","url":"https://qrkit.wooahouse.com/en/qr-wifi.html"}'),
    ('{"@type":"ListItem","position":4,"name":"명함 QR코드 생성","url":"https://qrkit.wooahouse.com/qr-vcard.html"}',
     '{"@type":"ListItem","position":4,"name":"Business Card QR Code Generator","url":"https://qrkit.wooahouse.com/en/qr-vcard.html"}'),
    ('{"@type":"ListItem","position":5,"name":"이메일 QR코드 생성","url":"https://qrkit.wooahouse.com/qr-email.html"}',
     '{"@type":"ListItem","position":5,"name":"Email QR Code Generator","url":"https://qrkit.wooahouse.com/en/qr-email.html"}'),
    ('{"@type":"ListItem","position":6,"name":"전화번호 QR코드 생성","url":"https://qrkit.wooahouse.com/qr-phone.html"}',
     '{"@type":"ListItem","position":6,"name":"Phone Number QR Code Generator","url":"https://qrkit.wooahouse.com/en/qr-phone.html"}'),
    ('{"@type":"ListItem","position":7,"name":"QR코드 읽기","url":"https://qrkit.wooahouse.com/qr-reader.html"}',
     '{"@type":"ListItem","position":7,"name":"QR Code Reader","url":"https://qrkit.wooahouse.com/en/qr-reader.html"}'),
    ('{"@type":"ListItem","position":8,"name":"카메라 QR코드 읽기","url":"https://qrkit.wooahouse.com/qr-camera.html"}',
     '{"@type":"ListItem","position":8,"name":"Camera QR Code Scanner","url":"https://qrkit.wooahouse.com/en/qr-camera.html"}'),
    ('{"@type":"ListItem","position":9,"name":"바코드 생성기","url":"https://qrkit.wooahouse.com/barcode-generator.html"}',
     '{"@type":"ListItem","position":9,"name":"Barcode Generator","url":"https://qrkit.wooahouse.com/en/barcode-generator.html"}'),
    ('{"@type":"ListItem","position":10,"name":"QR코드 배치 생성","url":"https://qrkit.wooahouse.com/qr-batch.html"}',
     '{"@type":"ListItem","position":10,"name":"Batch QR Code Generator","url":"https://qrkit.wooahouse.com/en/qr-batch.html"}'),
    ('{"@type":"ListItem","position":11,"name":"SMS QR코드 생성","url":"https://qrkit.wooahouse.com/qr-sms.html"}',
     '{"@type":"ListItem","position":11,"name":"SMS QR Code Generator","url":"https://qrkit.wooahouse.com/en/qr-sms.html"}'),
    ('{"@type":"ListItem","position":12,"name":"소셜미디어 QR코드 생성","url":"https://qrkit.wooahouse.com/qr-social.html"}',
     '{"@type":"ListItem","position":12,"name":"Social Media QR Code Generator","url":"https://qrkit.wooahouse.com/en/qr-social.html"}'),
    ('{"@type":"ListItem","position":13,"name":"위치 QR코드 생성","url":"https://qrkit.wooahouse.com/qr-location.html"}',
     '{"@type":"ListItem","position":13,"name":"Location QR Code Generator","url":"https://qrkit.wooahouse.com/en/qr-location.html"}'),
    ('{"@type":"ListItem","position":14,"name":"QR·바코드 이미지 읽기","url":"https://qrkit.wooahouse.com/qr-barcode-reader.html"}',
     '{"@type":"ListItem","position":14,"name":"QR & Barcode Image Reader","url":"https://qrkit.wooahouse.com/en/qr-barcode-reader.html"}'),

    # ── index.html features section ───────────────────────────────────────────
    ('<div class="feature-title">100% 안전</div>', '<div class="feature-title">100% Safe</div>'),
    ('<div class="feature-desc">파일이 서버로 전송되지 않습니다. 모든 처리가 브라우저 안에서 이루어집니다.</div>',
     '<div class="feature-desc">Files never sent to server. All processing happens in your browser.</div>'),
    ('<div class="feature-title">즉시 생성</div>', '<div class="feature-title">Instant Generation</div>'),
    ('<div class="feature-desc">입력 즉시 QR코드가 생성됩니다. 업로드 없이 빠르게 처리됩니다.</div>',
     '<div class="feature-desc">QR codes are generated instantly as you type. No upload needed.</div>'),
    ('<div class="feature-title">완전 무료</div>', '<div class="feature-title">Completely Free</div>'),
    ('<div class="feature-desc">회원가입 없이 모든 기능을 무제한 무료로 사용할 수 있습니다.</div>',
     '<div class="feature-desc">Use all features for free, unlimited, no signup required.</div>'),
    ('<div class="feature-title">모든 기기 지원</div>', '<div class="feature-title">All Devices</div>'),
    ('<div class="feature-desc">PC, 태블릿, 스마트폰 어디서나 사용 가능한 반응형 디자인.</div>',
     '<div class="feature-desc">Responsive design works on PC, tablet, and smartphone.</div>'),

    # ── index.html footer links ────────────────────────────────────────────────
    ('<p>무료 온라인 QR코드 도구 모음. 생성, 읽기, 바코드까지 모든 QR 작업을 안전하게 처리하세요.</p>',
     '<p>Free online QR code toolkit. Generate, read, and create barcodes — all safely in your browser.</p>'),
    ('<h4>QR 생성</h4>', '<h4>QR Generator</h4>'),
    ('<a href="qr-url.html">URL QR코드</a>', '<a href="qr-url.html">URL QR Code</a>'),
    ('<a href="qr-text.html">텍스트 QR코드</a>', '<a href="qr-text.html">Text QR Code</a>'),
    ('<a href="qr-wifi.html">WiFi QR코드</a>', '<a href="qr-wifi.html">WiFi QR Code</a>'),
    ('<a href="qr-vcard.html">명함 QR코드</a>', '<a href="qr-vcard.html">Business Card QR</a>'),
    ('<a href="qr-email.html">이메일 QR코드</a>', '<a href="qr-email.html">Email QR Code</a>'),
    ('<a href="qr-phone.html">전화번호 QR코드</a>', '<a href="qr-phone.html">Phone QR Code</a>'),
    ('<h4>QR 생성 (신규)</h4>', '<h4>QR Generator (New)</h4>'),
    ('<a href="qr-sms.html">SMS QR코드</a>', '<a href="qr-sms.html">SMS QR Code</a>'),
    ('<a href="qr-social.html">소셜미디어 QR코드</a>', '<a href="qr-social.html">Social Media QR</a>'),
    ('<a href="qr-location.html">위치 QR코드</a>', '<a href="qr-location.html">Location QR Code</a>'),
    ('<h4>QR 읽기 &amp; 바코드</h4>', '<h4>QR Reader &amp; Barcode</h4>'),
    ('<a href="qr-reader.html">QR코드 읽기</a>', '<a href="qr-reader.html">QR Code Reader</a>'),
    ('<a href="qr-camera.html">카메라 QR 읽기</a>', '<a href="qr-camera.html">Camera QR Scanner</a>'),
    ('<a href="barcode-generator.html">바코드 생성기</a>', '<a href="barcode-generator.html">Barcode Generator</a>'),
    ('<a href="qr-batch.html">QR 배치 생성</a>', '<a href="qr-batch.html">Batch QR Code</a>'),
    ('<a href="qr-barcode-reader.html">바코드 이미지 읽기</a>', '<a href="qr-barcode-reader.html">Barcode Image Reader</a>'),
    ('<h4>정보</h4>', '<h4>Info</h4>'),
    ('<a href="../about.html">서비스 소개</a>', '<a href="../about.html">About</a>'),
    ('<h4>WooaHouse 서비스</h4>', '<h4>WooaHouse Services</h4>'),

    # ── footer ─────────────────────────────────────────────────────────────────
    # footer-bottom link: 홈 (used in about/privacy standalone footer)
    ('<a href="../index.html">홈</a>', '<a href="../index.html">Home</a>'),
    ('© 2026 WooaQR by WooaHouse. 모든 권리 보유.', '© 2026 WooaQR by WooaHouse. All rights reserved.'),
    ('© 2026 WooaQR. 모든 권리 보유.', '© 2026 WooaQR. All rights reserved.'),

    # ── about page body ────────────────────────────────────────────────────────
    ('<h1>서비스 소개</h1>', '<h1>About WooaQR</h1>'),
    ('<p class="subtitle">WooaQR에 대해 알아보세요</p>', '<p class="subtitle">Learn about WooaQR</p>'),
    ('<h2>📱 WooaQR이란?</h2>', '<h2>📱 What is WooaQR?</h2>'),
    ('<p>WooaQR(WooaQR)은 QR코드 생성, QR코드 읽기, 바코드 생성을 브라우저에서 완전 무료로 제공하는 온라인 도구 모음입니다.</p>',
     '<p>WooaQR is a free online toolkit for QR code generation, reading, and barcode creation — all in your browser.</p>'),
    ('<p>URL·텍스트·WiFi·명함·이메일·전화번호 QR코드 생성부터 이미지 파일 및 카메라를 통한 QR코드 읽기, CODE128·EAN-13·UPC-A 바코드 생성, 배치 QR코드 생성까지 모든 QR 관련 작업을 한 곳에서 처리할 수 있습니다.</p>',
     '<p>From URL, text, WiFi, contact, email, and phone QR codes to image-based and camera QR reading, CODE128/EAN-13/UPC-A barcode generation, and batch QR code creation — all in one place.</p>'),
    ('<h2>✅ 서비스 특징</h2>', '<h2>✅ Features</h2>'),
    ('<li>모든 처리가 브라우저 안에서 이루어져 100% 안전</li>',
     '<li>All processing happens in your browser — 100% safe</li>'),
    ('<li>파일이나 데이터가 서버로 전송되지 않음</li>',
     '<li>No files or data are sent to any server</li>'),
    ('<li>회원가입·로그인 없이 즉시 사용 가능</li>',
     '<li>Use instantly without signup or login</li>'),
    ('<li>URL·텍스트·WiFi·명함·이메일·전화번호 등 다양한 QR코드 형식 지원</li>',
     '<li>Supports URL, text, WiFi, contact, email, phone, and more QR formats</li>'),
    ('<li>카메라 실시간 QR코드 스캔 지원</li>',
     '<li>Real-time camera QR code scanning supported</li>'),
    ('<li>CODE128, EAN-13, UPC-A, CODE39 바코드 생성</li>',
     '<li>Generate CODE128, EAN-13, UPC-A, CODE39 barcodes</li>'),
    ('<li>최대 20개 URL 배치 QR코드 생성 및 ZIP 다운로드</li>',
     '<li>Batch generate up to 20 QR codes and download as ZIP</li>'),
    ('<li>PC·태블릿·스마트폰 모든 기기에서 편리하게 이용 가능</li>',
     '<li>Works conveniently on PC, tablet, and smartphone</li>'),
    ('<h2>🔒 개인정보 보호</h2>', '<h2>🔒 Privacy</h2>'),
    ('<p>WooaQR의 모든 기능은 브라우저 내에서만 처리됩니다. 입력한 URL, 텍스트, 이미지 파일 등 어떤 데이터도 서버로 전송되거나 저장되지 않습니다.</p>',
     '<p>All WooaQR features run entirely in your browser. No URL, text, or image data is sent to or stored on any server.</p>'),
    ('<p>카메라 QR코드 스캔 역시 웹 브라우저 API를 통해 로컬에서만 처리되며 영상 데이터가 외부로 전송되지 않습니다.</p>',
     '<p>Camera QR scanning also runs locally via the browser API — no video data is transmitted externally.</p>'),
    ('<h2>🏠 WooaHouse 네트워크</h2>', '<h2>🏠 WooaHouse Network</h2>'),
    ('<p>WooaQR은 WooaHouse가 운영하는 서비스 중 하나입니다. 현재 운영 중인 서비스:</p>',
     '<p>WooaQR is one of the services operated by WooaHouse. Currently available services:</p>'),
    ('<h2>📬 문의</h2>', '<h2>📬 Contact</h2>'),
    ('<p>도구 추가 요청, 오류 제보, 제휴 문의 등은 아래 이메일로 연락 주세요.</p>',
     '<p>For tool requests, bug reports, or partnership inquiries, please contact us at:</p>'),

    # ── privacy page body ──────────────────────────────────────────────────────
    ('<p class="updated">최종 업데이트: 2026년 3월 15일</p>',
     '<p class="updated">Last updated: March 15, 2026</p>'),
    ('<h2>1. 개인정보 수집 여부</h2>', '<h2>1. Personal Information Collection</h2>'),
    ('<p>WooaQR(qrkit.wooahouse.com)은 회원가입, 로그인 등의 기능이 없으며, 사용자의 개인정보를 직접 수집하지 않습니다. 본 서비스는 정적 웹사이트로 운영되며, QR코드 생성·읽기·바코드 생성 등 모든 처리가 사용자의 브라우저 내에서만 이루어집니다. 입력된 URL, 텍스트, 이미지 파일 등 어떤 데이터도 서버로 전송되거나 저장되지 않습니다.</p>',
     '<p>WooaQR (qrkit.wooahouse.com) does not have account registration or login features, and does not directly collect personal information. This service operates as a static website where all processing — QR code generation, reading, and barcode creation — occurs entirely within the user\'s browser. No entered data such as URLs, text, or image files is sent to or stored on any server.</p>'),
    ('<h2>2. 제3자 서비스</h2>', '<h2>2. Third-Party Services</h2>'),
    ('<p>WooaQR은 아래 제3자 서비스를 사용하며, 각 서비스의 개인정보 처리방침이 적용됩니다.</p>',
     '<p>WooaQR uses the following third-party services, each governed by their own privacy policy.</p>'),
    ('<li><strong>Google AdSense:</strong> 광고 게재를 위해 사용됩니다. Google은 쿠키를 통해 광고 관련 정보를 수집할 수 있습니다.</li>',
     '<li><strong>Google AdSense:</strong> Used to display ads. Google may collect advertising-related information via cookies.</li>'),
    ('<li><strong>Google Analytics (해당 시):</strong> 익명화된 방문 통계 수집에 사용될 수 있습니다.</li>',
     '<li><strong>Google Analytics (if applicable):</strong> May be used to collect anonymized visitor statistics.</li>'),
    ('<li><strong>CDN 라이브러리:</strong> qrcodejs, jsQR, JsBarcode, QRCode.js, JSZip 등의 라이브러리를 CDN(jsdelivr, cdnjs)을 통해 로드합니다.</li>',
     '<li><strong>CDN Libraries:</strong> Libraries such as qrcodejs, jsQR, JsBarcode, QRCode.js, and JSZip are loaded via CDN (jsdelivr, cdnjs).</li>'),
    ('<h2>3. 카메라 접근</h2>', '<h2>3. Camera Access</h2>'),
    ('<p>카메라 QR코드 읽기 기능은 브라우저의 WebRTC API를 통해 카메라에 접근합니다. 이 기능은 사용자의 명시적 허가 후에만 작동하며, 카메라 영상 데이터는 브라우저 내에서만 처리됩니다. 영상 데이터가 서버로 전송되거나 저장되지 않습니다.</p>',
     '<p>The camera QR code reading feature accesses the camera via the browser\'s WebRTC API. This feature only works with explicit user permission. Camera video data is processed entirely within the browser and is never sent to or stored on any server.</p>'),
    ('<h2>4. 쿠키</h2>', '<h2>4. Cookies</h2>'),
    ('<p>WooaQR은 자체적으로 쿠키를 사용하지 않습니다. 다만 Google AdSense 등 제3자 서비스에서 광고 목적으로 쿠키를 사용할 수 있습니다. 브라우저 설정에서 쿠키를 비활성화할 수 있습니다.</p>',
     '<p>WooaQR does not use cookies itself. However, third-party services such as Google AdSense may use cookies for advertising purposes. You can disable cookies in your browser settings.</p>'),
    ('<h2>5. 외부 링크</h2>', '<h2>5. External Links</h2>'),
    ('<p>WooaQR의 링크는 외부 사이트로 연결될 수 있습니다. 해당 사이트의 개인정보 처리방침은 각 사이트에서 확인하시기 바랍니다. WooaQR은 외부 사이트의 개인정보 처리에 대해 책임지지 않습니다.</p>',
     '<p>Links on WooaQR may lead to external websites. Please review each site\'s own privacy policy. WooaQR is not responsible for the privacy practices of external sites.</p>'),
    ('<h2>6. 문의</h2>', '<h2>6. Contact</h2>'),
    ('<p>개인정보 처리방침 관련 문의는 아래 이메일로 연락 주세요.</p>',
     '<p>For questions about this privacy policy, please contact us at:</p>'),

    # ── barcode-generator.html: height label ──
    ('<span class="option-label">높이 (px)</span>', '<span class="option-label">Height (px)</span>'),

    # ── index.html: feature-desc partially translated ──
    ('모든 처리가 브라우저 안에서 이루어집니다.', 'All processing runs in your browser.'),

    # ── qr-custom.html: transparent label ──
    ('>투명<', '>Transparent<'),
    ('투명', 'Transparent'),

    # ── qr-social.html: JS comments ──
    ('// 플랫폼 버튼 클릭', '// platform button click'),
    ('// active 스타일 초기화', '// reset active style'),
    ('// 선택된 버튼 강조', '// highlight selected button'),
    ('// 입력 이벤트', '// input event'),
    ('// 다운로드', '// download'),
]

# ── 3. 언어 선택기 CSS ────────────────────────────────────────────────────────
LANG_SWITCHER_CSS = """    .lang-switcher { display:flex; align-items:center; gap:4px; }
    .lang-switcher a { color:rgba(255,255,255,0.7); text-decoration:none; font-size:0.8rem; font-weight:600; padding:3px 8px; border-radius:12px; transition:background 0.15s; }
    .lang-switcher a.active { color:white; background:rgba(255,255,255,0.25); }
    .lang-switcher a:hover { color:white; background:rgba(255,255,255,0.18); }
    .lang-switcher span { color:rgba(255,255,255,0.3); font-size:0.75rem; }
"""

def build_page(filename, meta):
    ko_path = os.path.join(BASE, filename)
    en_path = os.path.join(EN_DIR, filename)

    with open(ko_path, encoding='utf-8') as f:
        html = f.read()

    # ── 메타 태그 교체 ──
    html = re.sub(r'<title>[^<]+</title>', f'<title>{meta["title"]}</title>', html)
    html = re.sub(r'<meta name="description" content="[^"]*"',
                  f'<meta name="description" content="{meta["desc"]}"', html)
    if meta.get('kw'):
        html = re.sub(r'<meta name="keywords" content="[^"]*"',
                      f'<meta name="keywords" content="{meta["kw"]}"', html)
    html = re.sub(r'<meta property="og:title" content="[^"]*"',
                  f'<meta property="og:title" content="{meta["og_title"]}"', html)
    html = re.sub(r'<meta property="og:description" content="[^"]*"',
                  f'<meta property="og:description" content="{meta["og_desc"]}"', html)
    html = re.sub(r'<meta property="og:url" content="[^"]*"',
                  f'<meta property="og:url" content="https://qrkit.wooahouse.com/en/{filename}"', html)
    html = re.sub(r'<link rel="canonical" href="[^"]*"',
                  f'<link rel="canonical" href="https://qrkit.wooahouse.com/en/{filename}"', html)

    # ── hreflang 추가 (canonical 바로 뒤) ──
    hreflang = (f'\n  <link rel="alternate" hreflang="ko" href="https://qrkit.wooahouse.com/{filename}">'
                f'\n  <link rel="alternate" hreflang="en" href="https://qrkit.wooahouse.com/en/{filename}">'
                f'\n  <link rel="alternate" hreflang="x-default" href="https://qrkit.wooahouse.com/en/{filename}">')
    html = re.sub(r'(<link rel="canonical"[^>]*>)', r'\1' + hreflang, html)

    # ── ld+json 업데이트 ──
    html = re.sub(r'"name": "([^"]*[가-힣][^"]*)"', f'"name": "{meta["app_name"]}"', html)
    html = re.sub(r'"description": "([^"]*[가-힣][^"]*)"', f'"description": "{meta["desc"]}"', html)
    html = re.sub(
        r'"url": "https://qrkit\.wooahouse\.com/' + re.escape(filename) + '"',
        f'"url": "https://qrkit.wooahouse.com/en/{filename}"', html
    )

    # ── FAQ 교체 ──
    if meta.get('faq'):
        faq_items = meta['faq']
        faq_html_parts = []
        for i, (q, a) in enumerate(faq_items):
            is_last = (i == len(faq_items) - 1)
            mb = '' if is_last else 'margin-bottom:1.2rem;'
            faq_html_parts.append(
                f'      <div class="faq-item" style="{mb}padding:1rem;background:#f8f9fa;border-radius:8px;">\n'
                f'        <h3 style="font-size:1rem;font-weight:600;margin-bottom:0.5rem;">Q. {q}</h3>\n'
                f'        <p style="color:#555;margin:0;">{a}</p>\n'
                f'      </div>'
            )
        faq_inner = '\n'.join(faq_html_parts)
        html = re.sub(
            r'<div class="faq-list">.*?</div>\s*</section>',
            f'<div class="faq-list">\n{faq_inner}\n    </div>\n  </section>',
            html, flags=re.DOTALL
        )
        html = re.sub(r'<h2[^>]*>자주 묻는 질문</h2>',
                      '<h2 style="font-size:1.4rem;margin-bottom:1.5rem;">Frequently Asked Questions</h2>', html)

        # FAQPage ld+json 교체
        import json as _json
        faq_entities = []
        for q, a in faq_items:
            faq_entities.append({
                "@type": "Question",
                "name": q,
                "acceptedAnswer": {"@type": "Answer", "text": a}
            })
        new_faq_json = _json.dumps({
            "@context": "https://schema.org",
            "@type": "FAQPage",
            "mainEntity": faq_entities
        }, ensure_ascii=False, indent=2)
        html = re.sub(
            r'<script type="application/ld\+json">\s*\{[^<]*"FAQPage"[^<]*\}[^<]*</script>',
            f'<script type="application/ld+json">\n{new_faq_json}\n</script>',
            html, flags=re.DOTALL
        )

    # ── cross-link banner 교체 ──
    if meta.get('cross_banner_text'):
        html = re.sub(
            r'<span style="font-size:0\.95rem;color:#444;">[^<]*</span>',
            f'<span style="font-size:0.95rem;color:#444;">{meta["cross_banner_text"]}</span>',
            html
        )
        html = re.sub(
            r'<a href="[^"]*" target="_blank" rel="noopener" style="background:#4F6EF7[^>]*>[^<]*</a>',
            f'<a href="{meta["cross_banner_href"]}" target="_blank" rel="noopener" style="background:#4F6EF7;color:#fff;padding:0.5rem 1rem;border-radius:8px;text-decoration:none;font-size:0.9rem;white-space:nowrap;">{meta["cross_banner_link_text"]}</a>',
            html
        )
        # cross-link-tip style (qr-url.html uses .cross-link-tip)
        html = re.sub(
            r'(class="cross-link-tip">[^<]*<a href=")[^"]*(")',
            r'\g<1>' + meta['cross_banner_href'] + r'\g<2>',
            html
        )

    # ── Tool header (h1, desc, breadcrumb) ──
    if meta.get('h1'):
        replaced = re.sub(r'<h1 id="toolTitle">[^<]*</h1>', f'<h1 id="toolTitle">{meta["h1"]}</h1>', html)
        if replaced == html:
            replaced = re.sub(r'<h1>([^<]*)</h1>', f'<h1>{meta["h1"]}</h1>', html, count=1)
        html = replaced
    if meta.get('tool_desc'):
        replaced = re.sub(r'<p id="toolDesc">[^<]*</p>', f'<p id="toolDesc">{meta["tool_desc"]}</p>', html)
        if replaced == html:
            # Replace first <p> in tool-header
            replaced = re.sub(
                r'(<div class="tool-header">.*?<h1[^>]*>[^<]*</h1>\s*)<p>([^<]*)</p>',
                f'\\1<p>{meta["tool_desc"]}</p>',
                html, count=1, flags=re.DOTALL
            )
        html = replaced
    if meta.get('breadcrumb'):
        html = re.sub(r'<span id="breadcrumbTitle">[^<]*</span>',
                      f'<span id="breadcrumbTitle">{meta["breadcrumb"]}</span>', html)
        # Also replace last span in breadcrumb (no id)
        html = re.sub(
            r'(<div class="breadcrumb">.*?<span>›</span>\s*)<span>([^<가-힣]*[가-힣][^<]*)</span>',
            f'\\1<span>{meta["breadcrumb"]}</span>',
            html, count=1, flags=re.DOTALL
        )

    # ── 공통 문자열 치환 ──
    for ko, en in COMMON:
        html = html.replace(ko, en)

    # ── 언어 선택기 CSS 삽입 ──
    if 'lang-switcher' not in html:
        html = html.replace('  </style>', LANG_SWITCHER_CSS + '  </style>', 1)

    # ── 헤더에 언어 선택기 삽입 ──
    html = re.sub(
        r'(\s*</div>\s*</header>)',
        f'\n    <div class="header-right">\n'
        f'      <div class="lang-switcher">\n'
        f'        <a href="../{filename}">KO</a>\n'
        f'        <span>|</span>\n'
        f'        <a href="{filename}" class="active">EN</a>\n'
        f'      </div>\n'
        f'      <a href="../about.html" style="color:rgba(255,255,255,0.85); font-size:0.85rem; text-decoration:none; margin-left:8px;">About</a>\n'
        f'    </div>\n'
        f'  </div>\n'
        f'</header>',
        html, count=1
    )

    # ── 쿠팡 광고 블록 완전 제거 ──
    ADSENSE_BLOCK = (
        '<div style="text-align:center;margin:32px auto 0;max-width:728px;padding:0 8px">\n'
        '<ins class="adsbygoogle"\n'
        '     style="display:block"\n'
        '     data-ad-client="ca-pub-6464921081676309"\n'
        '     data-ad-slot="7080296704"\n'
        '     data-ad-format="auto"\n'
        '     data-full-width-responsive="true"></ins>\n'
        '<script>(adsbygoogle = window.adsbygoogle || []).push({});</script>\n'
        '</div>'
    )
    # head의 g.js 제거
    html = re.sub(r'\s*<script src="https://ads-partners\.coupang\.com/g\.js"></script>\n?', '', html)
    # PartnersCoupang 블록 제거 → AdSense로 교체
    html = re.sub(
        r'<!-- Coupang Partners -->\s*<div[^>]*>.*?</div>',
        ADSENSE_BLOCK,
        html, flags=re.DOTALL
    )
    html = re.sub(r'<script>\s*new PartnersCoupang\.G\([^)]*\);?\s*</script>', '', html)
    html = re.sub(r'<div[^>]*>\s*<script>\s*new PartnersCoupang\.G\([^)]*\);?\s*</script>\s*</div>', '', html)
    html = re.sub(r'<p class="coupang-notice">[^<]*</p>', '', html)

    # ── og:locale 교체 ──
    html = html.replace('content="ko_KR"', 'content="en_US"')

    with open(en_path, 'w', encoding='utf-8') as f:
        f.write(html)

    print(f'  ✅ en/{filename}')


# ── 4. 실행 ──────────────────────────────────────────────────────────────────
if __name__ == '__main__':
    print('Building English pages for WooaQR...')
    for filename, meta in PAGE_META.items():
        ko_path = os.path.join(BASE, filename)
        if os.path.exists(ko_path):
            build_page(filename, meta)
        else:
            print(f'  ⚠️  {filename} not found, skipping')

    print('\nDone! English pages written to en/')
