def main(argv):
    # このコードは引数と標準出力を用いたサンプルコードです。
    # このコードは好きなように編集・削除してもらって構いません。
    # ---
    # This is a sample code to use arguments and outputs.
    # Edit and remove this code as you like.
    out = "Hello"
    if argv[0] != "":
        out += " "+argv[0]+"!"
    else:
        out += "!"
    print(out)
    return
