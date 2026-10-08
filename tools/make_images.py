#!/usr/bin/env python3
"""n8n AI 업무 자동화 책용 이미지 생성 스크립트 (PIL 기반)."""
import os
import math
from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
ASSETS = os.path.join(os.path.dirname(HERE), "assets")

BOLD = "/usr/share/fonts/opentype/noto/NotoSansCJK-Bold.ttc"
REG = "/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc"

BG = (13, 19, 38)
PANEL = (24, 33, 62)
CORAL = (224, 120, 86)
TEAL = (78, 205, 196)
BLUE = (96, 150, 255)
WHITE = (245, 247, 250)
MUTED = (154, 167, 199)
LINE = (70, 88, 140)
LIGHT_BG = (250, 251, 253)
INK = (30, 41, 59)
SUB = (100, 116, 139)
CARD_LINE = (203, 213, 225)


def font(path, size):
    return ImageFont.truetype(path, size, index=1)


def text_center(d, cx, y, s, f, fill):
    bb = d.textbbox((0, 0), s, font=f)
    w = bb[2] - bb[0]
    d.text((cx - w / 2 - bb[0], y), s, font=f, fill=fill)


def rrect(d, box, radius, fill, outline=None, width=1):
    d.rounded_rectangle(box, radius=radius, fill=fill, outline=outline, width=width)


def arrow(d, x1, y1, x2, y2, fill=CORAL, width=4):
    d.line([x1, y1, x2, y2], fill=fill, width=width)
    ang = math.atan2(y2 - y1, x2 - x1)
    sz = 14
    for da in (2.6, -2.6):
        d.line([x2, y2, x2 + sz * math.cos(ang + da), y2 + sz * math.sin(ang + da)],
               fill=fill, width=width)


# ---------------------------------------------------------------- 표지 1000x1300
def make_cover():
    W, H = 1000, 1300
    img = Image.new("RGB", (W, H), BG)
    d = ImageDraw.Draw(img)
    for y in range(H):
        t = y / H
        r = int(13 + (30 - 13) * t)
        g = int(19 + (44 - 19) * t)
        b = int(38 + (82 - 38) * t)
        d.line([(0, y), (W, y)], fill=(r, g, b))
    d.ellipse([-180, -180, 320, 320], outline=(224, 120, 86, 90), width=3)
    d.ellipse([-120, -120, 260, 260], outline=(78, 205, 196, 70), width=2)
    d.ellipse([760, 980, 1180, 1400], outline=(96, 150, 255, 80), width=3)
    d.ellipse([820, 1040, 1120, 1340], outline=(224, 120, 86, 60), width=2)
    for i in range(6):
        x = 700 + i * 45
        d.line([(x, 0), (x + 220, 420)], fill=(255, 255, 255, 14), width=2)

    fb = lambda s: font(BOLD, s)
    fr = lambda s: font(REG, s)

    text_center(d, W / 2, 66, "W I K I D O C S   T E C H   B O O K", fr(26), CORAL)
    d.line([(120, 128), (880, 128)], fill=LINE, width=2)

    text_center(d, W / 2, 200, "n8n으로 만드는", fb(88), WHITE)
    text_center(d, W / 2, 320, "AI 업무 자동화", fb(88), CORAL)

    text_center(d, W / 2, 500, "코딩 없이 시작하는", fb(44), WHITE)
    text_center(d, W / 2, 566, "AI 워크플로우 실전서", fb(44), WHITE)

    rrect(d, [160, 680, 840, 748], 34, PANEL, outline=LINE, width=2)
    text_center(d, W / 2, 696, "워크플로우부터 AI 에이전트까지", fb(32), WHITE)

    topics = [
        "워크플로우 기초와 노드 연결",
        "조건 분기 · 반복 · 에러 처리",
        "LLM 노드와 AI 에이전트",
        "RAG 파이프라인 구축",
        "MCP 연동과 실전 프로젝트",
    ]
    y = 800
    text_center(d, W / 2, y, "이 책에서 다루는 내용", fr(26), MUTED)
    y += 44
    for i, t in enumerate(topics):
        rrect(d, [170, y, 830, y + 46], 23, (20, 28, 54), outline=(60, 76, 120), width=1)
        d.ellipse([194, y + 11, 228, y + 45], fill=TEAL)
        fnum = fb(26)
        num = str(i + 1)
        bb = d.textbbox((0, 0), num, font=fnum)
        d.text((211 - (bb[2] - bb[0]) / 2 - bb[0], y + 13), num, font=fnum, fill=(255, 255, 255))
        d.text((244, y + 15), t, font=fr(24), fill=WHITE)
        y += 56

    d.line([(120, 1130), (880, 1130)], fill=LINE, width=2)
    text_center(d, W / 2, 1158, "저자  이준수", fr(30), MUTED)
    text_center(d, W / 2, 1202, "기준일  2026-10-09", fr(26), MUTED)

    img.save(os.path.join(ASSETS, "cover.png"))
    print("cover.png saved")


