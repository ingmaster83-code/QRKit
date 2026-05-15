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
