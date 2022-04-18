import re
with open('input.txt', 'r') as INPUT:
    cod = 0
    pamyat = 0
    gif = 0

    def memory(string):
        emoji = string[1:-1]
        emoji = emoji.replace("\\\\", "x")
        emoji = emoji.replace("\\\"", "x")
        emoji, _  = re.subn('\\\\x..', 'x', emoji)
        return len(emoji)

    def esc(string):
        escaped = string
        escaped = escaped.replace("\\", "\\\\")
        escaped = escaped.replace('"', '\\"')
        escaped = '"' + escaped + '"'
        return len(escaped)
    for line in INPUT:
        chars = len(line)
        emoji = memory(line)
        escaped = esc(line)
        cod += len(line)
        pamyat += memory(line)
        gif += escaped

    with open('output1.txt', 'w') as OUTPUT:
        OUTPUT.write(str(cod - pamyat))