# ------------------------------------------------- 워크플로우 기본 구조 1400x560
def make_workflow_basics():
    W, H = 1400, 560
    img = Image.new("RGB", (W, H), LIGHT_BG)
    d = ImageDraw.Draw(img)
    fb = lambda s: font(BOLD, s)
    fr = lambda s: font(REG, s)

    text_center(d, W / 2, 24, "n8n Workflow Basics", fb(40), INK)
    text_center(d, W / 2, 78, "트리거에서 시작해 노드를 거쳐 데이터가 흐른다",
                fr(26), SUB)

    def node(x, y, w, h, title, desc, fill, tcolor=INK):
        rrect(d, [x, y, x + w, y + h], 18, fill, outline=CARD_LINE, width=2)
        text_center(d, x + w / 2, y + 22, title, fb(30), tcolor)
        for j, line in enumerate(desc.split("\n")):
            text_center(d, x + w / 2, y + 66 + j * 38, line, fr(24), SUB if tcolor == INK else (203, 213, 225))

    y0 = 170
    node(60, y0, 260, 220, "Trigger", "시작 조건\nManual / Schedule\nWebhook", (30, 41, 59), WHITE)
    arrow(d, 330, y0 + 110, 390, y0 + 110, fill=(148, 163, 184), width=5)
    node(400, y0, 260, 220, "Action Node", "실제 작업\nSlack / Sheets\nHTTP Request", (255, 255, 255))
    arrow(d, 670, y0 + 110, 730, y0 + 110, fill=(148, 163, 184), width=5)
    node(740, y0, 260, 220, "Logic Node", "흐름 제어\nIF / Loop\nMerge", (255, 255, 255))
    arrow(d, 1010, y0 + 110, 1070, y0 + 110, fill=(148, 163, 184), width=5)
    node(1080, y0, 260, 220, "Output", "결과 전달\n다음 노드\n또는 응답", (219, 234, 254))

    text_center(d, W / 2, 450, "데이터는 왼쪽에서 오른쪽으로, JSON 아이템 형태로 흐른다",
                fr(26), SUB)
    img.save(os.path.join(ASSETS, "fig-workflow-basics.png"))
    print("fig-workflow-basics.png saved")


# ------------------------------------------------- 데이터 아이템 흐름 1400x620
def make_data_items():
    W, H = 1400, 620
    img = Image.new("RGB", (W, H), LIGHT_BG)
    d = ImageDraw.Draw(img)
    fb = lambda s: font(BOLD, s)
    fr = lambda s: font(REG, s)
    mono = lambda s: font(REG, s)

    text_center(d, W / 2, 24, "Data Items and Expressions", fb(40), INK)
    text_center(d, W / 2, 78, "아이템은 JSON 객체, 표현식 {{ }} 으로 참조한다",
                fr(26), SUB)

    # 아이템 박스 3개
    items = [
        ('{ "name": "김민수", "amount": 62000 }', CORAL),
        ('{ "name": "이지은", "amount": 34000 }', BLUE),
        ('{ "name": "박준혁", "amount": 81000 }', TEAL),
    ]
    x0 = 90
    for i, (js, color) in enumerate(items):
        x = x0 + i * 400
        rrect(d, [x, 160, x + 360, 160 + 110], 16, (255, 255, 255), outline=color, width=3)
        d.text((x + 20, 176), f"item {i}", font=fr(22), fill=SUB)
        d.text((x + 20, 208), js, font=mono(20), fill=INK)

    arrow(d, 700, 300, 700, 350, fill=(148, 163, 184), width=5)
    rrect(d, [440, 360, 960, 470], 18, (30, 41, 59))
    text_center(d, 700, 378, "{{ $json.name }}  →  김민수", fb(28), WHITE)
    text_center(d, 700, 420, "표현식으로 필드를 꺼내 쓴다", fr(24), (203, 213, 225))

    text_center(d, W / 2, 520, "Set 노드는 정리용, Code 노드는 복잡한 변환용",
                fr(26), SUB)
    img.save(os.path.join(ASSETS, "fig-data-items.png"))
    print("fig-data-items.png saved")


