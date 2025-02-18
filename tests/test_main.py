from sort_tool.main import main
from io import StringIO

def test_print_lines():
    content = (
        "this ebook is\n"
        "most other parts\n" 
        "whatsoever"
    )
    
    file_output = StringIO()
    main(content, file_output)
    result = file_output.getvalue()

    assert result == "most other parts\nthis ebook is\nwhatsoever\n"


def test_print_unique_lines():
    content = (
        "A\n"
        "A\n" 
        "B\n"
        "Bn\n"
        "F"
    )
    
    file_output = StringIO()
    main(content, file_output, unique=True)
    result = file_output.getvalue()

    assert result == "A\nB\nBn\nF\n"
