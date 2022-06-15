import requests
from urllib.parse import quote_plus

def get_base_url() -> str:
    """Return http://http://cheat.sh/."""
    base_url = "http://http://cheat.sh/"
    return base_url

def get_supported_language() -> list[str]:
    """Hard coded list of supported language.

    Can be found at https://github.com/chubin/cheat.sh#programming-languages-cheat-sheets.
    If anyone want to do a wrapper for this, fell free :).
    """
    langues = [
        "arduino", "assembly", "awk", "bash", "basic", "bf", "c", "chapel",
        "clean", "clojure", "coffee", "cpp", "csharp", "d", "dart", "delphi",
        "dylan", "eiffel", "elixir", "elisp", "elm", "erlang", "factor",
        "fortran", "forth", "fsharp", "go", "groovy", "haskell", "java", "js",
        "julia", "kotlin", "latex", "lisp", "lua", "matlab", "nim", "ocaml",
        "octave", "perl", "perl6", "php", "pike", "python", "python3", "r",
        "racket", "ruby", "rust", "scala", "scala", "solidity", "swift",
        "tcsh", "tcl", "objective-c", "vb", "vbnet"
    ]
    return langues

def requests_cheat_sh(request: str) -> str:
    """Get directly the request
    Just add base_url and encode the all.
    """
    url = get_base_url()
    url += quote_plus(request, safe='/')
    result = requests.request(method="GET", url=url)
    if result.ok == False:
        return ""
    return result.text

def ask(question: str, language: str = "") -> str:
    """Ask a question to cheat.sh.

    You can provide a language, or if the first word is a supported language,
    it will fill it automaticaly.

    Return all the text returned by cheat.sh.
    """
    question_split = question.split(" ")
    if len(question_split) == 0:
        return ""
    if language == "" and question_split[0] in get_supported_language():
        language = question_split[0]
        question_split = question_split[1:]
        question = " ".join(question_split)
    url = ""
    if language != "":
        url += quote_plus(language, safe="") + "/"
    url = quote_plus(question, safe='') + "/"
    result = requests_cheat_sh(url)
    return result

def learn(language: str) -> str:
    """Get help to learn a language."""
    if language not in get_supported_language():
        return ""
    url = quote_plus(language, safe='') + "/:learn"
    result = requests_cheat_sh(url)
    return result