# ------------------------------------------------- AI 에이전트 구조 1400x700
def make_ai_agent():
    W, H = 1400, 700
    img = Image.new("RGB", (W, H), LIGHT_BG)
    d = ImageDraw.Draw(img)
    fb = lambda s: font(BOLD, s)
    fr = lambda s: font(REG, s)

    text_center(d, W / 2, 24, "AI Agent Node Structure", fb(40), INK)
    text_center(d, W / 2, 78, "모델이 도구를 골라 쓰며 목표를 달성한다",
                fr(26), SUB)

    # 중앙 에이전트
    rrect(d, [550, 220, 850, 420], 24, (30, 41, 59))
    text_center(d, 700, 250, "AI Agent", fb(36), WHITE)
    text_center(d, 700, 300, "목표 → 판단 → 도구 호출 → 반복", fr(24), (203, 213, 225))
    text_center(d, 700, 340, "순서를 미리 정하지 않는다", fr(24), CORAL)

    subs = [
        (140, 240, "Chat Model", "두뇌\nLLM 연결", BLUE),
        (140, 430, "Memory", "맥락 기억\nWindow Buffer", TEAL),
        (1050, 240, "Tool 1", "API 호출\nHTTP Request", CORAL),
        (1050, 430, "Tool 2", "문서 검색\nVector Store", (139, 92, 246)),
    ]
    for x, y, t, desc, color in subs:
        rrect(d, [x, y, x + 210, y + 130], 18, (255, 255, 255), outline=color, width=3)
        text_center(d, x + 105, y + 16, t, fb(28), INK)
        for j, line in enumerate(desc.split("\n")):
            text_center(d, x + 105, y + 56 + j * 34, line, fr(22), SUB)
    arrow(d, 350, 305, 540, 305, fill=BLUE, width=4)
    arrow(d, 350, 495, 540, 380, fill=TEAL, width=4)
    arrow(d, 860, 305, 1050, 305, fill=CORAL, width=4)
    arrow(d, 860, 380, 1050, 495, fill=(139, 92, 246), width=4)

    text_center(d, W / 2, 600, "도구의 이름과 설명이 명확해야 에이전트가 잘 쓴다",
                fr(26), SUB)
    img.save(os.path.join(ASSETS, "fig-ai-agent.png"))
    print("fig-ai-agent.png saved")


# ------------------------------------------------- RAG 파이프라인 1500x640
def make_rag_pipeline():
    W, H = 1500, 640
    img = Image.new("RGB", (W, H), LIGHT_BG)
    d = ImageDraw.Draw(img)
    fb = lambda s: font(BOLD, s)
    fr = lambda s: font(REG, s)

    text_center(d, W / 2, 24, "RAG Pipeline in n8n", fb(40), INK)

    def step(x, y, w, title, desc, color):
        rrect(d, [x, y, x + w, y + 150], 18, (255, 255, 255), outline=CARD_LINE, width=2)
        d.rectangle([x, y, x + w, y + 10], fill=color)
        text_center(d, x + w / 2, y + 26, title, fb(27), INK)
        for j, line in enumerate(desc.split("\n")):
            text_center(d, x + w / 2, y + 64 + j * 32, line, fr(22), SUB)

    SW, GAP, X0 = 330, 26, 40

    def row(y, label, label_color, steps):
        text_center(d, X0 + 60, y - 44, label, fb(26), label_color)
        x = X0
        for i, (t, desc, color) in enumerate(steps):
            step(x, y, SW, t, desc, color)
            if i < len(steps) - 1:
                arrow(d, x + SW + 4, y + 75, x + SW + GAP - 4, y + 75,
                      fill=(148, 163, 184), width=4)
            x += SW + GAP

    row(150, "인덱싱 (문서 넣기)", CORAL, [
        ("문서 읽기", "파일 · 웹페이지", CORAL),
        ("텍스트 분할", "적당한 길이로 나누기", CORAL),
        ("임베딩", "벡터로 변환", CORAL),
        ("저장", "Vector Store", CORAL),
    ])
    row(400, "검색 (질문 답하기)", BLUE, [
        ("질문 벡터화", "질문을 벡터로", BLUE),
        ("유사도 검색", "관련 조각 꺼내기", BLUE),
        ("프롬프트 구성", "문서 + 질문", BLUE),
        ("LLM 답변", "근거 기반 답변 생성", BLUE),
    ])

    text_center(d, W / 2, 590, "두 흐름은 같은 Vector Store를 공유한다 · 답이 틀리면 검색을 먼저 의심",
                fr(25), SUB)

    img.save(os.path.join(ASSETS, "fig-rag-pipeline.png"))
    print("fig-rag-pipeline.png saved")


