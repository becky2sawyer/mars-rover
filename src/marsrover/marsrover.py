"""marsrover 모듈.

화성에서 감자를 키우기 적합한 곳을 찾아 지구와 핑퐁 통신을 합니다.

Example:
    ``marsrover`` 사용법은 아래와 같습니다.

        $ pip install ./
        $ marsrover-ping
        $ marsrover-ping kr
        $ marsrover-ping en

en 또는 kr 로 통신 언어 설정이 가능합니다.

Attributes:
    MSG (list): ``통신가능 언어팩`` 이 담겨 있다. 한국어 및 영어 통신이 가능하며, 가각 kr, en 으로 설정 가능하다.

Todo:
    * 우주의 모든 언어 지원
    * ``marsrover-ping kr "지금 화성에서 가장 힘든점 한가지만 말해줘"`` 와 같이 의미를 해석하여 회신하도록 만들자!

"""

import sys
import random

MSG = [
    {"en": 'Oh no! I forgot to leave my potato seeds on Earth.', "kr": "이런! 깜빡하게 감자 종자를 지구에 두고 왔네요."},
    {"en": 'I miss my mom. Send him back to Earth.', "kr": "엄마가 보고 싶어요 지구로 돌려 보내 주세요"},
    {"en": 'Wow! It sprouted on the potatoes.', "kr": "와우! 감자에 싹이났어요."},
]


def what_about_there(language='kr', question='지금 뭐해?') -> str:
    """화성 지금 어떤가요?

    Args:
        language: kr or en
        question: 어떤 질문이라도 좋아요.

    Returns:
        영어 또는 한국어로 지금 화성 상황을 이야기함

    Todo:
        * question - 질문 수신하여 처리 필요 지금은 혼잣말!

    """

    msg = random.choice(MSG)
    return msg[language]


def ping() -> str:
    """화성탐사선의 현 상황을 회신함
        - main 함수
        - argv 의 첫번째 인자 kr,en 을 받아 동작

    Returns:
        Wow! It sprouted on the potatoes.

    Todo:
        * argv 를 인간 친화적으로 변경
    """
    try:
        lang = sys.argv[1] if sys.argv[1] in ['kr', 'en'] else 'kr'
    except IndexError:
        lang = 'en'

    return what_about_there(language=lang)