# ------------------------------------------------- 실전 프로젝트 구조 1500x720
def make_project_arch():
    W, H = 1500, 720
    img = Image.new("RGB", (W, H), LIGHT_BG)
    d = ImageDraw.Draw(img)
    fb = lambda s: font(BOLD, s)
    fr = lambda s: font(REG, s)

    text_center(d, W / 2, 24, "AI Customer Inquiry Auto-Response System", fb(38), INK)
    text_center(d, W / 2, 74, "웹훅 → AI 에이전트 → RAG 검색 → 답변 또는 담당자 전달",
                fr(26), SUB)

    def node(x, y, w, h, title, desc, fill, tcolor=INK):
        rrect(d, [x, y, x + w, y + h], 18, fill, outline=CARD_LINE, width=2)
        text_center(d, x + w / 2, y + 18, title, fb(28), tcolor)
        for j, line in enumerate(desc.split("\n")):
            text_center(d, x + w / 2, y + 58 + j * 34, line, fr(22), SUB if tcolor == INK else (203, 213, 225))

    y0 = 160
    node(40, y0, 220, 200, "문의 폼", "홈페이지\nPOST 전송", (255, 255, 255))
    arrow(d, 265, y0 + 100, 305, y0 + 100, fill=(148, 163, 184), width=5)
    node(310, y0, 220, 200, "Webhook", "n8n 수신\nProduction URL", (30, 41, 59), WHITE)
    arrow(d, 535, y0 + 100, 575, y0 + 100, fill=(148, 163, 184), width=5)
    node(580, y0, 260, 200, "AI Agent", "문서 검색 도구\n담당자 전달 도구", (255, 237, 230))
    arrow(d, 845, y0 + 60, 885, y0 + 60, fill=CORAL, width=4)
    node(890, y0 - 30, 240, 140, "Vector Store", "사내 문서\nRAG 검색", (219, 234, 254))
    arrow(d, 845, y0 + 140, 885, y0 + 140, fill=BLUE, width=4)
    node(890, y0 + 90, 240, 140, "담당자 전달", "근거 없을 때\n내부 알림", (255, 255, 255))
    arrow(d, 845, y0 + 100, 575 + 270, y0 + 100, fill=(148, 163, 184), width=3)

    # 답변 출력
    arrow(d, 710, y0 + 200, 710, y0 + 250, fill=(148, 163, 184), width=5)
    node(580, y0 + 255, 260, 150, "답변 반환", "문서 근거 기반\n고객에게 응답", (224, 242, 254))

    # 에러 처리
    rrect(d, [40, 560, 560, 660], 18, (255, 255, 255), outline=CORAL, width=2)
    text_center(d, 300, 576, "Error Workflow: 실패 시 담당자에게 알림", fr(24), INK)
    text_center(d, 300, 610, "자동화가 멈춰도 고객이 방치되지 않게", fr(22), SUB)

    rrect(d, [600, 560, 1460, 660], 18, (30, 41, 59))
    text_center(d, 1030, 576, "핵심 규칙: 근거 없는 내용을 지어내지 않는다", fb(26), CORAL)
    text_center(d, 1030, 614, "첫 일주일은 답변 로그를 사람이 검토하며 다듬는다", fr(22), (203, 213, 225))

    img.save(os.path.join(ASSETS, "fig-project-arch.png"))
    print("fig-project-arch.png saved")


if __name__ == "__main__":
    os.makedirs(ASSETS, exist_ok=True)
    make_cover()
    make_workflow_basics()
    make_data_items()
    make_ai_agent()
    make_rag_pipeline()
    make_project_arch()
